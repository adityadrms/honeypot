import subprocess

def create_crontab_entry():
    # Command to add to crontab
    command = '0 * * * * /usr/bin/python3 /home/raspberry/honeypot/service_ssh.py'

    # Get the current crontab
    result = subprocess.run(['crontab', '-l'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    current_crontab = result.stdout

    # Check if the command is already in the crontab
    if command not in current_crontab:
        # Append the new command to the current crontab
        new_crontab = current_crontab + command + '\n'

        # Write the new crontab
        subprocess.run(['crontab', '-'], input=new_crontab, text=True)
        print('Crontab entry added.')
    else:
        print('Crontab entry already exists.')

if __name__ == '__main__':
    create_crontab_entry()
