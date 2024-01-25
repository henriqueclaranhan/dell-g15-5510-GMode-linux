# dell-g15-5510-GMode-linux

## works on DELL G15-5510 and DELL G15-5520

Python script to control dell GMode on linux

# Dependencies:
    acpi_call kernel module
    pkexec or sudo
    python

# Usage: 

execute script with absolute file path `python /home/{{user}}/.local/bin/g15-Gmode-linux.py`

# Bind to shortcut on KDE:

move python script to `~/.local/bin/`

System settings -> shortcuts -> add command

add command `konsole -e python ~/.local/bin/g15-Gmode-linux.py` and bind to F9

