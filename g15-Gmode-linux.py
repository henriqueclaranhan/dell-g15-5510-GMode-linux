#!/usr/bin/python3
# ACPI methods from https://wiki.archlinux.org/title/Dell_G15_5525

import os
import sys

MODULE_NOT_LOADED_MSG = 'acpi_call module not loaded'

def gainRootPrivileges():
    if os.getuid() == 0:
        return

    args = [sys.executable] + sys.argv
    commands = []

    # uncomment below line to use sudo instead of pkexec
    # commands.append(["sudo"] + args)

    # comment out below line to use sudo instad of pkexec
    commands.append(["pkexec"] + args)

    for args in commands:
        os.execlp(args[0], *args)

def isFanOn():
    try:
        with open('/proc/acpi/call', 'w') as fanStatus:
            fanStatus.write('\\_SB.AMWW.WMAX 0 0x14 {0x0b, 0x00, 0x00, 0x00}')
        with open('/proc/acpi/call', 'r') as fanStatus:
            fanStatus = fanStatus.read()
            print(fanStatus)
            fanStatus = fanStatus[:4]
            if fanStatus == '0xab':
                return True
            else:
                return False

    except:
        print(MODULE_NOT_LOADED_MSG)


def turnOffFan():
    print('turnign off')

    try:
        with open('/proc/acpi/call', 'w') as acpi_call_0x15:
            acpi_call_0x15.write('\\_SB.AMWW.WMAX 0 0x15 {1, 0xa0, 0x00, 0x00}')
    except FileNotFoundError:
        print(MODULE_NOT_LOADED_MSG)

    try:
        with open('/proc/acpi/call', 'w') as acpi_call_0x25:
            acpi_call_0x25.write('\\_SB.AMWW.WMAX 0 0x25 {1, 0x00, 0x00, 0x00}')
    except FileNotFoundError:
        print(MODULE_NOT_LOADED_MSG)


def turnOnFan():
    print('turning on')

    try:
        with open('/proc/acpi/call', 'w') as acpi_call_0x15:
            acpi_call_0x15.write('\\_SB.AMWW.WMAX 0 0x15 {1, 0xab, 0x00, 0x00}')
    except FileNotFoundError:
        print(MODULE_NOT_LOADED_MSG)

    try:
        with open('/proc/acpi/call', 'w') as acpi_call_0x25:
            acpi_call_0x25.write('\\_SB.AMWW.WMAX 0 0x25 {1, 0x01, 0x00, 0x00}')
    except FileNotFoundError:
        print(MODULE_NOT_LOADED_MSG)

def main():
    gainRootPrivileges()

    if isFanOn():
        turnOffFan()
    else:
        turnOnFan()

if __name__ == "__main__":
    main()
