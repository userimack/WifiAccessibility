import os
import time

def wifi():

    while(True):
        #os.system("clear")
        print("1.Get Wifi Status")
        print("2.Turn Wifi ON")
        print("3.Turn Wifi OFF")
        print("4.List Available Access Points")
        print("5.Rescan List")
        print("6.Connect to an Open WiFi")
        print("7.Connect to a PasswordProtected WiFi ")
        print("8.Exit")
        print("")

        
        #try:
        choice =int( raw_input("Enter Your Choice:"))

        if(choice ==1):
            os.system("nmcli radio wifi")
            print("If it Disabled then Turn it On using 3rd option")
            print("")

        elif(choice ==2):
            os.system("nmcli radio wifi on")
            print("Turned On")
            print("")

        elif(choice ==3):
            os.system("nmcli radio wifi off")
            print("Turned Off")
            print("")

        elif(choice == 4):
            os.system("nmcli device wifi list")

        elif(choice == 5):                
            print("Rescanning....")
            os.system("nmcli device wifi list")

        elif(choice == 6):  

            Id = raw_input("Enter the SSID or BSSID: ")

            os.system("nmcli device wifi connect "+ Id)
        elif(choice ==7):       
            Id = raw_input("Enter the SSID or BSSID: ")
            print("")
            password = raw_input("Enter the password: ")

            os.system("nmcli device wifi connect "+ Id +"connect "+password)

        elif (choice == 8):
            exit(1)

        else:
            print("Wrong Input Please try again!!!")
'''
        except:
            print ("Input Error")
            print
'''

if __name__ =="__main__":

    wifi()
