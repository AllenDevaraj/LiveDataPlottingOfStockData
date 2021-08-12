import csv
import random
import time

x_value = 0
t1 = 1000
t2 = 1000

fieldnames = ["x_value","t1","t2"]

with open('data.csv','w') as csv_file:
    csv_writer = csv.DictWriter(csv_file,fieldnames=fieldnames)
    csv_writer.writeheader()
    
while True:
    with open('data.csv','a') as csv_file:
        csv_writer = csv.DictWriter(csv_file,fieldnames=fieldnames)

        info = {"x_value":x_value,"t1":t1,"t2":t2}
        csv_writer.writerow(info)
        print(x_value,t1,t2)

        x_value += 1
        t1 = t1 + random.randint(-8,8)
        t2 = t2 + random.randint(-7,7)
    time.sleep(1)
