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


#########
# Fix Users
#########

#!TODO audit Users, Admins, and Groups 

#########
# Fix Sudoers
#########

#TODO Remove NOPASSWD and #include. Also verify other sudo and wheel members

#########
# Stand up Firewalls
#########
