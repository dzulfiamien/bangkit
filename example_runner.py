import subprocess
# subprocess.run(["python", "example.py", "text.txt"])

run_command = subprocess.run(["python", "example.py", "text.txt"], capture_output=True)
print(run_command)