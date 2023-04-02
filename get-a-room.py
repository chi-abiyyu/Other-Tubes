import getpass

users = {
    'chiel': 'chi123',
    'zhi': 'xiao'
}


def login():
    print()
    print('Masuk :')
    username = input('Username : ')
    password = getpass.getpass('Password : ')

    while (username not in users) or (password != users[username]):
        print('Username atau Password Salah')
        username = input('Username : ')
        password = getpass.getpass('Password : ')
        print()

    print(f'Selamat Datang {username}')


def sign_up():
    print()
    print('Buat Akun Baru :')
    username = input('Username : ')
    while (username in users):
        print('Username Telah Digunakan')
        username = input('Username : ')
    password = getpass.getpass('Password : ')

    users[username] = password
    print('Akun Berhasil Dibuat')


def menu_kamar():
    print()
    print('Hotel Jingga')
    print('1. Kamar Standar')
    print('2. Kamar Delux')
    print('3. Keluar')
    pil_kam = True
    while pil_kam:
        pilihan_kamar = int(input('Masukan Pilihan Anda :'))

        if pilihan_kamar == 1:
            print('Kamar Standar')
            print('Harga : 300K')
            pil_kam = True
            menu = False
        elif pilihan_kamar == 2:
            print('Kamar Delux')
            print('Harga : 600K')
            pil_kam = True
            menu = False
        elif pilihan_kamar == 3:
            print('Keluar')
            pil_kam = False
            menu = True
        else:
            print('Pilihan Anda Tidak Valid')


class Pesanan:
    def __init__(self, nama, umur, check_in, time_in, check_out, time_out, price):
        self.nama = nama
        self.umur = umur
        self.check_in = check_in
        self.time_in = time_in
        self.check_out = check_out
        self.time_out = time_out
        self.price = price

    def formulir(self):
        print('=====================================')
        print('           FORMULIR PEMESANAN        ')
        print('=====================================')
        print('Nama            :', self.nama)
        print('Usia            :', self.umur)
        print('Tanggal Check-In:', self.check_in)
        print('Waktu Check-In  :', self.time_in)
        print('Tanggal Check-Out:', self.check_out)
        print('Waktu Check-Out  :', self.time_out)
        print('Total Biaya     :', self.price)
        print('=====================================')


def bantuan():
    # Tampilkan menu bantuan
    print("Menu Bantuan:")
    print("1. Cara memesan kamar")
    print("2. Ketentuan pembayaran")
    print("3. Kebijakan pembatalan")
    print("4. Hubungi kami")
    print("5. Keluar")
    sub_pilihan = True
    while sub_pilihan:
        subpilihan = int(input("Masukkan pilihan Anda: "))

        if subpilihan == 1:
            print("Untuk memesan kamar, silakan pilih 'Pesan Kamar' pada menu utama")
        elif subpilihan == 2:
            print("Ketentuan pembayaran dapat dilihat pada halaman informasi kamar")
        elif subpilihan == 3:
            print("Kebijakan pembatalan dapat dilihat pada halaman informasi kamar")
        elif subpilihan == 4:
            print(
                "Silakan hubungi kami melalui email: info@getaroom.com atau telepon: 0812-XXXX-XXXX")
        elif subpilihan == 5:
            print('Keluar dari Bantuan')
            sub_pilihan = False
            menu = True
        else:
            print("Pilihan tidak valid")


def price_kam(jum_kam, har_kam):
    return jum_kam * har_kam

# Fungsi untuk membuat garis pembatas


def print_separator():
    print('===============================================')


mulai = True
while mulai:
    print()
    print('Get A Room')
    print('1. Login')
    print('2. Sign Up')
    print('3. Keluar')
    start = int(input('>> '))

    if start == 1:
        login()

        menu = True
        while menu:
            print()
            print('Menu Aplikasi')
            print('1. Menu Kamar')
            print('2. Buat Pesanan')
            print('3. Bantuan')
            print('4. Keluar')
            pilihan_user = int(input('>> '))

            if pilihan_user == 1:
                menu_kamar()

            elif pilihan_user == 2:
                # Bagian Formulir Pemesanan
                print_separator()
                print('            Formulir Pemesanan')
                print_separator()

                nama = input('Nama : ')
                umur = int(input('Umur : '))
                check_in = input('Tanggal Check-In : ')
                time_in = input('Waktu Check-In : ')
                check_out = input('Tanggal Check-Out : ')
                time_out = input('Waktu Check-Out : ')

                # Bagian Pilihan Kamar
                print_separator()
                print('Pilihan Kamar')
                print('1. Kamar Standar')
                print('2. Kamar Deluxe')
                form_kam = True
                while form_kam:
                    pil_form_kam = int(input('Pilih Kamar : '))
                    if pil_form_kam == 1:
                        print_separator()
                        print('Jenis Kamar = Standar')
                        har_kam = 300000
                        jum_kam = int(input('Jumlah Kamar : '))
                        price = price_kam(har_kam, jum_kam)
                        Pesanan_user = Pesanan(nama, umur, check_in,
                                               time_in, check_out, time_out, price)
                        Pesanan_user.formulir()
                        form_kam = False
                    elif pil_form_kam == 2:
                        print_separator()
                        print('Jenis Kamar = Deluxe')
                        har_kam = 600000
                        jum_kam = int(input('Jumlah Kamar : '))
                        price = price_kam(har_kam, jum_kam)
                        Pesanan_user = Pesanan(nama, umur, check_in,
                                               time_in, check_out, time_out, price)
                        Pesanan_user.formulir()
                        form_kam = False
                    else:
                        print('Pilihan Tidak Valid')
            elif pilihan_user == 3:
                bantuan()
                menu = True
            elif pilihan_user == 4:
                print('Keluar')
                menu = False

            else:
                print('Pilihan Tidak Valid')
                menu = True

        break
    elif start == 2:
        sign_up()
    elif start == 3:
        print('Keluar')
        break
    else:
        print('Input Failed')
