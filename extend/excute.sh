#!/usr/bin/expect


# set your username 
set USERNAME [lindex $argv 0]

# set your network passwd
set PASSWORD [lindex $argv 1]

#set your current user's passwd 
set CurrentUserPassWord [lindex $argv 2]

# Not show log in terminal,set log_user to 0,default is 1
log_user 0

# save login log to your home directory 
#log_file "~/.hautclient.log"

# set wait time which you had excuted spawn
set timeout 10

# login 
if { $USERNAME != "none" && $PASSWORD != "none"} {
	spawn sudo hautclient -u $USERNAME -p $PASSWORD -b
} else {
	spawn sudo hautclient -l
}

# set he filtering character
expect ":"

# sent your current user's passwd to terminal
send "$CurrentUserPassWord\r"
interact
	
# copy shortcut to /usr/share/applications/
if { [file exists $env(HOME)/Desktop/hautclient.desktop] && ![file exists /usr/share/applications/hautclient.desktop]} {
	spawn sudo cp $env(HOME)/Desktop/hautclient.desktop /usr/share/applications/
	expect ":"
	send "$CurrentUserPassWord\r"
} elseif { [file exists $env(HOME)/桌面/hautclient.desktop] && ![file exists /usr/share/applications/hautclient.desktop]} {
	spawn sudo cp $env(HOME)/桌面/hautclient.desktop /usr/share/applications
	expect ":"
	send "$CurrentUserPassWord\r"
} else {
	spawn echo 
}

# exit expect
interact
