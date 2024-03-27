from google.colab import drive
drive.mount('/content/drive')

class MarketingDataETL():
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def extract(self):
        # Implementasi ekstraksi data dari file
        try:
            self.data = pd.read_csv(self.file_path, sep = ';')
            print("Data di file CSV berhasil diekstrak")
        except Exception as e:
            print("Gagal melakukan ekstrak data:", str(e))

    def transform(self):
        # Implementasi transformasi data
         if self.data is not None:
            try:
                self.data['purchase_date'] = pd.to_datetime(self.data['purchase_date']) # Melakukan transformasi mengubah  kolom 'tanggal' menjadi tipe datetime
                print("Data berhasil ditransformasi.")
            except Exception as e:
                print("Gagal melakukan transformasi data:", str(e))



class TargetedMarketingETL(MarketingDataETL):
    def __init__(self, file_path):
        super().__init__(file_path)

    def extract(self):
        # Implementasi ekstraksi data khusus
       self.data = [
            {'customer_id': 'C001', 'total_pembelian': 1200},
            {'customer_id': 'C002', 'total_pembelian': 750},
            {'customer_id': 'C003', 'total_pembelian': 350},
            {'customer_id': 'C004', 'total_pembelian': 2050},
            {'customer_id': 'C005', 'total_pembelian': 800},
        ]

    def segment_customers(self):
        if self.data is not None:
            try:
                # Logika segmentasi pelanggan
                total_spent_segments = {
                    'Low Spender': self.data['amount_spent'] < 50,
                    'Medium Spender': (self.data['amount_spent'] >= 50) & (self.data['amount_spent'] < 150),
                    'High Spender': self.data['amount_spent'] >= 150
                }

                product_categories = [
                    'Electronics',
                    'Books',
                    'Home & Garden',
                    'Beauty'
                ]

                self.data['customer_segment'] = None

                for segment_name, segment_condition in total_spent_segments.items():
                    for category in product_categories:
                        category_condition = self.data['product_category'] == category

                        if category_condition.sum() > 0:
                            customer_segment_condition = segment_condition & category_condition

                            if customer_segment_condition.sum() > 0:
                                self.data.loc[customer_segment_condition, 'customer_segment'] = f'{segment_name} - {category}'

                print("Data telah dibagi menjadi grup customer sesuai dengan pengeluaran dan kategori produk.")

            except Exception as e:
                print("Gagal melakukan pembagian grup customer:", str(e))
    def transform(self, data):
        # Panggil metode transform dari kelas dasar untuk melakukan transformasi dasar
        transformed_data = super().transform(data)

        # Tambahkan logika segmentasi pelanggan di sini
        for record in transformed_data:
            # Logika segmentasi pelanggan
            if record['total_pembelian'] > 1000:
                record['segment'] = 'Premium'
            else:
                record['segment'] = 'Regular'

        return transformed_data

    def total_pembelian(self):
        if self.data is not None:
            total = sum(record['total_pembelian'] for record in self.data if 'total_pembelian' in record)
            return total
        else:
            return 0

from pprint import pprint

data = [
    {'customer_id': 'C001', 'total_pembelian': 1200, 'product_category': 'Electronics'},
    {'customer_id': 'C002', 'total_pembelian': 750, 'product_category': 'Books'},
    {'customer_id': 'C003', 'total_pembelian': 350, 'product_category': 'Home & Garden'},
    {'customer_id': 'C004', 'total_pembelian': 2050,
     'product_category': 'Electronics'},
    {'customer_id': 'C005', 'total_pembelian': 800, 'product_category': 'Beauty'},
]

etl_process = TargetedMarketingETL("data_file.csv")
etl_process.extract()  # melakukan ekstraksi data khusus jika diperlukan
etl_process.segment_customers()  # melakukan segmentasi pelanggan
total_pembelian = etl_process.total_pembelian()
print("Total Pembelian:", total_pembelian)



pprint(etl.data)
