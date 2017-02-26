import csv
from random import randint
from random import choice


def random_girls(n):
    i = 0
    filename = 'girls_test.csv'
    try:
        outfile = open(filename, "wb")
        writer = csv.writer(outfile )
        while i < n:
            writer.writerow([ str("Girl" + str(i+1)), randint(1, 10), randint(30, 160),
                             randint(100, 10000), choice(['miser', 'generous', 'geek'])])
            i += 1
    finally:
        outfile.close()
    return filename


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