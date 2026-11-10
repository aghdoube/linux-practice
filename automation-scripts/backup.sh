#!/bin/bash

if [ -z "$1" ] 
then echo "Usage: ./backup.sh <folder>"
	exit 1
fi

if [ ! -d "$1" ]
then echo "Folder does not exist"
	exit 1
fi 

BACKUP="backup_$1"

mkdir -p "$BACKUP"

cp "$1"/* "$BACKUP"

if [ $? -ne 0 ]
then echo "Error encountered during the backup process"
	exit 1
else
	echo "Backup executed successfully"
	exit 0
fi
