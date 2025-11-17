import random
import time
import os

# ==================== STRUKTUR DATA GAME ====================

# TUPLE: Statistik dasar pemain (immutable/tidak berubah)
STAT_DASAR = ("Cyber-Runner", 100, "Pemula")  # (kelas, hp_maks, pangkat)

# LIST: Kekuatan cyber pemain yang sudah terbuka (mutable/dapat berubah)
kekuatan_terbuka = []

# SET: Musuh unik yang sudah dikalahkan dan area yang sudah dijelajahi
musuh_dikalahkan = set()
area_terjelajahi = set()

# Inventori pemain (LIST)
inventori = []

# Statistik pemain (dapat berubah)
data_pemain = {
    "username": "",
    "hp": 100,
    "xp": 0,
    "kredit": 50,
    "area_sekarang": "Lab Rahasia",
    "penggunaan_kekuatan": {"Pyrobyte": 0, "Cryostream": 0, "Aerosurge": 0, "Terracode": 0}
}

# ==================== SENI ASCII ====================

def tampilkan_judul():
    print("\n" + "="*60)
    print("""
    ███╗   ██╗███████╗ ██████╗ ███╗   ██╗
    ████╗  ██║██╔════╝██╔═══██╗████╗  ██║
    ██╔██╗ ██║█████╗  ██║   ██║██╔██╗ ██║
    ██║╚██╗██║██╔══╝  ██║   ██║██║╚██╗██║
    ██║ ╚████║███████╗╚██████╔╝██║ ╚████║
    ╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝
         ASCENT: Protokol Peninggalan Cyber
    """)
    print("="*60 + "\n")

def tampilkan_seni_kekuatan(kekuatan):
    seni = {
        "Pyrobyte": "🔥 [SISTEM TERMAL AKTIF]",
        "Cryostream": "❄️ [PROTOKOL CRYO TERLIBAT]",
        "Aerosurge": "🌪️ [PENDORONG KECEPATAN ONLINE]",
        "Terracode": "🪨 [MATRIKS PERTAHANAN DIKERAHKAN]"
    }
    print(f"\n{seni.get(kekuatan, '')}\n")

# ==================== PENANGANAN FILE ====================

def simpan_game():
    """Simpan kemajuan pemain ke file"""
    try:
        with open("neon_ascent_simpanan.txt", "w", encoding="utf-8") as f:
            f.write(f"USERNAME:{data_pemain['username']}\n")
            f.write(f"HP:{data_pemain['hp']}\n")
            f.write(f"XP:{data_pemain['xp']}\n")
            f.write(f"KREDIT:{data_pemain['kredit']}\n")
            f.write(f"AREA:{data_pemain['area_sekarang']}\n")
            f.write(f"KEKUATAN:{','.join(kekuatan_terbuka)}\n")
            f.write(f"INVENTORI:{','.join(inventori)}\n")
            f.write(f"DIKALAHKAN:{','.join(musuh_dikalahkan)}\n")
            f.write(f"TERJELAJAHI:{','.join(area_terjelajahi)}\n")
            
            # Simpan penggunaan kekuatan untuk menentukan akhir
            penggunaan = ','.join([f"{k}:{v}" for k, v in data_pemain['penggunaan_kekuatan'].items()])
            f.write(f"PENGGUNAAN:{penggunaan}\n")
        
        print("\n[SISTEM]: Game berhasil disimpan. Data terenkripsi.")
        time.sleep(1)
        return True
    except Exception as e:
        print(f"\n[ERROR]: Penyimpanan gagal - {e}")
        return False
    
