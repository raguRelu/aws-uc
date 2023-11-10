import os
import subprocess

def start_detached(executable, *args):
    pid = os.fork()
    
    if pid > 0:
        # Parent process
        return pid
    elif pid == 0:
        # Child process
        try:
            # Detach from the parent process
            os.setsid()
            
            # Execute the subprocess
            subprocess.Popen([executable, *args], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except Exception as e:
            print(f"Error: {e}")
        finally:
            os._exit(0)  # Terminate the child process



