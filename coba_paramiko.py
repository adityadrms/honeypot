import paramiko

# Buat objek SSHClient
ssh = paramiko.SSHClient()

# Secara default, klien tidak akan terhubung ke host yang tidak dikenali
# Tetapi Anda dapat mengatur opsi yang memungkinkan untuk otomatis menambahkan host ke known_hosts
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Masukkan informasi koneksi SSH (ganti dengan info Raspberry Pi Anda)
hostname = '192.168.40.35'
username = 'raspberry'
password = '123'

try:
    # Ganti dengan informasi koneksi Anda
    hostname = 'alamat_IP_Raspberry_Pi'
    username = 'username_ssh'
    password = 'password_ssh'

    # Secara default, klien tidak akan terhubung ke host yang tidak dikenali
    # Tetapi Anda dapat mengatur opsi yang memungkinkan untuk otomatis menambahkan host ke known_hosts
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Terhubung ke host
    ssh.connect(hostname, username=username, password=password)
    print("Koneksi berhasil!")

    # Lakukan sesuatu setelah terhubung, misalnya eksekusi perintah
    stdin, stdout, stderr = ssh.exec_command('ls -l')

    # Baca output dari perintah
    print(stdout.read().decode())
except Exception as e:
    print("Koneksi gagal:", str(e))
finally:
    # Tutup koneksi SSH
    ssh.close()
