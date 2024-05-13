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

# Terhubung ke host
ssh.connect(hostname, username=username, password=password)

# Lakukan sesuatu setelah terhubung, misalnya eksekusi perintah
stdin, stdout, stderr = ssh.exec_command('ls -l')

# Baca output dari perintah
print(stdout.read().decode())

# Tutup koneksi SSH
ssh.close()