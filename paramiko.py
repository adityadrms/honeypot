import paramiko

def ssh_command(hostname, username, password, command):
    # Inisialisasi klien SSH
    ssh_client = paramiko.SSHClient()
    # Setel kebijakan verifikasi host otomatis
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Koneksi ke host
        ssh_client.connect(hostname, username=username, password=password)

        # Eksekusi perintah SSH
        stdin, stdout, stderr = ssh_client.exec_command(command)

        # Baca output
        output = stdout.read().decode()

        # Cetak output
        print(output)

    except paramiko.AuthenticationException:
        print("Authentication failed, please verify your credentials")
    except paramiko.SSHException as sshException:
        print("Unable to establish SSH connection: %s" % sshException)
    finally:
        # Tutup koneksi
        ssh_client.close()

# Konfigurasi SSH
hostname = '192.168.134.35'
username = 'raspberry'
password = '123'
command = 'ls -l'

# Panggil fungsi untuk menjalankan perintah SSH
ssh_command(hostname, username, password, command)