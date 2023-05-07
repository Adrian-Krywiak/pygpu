import psutil
import time
import subprocess

def run_command(command):
    cmd = f"cmd.exe /c start {command}"
    process = subprocess.Popen(cmd, shell=True)
    process.wait()

def kill_process_by_name(process_name):
    for process in psutil.process_iter(['name']):
        try:
            if process_name.lower() in process.info['name'].lower():
                process.terminate()
                print(f"{process_name} process terminated.")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

def is_python_running():
    for process in psutil.process_iter(['name']):
        try:
            if 'python' in process.info['name'].lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

if __name__ == "__main__":
    is_python_running_check = False
    while time.sleep(1) is None:
        if is_python_running():
            print("Python is running")
            if is_python_running_check == True:
                print("Killing python process")
                kill_process_by_name('t-rex.exe')
                is_python_running_check = False
        else:
            print("Python is not running")
            if is_python_running_check == False:
                command = "C:\\Users\\Adrian\\Desktop\\Crypto\\t-rex-0.21.6-win\\t-rex.exe -a kawpow -o stratum+tcp://stratum-ravencoin.flypool.org:3333 -u RQYjTBjvjVBNgUM2jDn8HPfeVKQdN8uAXJ.rig -p x -d 0"
                run_command(command)
                is_python_running_check = True
