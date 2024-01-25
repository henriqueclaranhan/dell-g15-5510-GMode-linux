#!/usr/bin/python3
import os
import sys

# evevate privilages and run itself as root, use sudo
def elevate():
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

# check if the fan is turned on
def fanOn():
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
        print('acpi_call module not loaded')


# turn off GMode
def turnOff():
    print('turnign off')
    # echo "\_SB.AMWW.WMAX 0 0x15 {1, 0xa0, 0x00, 0x00}" > /proc/acpi/call
    # echo "\_SB.AMWW.WMAX 0 0x25 {1, 0x00, 0x00, 0x00}" > /proc/acpi/call
    # from https://wiki.archlinux.org/title/Dell_G15_5525

    try:
        with open('/proc/acpi/call', 'w') as acpi_call_0x15:
            acpi_call_0x15.write('\\_SB.AMWW.WMAX 0 0x15 {1, 0xa0, 0x00, 0x00}')
    except FileNotFoundError:
        print('acpi_call module not loaded')

    try:
        with open('/proc/acpi/call', 'w') as acpi_call_0x25:
            acpi_call_0x25.write('\\_SB.AMWW.WMAX 0 0x25 {1, 0x00, 0x00, 0x00}')
    except FileNotFoundError:
        print('acpi_call module not loaded')



# turn on GMode
def turnOn():
    print('turning on')
    # echo "\_SB.AMWW.WMAX 0 0x15 {1, 0xab, 0x00, 0x00}" > /proc/acpi/call
    # echo "\_SB.AMWW.WMAX 0 0x25 {1, 0x01, 0x00, 0x00}" > /proc/acpi/call
    # from https://wiki.archlinux.org/title/Dell_G15_5525

    try:
        with open('/proc/acpi/call', 'w') as acpi_call_0x15:
            acpi_call_0x15.write('\\_SB.AMWW.WMAX 0 0x15 {1, 0xab, 0x00, 0x00}')
    except FileNotFoundError:
        print('acpi_call module not loaded')

    try:
        with open('/proc/acpi/call', 'w') as acpi_call_0x25:
            acpi_call_0x25.write('\\_SB.AMWW.WMAX 0 0x25 {1, 0x01, 0x00, 0x00}')
    except FileNotFoundError:
        print('acpi_call module not loaded')

def main():
    # gain root privilages
    elevate()

    if fanOn():
        turnOff()
    else:
        turnOn()

if __name__ == "__main__":
    main()
