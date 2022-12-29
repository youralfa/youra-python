# tempat fungsi untuk pembacaan file text
def data (file) : 
    file = open(file, "r")
    #pembuatan dict
    list_data = [] #index : 0 book1, index : 1 book2, indekx: 2 book3, index : 3 book4, index : 4 book5
    baca_teks = file.readline().replace("\n","" )
    print("ISI DARI PEMBACAAN FILE")
    while baca_teks != "" : #perulangan
        list_kata = baca_teks.split() 
        list_data.append(list_kata) #melakukan penambahan ke list_data dari pembacaan file text
        print(list_kata) # output dari pembacaan text
        baca_teks = file.readline().replace("\n","" )
    file.close()
    print("\n")
    print("LIST DATA DARI PEMBACAAN FILE")
    print(list_data)
    

#bagian a
#Buatlah sebuah list daftar_buku dengan elemen berupa dictionary. Dictionary menyimpan data buku berupa ISBN, stok buku, dan jumlah buku yang dipinjam selama seminggu. 
#Gunakan tipe data terstruktur ini untuk proses pada fungsi yang diminta di bawah ini.
def pengisian(data_file) :
    data = data_file #index : 0 book1, index : 1 book2, index : 2 book3, index : 3 book4, index : 4 book5
    #untuk dictinary setiap minggunya, karena berdasarkan ISBN ada 5. jadi membuat 5 dictonary, yang terdiri dari {ISBN :..., STOK : ...., PEMINJAM : ...}.
    dict_book1 = {} 
    dict_book2= {}
    dict_book3= {}
    dict_book4 = {}
    dict_book5 = {}
    # perulangan untuk mengisi data di masing-masing dict

    #penjelasan untuk varibel dari list_data untuk melakukan pengisian book setiap minggunya ke dictionary 
    #index 0 merupakan book1, kemudian index 0 : ISBN , index : 1 STOK, index : 2:8 PEMINJAM
    #index 1 merupakan book2, kemudian index 0 : ISBN , index : 1 STOK, index : 2:8 PEMINJAM  
    #index 2 merupakan book3, kemudian index 0 : ISBN , index : 1 STOK, index : 2:8 PEMINJAM 
    #index 3 merupakan book4, kemudian index 0 : ISBN , index : 1 STOK, index : 2:8 PEMINJAM 
    #index 4 merupakan book5, kemudian index 0 : ISBN , index : 1 STOK, index : 2:8 PEMINJAM 
    for i in range(len(data)):
        dict_book1['ISBN'] = data[0][0] # berdasarkan index masing-masing minggu
        dict_book1['STOK'] = data[0][1] # berdasarkan index masing-masing minggu
        elemen = data[0][2:8] # berdasarkan index masing-masing minggu
        jumlah = 0
        for i in elemen:#perulangan untuk menambah total peminjam setiap
            a = i
            a_int = int(i)
            jumlah += a_int
            dict_book1['PEMINJAM'] = jumlah
    #book 2
    for i in range(len(data)):
        dict_book2['ISBN'] = data[1][0] # berdasarkan index masing-masing minggu
        dict_book2['STOK'] = data[1][1] # berdasarkan index masing-masing minggu
        elemen = data[1][2:8] # berdasarkan index masing-masing minggu
        jumlah = 0
        for i in elemen:#perulangan untuk menambah total peminjam setiap
            a = i
            a_int = int(i)
            jumlah += a_int
        dict_book2['PEMINJAM'] = jumlah 
    #book 3
    for i in range(len(data)):
        dict_book3['ISBN'] = data[2][0] # berdasarkan index masing-masing minggu
        dict_book3['STOK'] = data[2][1] # berdasarkan index masing-masing minggu
        elemen = data[2][2:8] # berdasarkan index masing-masing minggu
        jumlah = 0
        for i in elemen:
            a = i
            a_int = int(i)
            jumlah += a_int
        dict_book3['PEMINJAM'] = jumlah
    #book 4       
    for i in range(len(data)):
        dict_book4['ISBN'] = data[3][0] # berdasarkan index masing-masing minggu
        dict_book4['STOK'] = data[3][1] # berdasarkan index masing-masing minggu
        elemen = data[3][2:8] # berdasarkan index masing-masing minggu
        jumlah = 0
        for i in elemen:#perulangan untuk menambah total peminjam setiap
            a = i
            a_int = int(i)
            jumlah += a_int
        dict_book4['PEMINJAM'] = jumlah
    #book 5
    for i in range(len(data)):
        dict_book5['ISBN'] = data[4][0] # berdasarkan index masing-masing minggu
        dict_book5['STOK'] = data[4][1] # berdasarkan index masing-masing minggu
        elemen = data[4][2:8] # berdasarkan index masing-masing minggu
        jumlah = 0
        for i in elemen: #perulangan untuk menambah total peminjam setiap
            a = i
            a_int = int(i)
            jumlah += a_int
        dict_book5['PEMINJAM'] = jumlah
    #output dari masing-masing book
    print("\n")
    print("DICT DARI MASING-MASING MINGGUNYA : ")
    #output dari masing-masing minggu
    print(dict_book1)
    print(dict_book2)
    print(dict_book3)
    print(dict_book4)
    print(dict_book5)
    print("\n")

    #output dalam bentuk list
    print("LIST DAFTAR BUKU :")
    #output dari daftar_buku
    daftar_buku =[dict_book1, dict_book2, dict_book3, dict_book4, dict_book5] # dari ke lima dictionary di atas di buat list
    print(daftar_buku)
    print("\n")
    
