from __future__ import print_function
import os
import sys
import base64

# get details
host = raw_input('enter node IP:' + '\n')
username = raw_input('enter username:' + '\n')
password = raw_input('enter password:' + '\n')

f = open(os.path.join(sys.path[0],'details'),'w')

#encode and write to details file -MAKE SURE ONLY THE USER THE SCRIPT RUNS AS HAS ACCESS TO THIS

host = base64.standard_b64encode(host)
username = base64.standard_b64encode(username)
password = base64.standard_b64encode(password)

f.write(host + '\n')
f.write(username + '\n')
f.write(password + '\n')
exit()
