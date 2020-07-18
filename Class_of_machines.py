import os
import csv
import re

access = ('.jpeg', '.gif', '.jpg', '.png')
pattern = r'\D'


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]


class Car(CarBase):
    car_type = 'car'

    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(CarBase):
    car_type = 'truck'

    def __init__(self, brand, photo_file_name, carrying, body_whl, body_length=None, body_width=None,
                 body_height=None):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)
        self.body_whl = body_whl
        try:
            if self.body_whl == '' or len(self.body_whl.split('x')) > 3:
                self.body_whl = ['0.0', '0.0', '0.0']
            else:
                self.body_whl = body_whl.split('x')
        except AttributeError:
            pass
        self.body_length = float(self.body_whl[0])
        self.body_width = float(self.body_whl[1])
        self.body_height = float(self.body_whl[2])

    def get_body_volume(self):
        if self.body_whl == 0.0:
            return 0.0
        else:
            return float(self.body_length * self.body_width * self.body_height)


class SpecMachine(CarBase):
    car_type = 'spec_machine'

    def __init__(self, brand, photo_file_name, carrying, extra):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)
        self.extra = extra


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_file:
        reader = csv.reader(csv_file, delimiter=';')
        next(reader)
        for i in reader:
            if not i:
                continue
            if i[0] == 'car':
                if i[1] and i[2] and i[3] and i[5] and i[3].endswith(access):
                    try:
                        i[2] = int(i[2])
                        i[5] = float(i[5])
                    except ValueError:
                        continue
                    car_list += [Car(i[1], i[3], i[5], i[2])]
            if i[0] == 'truck':
                if i[1] and i[3] and i[5] and i[3].endswith(access):
                    if not i[4] or len(i[4].split('x')) < 3 or bool(re.match(pattern, i[4])):
                        a = '0.0x0.0x0.0'
                    else:
                        a = i[4].split('x')
                    try:
                        i[5] = float(i[5])
                    except ValueError:
                        continue
                    car_list += [Truck(i[1], i[3], i[5], a)]
            if i[0] == 'spec_machine':
                if i[1] and i[3] and i[5] and \
                        i[3].endswith(access) and i[6]:
                    try:
                        i[5] = float(i[5])
                    except ValueError:
                        continue
                    car_list += [SpecMachine(i[1], i[3], i[5], i[6])]
    return car_list