def muat_game():
    """Muat kemajuan pemain dari file"""
    try:
        with open("neon_ascent_simpanan.txt", "r", encoding="utf-8") as f:
            for line in f:
                kunci, nilai = line.strip().split(":", 1)
                
                if kunci == "USERNAME":
                    data_pemain['username'] = nilai
                elif kunci == "HP":
                    data_pemain['hp'] = int(nilai)
                elif kunci == "XP":
                    data_pemain['xp'] = int(nilai)
                elif kunci == "KREDIT":
                    data_pemain['kredit'] = int(nilai)
                elif kunci == "AREA":
                    data_pemain['area_sekarang'] = nilai
                elif kunci == "KEKUATAN":
                    kekuatan_terbuka.clear()
                    if nilai:
                        kekuatan_terbuka.extend(nilai.split(','))
                elif kunci == "INVENTORI":
                    inventori.clear()
                    if nilai:
                        inventori.extend(nilai.split(','))
                elif kunci == "DIKALAHKAN":
                    musuh_dikalahkan.clear()
                    if nilai:
                        musuh_dikalahkan.update(nilai.split(','))
                elif kunci == "TERJELAJAHI":
                    area_terjelajahi.clear()
                    if nilai:
                        area_terjelajahi.update(nilai.split(','))
                elif kunci == "PENGGUNAAN":
                    if nilai:
                        for pasangan in nilai.split(','):
                            kekuatan, jumlah = pasangan.split(':')
                            data_pemain['penggunaan_kekuatan'][kekuatan] = int(jumlah)
        
        print("\n[SISTEM]: File simpanan dimuat. Selamat datang kembali, Runner.")
        time.sleep(1)
        return True
    except FileNotFoundError:
        print("\n[SISTEM]: Tidak ada file simpanan terdeteksi.")
        time.sleep(1)
        return False
    except Exception as e:
        print(f"\n[ERROR]: Pemuatan gagal - {e}")
        return False

# ==================== FUNGSI INTI GAME ====================

def cetak_lambat(teks, jeda=0.03):
    """Cetak teks dengan efek mengetik"""
    for karakter in teks:
        print(karakter, end='', flush=True)
        time.sleep(jeda)
    print()

def inisialisasi_pemain():
    """Atur pemain baru"""
    print("\n[ANTARMUKA NEURAL MENGINISIALISASI...]")
    time.sleep(1)
    
    # Simulasi DO-WHILE: Dijamin dieksekusi sekali, lalu berulang jika tidak valid
    nama_valid = False
    while not nama_valid:
        nama = input("\n> Masukkan designasi Runner: ").strip()
        if nama:
            data_pemain['username'] = nama
            nama_valid = True
        else:
            print("[ERROR]: Designasi tidak valid. Coba lagi.")
    
    cetak_lambat(f"\n[DIKONFIRMASI]: Selamat datang, {data_pemain['username']}.")
    cetak_lambat(f"[STATUS]: Kelas: {STAT_DASAR[0]} | HP Maks: {STAT_DASAR[1]} | Pangkat: {STAT_DASAR[2]}")
    
    # Berikan kekuatan awal
    kekuatan_terbuka.extend(["Pyrobyte", "Cryostream"])
    inventori.append("Stimpack Neural")
    
    print(f"\n[KEKUATAN CYBER TERBUKA]: {', '.join(kekuatan_terbuka)}")
    time.sleep(1)

def tampilkan_statistik():
    """Tampilkan status pemain saat ini menggunakan loop FOR"""
    print("\n" + "─"*50)
    print(f"RUNNER: {data_pemain['username']} | HP: {data_pemain['hp']}/{STAT_DASAR[1]}")
    print(f"XP: {data_pemain['xp']} | Kredit: {data_pemain['kredit']}¢")
    print(f"Lokasi: {data_pemain['area_sekarang']}")
    
    # LOOP FOR: Tampilkan kekuatan yang terbuka
    print("\nKEKUATAN CYBER:")
    for i, kekuatan in enumerate(kekuatan_terbuka, 1):
        print(f"  {i}. {kekuatan}")
    
    # LOOP FOR: Tampilkan inventori
    print("\nINVENTORI:")
    if inventori:
        for item in inventori:
            print(f"  • {item}")
    else:
        print("  [KOSONG]")
    
    # Tampilkan data SET
    print(f"\nMusuh Dikalahkan: {len(musuh_dikalahkan)}")
    print(f"Area Terjelajahi: {len(area_terjelajahi)}")
    print("─"*50 + "\n")

def gunakan_kekuatan_cyber(nama_kekuatan):
    """Lacak penggunaan kekuatan untuk ending"""
    if nama_kekuatan in data_pemain['penggunaan_kekuatan']:
        data_pemain['penggunaan_kekuatan'][nama_kekuatan] += 1

