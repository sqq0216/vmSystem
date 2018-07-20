import paramiko

ip = '10.108.167.79'
uname = 'vm'
passwd = '123456'

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(ip, 22, username=uname, password=passwd, timeout=4)

while True:
    stdin, stdout, stderr = client.exec_command("pwd")
    path = ""
    for p in stdout.readlines():
        path += p[:-1]
    cmd = raw_input("["+uname+"@"+uname+" "+path+"]$ ")
    if cmd == "endssh": break
    stdin, stdout, stderr = client.exec_command(cmd)
    for std in stdout.readlines():
        print std,

client.close()
