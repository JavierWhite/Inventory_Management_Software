"""
#	This is a GUI displying the SQL database information into a comprehensive display.
#	The system shows each dealer ship, their stock and a check box to indacate "bought or avalible".
	

#	Using python, Xammp*, and mysql workbench*

#	@uther Javer White


#											Referances: 
#					@ DJ Oamen (YouTube), freeCodingCamp.org, Python tkinter library @ Python.org
#						"Starting out with >>> Python" fourth edition by Tony Gaddis

"""

from tkinter import *
from tkinter import Tk, StringVar, ttk
import random
import datetime
import time

# import tkinter.messagebox
# from PIL import ImageTK, Image

	
root =Tk()
root.geometry("1350x750+0+0") # window dimensions 
root.title("Inventory System") # name

		
# ------------------------------------------- Frames ------------------------------------------ #

TopFrame = Frame(root, width= 1350, height= 100, bd =14, bg='black', relief = 'raise')
TopFrame.pack(side=TOP)

BottomFrame = Frame(root, width= 1350, height= 200, bd =14, bg='black', relief = 'raise')
BottomFrame.pack(side=BOTTOM)

LeftMidFrame = Frame(BottomFrame, width= 750, height= 1000, bd =14, bg='darkgray', relief = 'raise')
LeftMidFrame.pack(side=LEFT)

RightMidFrame = Frame(BottomFrame, width= 600, height= 1000, bd =14, bg='darkgrey', relief = 'raise')
RightMidFrame.pack(side=RIGHT)

lblTitle = Label(TopFrame, font = ('arial', 40, 'bold'), text = "Inventory System", bd=10, width = 41, bg='orange', justify = 'center')
lblTitle.grid(row= 0, column= 0)
# --------------------------------------- End of Frames ---------------------------------------- #
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
Payment = StringVar()
Financing = StringVar()

Date = StringVar()


var1.set("")
var2.set("")
var3.set("")
var4.set("")
var5.set("")

Payment.set("")
Financing.set("")

Date.set(time.strftime("%m/%d/%Y"))
# --------------------------------------- Vehicle Details -------------------------------------- #	
lblVehicleID = Label(LeftMidFrame, font = ('arial', 14, 'bold'), text= "VIN", bd=10, bg='darkgray', width= 20, anchor='w')
lblVehicleID.grid(row= 0, column=0)

cmbVehicleID = ttk.Combobox(LeftMidFrame, font=('arial', 14, 'bold'), textvariable = var1, state= 'readonly', width= 16)
cmbVehicleID['value'] = ('ta2432646', 'ta2432646', 'na11001817', 'HA3-2031196','Na1-1005161','PID004')
cmbVehicleID.current(0)
cmbVehicleID.grid(row=0, column=1)

lblVehicleName = Label(LeftMidFrame, font = ('arial', 14, 'bold'), text = "Vehicle Name", bg='darkgray',  bd=10, width= 20, anchor='w')
lblVehicleName.grid(row= 1, column=0)

lblVehicleNameVar = Label(LeftMidFrame, font = ('arial', 14, 'bold'), textvariable = var2,  bd=10, width= 18, relief = 'sunken')
lblVehicleNameVar.grid(row= 1, column=1)

lblDescription1 = Label(LeftMidFrame, font = ('arial', 14, 'bold'), text= "Description", bg='darkgray',  bd=10, width= 20, anchor='w')
lblDescription1.grid(row= 2, column=0)
lblDescription2 = Label(LeftMidFrame, font = ('arial', 14, 'bold'), textvariable = var3, bd=10, width= 18, relief = 'sunken')
lblDescription2.grid(row= 2, column=1)

lblStockLevel1 = Label(LeftMidFrame, font = ('arial', 14, 'bold'), text= "Stock # ", bg='darkgray', bd=10, width= 20, anchor='w')
lblStockLevel1.grid(row= 3, column=0)
lblStockLevel2 = Label(LeftMidFrame, font = ('arial', 14, 'bold'), textvariable = var4, bd=10, width= 18, relief = 'sunken')
lblStockLevel2.grid(row= 3, column=1)

#
lblLot = Label(LeftMidFrame, font = ('arial', 14, 'bold'), text = "Lot #", bg='darkgray', bd=10, width= 20, anchor='w')
lblLot.grid(row= 4, column=0)

