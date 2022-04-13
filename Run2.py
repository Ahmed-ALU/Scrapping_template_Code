import email
from lib2to3.pytree import Base
from unicodedata import category
from GetData import GetData
# from GetUrls import GetUrls
from bs4 import BeautifulSoup as BS
from Config import *
from write import Write


class Scrap(GetData, Write):
    def __init__(self, firstPageUrl):
        self.firstPageUrl = firstPageUrl
        super().__init__(None)
    

    """
    Here we will write a specific script for each website using the methods we wrote in other classes
    """
    def Geoc_jp(self):

        self.GetPagsUrlsByIncrement(69, 20, 'http://www.geoc.jp/rashinban/dantai.php?from=', 0)
        self.GetSubPagesUrlsRGXList(self.pagesUrls, 'dantai_detail', 'http://www.geoc.jp/rashinban/', 'tbody')
        
        # The Source code for scrapping that specific website
        row = int(1)
        for subpage in self.subpages:
            print(f'Org Number {row} is in process')
            self.DirectHtmlParser(subpage, 'html.parser')
            tbodyCounter = int()
            for tbody in self.parsedHtml.find_all('tbody'):
                tbodyCounter+=1
                if tbodyCounter == 2:
                    for Name in tbody.find_all('td')[1]:
                        self.row_list.append(str(Name).encode('latin1').decode('utf-8'))
                    if len(self.row_list)<1:
                        self.row_list.append('Not Found')

                    for type in tbody.find_all('td')[2]:
                        self.row_list.append(str(type).encode('latin1').decode('utf-8'))
                    if len(self.row_list)<2:
                        self.row_list.append('Not Found')

                    for phone in tbody.find_all('td')[4]:
                        self.row_list.append(str(phone).encode('latin1').decode('utf-8'))
                    if len(self.row_list)<3:
                        self.row_list.append('Not Found')

                    for a in tbody.find_all('td')[6]:
                        for mail in BS(str(a), 'html.parser'):
                            self.row_list.append(str(mail.text).encode('latin1').decode('utf-8'))
                    if len(self.row_list)<4:
                        self.row_list.append('Not Found')

                    for a2 in tbody.find_all('td')[7]:
                        for web1 in BS(str(a2), 'html.parser'):
                            self.row_list.append(str(web1.text).encode('latin1').decode('utf-8'))
                    if len(self.row_list)<5:
                        self.row_list.append('Not Found')

                    for a3 in tbody.find_all('td')[8]:
                        for web2 in BS(str(a3), 'html.parser'):
                            self.row_list.append(str(web2.text).encode('latin1').decode('utf-8'))
                    if len(self.row_list)<6:
                        self.row_list.append('Not Found')

                    for a4 in tbody.find_all('td')[9]:
                        for web3 in BS(str(a4), 'html.parser'):
                            self.row_list.append(str(web3.text).encode('latin1').decode('utf-8'))
                    if len(self.row_list)<7:
                        self.row_list.append('Not Found')
                    
                    for a5 in tbody.find_all('td')[10]:
                        for web4 in BS(str(a5), 'html.parser'):
                            self.row_list.append(str(web4.text).encode('latin1').decode('utf-8'))
                    if len(self.row_list)<8:
                        self.row_list.append('Not Found')


            print(f'Org Number {row} has been added')
            row+=1

            for c in range(len(self.row_list)):
                if self.row_list[c] == '' or self.row_list[c] == ' ':
                    self.row_list[c] = 'Not Found'
                print(self.row_list[c])
            print()


            self.collective_list.append(self.row_list)
            self.row_list = list()
            Name, type, phone, mail, a, a2, a3, a4, a5, web1, web2, web3, web4 = '','','','','','','','','','','','',''

        return self.collective_list
            
            

    ####################New Website here############################

    def Arab(self):
        
        catgLinks = dict({
    'advocacy': {
        'civil-rights': 'https://arab.org/directory/activity/civil-rights/',
        'human-rights': 'https://arab.org/directory/activity/human-rights/',
        'labor-rights': 'https://arab.org/directory/activity/labor-rights/',
        'legal-affairs': 'https://arab.org/directory/activity/legal-affairs/',
        'media': 'https://arab.org/directory/activity/media/',
        'peace': 'https://arab.org/directory/activity/peace/',
        'security': 'https://arab.org/directory/activity/security/'
    },

    'animals': {
        'animal-welfare': 'https://arab.org/directory/activity/animal-welfare/',
        'hunting': 'https://arab.org/directory/activity/hunting/',
        'wildlife-conservation': 'https://arab.org/directory/activity/wildlife-conservation/'
    },

    'development': {
        'cultural': 'https://arab.org/directory/activity/cultural/',
        'research': 'https://arab.org/directory/activity/research/',
        'social': 'https://arab.org/directory/activity/social/',
        'sports': 'https://arab.org/directory/activity/sports/',
        'sustainability': 'https://arab.org/directory/activity/sustainability/'
    },

    'education': {
        'education': 'https://arab.org/directory/activity/education/',
        'skills-development': 'https://arab.org/directory/activity/skills-development/'
    },

    'environment': {
        'bio-diversity': 'https://arab.org/directory/activity/bio-diversity/',
        'conservation-protection': 'https://arab.org/directory/activity/conservation-protection/'
    },

    'faith-Based': {
        'beliefs': 'https://arab.org/directory/activity/beliefs/',
        'ethics': 'https://arab.org/directory/activity/ethics/',
        'religious': 'https://arab.org/directory/activity/religious/'
    },

    'finance': {
        'funding': 'https://arab.org/directory/activity/funding/',
        'micro-financing': 'https://arab.org/directory/activity/micro-financing/',
        'trade': 'https://arab.org/directory/activity/trade/'
    },

    'food': {
        'agriculture': 'https://arab.org/directory/activity/agriculture/',
        'food-security': 'https://arab.org/directory/activity/food-security/',
        'hunger': 'https://arab.org/directory/activity/hunger/',
        'nutrition': 'https://arab.org/directory/activity/nutrition/'
    },

    'health': {
        'ageing': 'https://arab.org/directory/activity/ageing/',
        'disabilities': 'https://arab.org/directory/activity/disabilities/',
        'diseases-disorders': 'https://arab.org/directory/activity/diseases-disorders/',
        'medical': 'https://arab.org/directory/activity/medical/',
        'patient-support': 'https://arab.org/directory/activity/patient-support/'
    },

    'people': {
        'children': 'https://arab.org/directory/activity/children/',
        'elderly': 'https://arab.org/directory/activity/elderly/',
        'family': 'https://arab.org/directory/activity/family/',
        'human-settlements': 'https://arab.org/directory/activity/human-settlements/',
        'indigenous-people': 'https://arab.org/directory/activity/indigenous-people/',
        'population': 'https://arab.org/directory/activity/population/',
        'women': 'https://arab.org/directory/activity/women/',
        'youth': 'https://arab.org/directory/activity/youth/'
    },

    'relief': {
        'disaster': 'https://arab.org/directory/activity/disaster/',
        'humanitarian': 'https://arab.org/directory/activity/humanitarian/',
        'refugees': 'https://arab.org/directory/activity/refugees/'
    }


})

        subCatgNums = [363, 505, 76, 191, 147, 150, 96, 42, 14, 78, 648, 445, 927, 39, 433, 860, 739, 79, 181, 21, 30, 103, 105, 105, 139, 90, 54, 28, 39, 16, 157, 116, 222, 241, 560, 34, 192, 60, 89, 236, 414, 683, 51, 169, 132]

        mainCatg = ['advocacy', 'animals', 'development', 'education', 'environment',
                    'faith-Based', 'finance', 'food', 'health', 'people', 'relief']

        subCatg = [['civil-rights', 'human-rights', 'labor-rights', 'legal-affairs', 'media', 'peace', 'security'],
                ['animal-welfare', 'hunting', 'wildlife-conservation'],
                ['cultural', 'research', 'social', 'sports', 'sustainability'],
                ['education', 'skills-development'],
                ['bio-diversity', 'conservation-protection'],
                ['beliefs', 'ethics', 'religious'],
                ['funding', 'micro-financing', 'trade'],
                ['agriculture', 'food-security', 'hunger', 'nutrition'],
                ['ageing', 'disabilities', 'diseases-disorders',
                    'medical', 'patient-support'],
                ['children', 'elderly', 'family', 'human-settlements',
                'indigenous-people', 'population', 'women', 'youth'],
                ['disaster', 'humanitarian', 'refugees']
                ]
        
        
        ###########################################
        # Writing the Subpages on a list
        NofPagesIndex = int()
        catgIndex = int()
        for main in mainCatg:
            
            # The sub Category is list of lists
            if catgIndex == len(mainCatg):
                pass
            elif catgIndex < len(mainCatg):
                catgIndex += 1
            
            for sub in subCatg[catgIndex-1]:
                url = str()

                # Get the first page url
                try:
                    url = catgLinks[main][sub]
                except BaseException as error:
                    print(error)
                    pass
                
                #Add the first url that has no number
                self.subpages.append(url)
                print(f'subpage added | {len(self.subpages)}')

                # Generating the pages number or amount
                if NofPagesIndex == 44:
                    print(catgLinks[main][sub])

                while True:
                    try:
                        num = int((subCatgNums[NofPagesIndex] /5) + 1)
                        break
                    except IndexError as error:
                        print(error)
                        # num -= 1
                
                # Adding the subpages with increment numbers 
                self.GetSubPagsUrlsByIncrement(num, 1, f'{self.subpages[-1]}/page', 2)

                # adding the categories to the lists
                for add in range (num):
                    self.Categories.append(main)
                    self.subCategories.append(sub)

                # To follow up with the pages numbers 
                NofPagesIndex += 1

        ####################################################################
        # Getting the data

        listingNumList = list()
        print(f'{len(self.subpages)} page has been added')

        for subpage in self.subpages[0:4]:

            print('############################')
            print(f"Page {self.subpages.index(subpage)} is being scrapped")
            print(subpage)
            print('############################')
            print ()
            
            self.DirectHtmlParseBlocked(subpage, 'html.parser')
            PageParsedHtml = self.parsedHtml

            for org in RGX.findall('wpbdp\-listing\-\d{3,6}', self.textHtml):
                
                if org not in listingNumList:
                    listingNumList.append(org)
                    for div1 in PageParsedHtml.find_all('div', class_ = org):
                        
                        print('Org is being scrapped')
                        print()
                        # Name storing 
                        for div2 in div1.find_all('div', class_ = 'listing-title'):
                            Name = ''
                            for a in div2.find_all('a'):
                                Name = str(a.text)
                                if len(Name)>1:
                                    self.row_list.append(Name)
                                else: 
                                    self.row_list.append('Not Found')

                        # The rest of the data:
                        for dataContainer in div1.find_all('div', class_ = 'listing-details'):
                            # Here we can loop in the title and the data itself one by one
                            
                            phone, acronym, offName, type, website, sMedia, activity = '', '', '', '', '', '', ''

                            for data in dataContainer.find_all('div', class_='wpbdp-field-display'):
                                

                                # Title of the data is here 
                                for span in data.find_all('span', class_ = 'field-label'):
                                    title = str(span.text).strip()
                                
                                # if condition to catch each type of data
                                if title.startswith("Organization's Official Na"):
                                    for value in data.find_all('div', class_="value"):
                                        for a1 in value.find_all('a'):
                                            offName = str(a1.text).strip()
                                            if len(offName)>1:
                                                self.row_list.append(offName)
                                            else: 
                                                self.row_list.append('Not Found')
                                
                                elif title.startswith("Acrony"):
                                    for value in data.find_all('div', class_="value"):
                                        acronym = str(value.text).strip()
                                        if len(acronym)>1:
                                                self.row_list.append(acronym)
                                        else: 
                                            self.row_list.append('Not Found')
                                
                                elif title.startswith("Typ"):
                                    for value in data.find_all('div', class_="value"):
                                        type = str(value.text).strip()
                                        if len(type)>1:
                                                self.row_list.append(type)
                                        else: 
                                            self.row_list.append('Not Found')

                                elif title.startswith("Activit"):
                                    for value in data.find_all('div', class_="value"):
                                        temp = list()
                                        for a2 in value.find_all('a'):
                                            temp.append(a2.text)
                                        for act in temp:    
                                            activity = activity + f', {act}'.strip()
                                        activity = activity[2:]
                                        temp = list()
                                        if len(activity)>1:
                                            self.row_list.append(activity)
                                        else: 
                                            self.row_list.append('Not Found')
                                
                                elif title.startswith("Phone"):
                                    for value in data.find_all('div', class_="value"):
                                        for a3 in value.find_all('a'):
                                            phone = str(a3.text).strip()
                                            if len(phone)>1:
                                                self.row_list.append(phone)
                                            else: 
                                                self.row_list.append('Not Found')
                                
                                elif title.startswith("Website"):
                                    for value in data.find_all('div', class_="value"):
                                        for a4 in value.find_all('a'):
                                            website = str(a4.get('href')).strip()
                                            if len(website)>1:
                                                self.row_list.append(website)
                                            else: 
                                                self.row_list.append('Not Found')
                                
                                #Getting the email
                                    if len(website) > 8:
                                        try:
                                            emailList = self.GetEmailByRGXMethod(website)
                                            if len(emailList) == 0:
                                                emailList = ['Not Found']
                                                self.emailsListofLists.append(emailList)
                                            elif emailList == self.emailsListofLists[-1]:
                                                emailList = ['Not Found']
                                                self.emailsListofLists.append(emailList)
                                            else:
                                                self.emailsListofLists.append(emailList)
                                                emailList = ['Not Found']
                                        
                                        except BaseException as error:
                                            print(error)
                                            self.emailsListofLists.append(['Error'])
                                            emailList = ['Not Found']
                                    else:
                                        emailList = ['Not Found']
                                        self.emailsListofLists.append(emailList)
                                    
                                    for em in self.emailsListofLists[-1]:
                                        if str(em).startswith('fancybox') or str(em).startswith('wght') or str(em).endswith('png') or str(em).endswith('localhost'):
                                            
                                            indx = list(self.emailsListofLists[-1]).index(em)
                                            self.emailsListofLists[-1][indx] = "Not Found"
                                    
                                    
                                        


                                elif title.startswith("Social"):
                                    for value in data.find_all('div', class_="value"):
                                        for a5 in value.find_all('a'):
                                            sMedia = str(a5.get('href')).strip()
                                            if len(sMedia)>1:
                                                self.row_list.append(sMedia)
                                            else: 
                                                self.row_list.append('Not Found')
                                
                                
                            # print(Name)
                            # print(type)
                            # print(website)
                            # print(sMedia)
                            # print()

                            for c in range(len(self.row_list)):
                                if self.row_list[c] == '' or self.row_list[c] == ' ':
                                    self.row_list[c] = 'Not Found'
                                print(self.row_list[c])
                            print()


                            self.collective_list.append(self.row_list)
                            while len(self.emailsListofLists) < len(self.collective_list):
                                self.emailsListofLists.append(['Not Found'])
                            phone, acronym, offName, type, website, sMedia, activity = '', '', '', '', '', '', ''
                            div1, div2, dataContainer, data, span, a, a1, a2, a3, a4, a5, span, title = '', '', '', '', '', '', '', '', '', '', '', '', ''
                            self.row_list = list()

        # The writing part: ############

        self.writeFromListofStrings(self.Categories, 'W:\ExtraC\Internships\Goodera\Contacts\Arab.org', 'Categories', "catgsData")
        self.writeFromListofStrings(self.subCategories, 'W:\ExtraC\Internships\Goodera\Contacts\Arab.org', 'SubCategories', "subcatgsData")
        self.writeFromListofLists(self.collective_list, 'W:\ExtraC\Internships\Goodera\Contacts\Arab.org', 'ArabOrg', 'Data')
        self.writeFromListofLists(self.emailsListofLists, 'W:\ExtraC\Internships\Goodera\Contacts\Arab.org', 'Emails', 'mails Lists')
    
    #################################################

    def npo_search(self):
        
        def email(string):
            r = int(string[:2], 16)
            email = ''.join([chr(int(string[i:i+2], 16) ^ r)
            for i in range(2, len(string), 2)])
            return email

        """
        It has 104 mainpages

        """
        self.firstPageUrl = 'https://npo-search.com/k-%E7%92%B0%E5%A2%83%E3%81%AE%E4%BF%9D%E5%85%A8/%E6%9D%B1%E4%BA%AC%E9%83%BD/'
        self.pagesUrls.append(self.firstPageUrl)
        self.GetPagsUrlsByIncrement(105, 1, 'https://npo-search.com/k-%E7%92%B0%E5%A2%83%E3%81%AE%E4%BF%9D%E5%85%A8/%E6%9D%B1%E4%BA%AC%E9%83%BD/page', 2, '.html')
        
        #Getting the subpages manually
        row = int(1)
        for page in self.pagesUrls:
            
            print('Getting Pages html --> subpages')
            print()
            self.DirectHtmlParser(page, 'html.parser')
            # Writing thr subpages of each mainpage
            for div in self.parsedHtml.find_all('div', class_ = "panel-heading"):
                for a in div.find_all('a'):
                    link = a.get('href')
                    self.subpages.append(f'https://npo-search.com/{link}')
        
        #Getting the data
        for subpage in self.subpages:
            print(f'Org Number {row} is in process')
            self.DirectHtmlParser(subpage, 'html.parser')

            for table in self.parsedHtml.find_all('table', class_ = 'table table-striped'):
                
                for Name in table.find_all('td')[0]:
                    self.row_list.append(Name[9:])
                if len(self.row_list)<1:
                    self.row_list.append('Not Found')

                for phone in table.find_all('td')[4]:
                    self.row_list.append(phone)  
                if len(self.row_list)<2:
                    self.row_list.append('Not Found')

                for a in table.find_all('td')[6]:
                    if str(a).startswith('<a'):
                        # temp_a = self.HtmlParser(a, 'html.parser')
                        web = a.text
                        self.row_list.append(web) 
                if len(self.row_list)<3:
                    self.row_list.append('Not Found')

                for a2 in table.find_all('td')[7]:
                    # temp_a2 = self.HtmlParser(a2, 'html.parser')
                    if str(a2).startswith('<a'):
                        temp_m = email(a2.get('data-cfemail'))
                        self.row_list.append(temp_m)
                if len(self.row_list)<4:
                    self.row_list.append('Not Found')



            print(f'Org Number {row} has been added')
            print()
            print()
            row+=1

            for c in range(len(self.row_list)):
                if self.row_list[c] == '' or self.row_list[c] == ' ':
                    self.row_list[c] = 'Not Found'
                print(self.row_list[c])
            print()
            
            try:
                if (self.row_list[-1] == 'Not Found' or self.row_list[-1] == '') and (self.row_list[2] != 'Not Found' or self.row_list[1] != ''):
                    self.DirectHtmlToTextOnline(self.row_list[2])
                    m = self.GetEmailByRGXMethod()
                    if len(m)>0:
                        self.row_list.append(m[0])
                    if len(m)>1:
                        self.row_list.append(m[1])
                    if len(m)>2:
                        self.row_list.append(m[2])
            except BaseException as error:
                print(error)
                pass
                    

            # zeros
            self.collective_list.append(self.row_list)
            self.row_list = list()

            Name, phone, a, temp_a, temp_m, web, a2, temp_a2, mail = '','','','','','','','',''
        
        return self.collective_list
    

                


                
                


# obj = Scrap('http://www.geoc.jp/rashinban/dantai.php?from=0')

# obj.writeFromListofLists(obj.Geoc_jp(), 'W:\ExtraC\Internships\Goodera\Contacts\Geoc', 'GeoC', 'data')

# obj2 = Scrap('https://npo-search.com/k-%E7%92%B0%E5%A2%83%E3%81%AE%E4%BF%9D%E5%85%A8/%E6%9D%B1%E4%BA%AC%E9%83%BD/')

# obj2.writeFromListofLists(obj2.npo_search(), r'W:\ExtraC\Internships\Goodera\Contacts\npo_seach', 'NPOsearch', 'data')

obj3 = Scrap('https://arab.org/directory/activity/civil-rights/')
obj3.Arab()