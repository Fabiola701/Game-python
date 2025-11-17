import json
import random

STAT_DASAR = ("Cyber-Runner", 100, "Pemula")

def get_data_pemain_baru():
    return {
        "username": "",
        "hp": 100,
        "hp_maks": 100,
        "xp": 0,
        "kredit": 50,
        "area_sekarang": "Lab Rahasia",
        "kekuatan_terbuka": ["Pyrobyte"],
        "inventori": ["Stimpack"],
        "area_terjelajahi": ["Lab Rahasia"],
        "musuh_dikalahkan": []
    }

data_pemain = get_data_pemain_baru()

def tampilkan_judul():
    print("\n" + "="*60)
    print("""
    ███╗   ██╗███████╗ ██████╗ ███╗   ██╗
    ████╗  ██║██╔════╝██╔═══██╗████╗  ██║
    ██╔██╗ ██║█████╗   ██║   ██║██╔██╗ ██║
    ██║╚██╗██║██╔══╝   ██║   ██║██║╚██╗██║
    ██║ ╚████║███████╗╚██████╔╝██║ ╚████║
    ╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝
          ASCENT: Protokol Peninggalan Cyber
    """)
    print("="*60 + "\n")

def simpan_game():
    try:
        with open("simpanan_neon.json", "w") as f:
            json.dump(data_pemain, f, indent=4)
        print("[SISTEM]: Game berhasil disimpan.")
    except Exception as e:
        print(f"[ERROR]: Penyimpanan gagal: {e}")

def muat_game():
    global data_pemain
    try:
        with open("simpanan_neon.json", "r") as f:
            data_pemain = json.load(f)
        print("[SISTEM]: Game berhasil dimuat.")
        return True
    except FileNotFoundError:
        print("[SISTEM]: Tidak ada file simpanan.")
        return False
    except Exception as e:
        print(f"[ERROR]: Pemuatan gagal: {e}")
        return False

def inisialisasi_pemain():
    global data_pemain
    data_pemain = get_data_pemain_baru()
    
    while True:
        nama = input("> Masukkan designasi Runner: ").strip()
        if nama:
            data_pemain['username'] = nama
            break
        else:
            print("[ERROR]: Designasi tidak valid.")
    
    print(f"\nSelamat datang, {data_pemain['username']}.")
    print(f"Status: {STAT_DASAR[0]} | HP: {data_pemain['hp_maks']}")
    print(f"Kekuatan Awal: {', '.join(data_pemain['kekuatan_terbuka'])}")

def tampilkan_statistik():
    print("\n" + "─"*30)
    print(f"RUNNER: {data_pemain['username']}")
    print(f"HP: {data_pemain['hp']} / {data_pemain['hp_maks']}")
    print(f"XP: {data_pemain['xp']} | Kredit: {data_pemain['kredit']}¢")
    print(f"Lokasi: {data_pemain['area_sekarang']}")
    
    print("\nKEKUATAN:")
    if not data_pemain['kekuatan_terbuka']:
        print("  [KOSONG]")
    else:
        for i, k in enumerate(data_pemain['kekuatan_terbuka'], 1):
            print(f"  {i}. {k}")
    
    print("\nINVENTORI:")
    if not data_pemain['inventori']:
        print("  [KOSONG]")
    else:
        for item in data_pemain['inventori']:
            print(f"  • {item}")
    print("─"*30 + "\n")

