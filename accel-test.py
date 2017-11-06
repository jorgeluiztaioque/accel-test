#!/usr/bin/env python
#-----------------------------------------------------------------------
# Usage:
# ./accel-test.py [IP_REMOTE_ACCEL]
# Like:
# ./accel-test.py 10.10.10.1
# put only IP or Hostname
#
#-----------------------------------------------------------------------

__author__ = 'Jorge Luiz Taioque'
__version__= 0.1

import socket
import sys
hostname = sys.argv[1]

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(10)
status = sock.connect_ex((hostname,2001))

if status == 0:
	print ("ACCEL-PPP is UP")
	sys.exit(0)
else:
	print ("ACCEL-PPP is Down")
	sys.exit(2)
#!/usr/bin/env python
#-----------------------------------------------------------------------
# Usage:
# ./accel-test.py [IP_REMOTE_ACCEL]
# Like:
# ./accel-test.py 10.10.10.1
# put only IP or Hostname
#
#-----------------------------------------------------------------------

__author__ = 'Jorge Luiz Taioque'
__version__= 0.1

import socket
import sys
hostname = sys.argv[1]

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(10)
status = sock.connect_ex((hostname,2001))

if status == 0:
	print ("ACCEL-PPP is UP")
	sys.exit(0)
else:
	print ("ACCEL-PPP is Down")
	sys.exit(2)

print status

print status
