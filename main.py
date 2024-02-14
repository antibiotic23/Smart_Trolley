import gspread
from oauth2client.service_account import ServiceAccountCredentials
from time import sleep





barcodes = [0,8902519009845,89007655,8901719101038,1122212]
productName = ["0","Classmate Notebook","Doublemint","Parle G","pencil"]
price = [0,95,10,5,8]

scope=["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds=ServiceAccountCredentials.from_json_keyfile_name("credentials.json",scope)
client=gspread.authorize(creds)

spreadsheet = client.open("Smart_Trolley Product Database")
worksheet= spreadsheet.get_worksheet(1)



count=0
item_cost=0
totalCost=0
SNo=0
scode=""
qty=1
scodePrev=0
item_name=""
entryF=[]


while (scode != "8906128542687"):
     try:
          scode = input("Scan the barcode")
          if scode == "8906128542687":  # Bill Printing Barcode pasted on the Thermal Printer
               print("Done shopping ")
              # lcd.clear()
               print(*entryF)
               print("Number of products = ")
               print(len(entryF))
               text_F = " "
               for i in range(0, len(entryF)):
                    text_F = text_F + entryF[i]
                    i = i + 1
               print("Total cost= ", totalCost)
#               lcd.cursor_pos = (0, 0)
#              lcd.write_string("Thanks for Shopping")
#               lcd.cursor_pos = (1, 7)
#               lcd.write_string("With Us")
#               lcd.cursor_pos = (3, 0)
#               lcd.write_string("Printing Invoice...")
#              print_receipt()
          else:
               cell = worksheet.find(scode)
               print("found on R%sC%s" % (cell.row, cell.col))
               item_cost = worksheet.cell(cell.row, cell.col + 2).value
               item_name = worksheet.cell(cell.row, cell.col + 1).value
#               lcd.clear()
               SNo = SNo + 1
               entry = [SNo, item_name, qty, item_cost]
               entryS = str(entry) + '\n'
               print("New Item ", *entry)
#               lcd.cursor_pos = (0, 2)
#               lcd.write_string(str(SNo))
#               lcd.cursor_pos = (0, 5)
#               lcd.write_string("Item(s) added")
#               lcd.cursor_pos = (1, 1)
 #              lcd.write_string(item_name)
  #             lcd.cursor_pos = (2, 5)
   #            lcd.write_string("of Rs.")
    #           lcd.cursor_pos = (2, 11)
     #          lcd.write_string(item_cost)
               item_cost = int(item_cost)
               totalCost = item_cost + totalCost
      #         lcd.cursor_pos = (3, 4)
       #        lcd.write_string("Cart Total")
        #       lcd.cursor_pos = (3, 15)
         #      lcd.write_string(str(totalCost))
               entryF.append(entryS)  # adding entry in Final Buffer
               print("Total cost=",totalCost)
               sleep(2)

     except:
        print("Unknown Barcode or Item Not Registered")
#        lcd.clear()
#        lcd.cursor_pos = (0, 0)
#        lcd.write_string("Item Not Found...")
#        lcd.cursor_pos = (2, 0)
#        lcd.write_string("Scan Again...")
        sleep(2)

