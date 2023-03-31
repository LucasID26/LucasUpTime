import requests
import time

# Definisikan URL yang akan dimonitor
url = "https://Asta-Robot.kulukgalak.repl.co"

# Set interval waktu untuk memeriksa URL (dalam detik)
interval = 60

# Set jumlah maksimum percobaan ulang URL yang akan dilakukan
max_retries = 3

# Set waktu tunggu antara setiap percobaan ulang URL (dalam detik)
retry_interval = 10

# Inisialisasi jumlah percobaan ulang URL yang telah dilakukan
retry_count = 0

# Loop utama
while True:
    # Lakukan permintaan GET ke URL
    response = requests.get(url)

    # Periksa status code dari respons
    if response.status_code == 200:
        print(f"{url} is up and running!")
        retry_count = 0
    else:
        print(f"{url} is down! Trying to restart ({retry_count+1}/{max_retries})...")
        retry_count += 1
        if retry_count >= max_retries:
            print(f"Max retries reached. Restarting {url}...")
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    print(f"{url} is up and running!")
                    retry_count = 0
                else:
                    print(f"Failed to restart {url}.")
            except:
                print(f"Failed to restart {url}.")
            retry_count = 0
        else:
            time.sleep(retry_interval)
            continue

    # Tunggu selama interval waktu sebelum memeriksa URL lagi
    time.sleep(interval)