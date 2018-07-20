import telnetlib

host = '10.108.167.79'
username = 'vm'
password = '123456'

tn = telnetlib.Telnet(host)
print tn.read_until('login: ', 1),
tn.write(username + '\r\n')
print tn.read_until('password: ', 1),
tn.write(password + '\r\n')

while True:
    while True:
        ans = tn.read_until('>', 0.5)
        if ans == "": break
        print ans.decode('gbk'),
    cmd = raw_input()
    if cmd == "endt":
        break
    tn.write(cmd + '\r\n')

tn.close()
