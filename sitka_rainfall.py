import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = '/Users/eugeneheynike/Desktop/DataVisualisation/sitka_precip.csv'

dates, precip = [], []
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for row in reader:
        current_date = datetime.strptime(row[0], '%Y%m%dT%H%M')
        dates.append(current_date)
        precipitation = float(row[2])
        precip.append(precipitation)

fig, ax = plt.subplots()
ax.plot(dates, precip)
plt.title('Sitka Rainfall')
plt.ylabel('Inches')
fig.autofmt_xdate()
plt.show()
for index, col_header in enumerate(header_row):
        print(index, col_header)

print(precip)