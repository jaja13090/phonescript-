import subprocess

target = 200

up = 0

down = 0

while (target < 255):

        ip = "192.168.31." +str(target)

        output = subprocess.Popen(["ping","-c","1",ip],stdout = subprocess.PIPE).communicate()[0]

        if ('Unreachable' in output):

                print 'Host ' + ip + " is offline or unavailable"

                down+= 1

        else:

                print "Host " + ip + " is online"

                up+= 1

        target = target+1

print "A total of " + str(up+down) + " hosts were scanned."

print str(up) + " hosts were alive, and " + str(down) + " hosts were unreachable. "

quit()
