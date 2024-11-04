import os
import subprocess
import sys

def check_command(command):
    """Check if a command is available on the system."""
    try:
        subprocess.run([command, '--version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError:
        print(f"{command} is required but it's not installed. Aborting.")
        sys.exit(1)

def run_command(command, cwd=None):
    """Run a shell command."""
    result = subprocess.run(command, shell=True, cwd=cwd)
    if result.returncode != 0:
        print(f"Command '{command}' failed with exit code {result.returncode}. Aborting.")
        sys.exit(1)

def run_command_background(command, cwd=None):
    """Run a shell command in the background."""
    process = subprocess.Popen(command, shell=True, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return process

def main():
    # Check if Node.js is installed
    check_command('node')

    # Check if Python is installed
    check_command('python')

    # Navigate to the client directory and install dependencies
    print("Setting up client...")
    run_command('npm ci', cwd='client')
    client_process = run_command_background('npm start', cwd='client')

    # Navigate to the server directory and install dependencies
    print("Setting up server...")
    run_command('npm ci', cwd='server')
    server_process = run_command_background('node index.js', cwd='server')

    # Install Python dependencies
    print("Setting up Python environment...")
    run_command('pip install -r requirements.txt')

    print("Setup complete. Your web application should now be running.")

    # Wait for the client and server processes to complete
    client_process.wait()
    server_process.wait()

if __name__ == "__main__":
    main()