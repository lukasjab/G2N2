#!/usr/bin/python3
import subprocess
ip = "192.168.209.133" # local ip address of the ubuntu machine (this one is actually my machine)
username = "student"
password = "Bolton2023"
command = f'rsync -avzp -e "sshpass -p {password} ssh -o StrictHostKeyChecking=no" /home/lblacklock/Programs/G2N2 {username}@{ip}:/home/{username}/Programs'
subprocess.run(command, shell=True, check=True)
# runs main.py on remote machine
command = f'SSHPASS={password} sshpass -e ssh {username}@{ip} /home/{username}/Programs/G2N2/.venv/bin/python /home/{username}/Programs/G2N2/source/main.py'
subprocess.run(command, shell=True, check=True)