#!/bin/bash

ipaddr=`hostname -I | awk '{print $1}'`;
echo $ipaddr;

curl