def pertarungan(nama_musuh, hp_musuh):
    print(f"\n[PERINGATAN!] {nama_musuh} terdeteksi! (HP: {hp_musuh})")
    
    while hp_musuh > 0 and data_pemain['hp'] > 0:
        print(f"\nHP Anda: {data_pemain['hp']} | HP Musuh: {hp_musuh}")
        print("Aksi: 1. Serang, 2. Gunakan Stimpack, 3. Kabur")
        pilihan = input("> ").strip()

        if pilihan == "1":
            if not data_pemain['kekuatan_terbuka']:
                print("Anda tidak punya kekuatan! Serangan gagal.")
                damage = 0
            else:
                print("Pilih kekuatan:")
                for i, k in enumerate(data_pemain['kekuatan_terbuka'], 1):
                    print(f"  {i}. {k}")
                try:
                    p_kekuatan = int(input("> ")) - 1
                    if 0 <= p_kekuatan < len(data_pemain['kekuatan_terbuka']):
                        kekuatan_dipilih = data_pemain['kekuatan_terbuka'][p_kekuatan]
                        print(f"\nMenggunakan {kekuatan_dipilih}!")
                        damage = random.randint(20, 35)
                        hp_musuh -= damage
                        print(f"Anda memberi {damage} damage!")
                    else:
                        print("Pilihan tidak valid.")
                        continue
                except ValueError:
                    print("Input tidak valid.")
                    continue
            
            if hp_musuh <= 0:
                break
                
            damage_musuh = random.randint(10, 20)
            data_pemain['hp'] -= damage_musuh
            print(f"{nama_musuh} menyerang balik! -{damage_musuh} HP")

        elif pilihan == "2":
            if "Stimpack" in data_pemain['inventori']:
                data_pemain['inventori'].remove("Stimpack")
                data_pemain['hp'] = min(data_pemain['hp_maks'], data_pemain['hp'] + 40)
                print(f"HP dipulihkan ke {data_pemain['hp']}.")
            else:
                print("Tidak punya Stimpack!")
                
        elif pilihan == "3":
            print("Anda berhasil kabur...")
            return False
    
    if data_pemain['hp'] <= 0:
        print("\n[FLATLINE]: Sistem Anda gagal...")
        return False
    
    if hp_musuh <= 0:
        print(f"\n[KEMENANGAN!] {nama_musuh} dinetralkan.")
        xp_dapat = random.randint(15, 30)
        kredit_dapat = random.randint(20, 40)
        data_pemain['xp'] += xp_dapat
        data_pemain['kredit'] += kredit_dapat
        data_pemain['musuh_dikalahkan'].append(nama_musuh)
        print(f"+{xp_dapat} XP | +{kredit_dapat}¢")
        return True

def jelajahi_area():
    area_list = ["Distrik Neon", "Vault Data", "Menara Skyline", "Plaza OmniCore"]
    print("\nPilih area untuk dijelajahi:")
    for i, a in enumerate(area_list, 1):
        status = "✓" if a in data_pemain['area_terjelajahi'] else " "
        print(f" {i}. [{status}] {a}")

    try:
        pilihan = int(input("> ")) - 1
        if not 0 <= pilihan < len(area_list):
            print("Lokasi tidak valid.")
            return
    except ValueError:
        print("Input tidak valid.")
        return

    nama_area = area_list[pilihan]
    data_pemain['area_sekarang'] = nama_area
    if nama_area not in data_pemain['area_terjelajahi']:
        data_pemain['area_terjelajahi'].append(nama_area)

    print(f"\n[MEMASUKI]: {nama_area}...")
    
    pertemuan = random.choice(["pertarungan", "jarahan", "tidak_ada"])

    if pertemuan == "pertarungan":
        musuh = random.choice(["Penjaga Korporasi", "AI Nakal", "Drone Keamanan"])
        pertarungan(musuh, random.randint(40, 60))
    elif pertemuan == "jarahan":
        bonus = random.randint(30, 50)
        data_pemain['kredit'] += bonus
        print(f"\n[PENEMUAN]: Menemukan {bonus} kredit!")
    else:
        print("\n[SCAN]: Area bersih. Tidak ada ancaman terdeteksi.")

    if "Cryostream" not in data_pemain['kekuatan_terbuka'] and data_pemain['xp'] >= 50:
        data_pemain['kekuatan_terbuka'].append("Cryostream")
        print("\n[TEROBOSAN]: Kekuatan cyber baru terbuka - Cryostream!")
        data_pemain['xp'] -= 50

