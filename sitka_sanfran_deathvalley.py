import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename1 = '/Users/eugeneheynike/Desktop/DataVisualisation/sitka_precip.csv'
filename2 = '/Users/eugeneheynike/Desktop/death_valley.csv'
filename3 = '/Users/eugeneheynike/Desktop/san_fran.csv'

dates1, dates2, dates3, temp1, temp2, temp3 = [], [], [], [], [], []

with open(filename1) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for row in reader:
        current_date = datetime.strptime(row[0], '%Y%m%dT%H%M')
        dates1.append(current_date)
        temperature = float(row[1])
        temp1.append(temperature)

with open(filename2) as f:
    reader = csv.reader(f)
    header_row2 = next(reader)
    for row in reader:
        current_date = datetime.strptime(row[0], '%Y%m%dT%H%M')
        dates2.append(current_date)
        temperature = float(row[1])
        temp2.append(temperature)

with open(filename3) as f:
    reader = csv.reader(f)
    header_row3 = next(reader)
    for row in reader:
        current_date = datetime.strptime(row[0], '%Y%m%dT%H%M')
        dates3.append(current_date)
        temperature = float(row[1])
        temp3.append(temperature)

fig, ax = plt.subplots()
ax.plot(dates1, temp1)
ax.plot(dates2, temp2)
ax.plot(dates3, temp3)
plt.title('Sitka(blue), Death Valley(orange), San Francisco(green) (Temperature)')
plt.ylabel('Degrees (C)')
fig.autofmt_xdate()
plt.show()
for index, col_header in enumerate(header_row3):
    print(index, col_header)
