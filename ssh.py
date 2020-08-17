from pexpect import pxssh
s = pxssh.pxssh()
if not s.login ('shell.xshellz.com', 'BlackRout', '$Q,..vnw5sIVz-=GD&9x'):
    print "SSH session failed on login."
    print str(s)
else:
    print "SSH session login successful"
    s.sendline ('ping 8.8.8.8')
    s.sendline = input("Enter..: ")
    s.prompt()         # match the prompt
    print s.before     # print everything before the prompt.
    s.logout()
