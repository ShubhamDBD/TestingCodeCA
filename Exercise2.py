from Exercise1 import *
from datetime import datetime


#######################################57#################################
gross_pay_avg = (Grosspay + Grosspay3 + Grosspay4)/3
print(f"The average gross pay for 'StaffID : 123457' is : {gross_pay_avg}")


#######################################57#################################
gross_pay_avg1 = (Grosspay1 + Grosspay6 + Grosspay7)/3
print(f"The average gross pay for 'StaffID : 123456' is : {gross_pay_avg1}")

###################################DateToday########################################
today_date = datetime.today().strftime('%d-%m-%y').strip()
print(f'Date today : {today_date}')

###################################Gross Pay########################################
gross_last_six_weeks = gross_pay_avg * 6 * 7
print(f"The total gross pay for each employee for the last six weeks 'StaffID : 123457' is : {gross_last_six_weeks}")
gross_last_six_weeks1 = gross_pay_avg1 * 6 * 7
print(f"The total gross pay for each employee for the last six weeks 'StaffID : 123456' is : {gross_last_six_weeks1}")