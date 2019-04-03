from datetime import datetime

# Forming a function for time
def measurement_time(func):
    def wrapper(message):
        return str(datetime.strftime(datetime.now(), '%Y.%m.%d %H:%M ')) + func(message)
    return wrapper

# Insert systolic pressure and diastolic pressure
@ measurement_time
def pressure(message):
    while True:
        try:
            indication = int(input(message))
            break
        except ValueError:
            print('You can input only numbers! Please try again')
    return str(indication)

# Variable for pressure
systolic_pressure = pressure('Input systolic pressure please: ')
diastolic_pressure = pressure('Input diastolic pressure please: ')

with open('systolic.txt', 'a') as f:
     f.write(systolic_pressure + '\n')

with open('diastolic.txt', 'a') as f:
    f.write(diastolic_pressure + '\n')

with open('pressure.txt', 'a') as f:
    f.write(systolic_pressure + '/' + diastolic_pressure + '\n')

print(systolic_pressure + '/' + diastolic_pressure[17:])