#
lblVehicleNameVar = Label(LeftMidFrame, font = ('arial', 14, 'bold'), textvariable = var2, bd=10, width= 18, relief = 'sunken')
lblVehicleNameVar.grid(row= 4, column=1)

#
lblMakel1 = Label(LeftMidFrame, font = ('arial', 14, 'bold'), text= "Make ", bg='darkgray', bd=10, width= 20, anchor='w')
lblMakel1.grid(row= 5, column=0)
lblMakel2 = Label(LeftMidFrame, font = ('arial', 14, 'bold'), textvariable = var3, bd=10, width= 18, relief = 'sunken')
lblMakel2.grid(row= 5, column=1)

#
lblModle1 = Label(LeftMidFrame, font = ('arial', 14, 'bold'), text= "Modle ", bg='darkgray', bd=10, width= 20, anchor='w')
lblModle1.grid(row= 6, column=0)
lblModle2 = Label(LeftMidFrame, font = ('arial', 14, 'bold'), textvariable = var4, bd=10, width= 18, relief = 'sunken')
lblModle2.grid(row= 6, column=1)

#
#lblDescription1.grid(row= 7, column=0)
#lblDescription2 = Label(LeftMidFrame, font = ('arial', 14, 'bold'), textvariable = var3, bd=10, width= 18, relief = 'sunken')
#lblDescription2.grid(row= 7, column=1)

#
lblStockLevel1 = Label(LeftMidFrame, font = ('arial', 14, 'bold'), text= "Stock* ", bg='darkgray', bd=10, width= 20, anchor='w')
lblStockLevel1.grid(row= 8, column=0)
lblStockLevel2 = Label(LeftMidFrame, font = ('arial', 14, 'bold'), textvariable = var4, bd=10, width= 18, relief = 'sunken')
lblStockLevel2.grid(row= 8, column=1)

#        
lblDate1 = Label(LeftMidFrame, font = ('arial', 14, 'bold'), text= "Date ", bg='darkgray', bd=10, width= 20, anchor='w')
lblDate1.grid(row= 9, column=0)
lblDate2 = Label(LeftMidFrame, font = ('arial', 14, 'bold'), textvariable = Date, bd=10, width= 18, relief = 'sunken')
lblDate2.grid(row= 9, column=1)

# ----------------------------------------------  Right  Mid Frame --------------------------------------------------------- # 

#       
lblMSRP1 = Label(RightMidFrame, font = ('arial', 14, 'bold'), text= "MSRP ", bg='darkgray', bd=10, width= 14, anchor='w')
lblMSRP1.grid(row= 0, column=0)
lblMSRP2 = Label(RightMidFrame, font = ('arial', 14, 'bold'), textvariable = var4, bd=10, width= 10, relief = 'sunken')
lblMSRP2.grid(row= 0, column=1)

#        
lblDiscount1 = Label(RightMidFrame, font = ('arial', 14, 'bold'), text= "Discount ", bg='darkgray', bd=10, width= 14, anchor='w')
lblDiscount1.grid(row= 0, column=2)
lblDiscount2 = Label(RightMidFrame, font = ('arial', 14, 'bold'), textvariable = var4, bd=10, width= 10, relief = 'sunken')
lblDiscount2.grid(row= 0, column=3)

#        
lblTrade1 = Label(RightMidFrame, font = ('arial', 14, 'bold'), text= "Trade In ", bg='darkgray', bd=10, width= 14, anchor='w')
lblTrade1.grid(row= 1, column=0)
lblTrade2 = Label(RightMidFrame, font = ('arial', 14, 'bold'), textvariable = var4, bd=10, width= 10, relief = 'sunken')
lblTrade2.grid(row= 1, column=1)

#        
lblTrade1 = Label(RightMidFrame, font = ('arial', 14, 'bold'), text= "Financing ", bg='darkgray', bd=10, width= 14, anchor='w')
lblTrade1.grid(row= 1, column=2)
lblTrade2 = Label(RightMidFrame, font = ('arial', 14, 'bold'), textvariable = var4, bd=10, width= 10, relief = 'sunken')
lblTrade2.grid(row= 1, column=3)


#        
lblPrice1 = Label(RightMidFrame, font = ('arial', 14, 'bold'), text= "Price ", bg='darkgray', bd=10, width= 14, anchor='w')
lblPrice1.grid(row= 2, column=0)
lblPrice2 = Label(RightMidFrame, font = ('arial', 14, 'bold'), textvariable = var4, bd=10, width= 10, relief = 'sunken')
lblPrice2.grid(row= 2, column=1)

