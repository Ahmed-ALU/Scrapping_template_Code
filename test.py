from numpy import append
import openpyxl as OPX
from openpyxl import load_workbook as readWorkbook
from openpyxl import Workbook as writeWorkbook
import re as RGX
import requests as REQ
from bs4 import BeautifulSoup as BS

html = REQ.get('http://www.geoc.jp/rashinban/dantai_detail_532.html').text

html = BS(html, 'html.parser')
x = int()
for tbody in html.find_all('tbody'):
    x+=1
    if x == 2:
        x = int(1)
        for td in tbody.find_all('td')[6]:
            print(f"{x-1}: {td}".encode('latin1').decode('utf-8').strip(':'))
            print() 
            x+=1



# txt = '<div class="flaglist"> <a href="/countries/algeria/" data-wpel-link="internal"><img title="NGO Directory of Algeria" src="https://arab.org/wp-content/uploads/2016/03/DZ.png" width="29" height="29"></a> <a href="/countries/bahrain/" data-wpel-link="internal"><img title="NGO Directory of Bahrain" src="https://arab.org/wp-content/uploads/2016/03/BH.png" width="29" height="29"></a> <a href="/portal/comoros/" data-wpel-link="internal"><img title="NGO Portal of Comoros" src="https://arab.org/wp-content/uploads/2016/03/KM.png" width="29" height="29"></a> <a href="/countries/djibouti/" data-wpel-link="internal"><img title="NGO Directory of Djibouti" src="https://arab.org/wp-content/uploads/2016/03/DJ.png" width="29" height="29"></a> <a href="/countries/egypt/" data-wpel-link="internal"><img title="NGO Directory of Egypt" src="https://arab.org/wp-content/uploads/2016/03/EG.png" width="29" height="29"></a> <a href="/countries/iraq/" data-wpel-link="internal"><img title="NGO Directory of Iraq" src="https://arab.org/wp-content/uploads/2016/03/IQ-1.png" width="29" height="29"></a><a href="/countries/jordan/" data-wpel-link="internal"><img title="NGO Directory of Jordan" src="https://arab.org/wp-content/uploads/2016/03/JO.png" width="29" height="29"></a> <a href="/countries/kuwait/" data-wpel-link="internal"><img title="NGO Directory of Kuwait" src="https://arab.org/wp-content/uploads/2016/03/KW.png" width="29" height="29"></a> <a href="/countries/lebanon/" data-wpel-link="internal"><img title="NGO Directory of Lebanon" src="https://arab.org/wp-content/uploads/2016/03/LB.png" width="29" height="29"></a> <a href="/countries/libya/" data-wpel-link="internal"><img title="NGO Directory of Libya" src="https://arab.org/wp-content/uploads/2016/03/LY.png" width="29" height="29"></a> <a href="/countries/mauritania/" data-wpel-link="internal"><img title="NGO Directory of Mauritania" src="https://arab.org/wp-content/uploads/2018/05/MR-1.png" width="29" height="29"></a> <a href="/countries/morocco/" data-wpel-link="internal"><img title="NGO Directory of Morocco" src="https://arab.org/wp-content/uploads/2016/03/MA.png" width="29" height="29"></a><a href="/countries/oman/" data-wpel-link="internal"><img title="NGO Directory of Oman" src="https://arab.org/wp-content/uploads/2016/03/OM.png" width="29" height="29"></a> <a href="/countries/qatar/" data-wpel-link="internal"><img title="NGO Directory of Qatar" src="https://arab.org/wp-content/uploads/2016/03/QA.png" width="29" height="29"></a> <a href="/countries/palestine/" data-wpel-link="internal"><img title="NGO Directory of Palestine" src="https://arab.org/wp-content/uploads/2016/03/PS.png" width="29" height="29"></a> <a href="/countries/saudi-arabia/" data-wpel-link="internal"><img title="NGO Directory of Saudi Arabia" src="https://arab.org/wp-content/uploads/2016/03/SA.png" width="29" height="29"></a> <a href="/countries/somalia/" data-wpel-link="internal"><img title="NGO Directory of Somalia" src="https://arab.org/wp-content/uploads/2016/03/SO.png" width="29" height="29"></a> <a href="/countries/sudan/" data-wpel-link="internal"><img title="NGO Directory of Sudan" src="https://arab.org/wp-content/uploads/2016/03/SD.png" width="29" height="29"></a><a href="/countries/syria/" data-wpel-link="internal"><img title="NGO Directory of Syria" src="https://arab.org/wp-content/uploads/2016/03/SY.png" width="29" height="29"></a> <a href="/countries/tunisia/" data-wpel-link="internal"><img title="NGO Directory of Tunisia" src="https://arab.org/wp-content/uploads/2016/03/TN.png" width="29" height="29"></a> <a href="/countries/uae/" data-wpel-link="internal"><img title="NGO Directory of the UAE" src="https://arab.org/wp-content/uploads/2016/03/AE.png" width="29" height="29"></a> <a href="/countries/yemen/" '

# x = int()
# l = list()
# for i in range(len(txt)):
#     if txt[i:].startswith("/co"):
#         l.append(txt[i:i+20])

# # print(l)

# l2 = ['/countries/algeria/', '/countries/bahrain/', '/countries/djibouti/', '/countries/egypt/', '/countries/iraq/', '/countries/jordan/', '/countries/kuwait/', '/countries/lebanon/', '/countries/libya/', '/countries/mauritania/', '/countries/morocco/', '/countries/oman/', '/countries/qatar/', '/countries/palestine', '/countries/saudi-arabia', '/countries/somalia/', '/countries/sudan/', '/countries/syria/', '/countries/tunisia/', '/countries/uae/', '/countries/yemen/']

# print(len(l2))


