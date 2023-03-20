list_data_siswa = [['A','Abdi','11110',100,100,100,'10-10-1990','abdi@gmail.com'],['B','Acung','11111',90,100,100,'10-12-1990','acung@gmail.com']] #list dalam list
from datetime import datetime 
def read_data():
    while True :
        read_data_siswa = (input('''
        ===Pilihan Menu Read Data===
        1.Tampilkan semua data 
        2.Tampilkan data bedasarkan nama, nim, kelas   
        3.Exit
        Masukkan pilihan yang diinginkan(1-3):'''))
        if read_data_siswa =='1':
            buka_data_siswa() #line 300
            continue
        elif read_data_siswa == '2': 
            cari_data_tertentu = input('''
            ===Pilihan Menu Mencari Data Tertentu===
            Tekan 1 -> Melakukan pencarian data 
            Tekan angka lain -> Tidak ingin melakukan pencarian data
            Pilihan Anda(Tekan Angka 1/Angka lain): ''')
            if cari_data_tertentu == '1':
                if len(list_data_siswa) == 0:
                    tidak_ada_data() #line 205
                else:
                    data_siswa_terisi() #line 296
                    data_dengan_kriteria = input('''\nApakah anda ingin mencari data dengan kriteria:
    1. Mencari data bedasarkan nama 
    2. Mencari data bedasarkan kelas
    3. Mencari data bedasarkan nim
    Masukkan pilihan diantara(1-3): ''')
                    if data_dengan_kriteria == '1':
                        mencari_data_kriteria = input('Masukkan nama yang ingin dicari: ').capitalize()
                        nama_sama = 0
                        jumlah_looping = 0  #untuk ngeloop sampe indeks terakhir kalau ga ketemu datanya ( jadi di awal ngecek apakah input= abdi terus masuk else apakah input=acung)
                        for i in range(len(list_data_siswa)):
                            if mencari_data_kriteria == list_data_siswa[i][1]:
                                nama_sama += 1
                                if nama_sama == 1:                    
                                    header = 'Indeks | Kelas | Nama     | NIM       | Nilai Matematika | Nilai Fisika | Nilai Kimia | Tanggal Lahir | Email'
                                    print(header)
                                    print('{:<7}| {:<6}| {:<15}| {:<10}| {:<17}| {:<13}| {:<12}| {:<16}| {}'.format(i, list_data_siswa[i][0], list_data_siswa[i][1], list_data_siswa[i][2], list_data_siswa[i][3], list_data_siswa[i][4], list_data_siswa[i][5], list_data_siswa[i][6], list_data_siswa[i][7]))
                            else: 
                                jumlah_looping += 1 #nambah terus skalau gak ketemu datanya
                        
                        if jumlah_looping == len(list_data_siswa):
                            tidak_ada_data()
                            read_data()
                    elif data_dengan_kriteria == '2':
                       mencari_data_kriteria = input('Masukkan kelas yang ingin dicari: ').upper()
                       kelas_sama = 0
                       jumlah_looping = 0  #untuk ngeloop sampe indeks terakhir kalau ga ketemu datanya 
                       for i in range(len(list_data_siswa)):
                            if mencari_data_kriteria == list_data_siswa[i][0]:
                                kelas_sama += 1
                                if kelas_sama == 1:                    
                                    header = 'Indeks | Kelas | Nama     | NIM       | Nilai Matematika | Nilai Fisika | Nilai Kimia | Tanggal Lahir | Email'
                                    print(header)
                                    print('{:<7}| {:<6}| {:<15}| {:<10}| {:<17}| {:<13}| {:<12}| {:<16}| {}'.format(i, list_data_siswa[i][0], list_data_siswa[i][1], list_data_siswa[i][2], list_data_siswa[i][3], list_data_siswa[i][4], list_data_siswa[i][5], list_data_siswa[i][6], list_data_siswa[i][7]))
                            else: 
                                jumlah_looping += 1 #nambah terus skalau gak ketemu datanya
                        
                       if jumlah_looping == len(list_data_siswa):
                            tidak_ada_data()
                            read_data()
                    elif data_dengan_kriteria == '3':
                        mencari_data_kriteria = input('Masukkan NIM yang ingin dicari: ')
                        nim_sama = 0
                        jumlah_looping = 0  #untuk ngeloop sampe indeks terakhir kalau ga ketemu datanya 
                        for i in range(len(list_data_siswa)):
                            if mencari_data_kriteria == list_data_siswa[i][2]:
                                nim_sama += 1
                                if nim_sama == 1:                    
                                    header = 'Indeks | Kelas | Nama     | NIM       | Nilai Matematika | Nilai Fisika | Nilai Kimia | Tanggal Lahir | Email'
                                    print(header)
                                    print('{:<7}| {:<6}| {:<15}| {:<10}| {:<17}| {:<13}| {:<12}| {:<16}| {}'.format(i, list_data_siswa[i][0], list_data_siswa[i][1], list_data_siswa[i][2], list_data_siswa[i][3], list_data_siswa[i][4], list_data_siswa[i][5], list_data_siswa[i][6], list_data_siswa[i][7]))
                            else: 
                                jumlah_looping += 1 #nambah terus skalau gak ketemu datanya
                        
                        if jumlah_looping == len(list_data_siswa):
                            tidak_ada_data()
                            read_data()
                            
        elif read_data_siswa =='3':
            menu_utama()        
        else :
            print('pilihan yang anda masukkan salah. silahkan masukkan angka diantara(1-3): ')
            read_data()