#        
lblDiscount1 = Label(RightMidFrame, font = ('arial', 14, 'bold'), text= "Fees ", bg='darkgray', bd=10, width= 14, anchor='w')
lblDiscount1.grid(row= 1, column=2)
lblDiscount2 = Label(RightMidFrame, font = ('arial', 14, 'bold'), textvariable = var4, bd=10, width= 10, relief = 'sunken')
lblDiscount2.grid(row= 1, column=3)

#        
lblMSRPs1 = Label(RightMidFrame, font = ('arial', 14, 'bold'), text= "Registration ", bg='darkgray', bd=10, width= 14, anchor='w')
lblMSRPs1.grid(row= 2, column=0)
lblMSRPs2 = Label(RightMidFrame, font = ('arial', 14, 'bold'), textvariable = var4, bd=10, width= 10, relief = 'sunken')
lblMSRPs2.grid(row= 2, column=1)

#        
lblDiscounts1 = Label(RightMidFrame, font = ('arial', 14, 'bold'), text= "Total ", bg='darkgray', bd=10, width= 14, anchor='w')
lblDiscounts1.grid(row= 2, column=2)
lblDiscounts2 = Label(RightMidFrame, font = ('arial', 14, 'bold'), textvariable = var4, bd=10, width= 10, relief = 'sunken')
lblDiscounts2.grid(row= 2, column=3)

#        
lblPayment1 = Label(RightMidFrame, font = ('arial', 14, 'bold'), text= "Payment type ", bg='darkgray', bd=10, width= 14, anchor='w')
lblPayment1.grid(row= 3, column=0)

cmbPayment = ttk.Combobox(RightMidFrame, font=('arial', 14, 'bold'), textvariable = var1, state= 'readonly', width= 16)
cmbPayment['value'] = ('','Cash', 'Debit Card', 'Credit Card', 'Check',)
cmbPayment.current(0)
cmbPayment.grid(row=3, column=1)

#        
lblDisscount1 = Label(RightMidFrame, font = ('arial', 14, 'bold'), text= " Original Payment ", bg='darkgray', bd=10, width= 14, anchor='w')
lblDisscount1.grid(row= 3, column=2)
lblDisscount2 = Label(RightMidFrame, font = ('arial', 14, 'bold'), textvariable = var4, bd=10, width= 10, relief = 'sunken')
lblDisscount2.grid(row= 3, column=3)

# -------------------------------------------------      Bottom Right    --------------------------------------------------------- #      
lblMSRP1 = Label(RightMidFrame, font = ('arial', 14, 'bold'), text= "Name ", bg='darkgray', bd=10, width= 14, anchor='w')
lblMSRP1.grid(row= 4, column=0)
lblMSRP2 = Label(RightMidFrame, font = ('arial', 14, 'bold'), textvariable = var4, bd=10, width= 10, relief = 'sunken')
lblMSRP2.grid(row= 4, column=1)

#        
lblDiscount1 = Label(RightMidFrame, font = ('arial', 14, 'bold'), text= "Number ", bg='darkgray', bd=10, width= 14, anchor='w')
lblDiscount1.grid(row= 4, column=2)
lblDiscount2 = Label(RightMidFrame, font = ('arial', 14, 'bold'), textvariable = var4, bd=10, width= 10, relief = 'sunken')
lblDiscount2.grid(row= 4, column=3)

#        
lblTrade1 = Label(RightMidFrame, font = ('arial', 14, 'bold'), text= "Email", bg='darkgray', bd=10, width= 14, anchor='w')
lblTrade1.grid(row= 5, column=0)
lblTrade2 = Label(RightMidFrame, font = ('arial', 14, 'bold'), textvariable = var4, bd=10, width= 10, relief = 'sunken')
lblTrade2.grid(row= 5, column=1)

#        
lblTrade1 = Label(RightMidFrame, font = ('arial', 14, 'bold'), text= "Financing ", bg='darkgray', bd=10, width= 14, anchor='w')
lblTrade1.grid(row= 5, column=2)
lblTrade2 = Label(RightMidFrame, font = ('arial', 14, 'bold'), textvariable = var4, bd=10, width= 10, relief = 'sunken')
lblTrade2.grid(row= 5, column=3)