def pertarungan(nama_musuh, hp_musuh):
    """Sistem pertarungan menggunakan kekuatan cyber"""
    print(f"\n[PERINGATAN!] {nama_musuh} terdeteksi!")
    print(f"HP Musuh: {hp_musuh}\n")
    
    while hp_musuh > 0 and data_pemain['hp'] > 0:
        print("Pilih aksi:")
        print("1. Serang dengan Kekuatan Cyber")
        print("2. Gunakan Item")
        print("3. Kabur")
        
        pilihan = input("\n> ").strip()
        
        if pilihan == "1":
            # Tampilkan kekuatan tersedia menggunakan loop FOR
            print("\nPilih Kekuatan Cyber:")
            for i, kekuatan in enumerate(kekuatan_terbuka, 1):
                print(f"{i}. {kekuatan}")
            
            try:
                pilihan_kekuatan = int(input("\n> ")) - 1
                if 0 <= pilihan_kekuatan < len(kekuatan_terbuka):
                    kekuatan_dipilih = kekuatan_terbuka[pilihan_kekuatan]
                    tampilkan_seni_kekuatan(kekuatan_dipilih)
                    gunakan_kekuatan_cyber(kekuatan_dipilih)
                    
                    # Damage berbeda berdasarkan kekuatan
                    damage = random.randint(20, 35)
                    hp_musuh -= damage
                    
                    print(f"[KENA!] Anda memberi {damage} damage!")
                    print(f"HP Musuh: {max(0, hp_musuh)}")
                    
                    if hp_musuh > 0:
                        damage_musuh = random.randint(10, 20)
                        data_pemain['hp'] -= damage_musuh
                        print(f"\n[DAMAGE DITERIMA] {nama_musuh} menyerang balik! -{damage_musuh} HP")
                        print(f"HP Anda: {data_pemain['hp']}")
                else:
                    print("[ERROR]: Pilihan kekuatan tidak valid.")
                    continue
            except (ValueError, IndexError):
                print("[ERROR]: Input tidak valid.")
                continue
                
        elif pilihan == "2":
            if "Stimpack Neural" in inventori:
                data_pemain['hp'] = min(STAT_DASAR[1], data_pemain['hp'] + 30)
                inventori.remove("Stimpack Neural")
                print("\n[ITEM DIGUNAKAN] +30 HP dipulihkan!")
            else:
                print("\n[ERROR]: Tidak ada item tersedia.")
                continue
                
        elif pilihan == "3":
            print("\n[MUNDUR]: Anda melarikan diri ke dalam bayangan...")
            return False
        
        time.sleep(1)
    
    if data_pemain['hp'] <= 0:
        print("\n[KRITIS]: Sistem gagal...")
        return False
    
    # Kemenangan
    musuh_dikalahkan.add(nama_musuh)
    xp_dapat = random.randint(15, 30)
    kredit_dapat = random.randint(20, 40)
    data_pemain['xp'] += xp_dapat
    data_pemain['kredit'] += kredit_dapat
    
    print(f"\n[KEMENANGAN!] {nama_musuh} dinetralkan.")
    print(f"+{xp_dapat} XP | +{kredit_dapat}¢")
    
    # Drop barang acak
    if random.random() > 0.5:
        jarahan = random.choice(["Modul Teknologi", "Chip Data", "Stimpack Neural"])
        inventori.append(jarahan)
        print(f"[JARAHAN]: Menemukan {jarahan}!")
    
    time.sleep(2)
    return True

def tantangan_puzzle():
    """Puzzle hacking yang membutuhkan kekuatan cyber spesifik"""
    print("\n[SISTEM TERKUNCI]: Enkripsi lanjutan terdeteksi.")
    print("Sebuah firewall menghalangi jalan Anda. Pilih pendekatan:\n")
    
    print("1. Pyrobyte - Bakar firewall")
    print("2. Cryostream - Bekukan protokol keamanan")
    print("3. Brute force - Coba bypass manual")
    
    pilihan = input("\n> ").strip()
    
    if pilihan == "1" and "Pyrobyte" in kekuatan_terbuka:
        tampilkan_seni_kekuatan("Pyrobyte")
        gunakan_kekuatan_cyber("Pyrobyte")
        cetak_lambat("[SUKSES]: Firewall meleleh. Akses diberikan.")
        data_pemain['xp'] += 20
        return True
    elif pilihan == "2" and "Cryostream" in kekuatan_terbuka:
        tampilkan_seni_kekuatan("Cryostream")
        gunakan_kekuatan_cyber("Cryostream")
        cetak_lambat("[SUKSES]: Keamanan dibekukan. Akses diberikan.")
        data_pemain['xp'] += 20
        return True
    else:
        print("\n[GAGAL]: Alarm terpicu! Lockdown sistem dimulai.")
        time.sleep(1)
        return pertarungan("Drone Keamanan", 40)

