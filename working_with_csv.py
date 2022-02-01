import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = '/Users/eugeneheynike/Desktop/pretoria_weather_modified.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)
    dates, temps, humidity = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[0], '%Y%m%dT%H%M')
        temp = round(float(row[1]))
        hum = row[2]
        dates.append(current_date)
        temps.append(temp)
        humidity.append(hum)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, temps, c='red')
# ax.plot(humidity, c='blue')
print(len(dates))
print(len(temps))
# Format plot
plt.title("Daily temperatures, 30/03 - 06/04/2021", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (C)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
