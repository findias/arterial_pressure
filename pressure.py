from datetime import datetime
import csv

# Fuction for pressure
def pressure(message):
    while True:
        try:
            indication = int(input(message))
            break
        except ValueError:
            print('You can input only numbers! Please try again')
    return str(indication)

# Write data to a CSV file path
def csv_writer(data_monitoring, path_monitoring):
    with open(path_monitoring, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(data_monitoring)

# Variable for pressure
systolic_pressure = pressure('Input systolic pressure please: ')
diastolic_pressure = pressure('Input diastolic pressure please: ')
monitoring_date = str(datetime.strftime(datetime.now(), '%Y.%m.%d %H:%M '))

# Variable and function for write csv
data_monitoring = [monitoring_date.strip(), systolic_pressure, diastolic_pressure]
path_monitoring = 'monitoring.csv'
csv_writer(data_monitoring, path_monitoring)

print(data_monitoring)