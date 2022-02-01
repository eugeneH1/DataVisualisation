import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = '/Users/eugeneheynike/Desktop/weather-anomalies-1964-2013.csv'
index = 0
limit = 300
data = {}
dates, highs, lows = [], [], []
dates1 = []

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    next_date = 0
    for row in reader:
        if index == limit:
            break
        current_date = datetime.strptime(row[0], '%Y-%m-%d')
        if current_date not in dates and current_date.year == 1977:
            dates.append(current_date)
            high = row[5]
            low = row[6]
            data[current_date] = [low, high]
            index += 1

sorted_data = {}
for key in sorted(data):
    sorted_data[key] = data[key]
    dates1.append(key)
    lows.append(float(data[key][0]))
    highs.append(float(data[key][1]))

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates1, highs, c='red')
ax.plot(dates1, lows, c='blue')
plt.title("Daily high temperatures, 1977", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (C)', fontsize=16)
plt.fill_between(dates1, highs, lows, facecolor='blue', alpha=0.1)
plt.show()

print(dates)
print(highs)
