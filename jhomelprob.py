#Lab Activity
print("EMPLOYEE PAY SLIP")
# nid = Employee ID
nid= str(input("Enter Employee Id:"))
name= str(input("Enter name of employee:"))
ar= str(input("Enter Academic Rank:"))
aca=float(2000.00)
#basic = monthly salary
basic=float(input("Enter Monthly Salary :"))
# gd = GSIS
# pd = Pag Ibig
# phd = Philhealth 
# taxa = Annual Income(Monthly salary times 2)
# taxd = excess of 250,000
# taxene = the 15% excess in the annual income
# tax = Overall computation of TAX (taxa,taxd,taxene)
# d = DEDUCTIONS 
# Netpay = Monthly - Deductions + allowance
gd= float(basic*0.09)
pd= float(100.00)
phd= float(basic*0.0175)
taxa=float(basic*12)
taxd=float(taxa-250000)
taxene= float((taxd*0.15))
tax= float(taxene/12)
d= (gd+pd+phd+tax)
netpay=float((basic-d)+aca)



print("\n\n")
print("==============================================")
print(" EMPLOYEE ID : ",nid)
print(" NAME OF EMPLOYEE : ",name)
print(" ACADEMIC RANK: ",ar)
print(" MONTHLY SALARY : ",basic)
print("\n\n")
print("DEDUCTIONS ")
print(" GSIS : ",gd)
print(" PAG-IBIG: ",pd)
print(" PHILHEALTH: ",phd)
print(" TAX : ",tax)
#DEDUCTIONS = GSIS/PAGIBIG/PHILHEALTH/TAX
print("DEDUCTIONS ",d)
print("ALLOWANCE ")
print("ACAPERA ",aca)
print("NETPAY: ",netpay)

