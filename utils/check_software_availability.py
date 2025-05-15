#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import subprocess

def check_software_availability(softwares):
    green_tick = '\033[92m\u2713\033[0m'
    red_cross = '\033[91m\u2717\033[0m'
    missing_softwares = []

    for software in softwares:
        try:
            p = subprocess.run(f'command -v {software}',
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=True,
                shell=True
            )
            #print(f"{green_tick} {software.ljust(10)}\tPATH:{p.stdout.decode('utf-8')}", end='')
        except subprocess.CalledProcessError as e:
            missing_softwares.append(software)
            print(f"{red_cross} {software.ljust(10)}\tNot Found!")

    if missing_softwares:
        print("\nMissing software:", ", ".join(missing_softwares))
        return False

    return True