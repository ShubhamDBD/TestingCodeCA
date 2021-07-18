import subprocess
from Exercise1 import *


with open("Payslip_123457_2021_07_04.txt", "wb") as f:
    subprocess.check_call(["python", "PaySlipGenerator1.py"], stdout=f)

with open("Payslip_123457_2021_07_11.txt", "wb") as f:
    subprocess.check_call(["python", "PaySlipGenerator2.py"], stdout=f)

with open("Payslip_123457_2021_07_18.txt", "wb") as f:
    subprocess.check_call(["python", "PaySlipGenerator3.py"], stdout=f)

with open("Payslip_123456_2021_07_04.txt", "wb") as f:
    subprocess.check_call(["python", "PaySlipGenerator4.py"], stdout=f)

with open("Payslip_123456_2021_07_11.txt", "wb") as f:
    subprocess.check_call(["python", "PaySlipGenerator5.py"], stdout=f)

with open("Payslip_123456_2021_07_18.txt", "wb") as f:
    subprocess.check_call(["python", "PaySlipGenerator6.py"], stdout=f)

