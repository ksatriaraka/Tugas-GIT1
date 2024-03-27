import pandas as pd
from google.colab import drive

# Menghubungkan dengan Google Drive
drive.mount('/content/drive')

class MarketingDataETL:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def extract(self): # akan membaca data dari sebuah file CSV yaitu, marketing_data.csv
        try:
            self.data = pd.read_csv(self.file_path, sep = ';')
            print("Data di file CSV berhasil diekstrak")
        except Exception as e:
            print("Gagal melakukan ekstrak data:", str(e))

    def clean(self):
        if self.data is not None:
            try:
                self.data.dropna(inplace=True) # Menghapus baris dengan nilai kosong
                print("Data berhasil dibersihkan dari nilai kosong.")
            except Exception as e:
                print("Gagal membersihkan data:", str(e))
        else:
            print("Tidak ada data untuk dibersihkan.")

    def transform(self):
        # Melakukan transformasi sederhana, misalnya mengubah format tanggal
        if self.data is not None:
            try:
                self.data['purchase_date'] = pd.to_datetime(self.data['purchase_date']) # Melakukan transformasi mengubah  kolom 'tanggal' menjadi tipe datetime
                print("Data berhasil ditransformasi.")
            except Exception as e:
                print("Gagal melakukan transformasi data:", str(e))
        else:
            print("Tidak ada data untuk ditransformasi.")

    def store(self, output):
        if self.data is not None:
            try:
                self.data.to_csv(output, index=False)
                print("Data berhasil disimpan ke", output)# menyimpan data yang telah ditransformasi ke dalam struktur data DataFrame, yaitu transform_marketing_data.csv
            except Exception as e:
                print("Gagal menyimpan data:", str(e))
        else:
            print("Tidak ada data yang disimpan.")

# Path file di Google Drive
file_path = '/content/drive/MyDrive/marketing_data.csv'
output = "/content/drive/MyDrive/transformed_marketing_data_finish.csv"

etl = MarketingDataETL(file_path)
etl.extract()
etl.clean()
etl.transform()
etl.store(output)
