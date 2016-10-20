#!/usr/bin/env python

import md5, time, csv

counter = 0

print('### MD5 Dictonary Attack Tool ###')
passHash = str(raw_input('Input the password hash to crack: '))
salt = str(raw_input('Input salt (leave empty for no salt): '))

wordfile = open('wordlist.csv', 'rb')
reader = csv.reader(wordfile)

startTime = time.time()

for row in reader:
    counter += 1
    currentPass = row[0] + salt
    digest = md5.new()
    digest.update(currentPass)
    currentHash = digest.hexdigest()

    if currentHash == passHash:
        stopTime = time.time()
        timeTaken = stopTime - startTime

        print('Password\t: %s' %currentPass)
        print('Time Taken \t: %s' %timeTaken)
        print('Attempts\t: %s' %counter)

        break
    
