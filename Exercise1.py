import json

##############################DATABASE SETUP########################
import mysql
myDatabase = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    port='3306',
    database='connector'
)
myCursor = myDatabase.cursor()

myCursor.execute('SELECT * FROM users')

users = myCursor.fetchall()

for user in users:
    print(user)

#################################DATA EXTRACTION FROM .txt & ,json FILE#################
with open('Employees.txt') as fo: #READING DATA FROM A .TXT FILE
    content = fo.read()
    content_list = content.split()

with open('Hours.txt') as fo1: #READING DATA FROM A .TXT FILE
    content1 = fo1.read()
    content_list1 = content1.split()

with open('tax.json') as fo2:   #READING DATA FROM A JSON FILE
    content2 = fo2.read()
    content_list2 = json.loads(content2)
    Standard_Rate = int(content_list2["Standard Rate"]) #extracted standard_rate from json file
    Higher_Rate = int(content_list2["Higher Rate"]) #extracted higher rates from json file




####################################(57/04)##########################################
Total_Hours = int(content_list[13]) * int(content_list[14])  #Total amount from regular work
Overtime_Hours = int(content_list1[5]) - int(content_list[13]) #Total hours from overtime work
Total_Overtime = Overtime_Hours * int(content_list[15]) #Total amount from overtime work
Grosspay = Total_Hours + Total_Overtime
Total_Standard_Band = int(content_list[17])*(Standard_Rate/100)
Higher_Rate_Pay = int(Grosspay)-int(content_list[17])
Total_Highet_Rate = int(Higher_Rate_Pay)*(Higher_Rate/100)
Total_Deductions = int(Total_Standard_Band)+int(Total_Highet_Rate)
Net_Deductions = Total_Deductions-int(content_list[16])
Net_Pay = int(Grosspay)-int(Net_Deductions)

def myFunction():
    print('.............................PAY SLIP.................................')
    print(f'StaffID: {content_list[9]}')
    print(f'Staff Name: {content_list[11]} {content_list[10]}')
    print(f'PPSN: {content_list[12]}')
    print(f'Date: {content_list1[3]}')
    print(f'            Hour Rate Total ')
    print(f'Regular:    {content_list[13]}    {content_list[14]}   {Total_Hours}')
    print(f'Overtime :  {Overtime_Hours}   {content_list[15]}   {Total_Overtime}')
    print('\n')
    print(f'Grosspay :   {Grosspay}')
    print(f'                     Rate     Total')
    print(f'Standard Band  :  {content_list[17]}   {Standard_Rate}%   {Total_Standard_Band}')
    print(f'Higher Rate    :  {Higher_Rate_Pay}   {Higher_Rate}%   {Total_Highet_Rate}')
    print('\n')
    print(f'Total Deductions: {Total_Deductions}')
    print(f'Tax Credit:       {content_list[16]}')
    print(f'Net Deductions:   {Net_Deductions}')
    print(f'Net Pay:          {Net_Pay}')





#########################################57/11###############################################
Total_Hours = int(content_list[13]) * int(content_list[14])  #Total amount from regular work
Overtime_Hours3 = int(content_list1[8]) - int(content_list[13]) #Total hours from overtime work
Total_Overtime3 = Overtime_Hours3 * int(content_list[15]) #Total amount from overtime work
Grosspay3 = Total_Hours + Total_Overtime3
Total_Standard_Band = int(content_list[17])*(Standard_Rate/100)
Higher_Rate_Pay3 = abs(int(Grosspay3) - int(content_list[17]))
Total_Highet_Rate3 = int(Higher_Rate_Pay3) * (Higher_Rate / 100)
Total_Deductions3 = int(Total_Standard_Band) + int(Total_Highet_Rate3)
Net_Deductions3 = Total_Deductions3 - int(content_list[16])
Net_Pay3 = int(Grosspay3) - int(Net_Deductions3)

def myFunction1():
    print('.............................PAY SLIP.................................')
    print(f'StaffID: {content_list[9]}')
    print(f'Staff Name: {content_list[11]} {content_list[10]}')
    print(f'PPSN: {content_list[12]}')
    print(f'Date: {content_list1[6]}')
    print(f'            Hour Rate Total ')
    print(f'Regular:    {content_list[13]}    {content_list[14]}   {Total_Hours}')
    print(f'Overtime :  {Overtime_Hours3}   {content_list[15]}   {Total_Overtime3}')
    print('\n')
    print(f'Grosspay :   {Grosspay3}')
    print(f'                     Rate     Total')
    print(f'Standard Band  :  {content_list[17]}   {Standard_Rate}%   {Total_Standard_Band}')
    print(f'Higher Rate    :  {Higher_Rate_Pay3}   {Higher_Rate}%   {Total_Highet_Rate3}')
    print('\n')
    print(f'Total Deductions: {Total_Deductions3}')
    print(f'Tax Credit:       {content_list[16]}')
    print(f'Net Deductions:   {Net_Deductions3}')
    print(f'Net Pay:          {Net_Pay3}')




