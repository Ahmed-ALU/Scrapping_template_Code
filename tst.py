# import requests
# from bs4 import BeautifulSoup
# from re import *
# import re

# url = 'https://arab.org/directory/activity/refugees/'

# head = {
#     "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"
# }

# response = requests.get(url, headers=head)

# txt = response.text

# # print(response.text)


# for i in re.findall('wpbdp\-listing\-\d{3,6}', txt):
#     print(i)

# with open(r'C:\Users\Hp\Desktop\test\tes.txt', 'w') as w:
#     w.write(txt)







# # for id in html.find_all(id = "wpbdp-page-category"):
#     # pass
#     # for div in id.find_all('') 
#     # print(i)




# """
# main container :
# id = "wpbdp-page-category"

# each org box:
# class="wpbdp-listing-\d"

# org name: 
# div (class="listing-title") --> a.text



# """


def email(string):
    r = int(string[:2], 16)
    email = ''.join([chr(int(string[i:i+2], 16) ^ r)
    for i in range(2, len(string), 2)])
    return email

print(email('cea6aba2a2a18ea2a7a8baa7bae0a7a0'))

