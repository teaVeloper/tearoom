#!/bin/bash

chosen=$(echo -e "󰍃 Lock\n⏾ Suspend\n⏻ Shutdown\n Reboot\n Logout" | rofi -dmenu -i -p "Power")

case "$chosen" in
  *Lock) i3lock ;;
  *Suspend) systemctl suspend ;;
  *Shutdown) systemctl poweroff ;;
  *Reboot) systemctl reboot ;;
  *Logout) qtile cmd-obj -o cmd -f shutdown ;;
esac

