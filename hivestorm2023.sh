#!/bin/bash

#######
# Name: Hivestorm 2023 script
# Goal: Secure both Ubuntu and Redhat low-hanging fruit
# By: Tristan Stapert (aka tbird)
# Credits: @Shane Donuhue and others for good inspiration
#######

#######
# Colors for clear output
#######

blue='\e[1m'
red='\033[1;31m'
yellow='\033[1;33m'
green='\033[1;32m'
nocolor='\e[m'

good="${green}[+] ${nocolor}"
prompt="${yellow}[?] ${nocolor}"
warn="${yellow}[!] ${nocolor}"
error="${red}[#] ${nocolor}"

########
# Common Variables
########

password_change="Password2@"

########
# Common Functions
########

confirm() {
    while true; do
        echo -en "\t$1 (y/n): "
        read
        case $REPLY in 
            [yY]) return 0;;
               *) return 1;;
        esac
    done
}

#########
# INIT
#########

clear

echo -e "\tWelcome to the quick and dirty script of Tbird. Hopefully this does something good!"
echo -e "\tThis does require an operator! please stand by"

if [[ $EUID -ne 0 ]]; then
    echo -e "${error} MUST BE RUN AS ROOT!"
    exit 1
fi

# DEBUG
#echo -e "${good} Welcome, root!"

#########
# Point Repositories at Repo.ialab.dsu.edu
# Then run a quick update so that later package installs go fast
#########
echo -e "${good}Correcting repositories based on system active system information."
os_version=$(cat /etc/os-release | awk -F= '/VERSION_CODENAME=/{print $2}');
os_id=$(cat /etc/os-release | awk -F= '/ID=/{print $2}');

if [ "$os_version" == "ubuntu" ]; then
    echo -e "${good}This is believed to be ubuntu. We are configuring the sources.list and moving source.list.d"
    repos="/etc/apt/sources.list"
    cp "$repos" "$repos.bak"
    mv "$repos.d" "$repos.d.bak"
    echo "deb http://repo.ialab.dsu.edu/ubuntu/ $os_id main restricted universe multiverse" > $repos
    echo "deb http://repo.ialab.dsu.edu/ubuntu/ $os_id-updates main restricted universe multiverse" >> $repos
    echo "deb http://repo.ialab.dsu.edu/ubuntu/ $os_id-backports main restricted universe multiverse" >> $repos
    echo "deb http://repo.ialab.dsu.edu/ubuntu/ $os_id-security main restricted universe multiverse" >> $repos

    
elif [ "$os_verison" == "fedora" ]; then
    echo -e "${good}This is believed to be fedora. We are configuring the /etc/yum.repos.d/"
    echo -e "${warn}Incomplete...."

else 
    echo -e "${error}Unexpected distribution. Script mishandle. DO REPO UPDATE BY HAND!!!!"
fi
    

#########
# Fix Users
#########

#!TODO audit Users, Admins, and Groups 
echo -e "${good}Moving onto User Auditing

#########
# Fix Sudoers
#########

#TODO Remove NOPASSWD and #include. Also verify other sudo and wheel members

#########
# Stand up Firewalls
#########
