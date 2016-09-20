import telnetlib
tn = telnetlib.Telnet('192.168.122.238')
print tn.read_until('login: ')
tn.write('vm01' + '\r\n')
print tn.read_until('password: ')
tn.write('123456\r')
tn.read_all()
tn.read_until('\n', 5)
'''
while True:
    print tn.read_until('\n')


tn.interact()
tn.write('start c:\\notepad.exe\r\n')
tn.write('tskill explorer\r\n')
tn.close()


tn.read_until(':~$ ')
#tn.write('start c:\\notepad.exe\n')
tn.write("dir\n")
tn.read_until(':~$')
tn.close()
'''
