# Pobranie bibliotek do wyświetlenia wykresów, pobrania daty, oraz inforamcji o kursach kryptowalut
import pandas_datareader as web
import matplotlib.pyplot as plt
import datetime as dt

# Waluta, do jakiej mają być porównywane kryptowaluty
currency = "USD"
# Ustawienie na wyświetlanie ostatniej wartości kryptowaluty
metric = "Close"

# Ustawienie początku i końca okresu, z którego ma wyświetlać kursy
start = dt.datetime(2021, 1, 1)
end = dt.datetime.now()

# Podanie wszystkich kryptowalut które program będzie nam wyświetlał
crypto = ['BTC', 'ETH', 'LTC', 'BNB', 'SOL', 'ADA', 'XRP', 'BUSD', 'ATOM', 'DOT']
# Pusta lista, do której później będą dodawane wartości 
colnames = []

first = True

# załadowanie baz danych oraz zapisanie ich do danych wykresu
for ticker in crypto:
    data = web.DataReader(f'{ticker}-{currency}', "yahoo", start, end)
    if first:
        combined = data[[metric]].copy()
        colnames.append(ticker)
        combined.columns = colnames
        first = False
    else:
        combined = combined.join(data[metric])
        colnames.append(ticker)
        combined.columns = colnames

# Zmiana ustawienia wykresu w celu lepeszej widzialności z powodu zróżnicowania kórsów bitcoina a reszty
plt.yscale('log')

# zapisanie danych do wykresów
for ticker in crypto:
    plt.plot(combined[ticker], label=ticker)

# Położenie legendy wykresów 
plt.legend(loc="upper right")

# Wyświetlenie wykresów
plt.show()