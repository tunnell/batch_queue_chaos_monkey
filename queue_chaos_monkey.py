"""Kill random jobs randomly

Idea from Netflix Chaos Monkey

tunnell@rice.edu
"""
import subprocess
import time
import random
import numpy as np


wait_time = 60 * 60 # 1 hour in seconds
number_of_jobs_to_kill = 0.5
command = "scancel %d"

def do():
    ids = subprocess.getoutput('squeue --user tunnell --state running --format %A')
    id = int(random.choice(ids.split()[1:]))
    print('Kill %d' % id)
    
    subprocess.getoutput(command % id)

while 1:
    for i in range(np.random.poisson(number_of_jobs_to_kill)):
        do()
    
    time.sleep(np.random.poisson(wait_time))
