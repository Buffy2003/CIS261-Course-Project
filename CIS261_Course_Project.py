# Rashelle Ward
# CIS261
# Course Project - Phase 1
def GetEmpName():
    empname = input("Enter employee name: ")
    return empname

#for the next three functions, you need to convert the input to a float, e.g., varname = float(input('descripion of input:  '))
def GetHoursWorked(): #write the GetHoursWorked function
    hours = float(input("Enter the total hours worked: "))
    return hours

def GetHourlyRate(): #write the GetHourlyRate function
    hourlyrate = float(input("Enter your hourly rate: "))
    return hourlyrate

def GetTaxRate(): # write the GetTaxRate function
    taxrate = float(input("Enter the tax rate: "))
    return taxrate

def CalcTaxAndNetPay(hours, hourlyrate, taxrate):
    grosspay = hours * hourlyrate
    incometax = grosspay * taxrate
    netpay = grosspay - incometax
    return grosspay, incometax, netpay

def printinfo(empname, hours, hourlyrate,grosspay, taxrate, incometax, netpay):
    print()
    print("Name:  ", empname) 
    print("Hours Worked: ", f"{hours:,.2f}")
     # write the lines of code to display hourlyrate, grosspay, taxrate, incometax and netpay with correct formatting
    print("Hourly Rate: ", f"{hourlyrate:,.2f}")
    print("Gross Pay: ", f"{grosspay:,.2f}")
    print("Tax Rate:  ", f"{taxrate:,.1%}")  # taxrate needs to be formatted as percentage
    print("Income Tax: ", f"{incometax:,.2f}")
    print("Net Pay: ", f"{netpay:,.2f}") 
    print()



def PrintTotals(TotEmployees, TotHours, TotGrossPay, TotTax, TotNetPay):    
    print()
    print(f"Total Number Of Employees: {TotEmployees}")
    print(f"Total Hours Worked: {TotHours:,.2f}")
    # write the code to print  TotGrossPay, TotTax, and TotNetpay with 2 decimal places
    print(f"Total Gross Pay: {TotGrossPay:,.2f}")
    print(f"Total Income Tax: {TotTax:,.2f} ")
    print(f"Total Net Pay: {TotNetPay:,.2f}")
    print()

if __name__ == "__main__":
    TotEmployees = 0
    TotHours = 0.00
    TotGrossPay = 0.00
    TotTax = 0.00
    TotNetPay = 0.00
    while True:
        
        empname = GetEmpName()
        if (empname.upper() == "END"):
            break
        hours = GetHoursWorked() #write the code to assign to hours the return value from GetHoursWorked
        hourlyrate = GetHourlyRate() # write the code to assign to hourlyrate the return value from GetHourlyRate
        taxrate = GetTaxRate() # write the code to assign to taxrate the return value from GetTaxRate

        grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)
        printinfo(empname, hours, hourlyrate, grosspay, taxrate, incometax, netpay)
        TotEmployees += 1
        TotHours += hours
        # write the code to increment the other total variables with the appropriate values
        TotGrossPay += grosspay
        TotTax += incometax
        TotNetPay += netpay



    PrintTotals (TotEmployees, TotHours, TotGrossPay, TotTax, TotNetPay)