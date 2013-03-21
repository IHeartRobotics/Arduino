#!/usr/bin/python
import serial

file = open('out.txt', 'w')
ser = serial.Serial('/dev/ttyACM5', 9600) 


while True:
    output = ser.readline()
    file.write(output)
    print output
file.close()
