# Write your code here :-)
import sys

def main():
    readings = {}
    while True:
        print('Choice 1: Log Sensor Reading')
        print('Choice 2: Update a Sensor Reading')
        print('Choice 3: Display All Sensor Readings')
        print('Choice 4: Exit\n')

        choice = input('Enter the number of your choice: ')

        if choice == '1':
            print(' LOGGING SENSOR READINGS: ')
            time = input(' Enter timestamp (hh:mm AM/PM): ')
            while True:
                temp = input(' Enter sensor reading: ')
                try:
                    float_temp = float(temp)
                    break
                except ValueError:
                    print('Invalid input')
            new_data(readings, time, float_temp)

        elif choice == '2':
            try:
                if time in readings:
                    print(' UPDATING A SENSOR READING:')
                    time = input(' Enter timestamp to update (h:mm AM/PM: ')
                    if time not in readings:
                        print(' Error: Timestamp has not been recorded.')
                        break
                    temp = input(' Enter new sensor reading: ')
                    float_temp = float(temp)
                    update(readings, time, float_temp)
            except UnboundLocalError:
                print(' Error: No timestamps have been recorded.\n')

        elif choice == '3':
            try:
                display(readings, time, float_temp)
            except UnboundLocalError:
                print(' Error: There are no readings to display.\n')

        elif choice == '4':
            sys.exit()

def new_data(readings, time, float_temp):
    if time not in readings:
        readings[time] = float_temp
        print(' Reading saved!\n')

def update(readings, time, float_temp):
    if time in readings:
        readings[time] = float_temp
        print('Reading updated!\n')

def display(readings, time, float_temp):
    print(' \nDISPLAY ALL SENSOR READING:')
    for key, value in readings.items():
        print(f' -{key} {value}' + chr(176) + 'F')
    print('')


if __name__ == "__main__":
    main()

