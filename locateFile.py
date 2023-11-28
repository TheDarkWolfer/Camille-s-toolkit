import subprocess, os

def locateFile(file_name):
    command = f"locate {file_name}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    if result.returncode == 0:
        file_path = result.stdout.strip()
        return file_path
    else:
        print("File not found.")
        return None
    
def checkFile(file_path,filename:str):
    if os.path.isfile(file_path):
        with open(file_path, "r") as f:
            data = f.read()
            if data == filename:
                return True
    else:
        return False