from __future__ import print_function
import paramiko # the only external library you will need download from here: https://github.com/paramiko/paramiko/tree/master/paramiko or pip install paramiko with 2.7
import sys, os.path
import smtplib
import time
import base64

def main():
    # remote command
    comm = 'mca-status'

    #details file
    d = open(os.path.join(sys.path[0],'details'),'w')

    #node details - decode these from the details file -MAKE SURE ONLY THE USER THE SCRIPT RUNS AS HAS ACCESS TO THIS

    ans = d.readlines()
    h = ans[0].strip()
    u = ans[1].strip()
    p = ans[2].strip()
    d.close()

    host = base64.standard_b64decode(h)
    user = base64.standard_b64decode(u)
    pw = base64.standard_b64decode(p)

    # ssh connection
    c = paramiko.SSHClient()
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    c.connect(host, username=user, password=pw)
    stdin, stdout, stderr = c.exec_command(comm)

    # initial results
    result = []
    for line in stdout:
        result.append(line.strip('\n'))
        c.close()

    WC = result[4]

    for line in WC:
        if 'wlanConnections=0' in line:
            mail()
        else:
            break



def mail():
#Get host ip for the email content

        d = open(os.path.join(sys.path[0],'details'),'w')
        ans = d.readlines()
        host = ans[0].strip()
        host.decode()
        d.close()

#format and send email

        FROM = 'email@'
        TO = ["email@"]
        SUBJECT = 'Node has 0 connected clients'
        TEXT = 'WARNING - The following device is reporting no clients connected!'
        message = """\
        From: %s
        To: %s
        Subject: %s
        %s

        %s
        """ % (FROM, ", ".join(TO), SUBJECT, host , TEXT)
        server = smtplib.SMTP('mailserver')
        server.sendmail(FROM, TO, message)
        server.quit()




if __name__ == '__main__':
    main()
