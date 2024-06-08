import paramiko
import subprocess
import time

def execute_ssh_command(ip, username, password, command):
    try:
        with paramiko.SSHClient() as ssh_client:
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh_client.connect(hostname=ip, username=username, password=password)
            stdin, stdout, stderr = ssh_client.exec_command(command)
            output = stdout.read().decode().strip()
            return output
    except paramiko.AuthenticationException:
        return "Authentication failed, please check your credentials."
    except paramiko.SSHException as ssh_err:
        return f"Unable to establish SSH connection: {ssh_err}"
    except Exception as e:
        return f"An error occurred: {str(e)}"

def check_ssh_status(ip, username, password):
    status = execute_ssh_command(ip, username, password, 'systemctl is-active ssh')
    return status

def enable_ssh_service(ip, username, password):
    enable_output = execute_ssh_command(ip, username, password, 'sudo systemctl enable ssh && sudo systemctl start ssh')
    return enable_output

def start_ssh_service():
    try:
        subprocess.run(['sudo', 'systemctl', 'start', 'ssh'], check=True)
        return "SSH service started successfully."
    except subprocess.CalledProcessError as e:
        return f"Error starting SSH service: {e}"

def power_on_server(ipmi_ip, ipmi_username, ipmi_password):
    # Logika untuk menyalakan server melalui IPMI atau solusi manajemen jarak jauh lainnya
    pass

if __name__ == "__main__":
    ip = '127.0.0.1'
    username = 'raspberry'
    password = '123'

    # Mengecek status SSH
    status = check_ssh_status(ip, username, password)

    if status == 'inactive':
        # Jika SSH tidak aktif, cobalah untuk menghidupkan server (misalnya melalui IPMI)
        ipmi_ip = 'ipmi_ip_address'
        ipmi_username = 'ipmi_username'
        ipmi_password = 'ipmi_password'

        power_on_server(ipmi_ip, ipmi_username, ipmi_password)

        # Tunggu beberapa saat untuk sistem menyala kembali, lalu coba aktifkan SSH
        # (Anda mungkin perlu menyesuaikan waktu menunggu sesuai dengan kebutuhan)
        time.sleep(5)  # Tunggu 60 detik (1 menit)

        # Coba aktifkan SSH lagi
        enable_output = enable_ssh_service(ip, username, password)
        print(enable_output)
    else:
        print("SSH is already active. Status:", status)

    # Coba juga untuk memulai kembali SSH jika belum aktif
    start_output = start_ssh_service()
    print(start_output)
