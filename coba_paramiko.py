import paramiko
import paramiko.util

# Aktifkan debug
paramiko.util.log_to_file('paramiko.log')
paramiko.util.log_level(paramiko.util.DEBUG)

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
    # Coba melakukan koneksi
    ssh.connect(hostname, username=username, password=password)
    print("Koneksi berhasil!")
except Exception as e:
    print("Koneksi gagal:", str(e))
finally:
    # Tutup koneksi SSH
    ssh.close()
