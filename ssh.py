import paramiko
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('192.168.122.12', 22, username='vm01', password='123456', timeout=4)
stdin, stdout, stderr = client.exec_command('dir')
for std in stdout.readlines():
    print std,
client.close()
