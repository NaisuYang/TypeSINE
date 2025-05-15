# Imports
import os
import re
import sys
import time

# Methods

def ask_user_overwrite(file):
    if os.path.exists(file):
        while True:
            user_input = input(f"\nThe {os.path.basename(file)} already exists. Do you want to overwrite it? (yes/no): ").strip().lower()
            if user_input in ("yes", "no"):
                return user_input == "yes"

def run_cmd(cmd):
    try:
        subprocess.run(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=True,shell=True)
    except Exception as e:
        print(e)
        sys.exit()

def run_cmd_parallel(commands):
    processes = []
    for cmd in commands:
        process = subprocess.Popen(cmd, shell=True)
        processes.append(process)
    for process in processes:
        process.communicate()

def bwa_index_cmd(fi):
    cmd = f"bwa-mem2 index {fi} > /dev/null 2>&1"
    return cmd

def calculate_run_time(tbegin,tend):
    """
    to calculate the time to evaluate the speed
    """
    tTotal=tend-tbegin
    tsec=tTotal%60
    ttolmin=tTotal//60
    thour=ttolmin//60
    tmin=ttolmin%60
    runtime="Elapsed Time: %dh%dm%.2fs"%(thour,tmin,tsec)
    return runtime

def extract_numbers(cigar):
    return [int(num) for num in re.findall(r'\d+', cigar)]

def calculate_cigar_overlap(cigar1, cigar2):
    numbers1 = extract_numbers(cigar1)
    numbers2 = extract_numbers(cigar2)
    
    start1, start2 = numbers1[0], numbers2[0]

    #start1 不应该比 start2 大
    if start1 > start2:
        return 1000
    
    end1 = numbers1[0] + sum(numbers1[1:-1])
    end2 = numbers2[0] + sum(numbers2[1:-1])
    
    overlap = min(end1, end2) - max(start1, start2)
    return overlap

def calculate_cigar_overlap2(cigar1, cigar2, strand):
    numbers1 = extract_numbers(cigar1)
    numbers2 = extract_numbers(cigar2)
    if strand == '-':
        numbers2.reverse()
    start1, start2 = numbers1[0], numbers2[0]

    #start1 不应该比 start2 大
    if start1 < start2:
        return 1000
    
    end1 = numbers1[0] + sum(numbers1[1:-1])
    end2 = numbers2[0] + sum(numbers2[1:-1])
    overlap = min(end1, end2) - max(start1, start2)
    return overlap

if __name__ == "__main__":
    cigar1 = "41S30M15S"
    cigar2 = "45S36M5S"
    print(calculate_cigar_overlap2(cigar1,cigar2,"-"))