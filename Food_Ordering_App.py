class Restaurent:
    def __init__(self):
        self.food_all = {}
        self.food_id = 0
        self.ordered_item_list = []
        self.personal_details = {}

#!!!!!!!!!!!!!!!!!!!!!!!!!! ADMIN FUNCTIONALITIES !!!!!!!!!!!!!!!!!!!!!!!!!!
    def Add_Food_Items(self, name, quantity, price, discount, stock):
        self.food_name = name
        self.food_quantity = quantity
        self.food_price = price
        self.discount = discount
        self.stock = stock

        self.item_details = {"Name": self.food_name, "Quantity": self.food_quantity, "Price": self.food_price, "Discount": self.discount, "Stock": self.stock}
        self.food_id = len(self.food_all) + 1
        self.food_all[self.food_id] = self.item_details


    def Add_Food_Item(self):        
        try:
            print("\n"+ "*"*10 + " Add Food Item " + "*"*10 + "\n")
            self.food_name = input("Enter the food name: ")
            self.food_quantity = input("Enter the quantity (in ml or pieces or gm): ")
            self.food_price = float(input("Enter the price (in ₹ per kg): "))
            self.discount = float(input("Enter the discount (in %): "))
            self.stock = float(input("Enter the Stock present (in kgs): "))

            self.item_details = {"Name": self.food_name, "Quantity": self.food_quantity, "Price": self.food_price, "Discount": self.discount, "Stock": self.stock}
            self.food_id = len(self.food_all) + 1
            self.food_all[self.food_id] = self.item_details

            print("\n" + "*"*10 + " Item :: %s has been added successfully" %(self.food_all[self.food_id]) + "*"*10)
        
        except Exception as e:
            print("\n" + "*"*10 + " FOOD ITEM WAS NOT ADDED PLEASE TRY AGAIN ...!"  + "*"*10)

    def View_Food_Items(self):
        try:
            print("\nList of all food items present are: \n")
            if len(self.food_all) > 0:
                for i in self.food_all.keys():
                    print("\n---> \t Food Item \t:  ", i, "\n")
                    for j in self.food_all[i]:
                        print(j, " : \t\t", self.food_all[i][j])
            else:
                print("\n" + "*"*10 + " No Food Items Added ....! " + "*"*10 + "\n")
        except Exception as e:
            print("\n" + "*"*10 + " ERROR PLEASE TRY AGAIN ...!"  + "*"*10)

    
    def Edit_Food_Item(self):
        try:
            # print("PRINTING ALL THE FOOD ITEMS PRESENT AND GIVING THE CHOICE ....!")
            print("\n" + "*"*10 + " IDs ....! " + "*"*10 + "\n")
            for i in self.food_all.keys():
                print(i, end="\t")

            Food_ID = int(input("\nEnter the ID (to be edited): "))

            if Food_ID in self.food_all.keys():

                # Current Food ID item to be printed for Details
                print()
                for j in self.food_all[i]:
                    print(j, ":\t\t", self.food_all[Food_ID][j])

                print("\n1. Food Name, 2. Quantity, 3. Price, 4. Discount, 5. Stock.\n")
                k = int(input("Enter your choice: "))
                if k == 1:
                    self.food_all[Food_ID]["Name"] = input("Food Name: ")
                    print("\n" + "*"*10 + " Food Name Updated Successfully ....! " + "*"*10 + "\n")

                elif k == 2:
                    self.food_all[Food_ID]["Quantity"] = input("Quantity: ")
                    print("\n" + "*"*10 + " Food Quantity Updated Successfully ....! " + "*"*10 + "\n")

                elif k == 3:
                    self.food_all[Food_ID]["Price"] = input("Price: ")
                    print("\n" + "*"*10 + " Food Price Updated Successfully ....! " + "*"*10 + "\n")

                elif k == 4:
                    self.food_all[Food_ID]["Discount"] = input("Discount: ")
                    print("\n" + "*"*10 + " Food Discount Updated Successfully ....! " + "*"*10 + "\n")

                elif k == 5:
                    self.food_all[Food_ID]["Stock"] = input("Stock: ")
                    print("\n" + "*"*10 + " Food Stock Updated Successfully ....! " + "*"*10 + "\n")

                else:
                    print("\n" + "*"*10 + " Invalid Choice ....! " + "*"*10 + "\n")

            else:
                print("\n" + "*"*10 + " Invalid ID ....! " + "*"*10 + "\n")
        except:
            print("\n" + "*"*10 + "FOOD ITEM WAS NOT UPDATED PLEASE TRY AGAIN ...!"  + "*"*10)

        
    def Remove_Food_Item(self):
        try:
            if len(self.food_all) > 0:
                print("\n" + "*"*10 + " IDs ....! " + "*"*10 + "\n")
                for i in self.food_all.keys():
                    print(i, end = "\t")            
                Food_ID = int(input("Enter the ID: "))

                if Food_ID in self.food_all.keys():
                    del self.food_all[i]
                    print("\n" + "*"*10 + " Food Item Deleted Successfully ....! " + "*"*10 + "\n")

                else:
                    print("\n" + "*"*10 + " ID Not Present ....! " + "*"*10 + "\n")    

            else:
                print("\n" + "*"*10 + " No Food Items Present ....! " + "*"*10 + "\n")
        except:
            print("\n" + "*"*10 + "FOOD ITEM WAS NOT REMOVED PLEASE TRY AGAIN ...!"  + "*"*10)


