#!/usr/bin/env python3
import os
import random
import string
import threading

test = "n"
print("Welcome the Bulk File Maker for Linux")

while test != "y":
    print("\n")
    inputFile = input("Enter the input file of random data you want to put in the files: ")
    outputLoc = input("Enter the Directory you wish to place the files (ex. format: /home/user/.../): ")
    fileName = str(input("Enter the file name that will be put in front of ID: "))
    fileType = str(input("Enter a file extension - example: txt, log, docx, pdf: "))
    amount = int(input("How many files do you want to make? "))
    min_size = int(input("Minimum Size of Files (in KiloBytes): "))
    max_size = int(input("Maximum Size of Files (in KiloBytes): "))
    i = 0
    print("\n\nPlease Confirm the following settings:")
    print("Input File- " + inputFile)
    print("Output File- " + outputLoc)
    print("File Name & Extenstion- " + fileName + "-<id>." + fileType)
    print("Amount of Files to be created- " + str(amount))
    print("Minimum File Size- " + str(min_size) + "KB")
    print("Maximum File Size- " + str(max_size) + "KB")
    test = input("***I confirm all settings are correct. Type y to begin or n to change the settings (y/n)***: ")



def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def file_maker(loc, name, type, fsize):
    thesize = str(fsize)
    command = "dd if=" + inputFile + " of=" + loc + name + "-" + id_generator() + "." + type + " bs=1K count=" + thesize
    os.system(command)


while i < amount:
    size1 = random.randint(min_size, max_size)
    thread1 = threading.Thread(target=file_maker, args=(outputLoc, fileName, fileType, size1))
    size2 = random.randint(min_size, max_size)
    thread2 = threading.Thread(target=file_maker, args=(outputLoc, fileName, fileType, size2))

    thread1.start()
    i = i + 1
    if (i < amount):
        thread2.start()
        i = i + 1
        thread2.join()

    thread1.join()

print("Your files have been created!")