#########################################57/18###############################################
Total_Hours = int(content_list[13]) * int(content_list[14])  #Total amount from regular work
Overtime_Hours4 = int(content_list1[14]) - int(content_list[13]) #Total hours from overtime work
Total_Overtime4 = Overtime_Hours4 * int(content_list[15]) #Total amount from overtime work
Grosspay4 = Total_Hours + Total_Overtime4
Total_Standard_Band = int(content_list[17])*(Standard_Rate/100)
Higher_Rate_Pay4 = abs(int(Grosspay4) - int(content_list[17]))
Total_Highet_Rate4 = int(Higher_Rate_Pay4) * (Higher_Rate / 100)
Total_Deductions4 = int(Total_Standard_Band) + int(Total_Highet_Rate4)
Net_Deductions4 = Total_Deductions4 - int(content_list[16])
Net_Pay4 = abs(int(Grosspay4) - int(Net_Deductions4))

def myFunction2():
    print('.............................PAY SLIP.................................')
    print(f'StaffID: {content_list[9]}')
    print(f'Staff Name: {content_list[11]} {content_list[10]}')
    print(f'PPSN: {content_list[12]}')
    print(f'Date: {content_list1[12]}')
    print(f'            Hour Rate Total ')
    print(f'Regular:    {content_list[13]}    {content_list[14]}   {Total_Hours}')
    print(f'Overtime :  {Overtime_Hours4}   {content_list[15]}   {Total_Overtime4}')
    print('\n')
    print(f'Grosspay :   {Grosspay4}')
    print(f'                     Rate     Total')
    print(f'Standard Band  :  {content_list[17]}   {Standard_Rate}%   {Total_Standard_Band}')
    print(f'Higher Rate    :  {Higher_Rate_Pay4}   {Higher_Rate}%   {Total_Highet_Rate4}')
    print('\n')
    print(f'Total Deductions: {Total_Deductions4}')
    print(f'Tax Credit:       {content_list[16]}')
    print(f'Net Deductions:   {Net_Deductions4}')
    print(f'Net Pay:          {Net_Pay4}')


####################################(56/04)##########################################
Total_Hours1 = int(content_list[4]) * int(content_list[5])  # Total amount from regular work
Overtime_Hours1 = int(content_list1[2]) - int(content_list[4])  # Total hours from overtime work
Total_Overtime1 = Overtime_Hours1 * int(content_list[6])  # Total amount from overtime work
Grosspay1 = Total_Hours1 + Total_Overtime1
Total_Standard_Band1 = int(content_list[8]) * (Standard_Rate / 100)
Higher_Rate_Pay1 = int(Grosspay1) - int(content_list[8])
Total_Highet_Rate1 = int(Higher_Rate_Pay1) * (Higher_Rate / 100)
Total_Deductions1 = int(Total_Standard_Band1) + int(Total_Highet_Rate1)
Net_Deductions1 = Total_Deductions1 - int(content_list[7])
Net_Pay1 = int(Grosspay1) - int(Net_Deductions1)

def myFunction3():
    print('.............................PAY SLIP.................................')
    print(f'StaffID: {content_list[0]}')
    print(f'Staff Name: {content_list[2]} {content_list[1]}')
    print(f'PPSN: {content_list[3]}')
    print(f'Date: {content_list1[0]}')
    print(f'            Hour Rate Total ')
    print(f'Regular:    {content_list[4]}   {content_list[5]}   {Total_Hours1}')
    print(f'Overtime :  {Overtime_Hours1}   {content_list[6]}   {Total_Overtime1}')
    print('\n')
    print(f'Grosspay :   {Grosspay1}           ')
    print(f'                     Rate     Total')
    print(f'Standard Band  :  {content_list[8]}   {Standard_Rate}%   {Total_Standard_Band1}')
    print(f'Higher Rate    :  {Higher_Rate_Pay1}   {Higher_Rate}%   {Total_Highet_Rate1}')
    print('\n')
    print(f'Total Deductions: {Total_Deductions1}')
    print(f'Tax Credit:       {content_list[7]}')
    print(f'Net Deductions:   {Net_Deductions1}')
    print(f'Net Pay:          {Net_Pay1}')



