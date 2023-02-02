# Rashelle Ward
# CIS261
# Course Project - Phase 2
def GetEmpName():
    empname = input("Enter employee name: ")
    return empname
def GetDatesWorked(): 
    fromdate = input("Please enter start date (mm/dd/yyy): ")
    todate = input("Please enter End Date (mm/dd/yyy): ")       
    return fromdate, todate                                     
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
    #print("Tax Rate:  ", f"{taxrate:,.1%}")
    #print("Income Tax: ", f"{incometax:,.2f}")
    #print("Net Pay: ", f"{netpay:,.2f}") 
    #print()
def printinfo(EmpDetailList):
    TotEmployees = 0
    TotHours = 0.00
    TotGrossPay = 0.00
    TotTax = 0.00
    TotNetPay = 0.00
    for EmpList in EmpDetailList:
        fromdate = EmpList[0]
        todate = EmpList[1]
        empname = EmpList[2]
        hours = EmpList[3]
        hourlyrate = EmpList[4]
        taxrate = EmpList[5]

        grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)
        print()
        print("Name: ", empname)
        print("From Date: ", fromdate)
        print("To Date: ", todate)
        print("Hours Worked: ", f"{hours:,.2f}")
        print("Hourly Rate: ", f"{hourlyrate:,.2f}")
        print("Gross Pay: ", f"{grosspay:,.2f}")
        print("Tax Rate: ", f"{taxrate:,.1%}")
        print("Income Tax: ", f"{incometax:,.2f}")
        print("Netpay: ", f"{netpay:,.2f}")
        print()                                                                                          
        TotEmployees += 1
        TotHours += hours
        TotGrossPay += grosspay
        TotTax += incometax
        TotNetPay += netpay 
        EmpTotals["TotEmp"] = TotEmployees 
        EmpTotals["Tothrs"] = TotHours
        EmpTotals["Totgross"] = TotGrossPay
        EmpTotals["TTax"] = TotTax
        EmpTotals["Totnet"] = TotNetPay
#def PrintTotals(TotEmployees, TotHours, TotGrossPay, TotTax, TotNetPay):    
    #print()
    #print(f"Total Number Of Employees: {TotEmployees}")
    #print(f"Total Hours Worked: {TotHours:,.2f}")
    #print(f"Total Gross Pay: {TotGrossPay:,.2f}")
    #print(f"Total Income Tax: {TotTax:,.2f} ")
    #print(f"Total Net Pay: {TotNetPay:,.2f}")
    #print()
def PrintTotals(EmpTotals):
    print(f'Total Number Of Employees: {EmpTotals["TotEmp"]}')
    print(f'Total Hours Worked: {EmpTotals["Tothrs"]:,.2f}')
    print(f'Total Gross Pay: {EmpTotals["Totgross"]:,.2f}')
    print(f'Total Income Tax: {EmpTotals["TTax"]:,.2f}')
    print(f'Total Net Pay: {EmpTotals["Totnet"]:,.2f}') 
    print()

if __name__ == "__main__":
    #TotEmployees = 0
    #TotHours = 0.00
    #TotGrossPay = 0.00
    #TotTax = 0.00
    #TotNetPay = 0.00

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

        #grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)
        #printinfo(empname, hours, hourlyrate, grosspay, taxrate, incometax, netpay)

        EmpDetail = [fromdate, todate, empname, hours, hourlyrate, taxrate]
        EmpDetailList.append(EmpDetail)

        #TotEmployees += 1
        #TotHours += hours
        #TotGrossPay += grosspay
        #TotTax += incometax
        #TotNetPay += netpay

    printinfo(EmpDetailList)  
    PrintTotals(EmpTotals)  