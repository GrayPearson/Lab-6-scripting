import requests
import hashlib
import subprocess
import os

file_url = 'http://download.videolan.org/pub/videolan/vlc/3.0.18/win64/vlc-3.0.18-win64.exe.sha256'
resp_msg = requests.get(file_url)

if resp_msg.status_code == requests.codes.ok:
    file_content = resp_msg.text


image_hash = hashlib.sha256(file_content).hexdigest()

print(image_hash)
##    with open(r'C:\temp\videolan.txt', 'w') as file:
##        file.write(file_content)

installer_path = r'C:\temp\vlc-3.0.17.4-win64.exe'
subprocess.run([installer_path, '/L=1033', '/S'])
os.remove(installer_path)