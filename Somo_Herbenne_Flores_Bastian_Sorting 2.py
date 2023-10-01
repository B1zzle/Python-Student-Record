'''
SOMO, HERBENNE REY V.
FLORES, BASTIAN BRAGI M.
BSIS-2AB-M

STUDENT RECORD MANAGEMENT PROGRAM WITH OOP
PRELIMS - PYTHON PROJECT # 1 - (OOP)

SORTING - INSERTION SORT
'''
import os
import csv, operator
from time import sleep

class Sort: # Insertion sort was used and applied for the user to choose what category to sort.
    def sort0():

            print("\n\t\t[1] Ascending\t\t\t[2] Descending")
            pick = int(input("\nEnter Sorting Option: "))
            if pick == 1:
                file = open('Records.csv', 'r')
                Reader = csv.reader(file, delimiter=',')

                sort = sorted(Reader, key = operator.itemgetter(0))

                for eachline in sort:
                    print(eachline)
                print("\n\t\tThank You!, Please Wait 10 sec to go back")
                print("\n\t\t\t DONT CLICK ANYTHING")
                sleep(10)
                os.system('cls')
            elif pick == 2:
                file = open('Records.csv', 'r')
                Reader = csv.reader(file, delimiter=',')

                sort = sorted(Reader, key = operator.itemgetter(0), reverse=True)

                for eachline in sort:
                    print(eachline)
                print("\n\t\tThank You!, Please Wait 10 sec to go back")
                print("\n\t\t\t DONT CLICK ANYTHING")
                sleep(10)
                os.system('cls')
    def sort1():

            print("\n\t\t[1] Ascending\t\t\t[2] Descending")
            pick = int(input("\nEnter Sorting Option: "))
            if pick == 1:
                file = open('Records.csv', 'r')
                Reader = csv.reader(file, delimiter=',')

                sort = sorted(Reader, key = operator.itemgetter(1))

                for eachline in sort:
                    print(eachline)
                print("\n\t\tThank You!, Please Wait 10 sec to go back")
                print("\n\t\t\t DONT CLICK ANYTHING")
                sleep(10)
                os.system('cls')
            elif pick == 2:
                file = open('Records.csv', 'r')
                Reader = csv.reader(file, delimiter=',')

                sort = sorted(Reader, key = operator.itemgetter(1), reverse=True)

                for eachline in sort:
                    print(eachline)
                print("\n\t\tThank You!, Please Wait 10 sec to go back")
                print("\n\t\t\t DONT CLICK ANYTHING")
                sleep(10)
                os.system('cls')

    def sort2():

            print("\n\t\t[1] Ascending\t\t\t[2] Descending")
            pick = int(input("\nEnter Sorting Option: "))
            if pick == 1:
                file = open('Records.csv', 'r')
                Reader = csv.reader(file, delimiter=',')

                sort = sorted(Reader, key = operator.itemgetter(2))

                for eachline in sort:
                    print(eachline)
                print("\n\t\tThank You!, Please Wait 10 sec to go back")
                print("\n\t\t\t DONT CLICK ANYTHING")
                sleep(10)
                os.system('cls')
            elif pick == 2:
                file = open('Records.csv', 'r')
                Reader = csv.reader(file, delimiter=',')

                sort = sorted(Reader, key = operator.itemgetter(2), reverse=True)

                for eachline in sort:
                    print(eachline)
                print("\n\t\tThank You!, Please Wait 10 sec to go back")
                print("\n\t\t\t DONT CLICK ANYTHING")
                sleep(10)
                os.system('cls')

    def sort3():

            print("\n\t\t[1] Ascending\t\t\t[2] Descending")
            pick = int(input("\nEnter Sorting Option: "))
            if pick == 1:
                file = open('Records.csv', 'r')
                Reader = csv.reader(file, delimiter=',')

                sort = sorted(Reader, key = operator.itemgetter(3))

                for eachline in sort:
                    print(eachline)
                print("\n\t\tThank You!, Please Wait 10 sec to go back")
                print("\n\t\t\t DONT CLICK ANYTHING")
                sleep(10)
                os.system('cls')
            elif pick == 2:
                file = open('Records.csv', 'r')
                Reader = csv.reader(file, delimiter=',')

                sort = sorted(Reader, key = operator.itemgetter(3), reverse=True)

                for eachline in sort:
                    print(eachline)
                print("\n\t\tThank You!, Please Wait 10 sec to go back")
                print("\n\t\t\t DONT CLICK ANYTHING")
                sleep(10)
                os.system('cls')

    def sort4():

            print("\n\t\t[1] Ascending\t\t\t[2] Descending")
            pick = int(input("\nEnter Sorting Option: "))
            if pick == 1:
                file = open('Records.csv', 'r')
                Reader = csv.reader(file, delimiter=',')

                sort = sorted(Reader, key = operator.itemgetter(4))

                for eachline in sort:
                    print(eachline)
                print("\n\t\tThank You!, Please Wait 10 sec to go back")
                print("\n\t\t\t DONT CLICK ANYTHING")
                sleep(10)
                os.system('cls')
            elif pick == 2:
                file = open('Records.csv', 'r')
                Reader = csv.reader(file, delimiter=',')

                sort = sorted(Reader, key = operator.itemgetter(4), reverse=True)

                for eachline in sort:
                    print(eachline)
                print("\n\t\tThank You!, Please Wait 10 sec to go back")
                print("\n\t\t\t DONT CLICK ANYTHING")
                sleep(10)
                os.system('cls')
    
    def sort5():

            print("\n\t\t[1] Ascending\t\t\t[2] Descending")
            pick = int(input("\nEnter Sorting Option: "))
            if pick == 1:
                file = open('Records.csv', 'r')
                Reader = csv.reader(file, delimiter=',')

                sort = sorted(Reader, key = operator.itemgetter(5))

                for eachline in sort:
                    print(eachline)
                print("\n\t\tThank You!, Please Wait 10 sec to go back")
                print("\n\t\t\t DONT CLICK ANYTHING")
                sleep(10)
                os.system('cls')
            elif pick == 2:
                file = open('Records.csv', 'r')
                Reader = csv.reader(file, delimiter=',')

                sort = sorted(Reader, key = operator.itemgetter(5), reverse=True)

                for eachline in sort:
                    print(eachline)
                print("\n\t\tThank You!, Please Wait 10 sec to go back")
                print("\n\t\t\t DONT CLICK ANYTHING")
                sleep(10)
                os.system('cls')