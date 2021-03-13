#!/usr/bin/env python

#Author: Sujal Shah

import flicklib
import subprocess

global next_move
global prev_move
global last_command
global command_count

next_move = 'NS'
prev_move = 'SN'
last_command = ''
command_count = 0

def issue_xdo_command(command):

    global last_command
    last_command = command

    xdo_command = ['xdotool']

    if command == 'reload':
        xdo_command.append('key')
        xdo_command.append('--clearmodifiers')
        xdo_command.append('ctrl-r')
    else
        if command == 'next_desktop'
            xdo_command.append('set_desktop')
            xdo_command.append('--relative')
            xdo_command.append('1')
        elif command == 'prev_desktop'
            xdo_command.append('set_desktop')
            xdo_command.append('--relative')
            xdo_command.append('--')
            xdo_command.append('-1')

    if xdo_command.length() > 1:
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