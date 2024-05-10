#!/bin/bash

# Fungsi untuk mengeksekusi perintah SSH
execute_ssh_command() {
    sshpass -p "$2" ssh -o StrictHostKeyChecking=no "$1"@"$3" "$4"
}

# Variabel konfigurasi SSH
USERNAME="raspberry"
PASSWORD="123"
HOST="192.16.134.35"
COMMAND="ls -l"

# Panggil fungsi untuk mengeksekusi perintah SSH
execute_ssh_command "$USERNAME" "$PASSWORD" "$HOST" "$COMMAND"
