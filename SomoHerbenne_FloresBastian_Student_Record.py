'''
SOMO, HERBENNE REY V.
FLORES, BASTIAN BRAGI M.
BSIS-2AB-M

STUDENT RECORD MANAGEMENT PROGRAM WITH OOP
PRELIMS - PYTHON PROJECT # 1 - (OOP)

STUDENT RECORD
'''

import os
from time import sleep

def Main_Menu(): # MENU
    
    print("\n\t\t\t\t\t  WELCOME TO STUDENT RECORD MENU\n")
    print("\t\t---------------------------------------------------------------------------------------\n")
    print("\t\t      [1] ADD STUDENT RECORD\t\t\t[5] READ STUDENT RECORD USING CSV")
    print("\t\t      [2] DISPLAY STUDENT RECORD\t\t[6] DELETE STUDENT RECORD")
    print("\t\t      [3] SEARCH STUDENT RECORD\t\t\t[7] SORT STUDENT RECORD")
    print("\t\t      [4] UPDATE STUDENT RECORD\t\t\t[8] EXIT THE PROGRAM")
  
while True:
    from Somo_Flores_main import importing
    os.system('cls')
    Main_Menu()
    menu_choice = int(input("\nEnter Your Choice: "))
    if (menu_choice== 1):
        importing.Add_Student()
    elif (menu_choice == 2):
        importing.Display_Student()
    elif (menu_choice == 3):
        importing.Search_Student()
    elif (menu_choice == 4):
        importing.Update_Record()
    elif (menu_choice == 5):
        importing.Read_from_CSV()
    elif (menu_choice == 6):
        importing.Delete_Student()
    elif (menu_choice == 7):
        while True:
            from Somo_Herbenne_Flores_Bastian_Sorting import Sort
            os.system('cls')
            print("\n\t\t\t\t\t    SORTING MENU\n")
            print("\t\t--------------------------------------------------------------------\n")
            print("\t\t[1] Sort By ID\t\t\t[4] Sort By Grade of Math Subject")
            print("\t\t[2] Sort By Name\t\t[5] Sort By Grade of English Subject")
            print("\t\t[3] Sort By Average\t\t[6] Sort By Grade of Science Subject")
            print("\n\t\t\t\t[7] Return to Main Menu")

            pick = int(input("\nEnter Your Choice: "))
            if pick == 1:
                Sort.sort0()
            elif pick == 2:
                Sort.sort1()
            elif pick == 3:
                Sort.sort5()
            elif pick == 4:
                Sort.sort2()
            elif pick == 5:
                Sort.sort3()
            elif pick == 6:
                Sort.sort4()
            elif pick == 7:
                print("\n\t\t\t\t\t    Returning...")
                sleep(2)
                break
            else:
                print("\n\t\t\t\t\t  Invalid option! Try Again.")
                
    elif (menu_choice == 8):
        exit()
    else:
        print("\n\t\t\t\t\t  Invalid option! Try Again.")
        