import os
import time

while(True):
	#os.system("clear")
	print("1.Get Wifi Status")
	print("2.Turn Wifi On")
	print("3.Turn Wifi Off")
	print("4.List Available Access Points")
	print("5.Rescan List")
	print("6.Connect to a Open Access Point")
	print("7.Connect to a Password Protected Access Point")
	print("8.Exit")
	print("")
	choice =int( raw_input("Enter Your Choice:"))

	if(choice ==1):
		os.system("nmcli radio wifi")
		print("If it Disabled then Turn it On using 2nd option")
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
                
		print("\rRescanning....")
                
		os.system("nmcli device wifi rescan")
	elif(choice ==6):		
		Id = raw_input("Enter the SSID or BSSID")

		os.system("nmcli device wifi connect "+ Id)
	elif(choice ==7):		
		Id = raw_input("Enter the SSID or BSSID")
		print("")
		password = raw_input("Enter the password")

		os.system("nmcli device wifi connect "+ Id +" connect "+password)
	elif (choice == 8):
		exit(1)
	else:
		print("Wrong Input Please try again!!!")
