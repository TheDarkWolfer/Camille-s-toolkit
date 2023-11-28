#create a function that returns the current mac address of the device

import subprocess

def get_mac_addr(interface="wlan0"):
    mac_addr = subprocess.check_output("ifconfig ## | grep ether | awk '{print $2}'".replace("##",interface), shell=True)
    mac_addr = mac_addr.decode('utf-8')
    mac_addr = mac_addr.replace('\n', '')
    return mac_addr

print(get_mac_addr())#;exit()

import time, pyautogui, datetime
iterations = 0
while True:
    last_mac_addr = get_mac_addr()
    time.sleep(0.1)
    if last_mac_addr != get_mac_addr():
        print(f"{get_mac_addr()} | Mac address has changed! | {datetime.datetime.now().strftime('%H:%M:%S')} | {iterations}",end="\r")
        pyautogui.alert("Mac address has changed!")
        break
    else:
        print(f"{get_mac_addr()} | Mac address has not changed! | {datetime.datetime.now().strftime('%H:%M:%S')} | {iterations}",end="\r")
    iterations += 1