import os
import time
import subprocess
"""
Monitor a process. if it has issue, the STATUS file will be created
Once pyProcMan detects the STATUS, it will kill the old process
and create a new one
"""
# Interval for detection
tSleep = 60
# STATUS file, including time of err and parameters for re-invoke proc
# Format: err_time, arg0, arg1
STATUS = "thisproc.status"
# LOG file
logFile = "pyprocman.log"
# Command to maintain, in a list
cmd = ["python", "mycmd", None, None]
#
with open(logFile, 'a') as f_log:
    flog.write("time,kill_at_param1,kill_at_param2")
child = subprocess.Popen(cmd)
while(True):
    time.sleep(tSleep)
    if os.path.exists(STATUS):
        with open(STATUS, 'r') as f_status:
            msg = f_status.readline().strip("\n").split(",")
        if len(msg) == 3 and msg[-1] == 'END':
            # msg is complete
            arg0 = msg[0]
            arg1 = msg[1]
            os.remove(STATUS)
            child.kill()
            now = time.ctime()
            with open(logFile, 'a') as f_log:
                f_log.write(now + "," + arg0 + "," + arg1)
            cmd[2] = arg0
            cmd[3] = arg1
            time.sleep(tSleep)
            child = subprocess.Popen(cmd)




