from Config import *
from ReadHtml import ReadHtml
import pathlib
class GetUrls(ReadHtml):
    def __init__(self, firstPageUrl):
        ReadHtml.__init__(self, firstPageUrl)
        

# /////////////////////////////////////NEW Method/////////////////////////////////////////////

    def GetPagesUrlsFromXlsx(self, fileName, sheetName, row=0):

        """
        This method is used when we have a list in excel sheet of the pages that 
        contains the lists of organizations we want to scrap. It works on reading each row
        of the excel sheet and append it to our local list of 'PagesUrls'.

        The needed Arguments are as the following:
            1- filename --> The name of the excel file without any additions.
            2- sheetName --> 
                - If you want to reach a specific sheet with a specific name
                    you just have to write the 'sheet name' text with no additions
                - If you want to get the current active sheet whatever it is, you 
                    hust have to right 'active' instead of the sheet name.
            3- row --> the column you want to get its data
                - 0 (default) --> A
                - 1 --> B 
                - And so on.
        """

        self.cfBool = True

        while self.cfBool:
            try:
                path = f'{pathlib.Path().resolve()}\\'
                r_workbook = readWorkbook(f'{path}{fileName}.xlsx')
                if (sheetName == 'active') or ('active' in sheetName):
                    r_sheet = r_workbook.active
                else:
                    r_sheet = r_workbook[f'{sheetName}']
                loopCounter = int(1)
                try:
                    for url in r_sheet:
                        self.pagesUrls.append(url[row])
                except BaseException as error:
                    print(error)
                    print('Error Happened while writing the urls on urlsList | GetPagesUrlsFromXlsx Method ')

            except BaseException as error:
                print(error)
                print ("Base Error happened while trying to get the pages Urls | GetPagesUrlsFromXlsx Method ")
                self.cfBool = int(input("Please Enter 1 for Continuing the loop (Try again),\n or 0 for ending the loop and go on with the error: "))
        
        
        return self.pagesUrls


# /////////////////////////////////////NEW Method/////////////////////////////////////////////

    def GetSubPagesUrlsFromXlsx(self, fileName, sheetName, row=0):

        """
        This method is used when we have a list in excel sheet of the subpages that 
        contains the lists of organizations we want to scrap. It works on reading each row
        of the excel sheet and append it to our local list of 'PagesUrls'.

        The needed Arguments are as the following:
            1- filename --> The name of the excel file without any additions.
            2- sheetName --> 
                - If you want to reach a specific sheet with a specific name
                    you just have to write the 'sheet name' text with no additions
                - If you want to get the current active sheet whatever it is, you 
                    hust have to right 'active' instead of the sheet name.
            3- row --> the column you want to get its data
                - 0 (default) --> A
                - 1 --> B 
                - And so on.
        """

        self.cfBool = True

        while self.cfBool:
            try:
                path = f'{pathlib.Path().resolve()}\\'
                r_workbook = readWorkbook(f'{path}{fileName}.xlsx')
                if (sheetName == 'active') or ('active' in sheetName):
                    r_sheet = r_workbook.active
                else:
                    r_sheet = r_workbook[f'{sheetName}']
                loopCounter = int(1)
                try:
                    for url in r_sheet:
                        self.subpages.append(url[row])
                except BaseException as error:
                    print(error)
                    print('Error Happened while writing the urls on urlsList | GetPagesUrlsFromXlsx Method ')

            except BaseException as error:
                print(error)
                print ("Base Error happened while trying to get the pages Urls | GetPagesUrlsFromXlsx Method ")
                self.cfBool = int(input("Please Enter 1 for Continuing the loop (Try again),\n or 0 for ending the loop and go on with the error: "))
        
        
        return self.subpages


# /////////////////////////////////////NEW Method/////////////////////////////////////////////

    def GetPgsUrlsByRGXandList(self, pageKeyword, urlHeader, nOfPages, readingMode = 'html.parser', urlTag = 'a'): 
        
        """
        This method is basically works on getting the urls of the main pages [1, 2, 3, 4, 5, ....>].
        It uses two main ways to do that, the frist one is to get the second half of the urls (in html you 
        only have to right the second half to reach a page inside the website), by the way, it get the second 
        half of the url of the pages by checking the page urls href using regular expressions with the 
        pages urls keywords (or repeated strings) and appending all the matched urls in the list + the page url header
        or first half to make a complete url.

        After that we go to the last page appended in the list and repeat the same things but makes sure that we only
        append the urls that are not in the list already to avoid repetition.

        The needed Arguments are as the following:
            1- pageKeyword --> a string that contains a keyword that makes the pages urls unique to get using regex.
            2- urlHeader --> The first half of the url to make a complete url with the second halfs.
            3- nOfPages --> The number of pages we have in the website, or the number of pages we want to limit in getting
            4- readingMode --> reading mode for parsing html using beautiful soup
            5- urlTag --> The tag that should contain the pages urls, ususally a (deafult = 'a')
        """

        self.cfBool = True

        # firstPageUrl = self.firstPageUrl
        self.pagesUrls.append(self.firstPageUrl)

        while self.cfBool:
            try:
                for page in range(nOfPages-1):
                    # self.HtmlParser(self.htmlToText(self.ReadHtmlOnline(self.pagesUrls[-1]))) #left 
                    self.DirectHtmlParser(self.pagesUrls[-1], readingMode)

                    for link in self.parsedHtml.find_all(urlTag, href = RGX.compile(pageKeyword)):
                        pageUrl = link.get('href')
                        pageUrl = f'{urlHeader}{pageUrl}'
                        if pageUrl not in self.pagesUrls:
                            self.pagesUrls.append(pageUrl)
                            break
                        
                self.cfBool = False
                break
            except BaseException as error:
                print(error)
                print ("Base Error happened while trying to get the main pages Urls | GetPagesUrlsByList Method ")
                self.cfBool = int(input("Please Enter 1 for Continuing the loop (Try again),\n or 0 for ending the loop and go on with the error: "))
        
        return self.pagesUrls

