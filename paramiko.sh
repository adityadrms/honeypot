import paramiko

hostname = 192.168.134.35
username = raspberry
password = 123

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh_client.connect(hostname, username=username, password=password)

stdin, stdout, stderr = ssh_client.exec_command('ls -l')

output = stdout.read().decode()
print(output)

ssh_client.close()
