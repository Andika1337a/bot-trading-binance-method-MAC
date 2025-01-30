# bot-trading-binance-method-MAC

### Prasyarat:
1. Install library yang diperlukan:
   ```bash
   pip install python-binance pandas
   ```
2. Dapatkan API Key dan Secret Key dari Binance:
   - Login ke Binance.
   - Buka [API Management](https://www.binance.com/en/my/settings/api-management).
   - Buat API Key dan Secret Key.

### Penjelasan:
1. **Library `python-binance`**: Digunakan untuk berinteraksi dengan API Binance.
2. **Strategi Moving Average Crossover**:
   - Jika moving average jangka pendek (misalnya 10 periode) memotong moving average jangka panjang (misalnya 50 periode) dari bawah ke atas, itu adalah sinyal beli.
   - Jika moving average jangka pendek memotong moving average jangka panjang dari atas ke bawah, itu adalah sinyal jual.
3. **Order Market**: Script menggunakan order market untuk membeli dan menjual aset.
4. **Interval Data**: Data harga diambil setiap 1 jam (`KLINE_INTERVAL_1HOUR`).

### Catatan:
- **Risiko Trading**: Bot ini hanya contoh sederhana. Trading otomatis memiliki risiko tinggi, terutama jika tidak diuji secara menyeluruh.
- **Testing**: Sebaiknya uji bot di lingkungan sandbox atau dengan jumlah dana kecil terlebih dahulu.
- **Keamanan API Key**: Jangan pernah membagikan API Key dan Secret Key Anda. Simpan dengan aman.
