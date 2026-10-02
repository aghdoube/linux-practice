#!/bin/bash
clear 

echo " === STARTING DEPLOYMENT===" >> deploy.log
sudo apt-get update >> deploy.log
sudo apt-get install nginx -y  >> deploy.log
ps aux | grep "nginx" >> deploy.log 
echo " === Deployment finished on : $(date)" >> deploy.log 