####################################(56/11)##########################################
Total_Hours6 = int(content_list[4]) * int(content_list[5])  # Total amount from regular work
Overtime_Hours6 = int(content_list1[5]) - int(content_list[4])  # Total hours from overtime work
Total_Overtime6 = Overtime_Hours6 * int(content_list[6])  # Total amount from overtime work
Grosspay6 = Total_Hours6 + Total_Overtime6
Total_Standard_Band6 = int(content_list[8]) * (Standard_Rate / 100)
Higher_Rate_Pay6 = int(Grosspay6) - int(content_list[8])
Total_Highet_Rate6 = int(Higher_Rate_Pay6) * (Higher_Rate / 100)
Total_Deductions6 = int(Total_Standard_Band6) + int(Total_Highet_Rate6)
Net_Deductions6 = Total_Deductions6 - int(content_list[7])
Net_Pay6 = int(Grosspay6) - int(Net_Deductions6)

def myFunction4():
    print('.............................PAY SLIP.................................')
    print(f'StaffID: {content_list[0]}')
    print(f'Staff Name: {content_list[2]} {content_list[1]}')
    print(f'PPSN: {content_list[3]}')
    print(f'Date: {content_list1[6]}')
    print(f'            Hour Rate Total ')
    print(f'Regular:    {content_list[4]}   {content_list[5]}   {Total_Hours6}')
    print(f'Overtime :  {Overtime_Hours6}   {content_list[6]}   {Total_Overtime6}')
    print('\n')
    print(f'Grosspay :   {Grosspay6}           ')
    print(f'                     Rate     Total')
    print(f'Standard Band  :  {content_list[8]}   {Standard_Rate}%   {Total_Standard_Band6}')
    print(f'Higher Rate    :  {Higher_Rate_Pay6}   {Higher_Rate}%   {Total_Highet_Rate6}')
    print('\n')
    print(f'Total Deductions: {Total_Deductions6}')
    print(f'Tax Credit:       {content_list[7]}')
    print(f'Net Deductions:   {Net_Deductions6}')
    print(f'Net Pay:          {Net_Pay6}')


####################################(56/18)##########################################
Total_Hours8 = int(content_list[4]) * int(content_list[5])  # Total amount from regular work
Overtime_Hours7 = abs(int(content_list1[11]) - int(content_list[4]))   # Total hours from overtime work
Total_Overtime7 = Overtime_Hours7 * int(content_list[6])  # Total amount from overtime work
Grosspay7 = Total_Hours8 + Total_Overtime7
Total_Standard_Band7 = int(content_list[8]) * (Standard_Rate / 100)
Higher_Rate_Pay7 = int(Grosspay7) - int(content_list[8])
Total_Highet_Rate7 = int(Higher_Rate_Pay7) * (Higher_Rate / 100)
Total_Deductions7 = int(Total_Standard_Band7) + int(Total_Highet_Rate7)
Net_Deductions7 = Total_Deductions7 - int(content_list[7])
Net_Pay7 = int(Grosspay7) - int(Net_Deductions7)

def myFunction5():
    print('.............................PAY SLIP.................................')
    print(f'StaffID: {content_list[0]}')
    print(f'Staff Name: {content_list[2]} {content_list[1]}')
    print(f'PPSN: {content_list[3]}')
    print(f'Date: {content_list1[12]}')
    print(f'            Hour Rate Total ')
    print(f'Regular:    {content_list[4]}   {content_list[5]}   {Total_Hours8}')
    print(f'Overtime :  {Overtime_Hours7}   {content_list[6]}   {Total_Overtime7}')
    print('\n')
    print(f'Grosspay :   {Grosspay7}           ')
    print(f'                     Rate     Total')
    print(f'Standard Band  :  {content_list[8]}   {Standard_Rate}%   {Total_Standard_Band7}')
    print(f'Higher Rate    :  {Higher_Rate_Pay7}   {Higher_Rate}%   {Total_Highet_Rate7}')
    print('\n')
    print(f'Total Deductions: {Total_Deductions7}')
    print(f'Tax Credit:       {content_list[7]}')
    print(f'Net Deductions:   {Net_Deductions7}')
    print(f'Net Pay:          {Net_Pay7}')




