import subprocess
import os.path
import sys

#Path of the file
run_process_file = "/sites/prowlist.pid"
#Refresh if the server is running

action = str(sys.argv[1])

if action == "start":
        if os.path.isfile(run_process_file):
                process = open(run_process_file, "r").read().strip()
                subprocess.call(["kill", "-9", process])
                subprocess.call(["rm", run_process_file])
        #Now we need to start the server again
        subprocess.call(["gunicorn", "prowlist.wsgi:application", "--bind", "127.0.0.1:8000", "--pid", run_process_file, "--daemon"])
elif action == "stop" :
        #If the process numbre exists 
        if os.path.isfile(run_process_file):
                process = open(run_process_file, "r").read().strip()
                subprocess.call(["kill", "-9", process])
                subprocess.call(["rm", run_process_file])