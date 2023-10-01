'''
SOMO, HERBENNE REY V.
FLORES, BASTIAN BRAGI M.
BSIS-2AB-M

STUDENT RECORD MANAGEMENT PROGRAM WITH OOP
PRELIMS - PYTHON PROJECT # 1 - (OOP)

MAIN
'''
import os
import csv
from abc import ABC, abstractmethod

os.system('cls')

# Parent class 
class STUDENT:
    
    studentList = list()
    
    # Constructor __init__ (dunder/magic method) 
    def __init__(self, studID, studName, subjectGrade_1 = 0, subjectGrade_2 = 0, subjectGrade_3 = 0, Average = 0):
        self.__studID = studID
        self.__studName = studName
        self.__subjectGrade_1 = subjectGrade_1
        self.__subjectGrade_2 = subjectGrade_2
        self.__subjectGrade_3 = subjectGrade_3
        self.__Average = Average

    # Setters and Getters
    def setStudID(self, studID):
        self.studID = studID
    def getStudID(self):
        return self.studID  
    
    def setStudName(self, studName):
        self.studName = studName
    def getStudName(self):
        return self.studName
    
    def setsubjectGrade_1(self, subjectGrade_1):
        self.subjectGrade_1 = subjectGrade_1
    def getsubjectGrade_1(self):
        return self.subjectGrade_1
    
    def setsubjectGrade_2(self, subjectGrade_2):
        self.subjectGrade_2 = subjectGrade_2
    def getsubjectGrade_2(self):
        return self.subjectGrade_2
    
    def setsubjectGrade_3(self, subjectGrade_3):
        self.subjectGrade_3 = subjectGrade_3
    def getsubjectGrade_3(self):
        return self.subjectGrade_3
    
    def setAverage(self, Average):
        self.Average = Average
    def getAverage(self):
        return self.Average
    
    # (dunder/magic method)
    def __str__(self):
        return "%s %s %d %d %d %.2f"%(self.__studID, self.__studName, self.__subjectGrade_1, self.__subjectGrade_2, self.__subjectGrade_3, self.__Average)

# abstract class
class STUDENT_RECORD(ABC):
    
    # abstract methods for readability and ease of use
    @abstractmethod 
    def add_Student(self):
        pass
    @abstractmethod
    def get_StudentList(self):
        pass

# Child class [ inherits class STUDENT (Inheritance) and class ABC (Abstraction) ]
class STUDENT_RECORD(STUDENT, ABC):
    
    def __init__(self, studID, studName, subjectGrade_1, subjectGrade_2, subjectGrade_3, Average): 
        super().__init__(studID, studName, subjectGrade_1, subjectGrade_2, subjectGrade_3, Average) # inherits the class STUDENT 
    
    def add_Student(self):
        STUDENT_RECORD.studentList.append(self)
        
    @classmethod # used a class method for child class the returns the student list
    def get_StudentList(self):
        return STUDENT_RECORD.studentList
        
student = STUDENT_RECORD("", "", 0, 0, 0, 0)

