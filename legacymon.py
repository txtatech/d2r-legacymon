import psutil
import os
import subprocess
import multiprocessing

def launch_legacy_guard():
    # Launch start_legacyguard.exe in the same directory
    directory = os.path.dirname(os.path.abspath(__file__))
    exe_path = os.path.join(directory, "start_legacyguard.exe")
    subprocess.Popen(exe_path)

if __name__ == '__main__':
    # Get the parent process ID (PPID) of the current process
    current_pid = os.getpid()
    parent_pid = psutil.Process(current_pid).ppid()

    # Get information about the parent process
    parent_process = psutil.Process(parent_pid)

    # Create a string with the captured information
    output = f"Parent Process ID (PPID): {parent_pid}\n"
    output += f"Parent Process Name: {parent_process.name()}\n"
    output += f"Parent Process Command Line: {' '.join(parent_process.cmdline())}\n"

    # Print a message to indicate that the data is ready
    print("Legacy Switch Found.")

    # Check if '-legacy' is present in the captured information
    if "-legacy" in output:
        # Launch start_legacyguard.exe in a separate process
        p = multiprocessing.Process(target=launch_legacy_guard)
        p.start()

    # Wait for the child process to finish
    p.join()

    # Print a message to indicate that the child process has completed
    print("Now monitoring GPU usage of all D2R processes.")
