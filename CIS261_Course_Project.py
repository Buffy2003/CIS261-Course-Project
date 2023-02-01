# Rashelle Ward
# CIS261
# Course Project - Phase 1
def GetEmpName():
    empname = input("Enter employee name: ")
    return empname
def GetDatesWorked():
    fromdate = input("Please enter start date (mm/dd/yyy): ")  #write the code to input fromdate and todate and return the values from the function.  
    todate = input("Please enter End Date (mm/dd/yyy): ")       #Prompt the user for the dates in the following format: mm/dd/yyyy
    return fromdate, todate                                     #no validations are needed for this input, we will assume the dates are entered correctly
def GetHoursWorked():
    hours = float(input("Enter the total hours worked: "))
    return hours
def GetHourlyRate():
    hourlyrate = float(input("Enter your hourly rate: "))
    return hourlyrate
def GetTaxRate():
    taxrate = float(input("Enter the tax rate: "))
    return taxrate
def CalcTaxAndNetPay(hours, hourlyrate, taxrate):
    grosspay = hours * hourlyrate
    incometax = grosspay * taxrate
    netpay = grosspay - incometax
    return grosspay, incometax, netpay
#def printinfo(empname, hours, hourlyrate,grosspay, taxrate, incometax, netpay):
    #print()
    #print("Name:  ", empname) 
    #print("Hours Worked: ", f"{hours:,.2f}")
    #print("Hourly Rate: ", f"{hourlyrate:,.2f}")
    #print("Gross Pay: ", f"{grosspay:,.2f}")
    #print("Tax Rate:  ", f"{taxrate:,.1%}")  # taxrate needs to be formatted as percentage
    #print("Income Tax: ", f"{incometax:,.2f}")
    #print("Net Pay: ", f"{netpay:,.2f}") 
    #print()
def printinfo(EmpDetailList):
    TotEmployees = 0
    TotHours = 0.00
    TotGrossPay = 0.00
    TotTax = 0.00
    TotNetPay = 0.00
    # the following code creates a for loop to read through EmpDetailList and assign values in list to variables
    for EmpList in EmpDetailList:
        fromdate = EmpList[0]
        #write code to assign values to todate, empname, hours, hourlyrate, and taxrate from EmpLst





        grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)
        print()
        print("Name:   ", empname)
        print("From Date:  ", fromdate)
        print("To Date:  ", todate)
        print("Hours Worked:  ", f"{hours:,.2f}:")
        print("Hourly Rate: ", f"{hourlyrate:,.2f}")
        print("Gross Pay: ", f"{grosspay:,.2f}")
        print("Tax Rate: ", f"{taxrate:,.1%}")
        print("Income Tax: ", f"{incometax:,.2f}")
        print("Netpay: ", f"{netpay:,.2f}")
        print()                                                                                                            
        ##print(fromdate, todate, empname, f"{hours:,.2f}",  f"{hourlyrate:,.2f}", f"{grosspay:,.2f}",  f"{taxrate:,.1%}",  f"{incometax:,.2f}",  f"{netpay:,.2f}")    #I think this needs fixed
        TotEmployees += 1
        TotHours += hours
        TotGrossPay += grosspay
        TotTax += incometax
        TotNetPay += netpay
        # the following line of code assigns TotEmployees totals to dictionary 
        EmpTotals["TotEmp"] = TotEmployees
        # write code to assign TotHours, TotGrossPay, TotTax, and TotNetPay to corresponding dictionary item



#def PrintTotals(TotEmployees, TotHours, TotGrossPay, TotTax, TotNetPay):    
    #print()
    #print(f"Total Number Of Employees: {TotEmployees}")
    #print(f"Total Hours Worked: {TotHours:,.2f}")
    #print(f"Total Gross Pay: {TotGrossPay:,.2f}")
    #print(f"Total Income Tax: {TotTax:,.2f} ")
    #print(f"Total Net Pay: {TotNetPay:,.2f}")
    #print()

#####    def PrintTotals(EmpTotals):    
    # use dictionary to print totals
    # the following line of code prints Total Employees from the dictionary
    print(f'Total Number Of Employees: {EmpTotals["TotEmp"]}')
    # write code to print TotalHrs, TotGrossPay, TotTax and TotNetPay from dictionary





if __name__ == "__main__":
    #TotEmployees = 0
    #TotHours = 0.00
    #TotGrossPay = 0.00
    #TotTax = 0.00
    #TotNetPay = 0.00

    #Create empty list and dictionary
    EmpDetailList = []
    EmpTotals = {}
    while True:
        empname = GetEmpName()
        if (empname.upper() == "END"):
            break
        fromdate, todate = GetDatesWorked()
        hours = GetHoursWorked() 
        hourlyrate = GetHourlyRate() 
        taxrate = GetTaxRate() 
        ## Comment out the following code
        #grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)
        #printinfo(empname, hours, hourlyrate, grosspay, taxrate, incometax, netpay)

        #write code to insert fromdate, todate, empname, hours, hourlyrate, and taxrate into list EmpDetail
        def list(EmpDetail):
            for i, empname in enumerate(EmpDetail, start=1):   #Not sure that this is right
                print(f"{i}. {empname}")
            print()


        #the following code appends the list EmpDetail to the list EmpDetailList
        EmpDetailList.append(EmpDetail)
    

        
        #TotEmployees += 1
        #TotHours += hours
        #TotGrossPay += grosspay
        #TotTax += incometax
        #TotNetPay += netpay



    #PrintTotals (TotEmployees, TotHours, TotGrossPay, TotTax, TotNetPay)
    printinfo(EmpDetailList)
    PrintTotals (EmpTotals)