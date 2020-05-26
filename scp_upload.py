# Upload files of specified types via SCP

import sys
import os
import pathlib

try:
    import paramiko
    import scp
except ImportError:
    print("Trying to install required modules (paramiko, scp)\n")
    os.system('python -m pip install paramiko scp')

import paramiko
import scp


HOST = "host.com"
USER = "ubuntu"
SOURCE_DIRECTORY = "./src"
TARGET_DIRECTORY = "/var/www/default"
FILE_TYPES = [".html", ".css", ".js"]



# Upload progress
def progress(filename, size, sent):
    sys.stdout.write(f"Progress: {float(sent)/float(size)*100:.2f}%\r")

# Recursive folder crawling
def check_folder(file_path, file_list):
    for child in file_path.iterdir():
        if child.is_dir():
            check_folder(child, file_list)
        else:
            if child.suffix in FILE_TYPES:
                file_list.append(child)



ssh_client = paramiko.SSHClient()
ssh_client.load_system_host_keys()
ssh_client.connect(HOST, 22, USER)

# Crawl folder and upload files
scp_client = scp.SCPClient(ssh_client.get_transport(), progress=progress)
try:
    upload_list = []
    # Work with pure paths
    SOURCE_DIRECTORY = pathlib.Path(SOURCE_DIRECTORY)
    TARGET_DIRECTORY = pathlib.Path(TARGET_DIRECTORY)
    check_folder(SOURCE_DIRECTORY, upload_list)
    for file in upload_list:
        print(f"Uploading {file}")
        try:
            target_path = TARGET_DIRECTORY / file.relative_to(SOURCE_DIRECTORY)
            scp_client.put(file, target_path.as_posix())
        except scp.SCPException as e:
            # SCP connection gets dropped if the directory is missing
            if "No such file or directory" in e.args[0]:
                print("Directory missing - creating and trying again")
                # Create the folder and reset the connection
                ssh_client.exec_command("mkdir " + target_path.parent.as_posix())
                scp_client = scp.SCPClient(ssh_client.get_transport(), progress=progress)
                print(f"Uploading {file}")
                scp_client.put(file, target_path.as_posix())
            else:
                print("Something has gone wrong")
                print(e)
                scp_client.close()
                exit()
finally:
    scp_client.close()