#        
lblPrice1 = Label(RightMidFrame, font = ('arial', 14, 'bold'), text= "Address", bg='darkgray', bd=10, width= 14, anchor='w')
lblPrice1.grid(row= 6, column=0)
lblPrice2 = Label(RightMidFrame, font = ('arial', 14, 'bold'), textvariable = var4, bd=10, width= 45, relief = 'sunken')
lblPrice2.grid(row= 6, column=1, columnspan =4)


#        
lblMSRPs1 = Label(RightMidFrame, font = ('arial', 14, 'bold'), text= "Down Payment ", bg='darkgray', bd=10, width= 14, anchor='w')
lblMSRPs1.grid(row= 7, column=0)
lblMSRPs2 = Label(RightMidFrame, font = ('arial', 14, 'bold'), text = " ", bd=10, width= 10, relief = 'sunken')
lblMSRPs2.grid(row= 7, column=1)


#        
lblDiscounts1 = Label(RightMidFrame, font = ('arial', 14, 'bold'), text= "Total ", bg='darkgray', bd=10, width= 14, anchor='w')
lblDiscounts1.grid(row= 8, column=0)
lblDiscounts2 = Label(RightMidFrame, font = ('arial', 14, 'bold'), textvariable = var4, bd=10, width= 10, relief = 'sunken')
lblDiscounts2.grid(row= 8, column=1)

#        
lblDiscount1 = Label(RightMidFrame, font = ('arial', 14, 'bold'), text= "Monthly Payment", bg='darkgray', bd=10, width= 14, anchor='w')
lblDiscount1.grid(row= 7, column=2)
lblDiscount2 = Label(RightMidFrame, font = ('arial', 14, 'bold'), text= "                ", bd=10, width= 10, relief = 'sunken')
lblDiscount2.grid(row= 7, column=3)

#        
lblDisscount1 = Label(RightMidFrame, font = ('arial', 14, 'bold'), text= "Mothly Payment ", bg='darkgray', bd=10, width= 14, anchor='w')
lblDisscount1.grid(row= 8, column=2)
lblDisscount2 = Label(RightMidFrame, font = ('arial', 14, 'bold'), textvariable = var4, bd=10, width= 10, relief = 'sunken')
lblDisscount2.grid(row= 8, column=3)

#        
lblDiscounts1 = Label(RightMidFrame, font = ('arial', 14, 'bold'), text= "Total ", bg='darkgray', bd=10, width= 14, anchor='w')
lblDiscounts1.grid(row= 9, column=0)
lblDiscounts2 = Label(RightMidFrame, font = ('arial', 14, 'bold'), textvariable = var4, bd=10, width= 10, relief = 'sunken')
lblDiscounts2.grid(row= 9, column=1)


btnNext = Button(RightMidFrame, font =('arial', 14, 'bold'), text = '>>', bd =2)
btnNext.grid(row = 9, column= 3)

btnBack = Button(RightMidFrame, font =('arial', 14, 'bold'), text = '<<', bd =2)
btnBack.grid(row = 9, column= 2)

btnExit = Button(RightMidFrame, font =('arial', 14, 'bold'), text = 'Exit', bd =6)
btnExit.grid(row = 9, column= 4)

# --------------------------- Widget, Text, Labels and Entry outter Frames --------------------- #


		
		
		

	# End

root.mainloop()

	
"""

LeftFrame0 = Frame(LeftFrame, bd=4, width=710, height=140, padx=5, bg="teal")
LeftFrame0.grid(row=0, column=0)

LeftFrame1 = Frame(LeftFrame, bd=4, width=710, height=170, padx=5, bg="teal")
LeftFrame1.grid(row=1, column=0)
		
LeftFrame2 = Frame(LeftFrame, bd=4, width=710, height=165, padx=5, bg="teal")
LeftFrame2.grid(row=2, column=0)
		
LeftFrame3 = Frame(LeftFrame, bd=4, width=710, height=95, padx=5, bg="teal")
LeftFrame3.grid(row=3, column=0)
		
RightFrame0 = Frame(RightFrame, bd=4, width=520, height=200, padx=5, bg="coral")
RightFrame0.grid(row=0, column=0)
		
RightFrame1 = Frame(RightFrame, bd=4, width=520, height=280, padx=5, bg="coral")
RightFrame1.grid(row=1, column=0)
		
RightFrame2 = Frame(RightFrame, bd=4, width=520, height=95, padx=5, bg="coral")
RightFrame2.grid(row=2, column=0)

"""