#FUNGSI UNTUK MENAMBAHKAN DATA 
def tambah_data():
    while True :
        buka_data_siswa() #line 300 
        tambah_data_siswa = (input('''
        === Selamat datang di Sekolah Pelangi ==
        1.Menambahkan Data Siswa Sekolah Pelangi
        Mohon Tekan 1 jika ingin menambahkan data, Jika tidak tekan angka selain satu '''))
        if tambah_data_siswa == '1':
            if len(list_data_siswa) == 0:
                tidak_ada_data() 
                save_data_siswa = input('''
====Opsi penyimpanan data(1/Tekan angka selain 1)====
    Keterangan:
    1. Menyimpan data
    ===Tekan selain angka 1 untuk balik ke menu tambah data==
    Masukkan pilihan (1/selain angka 1): ''')
                if save_data_siswa == '1':
                    list_data_siswa.append([kelas,nama,nim,mtk,fis,kim,tgl_lahir,email])
                    print('\nData siswa telah berhasil disimpan\n')
                else:
                    continue
            
            else: #ini kan len(list_data_siswa) kita bukan nol tapi di awal udah ada 2 data jadinya udah terisi makanya masuk ke sini. 
                nim = cek_nim(list_data_siswa)
                nama = (input('Masukkan Nama Siswa : '))
                nama = nama.capitalize()
                kelas = kelasinput(1) # line 223
                mtk = input("Masukkan Nilai Matematika: ")
                while not mtk.isdigit() or int(mtk) < 0 or int(mtk) > 100:
                    mtk = input("Nilai matematika di luar range.Masukkan Nilai Matematika (0-100): ")
                fis = input("Masukkan Nilai Fisika: ")
                while not fis.isdigit() or int(fis) < 0 or int(fis) > 100:
                    fis = input("Nilai fisika di luar range.Masukkan Nilai Fisika (0-100): ")
                kim = input("Masukkan Nilai Kimia: ")
                while not kim.isdigit() or int(kim) < 0 or int(kim) > 100:
                    kim = input("Nilai kimia di luar range.Masukkan Nilai Kimia (0-100): ")
                tgl_lahir = input_tgl_lahir() #line 247
                email = kriteria_email() #line 269

                save_data_siswa = input('''
Apakah data sudah benar dan ingin disimpan? [1/Tekan Selain 1]
    1 --------------> Simpan Data
    Tekan Selain 1 -> Kembali ke Menu Tambah Data
    Pilihan anda: ''')
                if save_data_siswa == '1':
                        list_data_siswa.append([kelas,nama,nim,mtk,fis,kim,tgl_lahir,email])
                        print('\nData telah berhasil disimpan\n')
        else:
           menu_utama()
