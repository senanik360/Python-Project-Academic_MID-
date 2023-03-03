import json
class PC : 

    def __init__(self,PC_List) :
        self.PC_List=PC_List
            # -----------------------------------------------------------------
            # =================================================================
            # -----------------------------------------------------------------

    def add_pc(self):
        """This method is to add new PC in the lab"""
        pc_no = input("PC no: ")

        with open('PcList.json') as f:
            FileContent=json.load(f)
        if pc_no in FileContent:
            print("PC number already exists.\n------\nPress\n")
            print("1. Modify existing PC")
            print("2. Remove existing PC")
            print("3. Back")

            check = int(input("\nEnter your choice: "))

            while check<1 or check>3:
                check=input("Invalid input.! Please Try Again. ")

            if check == 1:
                self.update_pc(pc_no)
                pass
            elif check == 2:
                self.remove_pc(pc_no)
                pass
            elif check == 3:
                self.main()
            
        elif(pc_no.isdigit()):
            os = input("Installed operating system : ")
            status = input("Status : ")
            self.PC_List[pc_no] = {"OS": os, "STATUS": status}
            print("PC added successfully.")
            self.store_pc()
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

            # -----------------------------------------------------------------
            # =================================================================
            # -----------------------------------------------------------------

    def store_pc(self):
        """This method is for storing all the PCs added"""
        # filename=input("Write Your File Name : ")
        # filename = filename+'.txt'
        filename = 'PcList.json'
        with open('PcList.json') as f:
            FileContent=json.load(f)

        with open(filename,'w') as f:
           json.dump(PC_List,f)

        m=int(input("\n\nPress 0 to go back to Menu: "))
        if m==0:
            self.main()

            # -----------------------------------------------------------------
            # =================================================================
            # -----------------------------------------------------------------          
 


            # -----------------------------------------------------------------
            # =================================================================
            # -----------------------------------------------------------------
    def remove_pc(self,pc_no):
        """This method is for deleting a particular pc from lab"""
        with open('PcList.json') as f:
            FileContent=json.load(f)

        if pc_no not in FileContent:
            print("PC is not found.")
        else:
            del FileContent[pc_no]
            with open('PcList.json','w') as f:
                json.dump(FileContent,f)
            print("PC removed successfully.")

        check=int(input("\n\nPress 0 to go back to Menu: "))
        if check==0:
            self.main()

            # -----------------------------------------------------------------
            # =================================================================
            # -----------------------------------------------------------------

    def update_pc(self,pc_no):
        """This is for updating PC info such as os,status"""

        with open('PcList.json') as f:
            FileContent=json.load(f)

        if pc_no not in FileContent:
            print("PC is not found.")

        else:
            os = input("Installed operating system in the PC: ")
            status = input("Status: ")
            FileContent[pc_no]["OS"] = os
            FileContent[pc_no]["STATUS"] = status

            with open('PcList.json','w') as f:
                json.dump(FileContent,f)

            print("PC information updated successfully.")

        check=int(input("\n\nPress 0 to go back to Menu: "))
        if check==0:
            self.main()            
            # -----------------------------------------------------------------
            # =================================================================
            # -----------------------------------------------------------------


    def show_all_pc(self):
        """This method will show all pc info including os, status"""

        print("\n\nLab PC information\n")
        with open('PcList.json') as f:
            FileContent=json.load(f)

        if not FileContent:
            print("No PCs found.")
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
        """This is for displaying info of a particular PC"""
        print("\nSearch for a PC info\n")
        pc_number = input("Enter PC number: ")
        with open('PcList.json') as f:
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
            # -----------------------------------------------------------------
            # =================================================================
            # -----------------------------------------------------------------  

    def main(self):
        print(PC_List)
        """This method is to display main menu"""

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

PC_List={}        
labobj=PC(PC_List)
labobj.main()