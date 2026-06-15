Grade = input("Enter any grade from A-F:")
City_tier = int(input("Enter the city tier (1-3): "))
Tier = 0
Basic_Pay = 0
other_Allowances = 0

if City_tier == 1:
    Tier = 0.3
elif City_tier == 2:
    Tier = 0.2
elif City_tier == 3:
    Tier = 0.1


if Grade == "A":
    Basic_Pay = 60000
    other_Allowances = 8000
elif Grade == "B":
    Basic_Pay = 50000
    other_Allowances = 7000
elif Grade =="C":
    Basic_Pay = 40000
    other_Allowances = 6000
elif Grade == "D":
    Basic_Pay = 30000
    other_Allowances = 5000
elif Grade == "E":
    Basic_Pay = 20000
    other_Allowances = 4000
elif Grade == "F":
    Basic_Pay = 10000
    other_Allowances = 3000

HRA = Tier*Basic_Pay
DA  = 0.5*Basic_Pay
EPF = 0.11 * Basic_Pay
TA = 900
Professional_Tax = 300
Gross_Pay = Basic_Pay+HRA+DA+other_Allowances+TA+Professional_Tax-EPF
Annual_Income = Gross_Pay * 12
print(Gross_Pay)
print(Annual_Income)
Tax_slab = 0
Tax = 0
for i in range(1,Annual_Income):

    if 0 <= Tax_slab <= 250000:
        Tax = Tax_slab*0
    elif 250001 <= Tax_slab <= 500000:
        Tax = Tax_slab*0.05
    elif 500001 <= Tax_slab <=750000:
        Tax = Tax_slab*0.10+12500
    elif 750001 <= Tax_slab <=1000000:
        Tax = Tax_slab*0.15+37500
    elif 1000001 <= Tax_slab <= 1250000:
        Tax = Tax_slab*0.20+75000
    elif 1250001 <= Tax_slab <=1500000:
        Tax = Tax_slab*0.25+125000
    elif Tax_slab>=1500000:
        Tax = Tax_slab*0.30+187500