# !!!!!!!!!!!!!!!!!!!!!!!!!! USER FUNCTIONALITIES !!!!!!!!!!!!!!!!!!!!!!!!!!
    def Adding_User(self, name, phone, email, address, password):
        # print("\n" + "*"*10 + " NEW USER ....! " + "*"*10 + "\n")

        self.user_full_name = name
        self.phone_number = phone
        self.user_email = email
        self.user_address = address
        self.user_password = password

        self.personal_details = {"User Name":self.user_full_name, "Phone":self.phone_number, "Email": self.user_email, "Address": self.user_address, "Password": self.user_password}
        
    def User_Registration(self):
        try:
            print("\n" + "*"*10 + " NEW USER ....! " + "*"*10 + "\n")

            self.user_full_name = input("Enter your full name: ")
            self.phone_number = input("Enter you phone number: ")
            self.user_email = input("Enter the email id: ")
            self.user_address = input('Enter your address: ')
            self.user_password = input("Enter the password: ")

            self.temp_user = {"User Name":self.user_full_name, "Phone":self.phone_number, "Email": self.user_email, "Address": self.user_address, "Password": self.user_password}
            print("\n" + "*"*10 + " User Registered Successfully ....! " + "*"*10 + "\n")    
        except:
            print("\n*" + "-"*10 + "REGISTRATION UNSUCCESSFUL PLEASE TRY AGAIN ...!"  + "-"*10 + "*")

    def User_Login(self):
        try:
            print("USER LOGIN")
            email = input("--> Email: ")
            password = input("--> Password: ")
            if self.user_email == email and self.user_password == password:
                print("\n1. Place New Order,\n2. Order History, \n3. Update Profile. \n4. Exit")
                User_Choice = int(input("Enter the choice: "))
                if User_Choice == 1:
                    # print("Place New Order")
                    print("\n" + "*"*10 + " Place New Order ....! " + "*"*10 + "\n")    
                    self.Place_New_Order()

                elif User_Choice == 2:
                    print("\n" + "*"*10 + " Order History ....! " + "*"*10 + "\n")    
                    print("Order History")
                    self.Order_History()

                elif User_Choice == 3:
                    # print("Update Profile")
                    self.Update_Profile()

                elif User_Choice == 4:
                    print("Exit")
                    return
                else:
                    print("Invalid Choice")

            elif self.user_email == email and self.user_password != password:
                print("\n" + "*"*10 + " Invalid Password ....! " + "*"*10 + "\n")    

            elif self.user_email != email and self.user_password == password:
                print("\n" + "*"*10 + " Invalid Email ....! " + "*"*10 + "\n")    

            elif self.user_email != email and self.user_password != password:
                print("\n" + "*"*10 + " Invalid Email and Password ....! " + "*"*10 + "\n")    

            else:
                print("\n" + "*"*10 + " Invalid Input ....! " + "*"*10 + "\n")    
        except:
            print("\n*" + "-"*10 + "LOGIN UNSUCCESSFUL PLEASE TRY AGAIN ...!"  + "-"*10 + "*")
            

    def Place_New_Order(self):
        try: 
            #CHECKING THE STOCK
            if len(self.food_all) != 0:
                list_of_fooditems = []
                
                # COPYING REQUIRED THINGS FROM THE DICTIONARY
                for i in self.food_all.keys():
                    list_of_fooditems.append([self.food_all[i]["Name"], self.food_all[i]["Quantity"], self.food_all[i]["Price"]])

                #PRINTING LIST OF FOOD ITEMS
                countdown = 0
                for i in list_of_fooditems:
                    countdown += 1
                    print(countdown, ".\t", i)
                
                while True:
                    print("\n1. Place Order, 2. Exit.")
                    z = int(input("Enter your choice: "))
                    if z == 1:
                        tempp = input("Enter the food items separated by spaces: ").split(" ")
                        sample_list = list(map(lambda x:int(x), tempp))

                        for i in sample_list:
                            if i <= len(self.food_all):
                                self.ordered_item_list.append(list_of_fooditems[i-1])
                            else:
                                print("\n" + "*"*10 + " Number out of the range ....! " + "*"*10 + "\n")    
                                return
                        print("\nOrdered Items: ")
                        for i in self.ordered_item_list:
                            print(i)
                        print()
                    elif z == 2:
                        print("\n" + "*"*10 + " EXITING ....! " + "*"*10 + "\n")    
                        return
                    else:
                        print("\n" + "*"*10 + " Invalid Choice ....! " + "*"*10 + "\n")    
                        
                # print()
            else:
                print("\nFood Items out of stock\n")
        except Exception as e:
            print(e)
            print("\n*" + "-"*10 + " YOUR ORDER WAS NOT PLACED PLEASE TRY AGAIN ...!"  + "-"*10 + "*")
    
    def Order_History(self):
        # print("Ordered History.")
        print("\n\n*"+ "-"*10 + " Order History " + "-"*10 + "*\n")
        for i in self.ordered_item_list:
            print(i)
            
    
    def Update_Profile(self):
        print("\n\n*"+ "-"*10 + " Updating User Profile " + "-"*10 + "*\n")
        try:
            while True:
                print("\n1. Name, 2. Phone, 3. Email, 4. Address, 5. Password, 6. Exit.")
                c = int(input("Enter your choice for profile update: "))
                if c == 1:
                    self.personal_details["User Name"] = input("Enter the user name: ")
                    print("*" + "-"*10 + " User Name Updated Successfully ...!" + "-"*10 + "*")
                elif c == 2:
                    self.personal_details["Phone"] = input("Enter the Phone Number: ")
                    print("*" + "-"*10 + " Phone Number Updated Successfully ...!" + "-"*10 + "*")
                elif c == 3:
                    self.personal_details["Email"] = input("Enter the Email Id: ")
                    self.user_email = self.personal_details["Email"]
                    print("*" + "-"*10 + " Email Id Updated Successfully ...!" + "-"*10 + "*")
                elif c == 4:
                    self.personal_details["Address"] = input("Enter the Address: ")
                    print("*" + "-"*10 + " Address Updated Successfully ...!" + "-"*10 + "*")
                elif c == 5:
                    self.personal_details["Password"] = input("Enter the Password: ")
                    self.user_email = self.personal_details["Password"]
                    print("*" + "-"*10 + " Password Updated Successfully ...!" + "-"*10 + "*")
                elif c == 6:
                    print("*" + "-"*10 + " EXITING ...!" + "-"*10 + "*")                    
                    break
                else:
                    print("*" + "-"*10 + " Invalid Choice ...!" + "-"*10 + "*")               
                
                if c in [1, 2, 3, 4, 5]:
                    print("\n")
                    for i in self.personal_details:
                        print("->",i, ":", self.personal_details[i])
                else:
                    print("*" + "-"*10 + " Invalid Choice ...!" + "-"*10 + "*")

        except Exception as e:
            print("*" + "-"*10 + " INVALID INPUT ...!" + "-"*10 + "*")


