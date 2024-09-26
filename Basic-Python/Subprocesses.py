import subprocess

output = subprocess.check_output('echo Hello, World!', shell=True, text=True)
print(output)