#bagian b
# Buatlah fungsi terbanyak untuk mengembalikkan (return) ISBN buku dengan total peminjaman terbanyak dan setiap minggunya.
def terbanyak (data_a) :
    data = data_a #variabel dari data_a
    '''print(data)'''
    print("TOTAL PEMINJAM : ")
     #perulangan untuk menampilkan elemen dari variabel daftar buku 
    for elemen in data : 
        x = elemen.get('PEMINJAM') # untuk mendapakan valuesnya menngunakan fungsi .get()
        y = elemen.get('ISBN')
        i = 0
        #perulangan untuk menampilkan jumlah peminjam setiap minggu
        while i != 1 : # perulangan untuk output
            print("ISBN : ", y,"atau setiap minggunya,", "Total peminjaman adalah",x )
            i += 1
    
#bagian c
#Buatlah fungsi report yang digunakan untuk menampilkan rata-rata peminjaman sebuah buku selama satu minggu.
def report (data_a) :
    data = data_a
    '''print(data)'''
    print("\n")
    print("JUMlAH RATA-RATA : ")
    #perulangan untuk menampilkan elemen dari variabel daftar buku 
    for elemen in data :
        x = elemen.get('PEMINJAM') # untuk mendapakan valuesnya menngunakan fungsi .get()
        y = elemen.get('ISBN')
        i = 0
        #perulangan untuk mengecek rata-rata buku sesuai dengan ISBNNYA
        while i != 1 :
            rata2 = x / 7 # rata-rata di sini di bagi tujuh, berdasarkan peminjam selama satu minggu
            print("ISBN : ", y,"atau setiap minggunya,", "Memiliki rata-rata adalah", rata2)
            i += 1
    print("\n")

#bagian d
#Buatlah main program yang digunakan untuk menampilkan dictionary dan memanggil fungsi yang dibuat
#main progaram
nama_file = "data.txt"
data(nama_file) 
#data ini di input berdasarkan hasil dari list_data
a = [['978-1523502776', '10', '4', '0', '0', '3', '2', '0'], ['978-1951204006', '3', '2', '0', '0', '1', '0', '0'], ['978-1119724414', '5', '3', '0', '1', '0', '0', '0'], ['978-0997316025', '6', '0', '0', '0', '1', '1', '1'], ['978-1734554908', '12', '2', '0', '4', '0', '0', '1']]
pengisian(a)
#data ini di input berdasarkan hasil dari daftar_buku
b = [{'ISBN': '978-1523502776', 'STOK': '10', 'PEMINJAM': 9}, {'ISBN': '978-1951204006', 'STOK': '3', 'PEMINJAM': 3}, {'ISBN': '978-1119724414', 'STOK': '5', 'PEMINJAM': 4}, {'ISBN': '978-0997316025', 'STOK': '6', 'PEMINJAM': 3}, {'ISBN': '978-1734554908', 'STOK': '12', 'PEMINJAM': 7}]
terbanyak(b)
#data ini di input berdasarkan hasil dari daftar_buku
c = [{'ISBN': '978-1523502776', 'STOK': '10', 'PEMINJAM': 9}, {'ISBN': '978-1951204006', 'STOK': '3', 'PEMINJAM': 3}, {'ISBN': '978-1119724414', 'STOK': '5', 'PEMINJAM': 4}, {'ISBN': '978-0997316025', 'STOK': '6', 'PEMINJAM': 3}, {'ISBN': '978-1734554908', 'STOK': '12', 'PEMINJAM': 7}]
report(c)



