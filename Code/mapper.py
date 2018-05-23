import sys

def mapper():
    # read standard input line by line
    for line in sys.stdin:
        # strip off extra whitespace, split on tab and put the data in an array
        data = line.strip().split("\t")

        # Parse the file to check if the line is in standard format
        if(len(data)!=6):
            continue

        # access the data with data[2] and data[5]
        date, time, store, item, cost, payment = data

        # Now print out the data that will be passed to the reducer
        print "{0}\t{1}".format(store, cost)
