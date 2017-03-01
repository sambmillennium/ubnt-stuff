# ubnt-stuff
Work in progress scripts for monitoring/logging ubiquiti airmax equipment

## Connect_Alert

Logs into the client via SSH and gets the wlanUptime and wlanConnections properties and outputs these to a logfile. The script is currently configured to send an email alert if the connected clients is 0.

### Usage

Install paramiko 'pip install paramiko'. Copy the script to your server and run 'update.py' to add details for your device. This is best used as a cron job in it's current form to notify of downtime. The script can be easily modified to log any of the output of the mca-status command.

