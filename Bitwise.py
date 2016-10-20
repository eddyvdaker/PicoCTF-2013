#!/usr/bin/env python

pass_numbers = [193, 35, 9, 33, 1, 9, 3, 33, 9, 225]
password = ''
for x in range(10):
    for y in range(255):
        z = (((y << 5) | (y >> 3)) ^ 111) & 255
        if z == pass_numbers[x]:
            password = password + chr(y)

print(password)
