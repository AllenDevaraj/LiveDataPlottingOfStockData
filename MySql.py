import time
import mysql.connector as cnt
import pandas
from mysql.connector import errorcode

mydb = cnt.connect(host='localhost', user='root', passwd='<insert your passwd>' , database='project')
c = mydb.cursor()
try:
    c.execute('create database project')
    c.execute('use project')
except cnt.Error as err:
    if err.errno == 1007:   #errorcode.ER_DATABASE_EXISTS_ERROR
        c.execute('drop database project')
        c.execute('create database project')
        c.execute('use project')

print("At a time, you can view the live graphical representation for any two companies...")
time.sleep(3)
def main():
    print("You can present your choice of any two companies from the ones given below : ")
    time.sleep(3)
    print()
    print("1.Apple")
    time.sleep(1)
    print("2.Microsoft")
    time.sleep(1)
    print("3.Google")
    time.sleep(2)
    print()
    choice1 = int(input("Choose the first company who's live stocks you'd like to view.Choose from the above three companies only (1/2/3) : "))
    print()
    choice2 = int(input("Choose the second company who's live stocks you'd like to view.Choose from the remaining two companies only (1/2/3) : "))
    print()
    print("Checking the entries.This might take a few seconds...")
    time.sleep(4)
    if choice1 != choice2:
        print()
        print("Thank You for the entries...")
        if choice1 == 1:
            if choice2 == 2:
                try:
                    c.execute('create table first(x_value int, t1 int)')
                except cnt.Error as err:
                    if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:   #1064
                        c.execute('delete from table first')
                        c.execute('drop table first')
                        c.execute('create table first(x_value int, t1 int)')
                c.execute('insert into first values(0, 1000)')
                c.execute('insert into first values(1, 1000)')
                c.execute('insert into first values(2, 1004)')
                c.execute('insert into first values(3, 997)')
                c.execute('insert into first values(4, 1008)')
                c.execute('insert into first values(5, 999)')
                c.execute('insert into first values(6, 996)')
                c.execute('insert into first values(7, 988)')
                c.execute('insert into first values(8, 995)')
                c.execute('insert into first values(9, 998)')
                c.execute('insert into first values(10, 1005)')
                try:
                    c.execute('create table second(x_value int, t2 int)')
                except cnt.Error as err:
                    if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                        c.execute('delete from table second')
                        c.execute('drop table second')
                        c.execute('create table second(x_value int, t2 int)')
                c.execute('insert into second values(0, 1000)')
                c.execute('insert into second values(1, 1005)')
                c.execute('insert into second values(2, 1010)')
                c.execute('insert into second values(3, 1011)')
                c.execute('insert into second values(4, 1002)')
                c.execute('insert into second values(5, 1014)')
                c.execute('insert into second values(6, 1020)')
                c.execute('insert into second values(7, 1019)')
                c.execute('insert into second values(8, 1018)')
                c.execute('insert into second values(9, 1022)')
                c.execute('insert into second values(10, 1018)')
                c.execute('create table final as select first.*,second.t2 from first join second on first.x_value=second.x_value')

            if choice2 == 3:
                try:
                    c.execute('create table first(x_value int, t1 int)')
                except cnt.Error as err:
                    if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                        c.execute('delete from table first')
                        c.execute('drop table first')
                        c.execute('create table first(x_value int, t1 int)')
                c.execute('insert into first values(0, 1000)')
                c.execute('insert into first values(1, 1000)')
                c.execute('insert into first values(2, 1004)')
                c.execute('insert into first values(3, 997)')
                c.execute('insert into first values(4, 1008)')
                c.execute('insert into first values(5, 999)')
                c.execute('insert into first values(6, 996)')
                c.execute('insert into first values(7, 988)')
                c.execute('insert into first values(8, 995)')
                c.execute('insert into first values(9, 998)')
                c.execute('insert into first values(10, 1005)')
                try:
                    c.execute('create table second(x_value int, t2 int)')
                except cnt.Error as err:
                    if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                        c.execute('delete from table second')
                        c.execute('drop table second')
                        c.execute('create table second(x_value int, t2 int)')
                c.execute('insert into second values(0, 1000)')
                c.execute('insert into second values(1, 1003)')
                c.execute('insert into second values(2, 1007)')
                c.execute('insert into second values(3, 1006)')
                c.execute('insert into second values(4, 1012)')
                c.execute('insert into second values(5, 1010)')
                c.execute('insert into second values(6, 1007)')
                c.execute('insert into second values(7, 1001)')
                c.execute('insert into second values(8, 1014)')
                c.execute('insert into second values(9, 1020)')
                c.execute('insert into second values(10, 1023)')
                c.execute('create table final as select first.*,second.t2 from first join second on first.x_value=second.x_value')
        if choice1==2:
            if choice2==1:
                try:
                    c.execute('create table first(x_value int, t1 int)')
                except cnt.Error as err:
                    if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                        c.execute('delete from table first')
                        c.execute('drop table first')
                        c.execute('create table first(x_value int, t1 int)')
                c.execute('insert into first values(0, 1000)')
                c.execute('insert into first values(1, 1005)')
                c.execute('insert into first values(2, 1010)')
                c.execute('insert into first values(3, 1011)')
                c.execute('insert into first values(4, 1002)')
                c.execute('insert into first values(5, 1014)')
                c.execute('insert into first values(6, 1020)')
                c.execute('insert into first values(7, 1019)')
                c.execute('insert into first values(8, 1018)')
                c.execute('insert into first values(9, 1022)')
                c.execute('insert into first values(10, 1018)')
                try:
                    c.execute('create table second(x_value int, t2 int)')
                except cnt.Error as err:
                    if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                        c.execute('delete from table second')
                        c.execute('drop table second')
                        c.execute('create table second(x_value int, t2 int)')
                c.execute('insert into second values(0, 1000)')
                c.execute('insert into second values(1, 1000)')
                c.execute('insert into second values(2, 1004)')
                c.execute('insert into second values(3, 997)')
                c.execute('insert into second values(4, 1008)')
                c.execute('insert into second values(5, 999)')
                c.execute('insert into second values(6, 996)')
                c.execute('insert into second values(7, 988)')
                c.execute('insert into second values(8, 995)')
                c.execute('insert into second values(9, 998)')
                c.execute('insert into second values(10, 1005)')
                c.execute('create table final as select first.*,second.t2 from first join second on first.x_value=second.x_value')
            if choice2==3:
                try:
                    c.execute('create table first(x_value int, t1 int)')
                except cnt.Error as err:
                    if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                        c.execute('delete from table first')
                        c.execute('drop table first')
                        c.execute('create table first(x_value int, t1 int)')
                c.execute('insert into first values(0, 1000)')
                c.execute('insert into first values(1, 1005)')
                c.execute('insert into first values(2, 1010)')
                c.execute('insert into first values(3, 1011)')
                c.execute('insert into first values(4, 1002)')
                c.execute('insert into first values(5, 1014)')
                c.execute('insert into first values(6, 1020)')
                c.execute('insert into first values(7, 1019)')
                c.execute('insert into first values(8, 1018)')
                c.execute('insert into first values(9, 1022)')
                c.execute('insert into first values(10, 1018)')
                try:
                    c.execute('create table second(x_value int, t2 int)')
                except cnt.Error as err:
                    if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                        c.execute('delete from table second')
                        c.execute('drop table second')
                        c.execute('create table second(x_value int, t2 int)')
                c.execute('insert into second values(0, 1000)')
                c.execute('insert into second values(1, 1003)')
                c.execute('insert into second values(2, 1007)')
                c.execute('insert into second values(3, 1006)')
                c.execute('insert into second values(4, 1012)')
                c.execute('insert into second values(5, 1010)')
                c.execute('insert into second values(6, 1007)')
                c.execute('insert into second values(7, 1001)')
                c.execute('insert into second values(8, 1014)')
                c.execute('insert into second values(9, 1020)')
                c.execute('insert into second values(10, 1023)')
                c.execute('create table final as select first.*,second.t2 from first join second on first.x_value=second.x_value')
        if choice1==3:
            if choice2==1:
                try:
                    c.execute('create table first(x_value int, t1 int)')
                except cnt.Error as err:
                    if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                        c.execute('delete from table first')
                        c.execute('drop table first')
                        c.execute('create table first(x_value int, t1 int)')
                c.execute('insert into first values(0, 1000)')
                c.execute('insert into first values(1, 1003)')
                c.execute('insert into first values(2, 1007)')
                c.execute('insert into first values(3, 1006)')
                c.execute('insert into first values(4, 1012)')
                c.execute('insert into first values(5, 1010)')
                c.execute('insert into first values(6, 1007)')
                c.execute('insert into first values(7, 1001)')
                c.execute('insert into first values(8, 1014)')
                c.execute('insert into first values(9, 1020)')
                c.execute('insert into first values(10, 1023)')
                try:
                    c.execute('create table second(x_value int, t2 int)')
                except cnt.Error as err:
                    if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                        c.execute('delete from table second')
                        c.execute('drop table second')
                        c.execute('create table second(x_value int, t2 int)')
                c.execute('insert into second values(0, 1000)')
                c.execute('insert into second values(1, 1000)')
                c.execute('insert into second values(2, 1004)')
                c.execute('insert into second values(3, 997)')
                c.execute('insert into second values(4, 1008)')
                c.execute('insert into second values(5, 999)')
                c.execute('insert into second values(6, 996)')
                c.execute('insert into second values(7, 988)')
                c.execute('insert into second values(8, 995)')
                c.execute('insert into second values(9, 998)')
                c.execute('insert into second values(10, 1005)')
                c.execute('create table final as select first.*,second.t2 from first join second on first.x_value=second.x_value')
            if choice2==2:
                try:
                    c.execute('create table first(x_value int, t1 int)')
                except cnt.Error as err:
                    if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                        c.execute('delete from table first')
                        c.execute('drop table first')
                        c.execute('create table first(x_value int, t1 int)')
                c.execute('insert into first values(0, 1000)')
                c.execute('insert into first values(1, 1003)')
                c.execute('insert into first values(2, 1007)')
                c.execute('insert into first values(3, 1006)')
                c.execute('insert into first values(4, 1012)')
                c.execute('insert into first values(5, 1010)')
                c.execute('insert into first values(6, 1007)')
                c.execute('insert into first values(7, 1001)')
                c.execute('insert into first values(8, 1014)')
                c.execute('insert into first values(9, 1020)')
                c.execute('insert into first values(10, 1023)')
                try:
                    c.execute('create table second(x_value int, t2 int)')
                except cnt.Error as err:
                    if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                        c.execute('delete from table second')
                        c.execute('drop table second')
                        c.execute('create table second(x_value int, t2 int)')
                c.execute('insert into second values(0, 1000)')
                c.execute('insert into second values(1, 1005)')
                c.execute('insert into second values(2, 1010)')
                c.execute('insert into second values(3, 1011)')
                c.execute('insert into second values(4, 1002)')
                c.execute('insert into second values(5, 1014)')
                c.execute('insert into second values(6, 1020)')
                c.execute('insert into second values(7, 1019)')
                c.execute('insert into second values(8, 1018)')
                c.execute('insert into second values(9, 1022)')
                c.execute('insert into second values(10, 1018)')
                c.execute('create table final as select first.*,second.t2 from first join second on first.x_value=second.x_value')
    if choice1 == choice2:
        print()
        print("Error : You can't choose the same company more than once.")
        time.sleep(2)
        print()
        main()

    query = 'select * from final'

    results = pandas.read_sql_query(query, mydb)      #mysql to csv 
    results.to_csv("data.csv", index=False)

    f = open("choice1.txt","w")
    f.write(str(choice1))
    f.close()

    f = open("choice2.txt","w")
    f.write(str(choice2))
    f.close()

main()
