#!/usr/bin/env python

#Author: Sujal Shah

import flicklib
import subprocess
import time

global next_move
global prev_move
global last_command
global command_count
global last_reload_time
global min_reload_interval

last_command = ''
command_count = 0
last_reload_time = time.time()

# Initialize mappings
next_move = 'SN'
prev_move = 'NS'
min_reload_interval = 2


def issue_xdo_command(command):

    global last_command
    global last_reload_time
    last_command = command

    xdo_command = ['xdotool']

    if command == 'reload' and (time.time()-last_reload_time) > min_reload_interval:
	last_reload_time = time.time()
        xdo_command.append('key')
        xdo_command.append('--clearmodifiers')
        xdo_command.append('ctrl+r')
    else:
        if command == 'next_desktop':
            xdo_command.append('set_desktop')
            xdo_command.append('--relative')
            xdo_command.append('1')
        elif command == 'prev_desktop':
            xdo_command.append('set_desktop')
            xdo_command.append('--relative')
            xdo_command.append('--')
            xdo_command.append('-1')

    if len(xdo_command) > 1:
        print('sending command: ', ' '.join(xdo_command))
        subprocess.call(xdo_command)


@flicklib.flick()
def flick(start,finish):
    move = start[0].upper() + finish[0].upper()
    if move == next_move:
        issue_xdo_command('next_desktop')
    elif move == prev_move:
        issue_xdo_command('prev_desktop')

@flicklib.airwheel()
def airwheel_gesture(delta):
    issue_xdo_command('reload')

def main():

    global command_count
    global last_command

    while True:
        command_count += 1
        time.sleep(0.1)


main()
