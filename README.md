# systemd_automation
For running .py scripts with systemd fail-proof, with shortcuts like in pm2


## 1) Enable crash-autorestart AND no-signal restart

`sudo nano /etc/systemd/system/my_scriptname.service`

fill and customize from: [script_name.service](https://github.com/normas/systemd_automation/blob/main/script_name.service)

python3 -m pip install pytest sdnotify
script_name.py should contain sdnotify watchdog signaling and be able to read its local yaml config file: [crash_test.py](https://github.com/normas/systemd_automation/blob/main/crash_test.py)


install module(s) system wide:\
`sudo /usr/bin/python3 -m pip install sdnotify`  
`sudo /usr/bin/python3 -m pip install redis`

## 2) Enable system reboot startup:
`sudo systemctl enable script_name.service`



## 3) sd2 helper:

wrapper for commands like:\
> sudo systemctl status all_of_my_scripts  
> sudo journalctl -u script_name.service -f --since "now"  
> sudo systemctl stop/start/restart script_name.service`  
    
`touch sd2.sh`  
fill and customize from from: [sd2.sh](https://github.com/normas/systemd_automation/blob/main/sd2.sh)



`sudo cp sd2.sh /usr/local/bin/sd2`\
`sudo chmod +x /usr/local/bin/sd2`\

usage:  
> sudo sd2 status | monit script | start/stop/restart script


## 4) Autocompletion for sd2 helper

`nano ~/.bash_completion`  
fill and customize from: [bash_completion](https://github.com/normas/systemd_automation/blob/main/bash_completion)  
`source ~/.bash_completion`  

i.e., when typing: sd2 monit my... + TAB - autocompletes