class importing:
    def Add_Student(): # ADD/INSERT RECORDS
        
        
        with open('Records.csv', 'w+', newline='') as csv_file:
            myFile = csv.writer(csv_file)
            myFile.writerow(["!ID", "!Name", "!Math", "!English", "!Science", "!Average"])
            numStud = int(input("\n\t\t\tHow many STUDENTS you wanted to ADD? (MINUMUM OF 5 STUDENTS): "))
            if numStud < 5:
                print("\n\t\t\tMINIMUM OF 5 Students Only!")
                print("\n")
                os.system('pause')
            else:
                for i in range(numStud):
                    studID = input("\nSTUDENT " + str(i + 1) + " : Enter the ID of Student: ")
                    studName = input("\nSTUDENT " + str(i + 1) + " : Enter the NAME of Student: ")
                    studSubject_1 = int(input("\nSTUDENT " + str(i + 1) + " : Enter the GRADE in MATH: "))
                    studSubject_2 = int(input("\nSTUDENT " + str(i + 1) + " : Enter the GRADE in ENGLISH: "))
                    studSubject_3 = int(input("\nSTUDENT " + str(i + 1) + " : Enter the GRADE in SCIENCE: "))
                    Average = (round((studSubject_1 + studSubject_2 + studSubject_3) / 3.0, 2))  
                    stud = STUDENT_RECORD(studID, studName, studSubject_1, studSubject_2, studSubject_3, Average)
                    stud.add_Student()
                    myFile.writerow([studID, studName, studSubject_1, studSubject_2, studSubject_3, Average])
                    print("\n\t\t\tStudent {}, {} has been ADDED Succesfully.".format(studID, studName))
                    print("\nHere are the newly added student/s:\n")
                    for stud in student.get_StudentList():
                        print(stud)
                print("\n")
                os.system('pause')
                
    def Display_Student(): # VIEW/DISPLAY RECORDS
            
            file = open('Records.csv', 'r', newline='\n')
            Reader = csv.reader(file)
            print("\n")
            for rec in Reader:
                print(rec)
            print("\n")
            os.system('pause')
            file.close()
            
    def Search_Student(): # SEARCH FOR A RECORD

            data = []
            with open("Records.csv") as file:
                reader = csv.reader(file)
                for row in reader:
                    data.append(row)
            studID = input("Enter the ID of Student you wanted to SEARCH: ")
            col = [x[0] for x in data]
            if studID in col:
                for x in range(0, len(data)):
                    if studID == data[x][0]:
                        print("\nThis is the DATA that you SEARCHED for\n")
                        print(data[x])
                        print("\n")
                        os.system('pause')
                        os.system('cls')
            else:
                print("The Student entered to be searched does not EXIST!")
                print("\n")
                os.system('pause')
                os.system('cls')
                

    def Update_Record(): # UPDATE A RECORD
        
            file = open('Records.csv', 'r', newline='\n')
            print("\n")
            studID = input("Enter the ID of STUDENT you wanted to UPDATE: ")
            found = 0
            Reader = csv.reader(file)
            data = []
            for rec in Reader:
                if rec[0] == studID:
                    print("\n")
                    print("The Student Chosen: ", rec)  
                    rec[0] = input("Enter the New STUDENT ID: ")
                    rec[1] = input("Enter the New STUDENT NAME: ")
                    rec[2] = int(input("Enter the STUDENT's New Grade for Math: "))
                    rec[3] = int(input("Enter the STUDENT's New Grade for English: "))
                    rec[4] = int(input("Enter the STUDENT's New Grade for Science: "))
                    rec[5] = (round((rec[2] + rec[3] + rec[4]) / 3))
                    print("\nUpdated Student: ", rec)
                    found = 1
                    print("\n\t\t\tStudent ID: {} has been UPDATED Succesfully.".format(studID))
                data.append(rec)

            if found == 0:
                print("The Student entered to be updated does not EXIST!")
                file.close()
                print("\n")
                os.system('pause')
                os.system('cls')
            else:
                file = open('Records.csv', 'w', newline='')
                Writer = csv.writer(file)
                Writer.writerows(data)
                file.close()
                print("\n")
                os.system('pause')
                os.system('cls')

    def Read_from_CSV(): # READ RECORD SPECIFICALLY IN THE CSV
        
            with open('Records.csv') as file:
                reader = csv.DictReader(file)
                count = 0
                print("\n")
                print("\t\t[1] FOR ID\t\t\t[4] ENGLISH GRADE")
                print("\t\t[2] NAME\t\t\t[5] SCIENCE GRADE")
                print("\t\t[3] MATH GRADE\t\t\t[6] AVERAGE")
                catchoice = int(input("\nChoose What you wanted to see: "))
                if catchoice == 1:
                    print("\n")
                    print("LIST OF THE ID OF THE STUDENTS")
                    for row in reader:
                        print(row['!ID'])

                        if count > 5:
                            break
                        count += 1
                    print("\n")
                    os.system('pause')
                    os.system('cls')
                elif catchoice == 2:
                    print("\n")
                    print("LIST OF THE NAME OF THE STUDENTS")
                    for row in reader:
                        print(row['!Name'])

                        if count > 5:
                            break
                        count += 1
                    print("\n")
                    os.system('pause')
                    os.system('cls')
                elif catchoice == 3:
                    print("\n")
                    print("LIST OF MATH SUBJECT GRADE OF THE STUDENTS")
                    for row in reader:
                        print(row['!Math'])

                        if count > 5:
                            break
                        count += 1
                    print("\n")
                    os.system('pause')
                    os.system('cls')
                elif catchoice == 4:
                    print("\n")
                    print("LIST OF ENGLISH SUBJECT GRADE OF THE STUDENTS")
                    for row in reader:
                        print(row['!English'])

                        if count > 5:
                            break
                        count += 1
                    print("\n")
                    os.system('pause')
                    os.system('cls')
                elif catchoice == 5:
                    print("\n")
                    print("LIST OF SCIENCE PROJECT GRADE OF THE STUDENTS")
                    for row in reader:
                        print(row['!Science'])

                        if count > 5:
                            break
                        count += 1
                    print("\n")
                    os.system('pause')
                    os.system('cls')
                elif catchoice == 6:
                    print("LIST OF THE GRADE AVERAGE OF THE STUDENTS")
                    for row in reader:
                        print(row['!Average'])

                        if count > 5:
                            break
                        count += 1
                    print("\n")
                    os.system('pause')
                    os.system('cls')
                else:
                    print("\t\tInvalid option! Try Again.")
                    print("\n")
                    os.system('pause')
                    os.system('cls')
        
    def Delete_Student(): # DELETE RECORD
            
            file = open('Records.csv', 'r')
            Reader = csv.reader(file)
            found = 0
            data = []
            print("\n")
            studID = input("Enter The Student of ID you wanted to Delete: ")
            for rec in Reader:
                if (rec[0] != studID):
                    data.append(rec)
                else:
                    found = 1
            file.close()

            if found == 0:
                print("The Student entered to be Deleted does not EXIST!")
            else:
                file = open('Records.csv', 'w', newline='')
                Reader = csv.writer(file)
                Reader.writerows(data)
                print("\n\t\t\tStudent ID: {} has been DELETED Succesfully.".format(studID))
                print("\n")
                os.system('pause')
                file.close()
            os.system('cls')
 