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

            'relief': {
                'disaster': 'https://arab.org/directory/activity/disaster/',
                'humanitarian': 'https://arab.org/directory/activity/humanitarian/',
                'refugees': 'https://arab.org/directory/activity/refugees/'
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
            }

        })

        mainCatg = ['advocacy', 'animals', 'development', 'education', 'environment',
                    'faith-Based', 'finance', 'food', 'health', 'relief', 'people']

        subCatg = [['civil-rights', 'human-rights', 'labor-rights', 'legal-affairs', 'media', 'peace', 'security'],
                ['animal-welfare', 'hunting', 'wildlife-conservation'],
                ['cultural', 'research', 'social', 'sports', 'sustainability'],
                ['skills-development'],
                ['bio-diversity', 'conservation-protection'],
                ['beliefs', 'ethics', 'religious'],
                ['funding', 'micro-financing', 'trade'],
                ['agriculture', 'food-security', 'hunger', 'nutrition'],
                ['ageing', 'disabilities', 'diseases-disorders',
                    'medical', 'patient-support'],
                ['disaster', 'humanitarian', 'refugees'],
                ['children', 'elderly', 'family', 'human-settlements',
                'indigenous-people', 'population', 'women', 'youth']
                ]


    
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
            
            if (self.row_list[-1] == 'Not Found' or self.row_list[-1] == '') and (self.row_list[2] != 'Not Found' or self.row_list[1] != ''):
                self.DirectHtmlToTextOnline(self.row_list[2])
                m = self.GetEmailByRGXMethod()
                if len(m)>0:
                    self.row_list.append(m[0])
                if len(m)>1:
                    self.row_list.append(m[1])
                if len(m)>2:
                    self.row_list.append(m[2])
                

            # zeros
            self.collective_list.append(self.row_list)
            self.row_list = list()

            Name, phone, a, temp_a, temp_m, web, a2, temp_a2, mail = '','','','','','','','',''
        
        return self.collective_list
    

                


                
                


obj = Scrap('http://www.geoc.jp/rashinban/dantai.php?from=0')

obj.writeFromListofLists(obj.Geoc_jp(), 'W:\ExtraC\Internships\Goodera\Contacts\Geoc', 'GeoC', 'data')

# obj2 = Scrap('https://npo-search.com/k-%E7%92%B0%E5%A2%83%E3%81%AE%E4%BF%9D%E5%85%A8/%E6%9D%B1%E4%BA%AC%E9%83%BD/')

# obj2.writeFromListofLists(obj2.npo_search(), r'W:\ExtraC\Internships\Goodera\Contacts\npo_seach', 'NPOsearch', 'data')
