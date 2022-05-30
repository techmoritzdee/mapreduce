import sys


for line in sys.stdin:
    data = line.strip().split("\t")

    if len(data) != 6:
        sys.stdout.write("Error: The data do not contain 6 elements")
    else:
        date, time, item, category, sales, payment = data
    
        sys.stdout.write("{0}\t{1}\n".format(category, sales))
