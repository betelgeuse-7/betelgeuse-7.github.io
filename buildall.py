import os
import sys

def invoke_command(filename):
    command = f"python3 blogmaker.py {filename}"
    os.system(command)

if __name__ == "__main__":
    files = os.listdir()
    md_files = [file for file in files if file.endswith('.md')]
    for md_file in md_files:
        invoke_command(md_file)

    os.system("python3 blogmaker.py")