def jelajahi_area(nama_area):
    """Eksplorasi area dengan pertemuan acak"""
    data_pemain['area_sekarang'] = nama_area
    area_terjelajahi.add(nama_area)
    
    print(f"\n[MEMASUKI]: {nama_area}")
    cetak_lambat("Hujan mengalir di gedung-gedung berlampu neon. Hologram berkelap-kelip di kejauhan...")
    
    # Pertemuan acak
    pertemuan = random.choice(["pertarungan", "puzzle", "jarahan", "tidak_ada"])
    
    if pertemuan == "pertarungan":
        musuh = ["Penjaga Korporasi", "AI Nakal", "Drone Keamanan", "Netrunner"]
        musuh_dipilih = random.choice(musuh)
        pertarungan(musuh_dipilih, random.randint(40, 60))
    elif pertemuan == "puzzle":
        tantangan_puzzle()
    elif pertemuan == "jarahan":
        temuan = random.choice(["Modul Teknologi", "Cache Kredit", "Core Kekuatan"])
        if temuan == "Cache Kredit":
            bonus = random.randint(30, 50)
            data_pemain['kredit'] += bonus
            print(f"\n[PENEMUAN]: Menemukan {bonus} kredit!")
        else:
            inventori.append(temuan)
            print(f"\n[PENEMUAN]: Menemukan {temuan}!")
    else:
        print("\n[SCAN]: Area bersih. Tidak ada ancaman terdeteksi.")
    
    time.sleep(2)

def buka_kekuatan_baru():
    """Buka kekuatan tersisa melalui progres cerita"""
    tersisa = ["Aerosurge", "Terracode"]
    tersedia = [k for k in tersisa if k not in kekuatan_terbuka]
    
    if tersedia and data_pemain['xp'] >= 50:
        kekuatan_baru = tersedia[0]
        kekuatan_terbuka.append(kekuatan_baru)
        print(f"\n[TEROBOSAN]: Kekuatan cyber baru terbuka - {kekuatan_baru}!")
        tampilkan_seni_kekuatan(kekuatan_baru)
        time.sleep(2)
        return True
    return False

def tentukan_akhir():
    """Beberapa ending berdasarkan kekuatan yang paling banyak digunakan"""
    penggunaan = data_pemain['penggunaan_kekuatan']
    paling_digunakan = max(penggunaan, key=penggunaan.get)
    
    print("\n" + "="*60)
    cetak_lambat("[PENINGGALAN CYBER DIPEROLEH]")
    print("="*60 + "\n")
    
    akhir = {
        "Pyrobyte": "Anda menyalurkan kekuatan Peninggalan melalui api, membersihkan sistem kontrol OmniCore. Megakorporasi terbakar, dan kebebasan bangkit dari abu.",
        "Cryostream": "Anda membekukan kode Peninggalan, menjaganya untuk dipelajari. Dengan presisi dingin, Anda mengungkap korupsi OmniCore. Keadilan, disajikan sedingin es.",
        "Aerosurge": "Bergerak lebih cepat dari pikiran, Anda mendistribusikan data Peninggalan ke seluruh Net. Informasi ingin bebas—dan sekarang sudah bebas.",
        "Terracode": "Anda memperkuat Peninggalan dalam vault yang tak tertembus. OmniCore tidak akan pernah mendapatkannya. Terkadang, pertahanan terkuat adalah serangan terbaik."
    }
    
    cetak_lambat(f"\n{akhir.get(paling_digunakan, akhir['Pyrobyte'])}")
    print(f"\nKekuatan Dominan: {paling_digunakan}")
    print(f"XP Akhir: {data_pemain['xp']}")
    print(f"Kredit: {data_pemain['kredit']}¢")
    print(f"Musuh Dikalahkan: {len(musuh_dikalahkan)}")
    print(f"Area Terjelajahi: {len(area_terjelajahi)}")
    print("\n[TRANSMISI BERAKHIR]\n")

# ==================== LOOP GAME UTAMA ====================

def menu_utama():
    """Menu utama dengan loop WHILE"""
    tampilkan_judul()
    
    # LOOP WHILE: Navigasi menu utama
    while True:
        print("╔════════════════════════════╗")
        print("║      TERMINAL UTAMA        ║")
        print("╠════════════════════════════╣")
        print("║  1. Mulai Game Baru        ║")
        print("║  2. Muat Game              ║")
        print("║  3. Keluar Sistem          ║")
        print("╚════════════════════════════╝\n")
        
        pilihan = input("> ").strip()
        
        if pilihan == "1":
            inisialisasi_pemain()
            loop_game()
            break
        elif pilihan == "2":
            if muat_game():
                loop_game()
            else:
                print("Memulai game baru...")
                time.sleep(1)
                inisialisasi_pemain()
                loop_game()
            break
        elif pilihan == "3":
            cetak_lambat("\n[SISTEM]: Koneksi diputus. Tetap aman, Runner.")
            break
        else:
            print("[ERROR]: Perintah tidak valid.\n")

