from binance.client import Client
import pandas as pd
import time

# Ganti dengan API Key dan Secret Key Anda
API_KEY = 'your_api_key'
API_SECRET = 'your_api_secret'

# Inisialisasi client Binance
client = Client(API_KEY, API_SECRET)

# Parameter trading
symbol = 'BTCUSDT'  # Pasangan trading
quantity = 0.001    # Jumlah aset yang akan dibeli/dijual
short_window = 10   # Jangka pendek moving average
long_window = 50    # Jangka panjang moving average

# Fungsi untuk mendapatkan data harga historis
def get_historical_data(symbol, interval, lookback):
    klines = client.get_historical_klines(symbol, interval, lookback)
    data = pd.DataFrame(klines, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'])
    data['close'] = data['close'].astype(float)
    return data

# Fungsi untuk menghitung moving average
def calculate_moving_averages(data, short_window, long_window):
    data['short_ma'] = data['close'].rolling(window=short_window).mean()
    data['long_ma'] = data['close'].rolling(window=long_window).mean()
    return data

# Fungsi untuk mengecek sinyal trading
def check_trading_signal(data):
    if data['short_ma'].iloc[-1] > data['long_ma'].iloc[-1] and data['short_ma'].iloc[-2] <= data['long_ma'].iloc[-2]:
        return 'buy'
    elif data['short_ma'].iloc[-1] < data['long_ma'].iloc[-1] and data['short_ma'].iloc[-2] >= data['long_ma'].iloc[-2]:
        return 'sell'
    else:
        return 'hold'

# Fungsi untuk melakukan order beli
def place_buy_order(symbol, quantity):
    try:
        order = client.order_market_buy(symbol=symbol, quantity=quantity)
        print(f"Order Beli Berhasil: {order}")
    except Exception as e:
        print(f"Gagal melakukan order beli: {e}")

# Fungsi untuk melakukan order jual
def place_sell_order(symbol, quantity):
    try:
        order = client.order_market_sell(symbol=symbol, quantity=quantity)
        print(f"Order Jual Berhasil: {order}")
    except Exception as e:
        print(f"Gagal melakukan order jual: {e}")

# Main loop
def main():
    print("Memulai bot trading...")
    while True:
        # Ambil data historis
        data = get_historical_data(symbol, Client.KLINE_INTERVAL_1HOUR, "1 day ago UTC")
        
        # Hitung moving averages
        data = calculate_moving_averages(data, short_window, long_window)
        
        # Cek sinyal trading
        signal = check_trading_signal(data)
        
        # Eksekusi order berdasarkan sinyal
        if signal == 'buy':
            print("Sinyal Beli Ditemukan!")
            place_buy_order(symbol, quantity)
        elif signal == 'sell':
            print("Sinyal Jual Ditemukan!")
            place_sell_order(symbol, quantity)
        else:
            print("Tidak ada sinyal trading. Menunggu...")
        
        # Tunggu sebelum melakukan iterasi berikutnya
        time.sleep(3600)  # Tunggu 1 jam

if __name__ == "__main__":
    main()
