import os
import time

## Authentications ##
Auth1 = "jvance1@@foundation.scp | password9910"
Auth2 = "hmasterson4@@foundation.scp | 1234Ilovethemarinecorps"
Auth3 = "jchoi9@@foundation.scp | beethovens9th123"
Auth4 = "vfellini2@@foundation.scp | Sierra charLy pOPPA"
Auth5 = "kpcrow@@foundation.scp | sometimesifeeellikeamotherlesschild"
Auth6 = "O5-13 | sIERRa tANGo CASpER 3CH0."

## Level Clearances ##
Auth1Clearance = "0"
Auth2Clearance = "1"
Auth3Clearance = "2"
Auth4Clearance = "3"
Auth5Clearance = "4"
Auth6Clearance = "05"

## Functions
def clear():
  os.system('clear')

def SCP_File(SCP, Clearance):
  if SCP == "SCP-2317":
    if Clearance == "0":
      clear()
      print("USER NAME: Jonathan Vance")
      print("TITLE: Research Assistant, Site 179")
      print("DISPLAYING SCP-2317, CLEARANCE LEVEL 0")
      print(" ")
      print("SCP-2317")
      print("----------------")
      print("Item #: SCP-2317")
      print("Object Class: [DATA EXPUNGED]")
      print(" ")
      print("Special Containment Procedures: SCP-2317 is to be secured at Containment Area-179 in a reinforced 3m x 3m x 3m containment chamber. Armed guards are to be in place at all times in order to prevent unauthorized access to the facility.")
      print(" ")
      print("Description: SCP-2317 is a wooden door and frame originally constructed as a basement door for a 19th-century Massachusetts brownstone. Upon opening the door, any person stepping through the door frame will be transported to an alternate reality.")
      print(" ")
      print("FURTHER INFORMATION ON SCP-2317 IS CLASSIFIED LEVEL 1 (RESTRICTED) OR HIGHER. INSUFFICIENT SECURITY CLEARANCE.")
      print(" ")
      print("LEVEL CLEARANCE ONLY GRANTS 1 MINUTE OF ACCESS PER SESSION.")
      time.sleep(60)
      print(" ")
      print(" ")
      print("Logging out. Time limit reached.")
      time.sleep(2)
      clear()
      print("Logged Out.")
      print(" ")
      print("Thank you for using SCiPNET Terminal. Message clearing in 3 seconds.")
      time.sleep(3)
      clear()

def Jonathan_Vance():
  print("AUTHENTICATION ACCEPTED. PLEASE ENTER COMMAND")
  Command_1 = input("Terminal: ")
  if Command_1 == "access SCP-2317 0":
    SCP_File("SCP-2317", "0")

## Terminal ##
print("WELCOME TO SCiPNET DIRECT ACCESS TERMINAL. PLEASE ENTER COMMAND")
print("PLEASE ENTER COMMAND")
print(" ")
Terminal_Main = input("Terminal: ")
print(" ")

if Terminal_Main == "login":
  print("PLEASE ENTER USER AUTHENTICATION")
  login = input("Terminal: ")
  if login == Auth1:
    Jonathan_Vance()
