import json
from jsonModule import *

jsonFileName='E:\\Python\\MID Project\\PcList.json'
PC_List={}        

class LAB : 


    def __init__(self,PC_List) :
        self.PC_List=PC_List


    def main(self):        
        print("\n\t\t~~~~~~~~~ Menu ~~~~~~~~~\n")
        print("\t|----------------------------------")
        print("\t| 1. Show all PC")
        print("\t| 2. Search a PC")
        print("\t| 3. Add PC")
        print("\t| 4. Update PC")
        print("\t| 5. Remove PC")
        print("\t| 6. Quit")
        print("\t|----------------------------------")

        check=int(input("--> Select an option <--\n"))


        while check<1 or check>6:
            check=int(input("\n\nInvalid input! Try again.: "))

        if check==1:
            self.showAllPc()
        elif check==2:
            self.showPc()
        elif check==3:
            self.addPc()
        elif check==4:
            check=input("Press the PC No. you want to update: ")
            self.updatePc(check)
        elif check==5:
            check=input("Press the PC No. you want to remove: ")
            self.removePc(check)
        else: 
            print("Logged Out Successfully")
            return 


    def addPc(self):
        """For add new PC in Lab"""
        pc_no = input("PC no: ")

        try:
            
            if pc_no in load():
                print("PC number already exists.\n------\nPress\n")
                print("1. Modify existing PC")
                print("2. Remove existing PC")
                print("3. Back")
            

                check = int(input("\nEnter your choice: "))

                while check<1 or check>3:
                    check=input("Invalid input.! Please Try Again. ")    

                if check == 1:
                    self.updatePc(pc_no)
                
                elif check == 2:
                    self.removePc(pc_no)
                
                elif check == 3:
                  self.main()
                
                
            
            elif(pc_no.isdigit()):
                os = input("Installed operating system : ")
                status = input("Status : ")
                self.PC_List[pc_no] = {"OS": os, "STATUS": status}
            # temporary taken in a list.
                print("PC added successfully.")
                self.storePc(pc_no)
            
            else:
                print("\t------ Numerical input expected. -------\n")
                print("\n------\nPress\n")
                print("1. Go back to menu")
                print("2. Try Again")
                check=int(input())
                while check!=1 and check!=2:
                    check=input("Invalid input.! Please Try Again. ")
                if check==1:
                    self.main()
                else:
                    self.addPc()
            check=int(input("\n\nPress 0 to go back to Menu: "))
            while check!=0:
                    check=int(input("Invalid input.! Please Try Again. "))    
            if check==0:
                self.main()
         
        except FileNotFoundError:
            print("File Not Found")


    def storePc(self,pc_no):
        """For storing PC in Lab"""
        filename = 'PcList.json'
        with open(jsonFileName,'r') as f:
            FileContent=json.load(f)

        with open(jsonFileName,'w') as f:
           json.dump(PC_List,f)

        check=int(input("\n\nPress 1 to save info in a text file \n\tOR\nPress 0 to go back to menu : "))
        while check!=0 or check!=1:
            if check==0:
                self.main()
            else:
                filename=input("Write File Name: ")
                filename+='.txt'
                filename='E:\\Python\\MID Project\\'+filename

                try:
                    with open(filename, 'a') as file:
                            for pc_no,pc_function in FileContent.items():
                                file.write(f"PC number:{pc_no}\n", )
                                file.writelines(f"OS:{pc_function['OS']}\n", )
                                file.writelines(f"STATUS:{pc_function['STATUS']}\n", )
                                file.write("\n")

                            print("\nPC details stored in file\n")
                            check=int(input("To see the stored details press 1: "))
                            if check==1:
                                with open(filename) as file:
                                    for line in file:
                                        print(line)
                except FileNotFoundError: 
                    print("Sorry, file not found")

                check=int(input("\n\nPress 0 to go back to Menu: "))
                if check==0:
                    self.main()


    def removePc(self,pc_no):
        """used for remove particular pc"""
        with open(jsonFileName) as f:
            FileContent=json.load(f)

        if pc_no not in FileContent:
            print("PC is not found.")
        else:
            del FileContent[pc_no]
            with open(jsonFileName,'w') as f:
                json.dump(FileContent,f)
            print("PC removed successfully.")

        check=int(input("\n\nPress 0 to go back to Menu: "))
        if check==0:
            self.main()


    def updatePc(self,pc_no):
        """used for update particular pc"""

        with open(jsonFileName) as f:
            FileContent=json.load(f)

        if pc_no not in FileContent:
            print("PC is not found.")

        else:
            os = input("Installed operating system in the PC: ")
            status = input("Status: ")
            FileContent[pc_no]["OS"] = os
            FileContent[pc_no]["STATUS"] = status

            with open(jsonFileName,'w') as f:
                json.dump(FileContent,f)

            print("PC information updated successfully.")

        check=int(input("\n\nPress 0 to go back to Menu: "))
        if check==0:
            self.main()         



    def showAllPc(self):
        """used for show the details of all pc """

        print("\n\n******Records*****\n")
        with open(jsonFileName) as f:
            FileContent=json.load(f)

        if not FileContent:
            print("No PC found.")
        else:
            for pc_no,pc_function in FileContent.items():
                print(f"PC number:{pc_no}", )
                print(f"Operating system: {pc_function['OS']}" )
                print(f"Status: {pc_function['STATUS']}")
                print()

        check=int(input("\n\nPress 0 to go back to Menu: "))
        if check==0:
            self.main()


    def showPc(self):
        """used for search particular PC"""
        print("\nSearch for a PC info\n")
        pc_number = input("Enter PC number: ")
        with open(jsonFileName) as f:
            FileContent=json.load(f)
        if pc_number in FileContent:
            for pc_no,pc_function in FileContent.items():
                if pc_no==pc_number:
                    print(f"PC number:{pc_no}", )
                    print(f"Operating system: {pc_function['OS']}" )
                    print(f"Status: {pc_function['STATUS']}")
                    print()
        else:
            print("\nPC not found.")
        
        check=input("\n\nPress 0 to go back to Menu: ")
        if check=='0':
            self.main()
 



obj=LAB(PC_List)
obj.main()