#====================UPDATE DATA=======================#
def update_data():
    while True :
        if len(list_data_siswa) == 0:
            tidak_ada_data() # line 328
            break
        elif len(list_data_siswa)>0:
            data_siswa_terisi() # line 314
        updatedata = (input('''
Ingin update data? [1/Tekan Selain 1]
    1 --------------> Lanjut update
    Tekan Selain 1 -> Ke Menu Proceed (Exit)
    Pilihan anda: '''))
        if updatedata == '1':
            while True:
                indeks = input('Masukkan indeks siswa yang ingin diubah: ')
                if indeks == '0' or (indeks.isdigit() and int(indeks) in range(len(list_data_siswa)+1)):
                    break
                else :
                    templatestring() 
            if int(indeks) in range(len(list_data_siswa)+1):
                global j 
                j = int(indeks)
                data_akan_diperbaharui(j) 
                updatedata= (input('''
    Apakah anda ingin melakukan update data? 
    Tekan angka 1 --> Melakukan update data
    Tekan Selain 1 -> Kembali ke Menu Update
    Pilihan anda(1/angka lain): '''))
                if updatedata == '1':
                    updating_data(j) 
                else:
                  continue
            else :  
               indekssalah() # line 334
               continue
        else:
            menu_utama()

def delete_data():
    while True :
        if len(list_data_siswa) == 0:
            tidak_ada_data() # line 328
            break
        elif len(list_data_siswa)>0:
            data_siswa_terisi() # line 314
        delettedata = (input('''
Apakah anda ingin menghapus data? 
    Tekan angka 1 --> Melakukan delete data
    Tekan Selain 1 -> Ke Menu Proceed (Exit)
    Pilihan anda(1/Angka lain): '''))
        if delettedata == '1':
            while True:
                indeks = input('Masukkan indeks siswa yang ingin dihapus: ')
                if indeks =='0' or (indeks.isdigit() and int(indeks) in range(len(list_data_siswa)+1)): #ini perlu len_list_data_siswa + 1 soalnya indeksnya startnya di nol maka indeks terakhirnya len(list_data_siswa)-1
                    break  #langsung lanjut ke delete data gak looping lagi
                else:
                    templatestring() # line 296
            if int(indeks) in range(len(list_data_siswa)+1): 
                global j
                j = int(indeks)
                deleteupdate(j) # line 340
                delettedata = (input('''
 Apakah anda ingin menghapus data? 
    Tekan angka 1 --> Melakukan delete data
    Tekan Selain 1 -> Ke Menu Proceed (Exit)
    Pilihan anda(1/Angka lain): '''))
                if delettedata == '1':
                    print('''
    =================================
    DATA YANG DIPILIH SUDAH DIHAPUS!!
    =================================
    ''')
                    del list_data_siswa[j]
                    
                else :
                  continue    
            else :
                indekssalah() # line 334
                continue
        else:
                break


        continue
def kelasinput(digit):
    while True:
        while True:
            kelas = input('Masukkan Kelas Siswa (1 Huruf A - Z): ')
            t = kelas.isnumeric() #KALAU MASUKIN KELASNYA ANGKA SALAH KELASNYA HARUS HURUF
            if t == False:
                break
            else:
                print('''
    =================================
    INPUT TIDAK BOLEH MENGANDUNG ANGKA
    =================================
    ''')
        kelas = kelas.upper()
        if len(kelas) == digit:
            return kelas
        else:
            print('''
    =================================
        MASUKKAN HANYA 1 HURUF
    =================================
    ''')
            
import re
def input_tgl_lahir():
    while True:
        tgl_lahir = input('Masukkan Tanggal Lahir Siswa (Format: dd-mm-yyyy): ')
        try:
            tgl_lahir = datetime.strptime(tgl_lahir, '%d-%m-%Y').date()
            return tgl_lahir
        except ValueError:
            print('Format tanggal lahir salah. Masukkan tanggal lahir dengan format dd-mm-yyyy.')

def cek_nim(list_data_siswa):
    while True:
        nim = input('Masukkan Nomor NIM Siswa (5 Digit): ')
        nim_regex = r'\b[a-zA-Z0-9]{5}\b'
        if re.fullmatch(nim_regex, nim):
            nim_list = [data[2] for data in list_data_siswa]
            if nim not in nim_list:
                return nim
            else:
                print('NIM sudah ada. Masukkan NIM yang berbeda.')
        else:
            print('NIM tidak valid. Pastikan NIM terdiri dari 5 karakter alfanumerik.')
import re
def kriteria_email():
    while True:
        email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        email = input('Masukkan email siswa: ')
        if re.match(email_regex, email):
            return email
            
        else:
            print('Masukkan email sesuai kriteria: ')
            kriteria_email()

    
def data_yang_ingin_ditemukan():
    print('''
    ================================
       SELAMAT DATA TELAH DITEMUKAN
    ================================
    ''')
