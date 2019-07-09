from os import walk
import subprocess
import shlex

files = []
# pwd path (/media/usr/Expansion Drive/location folder)
path = ""

# foward slash path with backslash for space
# (/media/usr/Expansion\ Drive/localtion\ folder)
source_path = ""

# output format same as path
output_path = ""

command = f'sudo apt-get install ffmpeg:i386 ffmpeg'
subprocess.run(shlex.split(command))

for (dirpath, dirnames, filenames) in walk(path):
    print(filenames)
    for file in filenames :
        new_file = file.strip('.mkv')
        command = f'ffmpeg -i {source_path}/{file} -codec copy {output_path}/{new_file}.mp4'
        subprocess.run(shlex.split(command))
        print(command)

# subprocess.run(shlex.split("sudo apt-get update"))

