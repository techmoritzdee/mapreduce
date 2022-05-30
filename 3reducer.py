import sys


for line in sys.stdin:
    data = line.strip().split("\t")

    date, time, item, category, sales, payment = data
    
    if len(data) != 6:
        sys.stdout.write("Error: The data do not contain 6 elements")
    else:
        cat = ["Computers", "Cameras", "Video Games"]
        if category in cat:
            sys.stdout.write("{0}\t{1}\n".format(category, sales))