def pasar_gelap():
    print("\n[PASAR GELAP]: Pedagang teduh mendekat...")
    print(f"Kredit Anda: {data_pemain['kredit']}¢\n")
    print("1. Stimpack - 40¢")
    print("2. Upgrade HP Maks (+20) - 100¢")
    print("3. Pergi")
    
    toko = input("\n> ").strip()
    if toko == "1":
        if data_pemain['kredit'] >= 40:
            data_pemain['kredit'] -= 40
            data_pemain['inventori'].append("Stimpack")
            print("[DIBELI]: Stimpack diperoleh.")
        else:
            print("Kredit tidak cukup.")
    elif toko == "2":
        if data_pemain['kredit'] >= 100:
            data_pemain['kredit'] -= 100
            data_pemain['hp_maks'] += 20
            print(f"[DIBELI]: HP Maks kini {data_pemain['hp_maks']}.")
        else:
            print("Kredit tidak cukup.")
    else:
        print("Pedagang mengangguk dan menghilang...")

def misi_akhir():
    print("\n[MISI AKHIR]: Anda menemukan vault OmniCore...")
    
    if len(data_pemain['kekuatan_terbuka']) < 2 or data_pemain['xp'] < 100:
        print("[TERBLOKIR]: Anda perlu lebih banyak kekuatan (min 2) dan pengalaman (min 100 XP).")
        print(f"Saat ini: {len(data_pemain['kekuatan_terbuka'])} kekuatan, {data_pemain['xp']} XP")
        return False

    print("Sebuah AI Guardian Elite menghalangi jalan!")
    if pertarungan("AI Guardian Elite", 150):
        print("\n" + "="*60)
        print("[PENINGGALAN CYBER DIPEROLEH]")
        print(f"Selamat, {data_pemain['username']}! Anda telah menyelamatkan Neonhaven.")
        print(f"XP Akhir: {data_pemain['xp']}")
        print(f"Musuh Dikalahkan: {len(data_pemain['musuh_dikalahkan'])}")
        print("="*60 + "\n")
        return True
    else:
        print("\n[MISI GAGAL]: Anda dikalahkan oleh Guardian...")
        return False

def menu_utama():
    tampilkan_judul()
    while True:
        print("1. Mulai Game Baru\n2. Muat Game\n3. Keluar Sistem")
        pilihan = input("> ").strip()
        
        if pilihan == "1":
            inisialisasi_pemain()
            loop_game()
            break
        elif pilihan == "2":
            if muat_game():
                loop_game()
                break
        elif pilihan == "3":
            print("\n[SISTEM]: Koneksi diputus.")
            break
        else:
            print("[ERROR]: Perintah tidak valid.\n")

def loop_game():
    game_aktif = True
    while game_aktif and data_pemain['hp'] > 0:
        print("\n" + "▼"*30 + "\nTERMINAL PERINTAH")
        print("1. Lihat Status")
        print("2. Jelajahi Area")
        print("3. Kunjungi Pasar Gelap")
        print("4. Cari Peninggalan Cyber (MISI AKHIR)")
        print("5. Simpan Game")
        print("6. Keluar Game")
        print("─"*30)
        
        aksi = input("\n> ").strip()

        if aksi == "1":
            tampilkan_statistik()
        elif aksi == "2":
            jelajahi_area()
        elif aksi == "3":
            pasar_gelap()
        elif aksi == "4":
            if misi_akhir():
                game_aktif = False
        elif aksi == "5":
            simpan_game()
        elif aksi == "6":
            print("\n[SISTEM]: Memutuskan tautan neural...")
            game_aktif = False
        else:
            print("[ERROR]: Perintah tidak dikenali.")
    
    if data_pemain['hp'] <= 0:
        print("\n[GAME OVER]: Anda telah flatline.")

if __name__ == "__main__":
    try:
        menu_utama()
    except KeyboardInterrupt:
        print("\n\n[PEMUTUSAN DARURAT]")
    finally:
        print("\n[SHUTDOWN SELESAI]\n")