# Program Python3 untuk Heuristik Karakter Buruk
# dari Algoritma Pencocokan String Boyer Moore

NO_OF_CHARS = 256

def badCharHeuristic(string, size):
    '''
    Fungsi pra-pemrosesan untuk
    heuristik karakter buruk Boyer Moore
    '''

    # Inisialisasi semua kemunculan menjadi -1
    badChar = [-1]*NO_OF_CHARS

    # Isi nilai aktual kemunculan terakhir
    for i in range(size):
        badChar[ord(string[i])] = i;

    # kembalikan daftar yang diinisialisasi
    return badChar

def search(txt, pat):
    '''
    Fungsi pencarian pola yang menggunakan
    heuristik karakter buruk Algoritma Boyer Moore
    '''

    m = len(pat)
    n = len(txt)

    # Buat daftar karakter buruk dengan memanggil
    # fungsi pra-pemrosesan badCharHeuristic()
    # untuk pola yang diberikan
    badChar = badCharHeuristic(pat, m)

    # s adalah pergeseran pola terhadap teks
    s = 0
    while(s <= n-m):
        j = m-1

        # Terus kurangi indeks j dari pola saat
        # karakter pola dan teks cocok
        # pada pergeseran s ini
        while j>=0 and pat[j] == txt[s+j]:
            j -= 1

        # Jika pola ada pada pergeseran saat ini,
        # maka indeks j akan menjadi -1 setelah loop di atas
        if j<0:
            print("Pola muncul pada pergeseran = {}".format(s))

            '''
            Geser pola sehingga karakter berikutnya dalam teks
            sejajar dengan kemunculan terakhirnya dalam pola.
            Kondisi s+m < n diperlukan untuk kasus ketika
            pola muncul di akhir teks
            '''
            s += (m-badChar[ord(txt[s+m])] if s+m<n else 1)
        else:
            '''
            Geser pola sehingga karakter buruk dalam teks
            sejajar dengan kemunculan terakhirnya dalam pola. Fungsi max
            digunakan untuk memastikan bahwa kita mendapatkan pergeseran positif.
            Kita mungkin mendapatkan pergeseran negatif jika kemunculan terakhir
            karakter buruk dalam pola ada di sebelah kanan karakter saat ini.
            '''
            s += max(1, j-badChar[ord(txt[s+j])])

# Program utama untuk menguji fungsi di atas
def main():
    txt = "ABAAABCD"
    pat = "ABC"
    search(txt, pat)

if __name__ == '__main__':
    main()
