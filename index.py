import json
from jsonModule import *

jsonFileName='E:\\Python\\MID Project\\PcList.json'
PC_List={}        

class PC : 


    def __init__(self,PC_List) :
        self.PC_List=PC_List


           # -----------------------------------------------------------------
            # =================================================================
            # -----------------------------------------------------------------  

    def main(self):        
        print("\n\t\t****** Menu ******\n")
        print("\t|----------------------------------")
        print("\t| 1. Show all PC")
        print("\t| 2. Search a PC")
        print("\t| 3. Add PC")
        print("\t| 4. Update PC")
        print("\t| 5. Remove PC")
        print("\t| 6. Functionality of PC")
        print("\t| 7. Store PC")
        print("\t| 8. Quit")
        print("\t|----------------------------------")

        check=int(input("--> Select an option <--\n"))


        while check<1 or check>8:
            check=int(input("\n\nInvalid input! Try again.: "))

        if check==1:
            self.show_all_pc()
        elif check==2:
            self.show_pc()
        elif check==3:
            self.add_pc()
        elif check==4:
            check=input("Press the PC No. you want to update: ")
            self.update_pc(check)
        elif check==5:
            check=input("Press the PC No. you want to remove: ")
            self.remove_pc(check)
        elif check==6:
            self.show_functionality()
        elif check==7:
            self.store_pc()
        else: 
            return 

            # -----------------------------------------------------------------
            # =================================================================
            # -----------------------------------------------------------------

    def add_pc(self):
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
                    self.update_pc(pc_no)
                
                elif check == 2:
                    self.remove_pc(pc_no)
                
                elif check == 3:
                  self.main()
                
                
            
            elif(pc_no.isdigit()):
                os = input("Installed operating system : ")
                status = input("Status : ")
                self.PC_List[pc_no] = {"OS": os, "STATUS": status}
            # temporary taken in a list.
                print("PC added successfully.")
                self.store_pc(pc_no)
            
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
                    self.add_pc()
            check=int(input("\n\nPress 0 to go back to Menu: "))
            while check!=0:
                    check=int(input("Invalid input.! Please Try Again. "))    
            if check==0:
                self.main()
         
        except FileNotFoundError:
            print("File Not Found")

            # -----------------------------------------------------------------
            # =================================================================
            # -----------------------------------------------------------------

    def store_pc(self,pc_no):
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


            # -----------------------------------------------------------------
            # =================================================================
            # -----------------------------------------------------------------


    def remove_pc(self,pc_no):
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

            # -----------------------------------------------------------------
            # =================================================================
            # -----------------------------------------------------------------

    def update_pc(self,pc_no):
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


            # -----------------------------------------------------------------
            # =================================================================
            # -----------------------------------------------------------------


    def show_all_pc(self):
        """used for show the details of all pc """

        print("\n\nLab PC information\n")
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

            # -----------------------------------------------------------------
            # =================================================================
            # -----------------------------------------------------------------

    def show_pc(self):
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
 



obj=PC(PC_List)
obj.main()