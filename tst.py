import requests
from bs4 import BeautifulSoup
from re import *
import re



url = 'https://arab.org/directory/activity/refugees/page/10'

head = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"
}

response = requests.get(url, headers=head)

txt = response.text

html = BeautifulSoup(txt, 'html.parser')

# print(response.text)

listingNumList = list()
for org in re.findall('wpbdp\-listing\-\d{3,6}', txt):
    
    if org not in listingNumList:
        listingNumList.append(org)
        for div1 in html.find_all('div', class_ = org):
            
            # Name storing 
            for div2 in div1.find_all('div', class_ = 'listing-title'):
                for a in div2.find_all('a'):
                    Name = str(a.text)

            # The rest of the data:
            for dataContainer in div1.find_all('div', class_ = 'listing-details'):
                # Here we can loop in the title and the data itself one by one
                type, website, sMedia, activity = '', '', '', ''
                for data in dataContainer.find_all('div', class_='wpbdp-field-display'):
                    

                    # Title of the data is here 
                    for span in data.find_all('span', class_ = 'field-label'):
                        title = str(span.text).strip()
                    
                    # if condition to catch each type of data
                    if title.startswith("Organization's Official Na"):
                        for value in data.find_all('div', class_="value"):
                            for a in value.find_all('a'):
                                offName = str(a.text).strip()
                    
                    elif title.startswith("Acrony"):
                        for value in data.find_all('div', class_="value"):
                            acronym = str(value.text).strip()
                    
                    elif title.startswith("Typ"):
                        for value in data.find_all('div', class_="value"):
                            type = str(value.text).strip()

                    elif title.startswith("Activit"):
                        for value in data.find_all('div', class_="value"):
                            temp = list()
                            for a in value.find_all('a'):
                                temp.append(a.text)
                            for act in temp:    
                                activity = activity + f', {act}'.strip()
                            activity = activity[2:]
                            temp = list()
                    
                    elif title.startswith("Phone"):
                        for value in data.find_all('div', class_="value"):
                            for a in value.find_all('a'):
                                phone = str(a.text).strip()
                    
                    elif title.startswith("Website"):
                        for value in data.find_all('div', class_="value"):
                            for a in value.find_all('a'):
                                website = str(a.get('href')).strip()
                    
                    #Getting the email
                    ##########Code########
                    
                    elif title.startswith("Social"):
                        for value in data.find_all('div', class_="value"):
                            for a in value.find_all('a'):
                                sMedia = str(a.get('href')).strip()
                    
                    
                print(Name)
                print(type)
                print(website)
                print(sMedia)
                print(activity)
                print()
                Name, type, website, sMedia, activity = '', '', '', '', ''
        # print()
        # print()


# with open(r'C:\Users\Hp\Desktop\test\tes.txt', 'w', encoding="utf-8") as w:
    # w.write(txt)







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


# def email(string):
#     r = int(string[:2], 16)
#     email = ''.join([chr(int(string[i:i+2], 16) ^ r)
#     for i in range(2, len(string), 2)])
#     return email

# print(email('cea6aba2a2a18ea2a7a8baa7bae0a7a0'))