def main():
    try:
        res_title = "PRAWIN SAI's RESTAURENT"
        # Creating an Restaurent Object
        Res = Restaurent()
        
        print("*"*15 + " %s " %(res_title) + "*"*15)
        print("\n\n")


        print("1. ADMIN, \n2. USER, \n3. EXIT.")
        print("Enter the number: ")
        login_type = int(input())

        # Initially Adding the Items
        Res.Add_Food_Items("Tandoori", "4 pieces", 240.00, 2.0, 20.00)
        Res.Add_Food_Items("Vegan Burger", "1 piece", 320.00, 0.0, 5.00)
        Res.Add_Food_Items("Truffle Cake", "500 gm", 900.00, 5.0, 30.00)

        # Adding Users
        Res.Adding_User("Kannadasan Prawin Sai", 8688666694, "sai@gmail.com", "13/432, Thiruvalluvar Street, Perungudi, Chennai, 600096", "Kps@123*")
        # Res.Adding_User("R Kalidas", 9786544432, "Kalidas@gmail.com", "42-213/2, Challandipalayam Street, Karur, 639001", "Kali@123*")
        # Res.Adding_User("K Sri", 6789765542, "Sri@gmail.com", "543/2, Edepalli, Machilipatnam, 521001", "Sri@123*")


        while(True):

            if login_type == 1:
                #!!!!!!!!!!!!!!!!!!!!!!!!!! ADMIN !!!!!!!!!!!!!!!!!!!!!!!!!!

                print("\n" + "*"*20 + " WELCOME, ADMIN " + "*"*20 + "\n")
                print("1. Add New Food Item, \n2. Edit Food Item, \n3. View The List Of All Food Items, \n4. Remove A Food Item From the Menu, \n5. Exit")
                Admin_Choice = int(input("Enter the choice: "))

                if Admin_Choice == 1:
                    print("\n" + "*"*10 + " Add New Food Item " + "*"*10)
                    Res.Add_Food_Item()

                elif Admin_Choice == 2:
                    print("\n" + "*"*10 + " Edit Food Item " + "*"*10)
                    Res.Edit_Food_Item()

                elif Admin_Choice == 3:
                    print("\n" + "*"*10 + " View The List Of All Food Items " + "*"*10)
                    Res.View_Food_Items()

                elif Admin_Choice == 4:
                    print("\n" + "*"*10 + " Remove A Food Item From the Menu " + "*"*10)
                    Res.Remove_Food_Item()

                elif Admin_Choice == 5:
                    print("\n" + "*"*10 + " Exiting " + "*"*10)
                    break
                else:
                    print("\n" + "*"*10 + " Invalid Choice " + "*"*10)


            elif login_type == 2:
                #!!!!!!!!!!!!!!!!!!!!!!!!!! USER !!!!!!!!!!!!!!!!!!!!!!!!!!
                print("\n" + "*"*10 + " WELCOME, USER " + "*"*10)

                print("1. Register User, \n2. Login (Existing User), \n3. Exit.")
                User__Choice = int(input("Enter your Choice: "))

                if User__Choice == 1:
                    # print("\n" + "*"*10 + " NEW USER ....! " + "*"*10 + "\n")
                    Res.User_Registration()

                elif User__Choice == 2:
                    # print("\n" + "*"*10 + " EXISTING USER ....! " + "*"*10 + "\n")
                    Res.User_Login()

                elif User__Choice == 3:
                    print("\n" + "*"*10 + " Exiting ....!" + "*"*10)
                    break   

            elif login_type == 3:
                print("\n" + "*"*10 + " Exiting ....! " + "*"*10)            
                break


            else:
                print("*"*10 + "Invalid Member Type...!" + "*"*10)
    except:
        print("\n*" + "-"*10 + " REGISTRATION UNSUCCESSFUL PLEASE TRY AGAIN ...!"  + "-"*10 + "*")

if __name__ == '__main__':
    main()