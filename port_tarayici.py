import socket


target_ip = input("Hedef IP adresini girin: ")
start_port = int(input("Başlangıç portunu girin: "))
end_port = int(input("Bitiş portunu girin: "))

print("\nTarama başlatılıyor...")


for port in range(start_port, end_port + 1):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
        sock.settimeout(1)
        result = sock.connect_ex((target_ip, port))

        if result == 0:
            print(f"Port {port} açık")
        else:
            print(f"Port {port} kapalı")
        sock.close()
    except KeyboardInterrupt:
        print("\nKullanıcı tarafından durduruldu.")
        break
    except socket.error as err:
        print(f"Socket hatası: {err}")
        break

print("\nby ENTError")
input("\nTarama bitti. Çıkmak için ENTER'a basın...")

