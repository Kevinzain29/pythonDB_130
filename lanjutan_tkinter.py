import sqlite3 
import tkinter as tk

#fungsi untuk menentukan prediksi fakultas
def prediksi_fakultas (biologi, fisika, inggris):
    if biologi > fisika and biologi > inggris:
        return "Kedokteran"
    elif fisika > biologi and fisika > inggris:
        return "Teknik"
    elif inggris > biologi and inggris > fisika:
        return "Bahasa"
    else :
        return "tidak bisa di prediksi"
    
#fungsi untuk menyimpan data ke dalam sqllite
def simpan_data(nama_siswa, biologi, fisika, inggris):
        conn = sqlite3.connect("D:\SEMESTER 3\pemrograman multiplatform\database python 2\database python 2.db")
        cursor = conn.cursor()

# membuat tabel
        cursor.execute(''' CREATE TABLE IF NOT EXISTS nilai_siswa
               (nama_siswa TEXT,
               biologi INTEGER,
               fisika INTEGER,
               inggris INTEGER,
               prediksi_fakultas TEXT)
               ''')
        
#untuk menghitung prediksi fakultas
        prediksi = prediksi_fakultas(biologi, fisika, inggris)
#memasukkan data ke dalam tabel yang sudah dibuat
        cursor.execute('''
    INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris, prediksi_fakultas)
    VALUES (?, ?, ?, ?, ?)
''', (nama_siswa, biologi, fisika, inggris, prediksi))

        conn.commit()
        conn.close()

def submit_nilai():
    nama_siswa = entry_nama.get()
    biologi = int(entry_biologi.get())
    fisika = int(entry_fisika.get())
    inggris = int(entry_inggris.get())

    simpan_data(nama_siswa, biologi, fisika, inggris)

#Membuat GUI menggunakan Tkinter
root = tk.Tk()
root.title("Input Nilai Siswa")

# Label dan Entry untuk mama siswa
label_nama = tk.Label(root, text="Nama Siswa:")
label_nama.pack()
entry_nama = tk.Entry(root)
entry_nama.pack()

# Label dan Entry untuk nilai biologi
label_biologi = tk.Label(root, text="Nilai Biologi:")
label_biologi.pack()
entry_biologi = tk.Entry(root)
entry_biologi.pack()

# Label dan Entry untuk nilai fisika
label_fisika = tk.Label(root, text="Nilai Fisika:")
label_fisika.pack()
entry_fisika = tk.Entry(root)
entry_fisika.pack()

# Label dan Entry untuk nilai inggris
label_inggris = tk.Label(root, text="Nilai Inggris:")
label_inggris.pack()
entry_inggris = tk.Entry(root)
entry_inggris.pack()

# Button untuk hasil prediksi
predict_button = tk.Button(root, text="Submit", command=submit_nilai)
predict_button.pack()

root.mainloop()