def templatestring():
    print('''
    =================================
        JANGAN MASUKKAN STRING !!
    =================================
    ''')
def templatedatatidakada():
    print('''
    ================================
          MAAF DATA TIDAK ADA 
    ================================
    ''')  
def data_siswa_terisi():
    print('\nData Siswa Sekolah Pelangi\n')
    print_data(list_data_siswa)
   
def buka_data_siswa():
    if len(list_data_siswa) == 0:
        print('Data belum terisi')   
    elif len(list_data_siswa)>0:
        data_siswa_terisi() # line 314
def tidak_ada_data():
    print('===Tidak Terdapat Data===')
def indekssalah():
    print('''
    ============================================
         Indeks siswa yang dimasukkan salah
    ============================================
    ''')
def deleteupdate(j):
    print('\nDaftar Nilai Siswa\n')
    print('Nomor Unik| Kelas | Nama\t| NISN       | Nilai Matematika | Nilai Fisika  | Nilai Kimia\t| Nilai Biologi \t|Email ')
    print('{}\t  | {}     | {}\t| {} | {}  \t| {}  \t| {}  \t| {}'.format(j,list_data_siswa[j][1],list_data_siswa[j][2],list_data_siswa[j][3],list_data_siswa[j][4],list_data_siswa[j][5],list_data_siswa[j][6],list_data_siswa[j][7]))
def data_akan_diperbaharui(j):
    print('\nDaftar Nilai Siswa\n')
    print('Nomor Unik| Kelas | Nama\t| NISN       | Nilai Matematika | Nilai Fisika  | Nilai Kimia\t| Nilai Biologi \t|Email ')
    print('{}\t  | {}     | {}\t| {} | {}  \t| {}  \t| {}  \t| {}'.format(j,list_data_siswa[j][1],list_data_siswa[j][2],list_data_siswa[j][3],list_data_siswa[j][4],list_data_siswa[j][5],list_data_siswa[j][6],list_data_siswa[j][7]))  
