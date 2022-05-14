with open("/mnt/c/Users/billc/Pictures/voices.csv") as file:
    for line in file:
        cols = line.rstrip().split(",")
        print("insert into voices (id, locale, gender, name) values (%s,'%s','%s','%s');" % (cols[0],cols[1],cols[2],cols[3]))