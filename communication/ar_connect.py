# +------------+--------------+-----------------------------------------------------------+
# |   Author   |     Date     |                         Changed                           |
# +------------+--------------+-----------------------------------------------------------+
# |  Jayden J. |  2022/10/13  | Initial release (added read_temp/insert_db func           |
# +------------+--------------+-----------------------------------------------------------+


import serial
ser = serial.Serial( 
    port="COM4",
    boudrate=9600
)


def insert_db():
    pass


def read_temp():

    while not ser.readable():
        pass

    data = ser.read()

    insert_db()