def updating_data(j):
    print('\nDaftar Nilai Siswa\n')
    header = 'Indeks | Kelas | Nama     | NIM       | Nilai Matematika | Nilai Fisika | Nilai Kimia | Tanggal Lahir | Email'
    print(header)
    print('{:<7}| {:<6}| {:<15}| {:<10}| {:<17}| {:<13}| {:<12}| {:<16}| {}'.format(j, list_data_siswa[j][0], list_data_siswa[j][1], list_data_siswa[j][2], list_data_siswa[j][3], list_data_siswa[j][4], list_data_siswa[j][5], list_data_siswa[j][6], list_data_siswa[j][7]))
    while True:
        while True:
            kolompilih = int(input('''
Pilih nomor kolom yang ingin di update [
======PILIHAN UPDATE KOLOM=====
    -KELAS = 0 
    -NAMA = 1 
    -NIM = 2  
    -MATEMATIKA = 3  
    -FISIKA = 4 
    -KIMIA = 5  
    -Tanggal Lahir = 6
    -EMAIL = 7]
: '''))
            

            if kolompilih == 0: #merefer ke kelas siswa
                kolombaru = kelasinput(1)
                simpan = input('''
    Apakah data sudah benar dan ingin diupdate? [1/Tekan Selain 1]
        1 --------------> Data akan diubah
        Tekan Selain 1 -> Data tidak diubah
        Pilihan anda: ''')
                if simpan == '1':
                    list_data_siswa[j][kolompilih] = kolombaru
                    print('\nData Terupdate\n')
                    break
                else:
                    break
            elif kolompilih == 1: #merefer ke nama siswa
                kolombaru = input('Silahkan masukkan nama baru: ')
                kolombaru = kolombaru.upper()
                simpan = input('''
    Apakah data sudah benar dan ingin diupdate? [1/Tekan Selain 1]
        1 --------------> Data akan diubah
        Tekan Selain 1 -> Data tidak diubah
        Pilihan anda: ''')
                if simpan == '1':
                    list_data_siswa[j][kolompilih] = kolombaru
                    print('\nData Terupdate\n')
                    break
                else:
                    break
            elif kolompilih == 2: #merefer ke nim siswa
                kolombaru = cek_nim(list_data_siswa)
                simpan = input('''
    Apakah anda ingin melakukan update data? 
    Tekan angka 1 --> Melakukan update data
    Tekan angka lain --> Data tidak diupdate
        Pilihan anda(1/Angka lain): ''')
                if simpan == '1':
                    list_data_siswa[j][kolompilih] = kolombaru
                    print('\nData Terupdate\n')
                    break
                else:
                    break
            elif kolompilih == 3: #merefer ke nilai mat
                kolombaru = input('Silahkan masukkan nilai matematika baru: ')
                simpan = input('''
    Apakah anda ingin melakukan update data? 
        Tekan angka 1 --> Melakukan update
        Tekan angka lain --> Data tidak diupdate
        Pilihan anda(1/Angka lain): ''')
                if simpan == '1':
                    list_data_siswa[j][kolompilih] = kolombaru
                    print('\nData Terupdate\n')
                    break
                else:
                    break 
            elif kolompilih == 4: #merefer ke nilai fis
                kolombaru = input('Silahkan masukkan nilai fisika baru: ')
                simpan = input('''
    Apakah anda ingin melakukan update data? 
    Tekan angka 1 --> Melakukan update data
    Tekan angka lain --> Data tidak diupdate
        Pilihan anda(1/Angka lain): ''')
                if simpan == '1':
                    list_data_siswa[j][kolompilih] = kolombaru
                    print('\nData Terupdate\n')
                    break
                else:
                    break
            elif kolompilih == 5: #merefer ke nilai kim
                kolombaru = input('Silahkan masukkan nilai kimia baru: ')
                simpan = input('''
    Apakah anda ingin melakukan update data? 
    Tekan angka 1 --> Melakukan update data
    Tekan angka lain --> Data tidak diupdate
        Pilihan anda(1/Angka lain): ''')
                if simpan == '1':
                    list_data_siswa[j][kolompilih] = kolombaru
                    print('\nData Terupdate\n')
                    break
                else:
                    break
            elif kolompilih == 6:
                kolombaru = input_tgl_lahir()
                simpan = input('''
    Apakah anda ingin melakukan update data? 
    Tekan angka 1 --> Melakukan update data
    Tekan angka lain --> Data tidak diupdate
        Pilihan anda(1/Angka lain): ''')
                if simpan == '1':
                    list_data_siswa[j][kolompilih] = kolombaru
                    print('\nData Terupdate\n')
                    break
                else:
                    break
            elif kolompilih == 7:
                kolombaru = input('Silahkan masukkan nilai email baru: ')
                simpan = input('''
    Apakah anda ingin melakukan update data? 
    Tekan angka 1 --> Melakukan update data
    Tekan angka lain --> Data tidak diupdate
        Pilihan anda(1/Angka lain): ''')
                if simpan == '1':
                    list_data_siswa[j][kolompilih] = kolombaru
                    print('\nData Terupdate\n')
                    break
                else:
                    break
            else:
                print('''
                    =============================================
                    Nomor Kolom yang dimasukkan tidak ditemukan!!
                    =============================================
                    ''')
                continue
        break


def print_data(student_data):
    header = 'Indeks | Kelas | Nama     | NIM       | Nilai Matematika | Nilai Fisika | Nilai Kimia | Tanggal Lahir | Email'
    print(header)
    for index, data in enumerate(student_data):
        if len(data) >= 8:
             print('{:<7}| {:<6}| {:<15}| {:<10}| {:<17}| {:<13}| {:<12}| {:<16}| {}'.format(index, data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7]))
        else:
            print('Invalid student data: {}'.format(data))

def menu_utama():
    while True :
        print('''
            === Selamat Datang di Sekolah Pelangi ===
            === Terdapat 5 Menu yang dapat dipilih ===

            1. Menampilkan Data Siswa
            2. Menambah Data Siswa
            3. Mengupdate Data Siswa
            4. Menghapus Data Siswa
            5. Exit Program
        ''')
        
        menu_choice = input("Pilih menu yang akan dilakukan (1-5): ")


        if(menu_choice ==   '1') :
           read_data() # line 7
        elif(menu_choice == '2') :
           tambah_data() # line 85
        elif(menu_choice == '3') :
           update_data() # line 152
        elif(menu_choice == '4') :
           delete_data() # line 198
        elif(menu_choice == '5') :
           break
        else:
            print('Pilihan yang anda masukkan salah.Masukkan pilihan diantara(1-5): ')

menu_utama()