def loop_game():
    """Loop gameplay utama"""
    print("\n[BRIEFING MISI DIMUAT]")
    cetak_lambat("Implan neural Anda berdengung: 'Temukan Peninggalan Cyber sebelum OmniCore melakukannya.'")
    time.sleep(2)
    
    # LOOP WHILE: Gameplay utama
    game_aktif = True
    while game_aktif and data_pemain['hp'] > 0:
        print("\n" + "▼"*60)
        print("║ TERMINAL PERINTAH")
        print("▼"*60)
        print("1. Lihat Status")
        print("2. Jelajahi Area")
        print("3. Kunjungi Pasar Gelap")
        print("4. Cari Peninggalan Cyber")
        print("5. Simpan Game")
        print("6. Keluar Game")
        print("─"*60)
        
        aksi = input("\n> ").strip()
        
        if aksi == "1":
            tampilkan_statistik()
            
        elif aksi == "2":
            area = [
                "Distrik Neon",
                "Vault Data",
                "Menara Skyline",
                "Pasar Bawah Tanah",
                "Plaza OmniCore"
            ]
            
            print("\nLokasi Tersedia:")
            # LOOP FOR: Tampilkan area
            for i, a in enumerate(area, 1):
                status = "✓" if a in area_terjelajahi else " "
                print(f"{i}. [{status}] {a}")
            
            try:
                pilihan_area = int(input("\nPilih lokasi: ")) - 1
                if 0 <= pilihan_area < len(area):
                    jelajahi_area(area[pilihan_area])
                    buka_kekuatan_baru()
                else:
                    print("[ERROR]: Lokasi tidak valid.")
            except ValueError:
                print("[ERROR]: Input tidak valid.")
                
        elif aksi == "3":
            print("\n[PASAR GELAP]: Pedagang teduh mendekat...")
            print(f"Kredit Anda: {data_pemain['kredit']}¢\n")
            print("1. Stimpack Neural - 40¢")
            print("2. Modul Teknologi - 60¢")
            print("3. Pergi")
            
            toko = input("\n> ").strip()
            if toko == "1" and data_pemain['kredit'] >= 40:
                data_pemain['kredit'] -= 40
                inventori.append("Stimpack Neural")
                print("[DIBELI]: Stimpack Neural diperoleh.")
            elif toko == "2" and data_pemain['kredit'] >= 60:
                data_pemain['kredit'] -= 60
                inventori.append("Modul Teknologi")
                print("[DIBELI]: Modul Teknologi diperoleh.")
            elif toko == "3":
                print("Pedagang mengangguk dan menghilang ke bayangan...")
            else:
                print("[ERROR]: Kredit tidak cukup.")
                
        elif aksi == "4":
            if len(kekuatan_terbuka) >= 3 and data_pemain['xp'] >= 100:
                print("\n[OBJEKTIF DITEMUKAN]: Vault OmniCore di depan...")
                print("Sistem keamanan akhir terdeteksi.\n")
                
                if pertarungan("AI Guardian Elite", 100):
                    tentukan_akhir()
                    game_aktif = False
                else:
                    print("\n[MISI GAGAL]: Anda dikalahkan...")
                    game_aktif = False
            else:
                print("\n[TERBLOKIR]: Anda perlu lebih banyak kekuatan dan pengalaman.")
                print(f"Saat ini: {len(kekuatan_terbuka)}/3 kekuatan, {data_pemain['xp']}/100 XP")
                
        elif aksi == "5":
            simpan_game()
            
        elif aksi == "6":
            print("\n[SISTEM]: Memutuskan tautan neural...")
            game_aktif = False
            
        else:
            print("[ERROR]: Perintah tidak dikenali.")
        
        time.sleep(1)
    
    if data_pemain['hp'] <= 0:
        print("\n[FLATLINE]: Sistem Anda gagal. Misi dihentikan.")
        time.sleep(2)

# ==================== MULAI GAME ====================

if __name__ == "__main__":
    try:
        menu_utama()
    except KeyboardInterrupt:
        print("\n\n[PEMUTUSAN DARURAT]: Sesi dihentikan.")
    except Exception as e:
        print(f"\n[ERROR KRITIS]: {e}")
    finally:
        print("\n[SHUTDOWN SISTEM SELESAI]\n")