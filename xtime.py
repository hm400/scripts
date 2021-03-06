#!/usr/bin/env python3
import subprocess, re, os
from datetime import datetime

def main():
  sysos()
  systime()
  sysuptime()
  sessions()
  loadavg()
  users()
  memory()
  storage()

def sysos():
  output = str.splitlines(os.fsdecode(subprocess.check_output(['lsb_release', '-idrc'])))
  print('\n' + esc('1;93') + ' Operating System Description' + esc(0))
  for line in output:
    print(' ' + line)
  print()

def systime():
  time = datetime.now()
  print(esc('1;93') + ' System Time: '+ esc(0)  + time.strftime('%I:%M %p -> %b %d %Y'))

def sysuptime():
  output = os.fsdecode(subprocess.check_output(['uptime', '-p']))
  sysuptime = re.search(r"up\s(.*)" , output).group(1)
  print(esc('1;93') + ' System\'s been up for:' + esc(0), sysuptime)

def sessions():
  output = os.fsdecode(subprocess.check_output('uptime'))
  out = re.search(r"(\d+)\s+[users]|[user]", output).group(1)
  print(esc('1;93') + ' Number of active user sessions: ' + esc(0), out + ' user sessions')

def loadavg():
  output = os.fsdecode(subprocess.check_output('uptime'))
  load = re.search(r"(load average):(.*)", output).group(2)
  print(esc('1;93') + ' Load average for last 1, 5 and 15 minutes:' + esc(0), load + '\n')

def users():
  output = str.splitlines(os.fsdecode(subprocess.check_output(['w', '-h'])))
  print(esc('1;93') + " List of logged in users and what they're doing" + esc(0))
  for line in output:
    print(" " + line)
  print('')

def memory():
  output = str.splitlines(os.fsdecode(subprocess.check_output(['free', '-ht'])))
  print(esc('1;93') + " Free and used system memory " + esc(0))
  for line in output:
    print(" " + line)
  print('')

def storage():
  output = str.splitlines(os.fsdecode(subprocess.check_output(['lsblk', '-fm', '-o' 'NAME,' 'FSTYPE,' 'FSAVAIL,' 'FSUSE%,' 'MOUNTPOINT,' 'SIZE,' 'OWNER,' 'GROUP,' 'MODE', '-e 7'])))
  print(esc('1;93') + " List of drives, partitions, and details" + esc(0))
  for line in output:
    print(" " + line)
  print('')

def esc(code):
  return f'\033[{code}m'

if __name__=='__main__':
      main()