# /////////////////////////////////////NEW Method/////////////////////////////////////////////

    def GetPagsUrlsByIncrement(self, NofPages, IncrementAmount, PageUrl,  IncrementStart, afterUrl=''):

        self.cfBool = True
        
        while self.cfBool:
            try:
                self.PIncrement = int(IncrementStart)
                for p in range(IncrementStart, NofPages):
                    print('Page adding')
                    page = f'{PageUrl}{self.PIncrement}{afterUrl}'
                    self.pagesUrls.append(page)
                    print('Page added')
                    self.PIncrement += IncrementAmount
                    print(f'num = {self.PIncrement}')
                    print()
                self.cfBool = False
                break
            except BaseException as error:
                print(error)
                print ("Base Error happened while Creating pages Urls | GetPgsUrlsByIncrement Method ")
                self.cfBool = int(input("Please Enter 1 for Continuing the loop (Try again),\n or 0 for ending the loop and go on with the error: "))
        
        return self.pagesUrls   

# /////////////////////////////////////NEW Method/////////////////////////////////////////////

    def GetSubPagsUrlsByIncrement(self, NofPages, IncrementAmount, PageUrl, IncrementStart):

        self.cfBool = True
        
        while self.cfBool:
            try:
                self.PIncrement = int(IncrementStart)
                for p in range(NofPages):
                    print('Page adding')
                    page = f'{PageUrl}{self.PIncrement}'
                    self.subpages.append(page)
                    print('Page added')
                    self.PIncrement += IncrementAmount
                    print(f'num = {self.PIncrement}')
                    print()
                self.cfBool = False
                break
            except BaseException as error:
                print(error)
                print ("Base Error happened while Creating pages Urls | GetPgsUrlsByIncrement Method ")
                self.cfBool = int(input("Please Enter 1 for Continuing the loop (Try again),\n or 0 for ending the loop and go on with the error: "))
        
        return self.subpages  

# /////////////////////////////////////NEW Method/////////////////////////////////////////////

    def GetSubPagesUrlsRGXList(self, pagesUrls, hyperlinkKeyword, hyperlinkHeader, containerTag,  readingMode = 'html.parser' , urlTag = 'a'):
        
        """
        This method working in finding the subpges urls from the pages urls/htmls and append it in a list.
        It works as the following:
            - getting all the container tags (parents) with all of its childs (that eliminate possibilities)
            - getting the url tag (usually 'a') from those parents
            - matching it wiyht our aimed tag reg ex
            - put it in a list
        
        The needed Arguments are as the following:
            1- pagesUrls --> list of main pages urls.
            1- hyperlinkKeyword --> a string that contains a keyword that makes the pages urls unique to get using regex.
            2- hyperlinkHeader --> The first half of the url to make a complete url with the second halfs.
            3- containerTag --> The parent tag == str()
            4- readingMode --> reading mode for parsing html using beautiful soup
            5- urlTag --> The tag that should contain the pages urls, ususally a (deafult = 'a')
        """
        
        self.cfBool = True
        
        while self.cfBool:
            try:
                for page in pagesUrls:
                    self.DirectHtmlParser(page, readingMode)
                    for a in self.parsedHtml.find_all(containerTag):
                        for link in a.find_all(urlTag, href = RGX.compile(hyperlinkKeyword)):
                            if link not in self.subpages:
                                secUrl = link.get('href')
                                self.subpages.append(f'{hyperlinkHeader}{secUrl}')
                                print(f'subpage added {len(self.subpages)}')
                                print()
                        
                self.cfBool = False
                break
            except BaseException as error:
                print(error)
                print ("Base Error happened while Getting subpages Urls | GetSubPagesUrls Method ")
                self.cfBool = int(input("Please Enter 1 for Continuing the loop (Try again),\n or 0 for ending the loop and go on with the error: "))
        
        return self.subpages



