"""
utility class for generating test csv files
"""
import csv
from random import randint
from random import choice

"""
method for generating random girls and writing into 'girls_test.csv' file 
"""
def random_girls(n):
    i = 0
    filename = 'girls_test.csv'
    try:
        outfile = open(filename, "wb")
        writer = csv.writer(outfile )
        while i < n:
            writer.writerow([ str("Girl" + str(i+1)), randint(1, 10), randint(30, 160),
                             randint(100, 10000), choice(['choosy', 'normal', 'desperate'])])
            i += 1
    finally:
        outfile.close()
    return filename

"""
method for generating random boys and writing into 'boys_test.csv' file 
"""
def random_boys(n):
    i = 0
    filename = 'boys_test.csv'
    try:
        outfile = open(filename, "wb")
        writer = csv.writer(outfile)
        while i < n:
            writer.writerow([ "Boy" + str(i + 1), randint(1, 10), randint(30, 160),
                             randint(100, 10000), randint(2, 10),choice(['miser', 'generous', 'geek']) ])
            i += 1
    finally:
        outfile.close()
    return filename

"""
method for generating random gifts and writing into 'gifts_test.csv' file 
"""
def random_gifts(n):
    i = 0
    filename = 'gifts_test.csv'
    try:
        outfile = open(filename,"wb")
        writer = csv.writer(outfile)
        while i < n:
            i += 1
            type = choice(['essential', 'luxurious', 'utility'])
            writer.writerow([ i, randint(10, 5000), randint(0, 5000),randint(1, 10), randint(1, 10), type])
    finally:
        outfile.close()
    return filename
