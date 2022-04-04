from GetData import GetData

def ChoicedLoop(readingMode='html.parser'):
        
        """
        This method is just for initilizing the methods of getting the specific data
        that has been chosen by the user.
        
        The arguments are as the following:
            - The methods to get each data type as shown in the code below...
        """
        
        print('ChoicedLoop Started')

        Geoc_jp.cfBool = True
        while Geoc_jp.cfBool:
            try:
                for subpage in Geoc_jp.subpages:
                    # Parse it and request it one time here
                    Geoc_jp.DirectHtmlParser(subpage, readingMode)
                    # Geoc_jp.parsedHtml = Geoc_jp.HtmlParser(Geoc_jp.htmlToText(Geoc_jp.ReadHtmlOnline(subpage)))
                    # ---------
                    Geoc_jp.currentSubpage = subpage
                    # Names Method is called here
                    if Geoc_jp.getNames:
                        Geoc_jp.GetNameMethod('td', 1)
                    #Emails Mthod is called Here
                    if Geoc_jp.getMailes:
                        Geoc_jp.GetEmailByRGXMethod()
                    #Urls Mthod is called Here
                    if Geoc_jp.getUrls:
                        pass
                        # Geoc_jp.
                    #Phones Mthod is called Here
                    if Geoc_jp.getPhones:
                        Geoc_jp.GetphoneByRGXMethod
                    #ContactName Mthod is called Here
                    if Geoc_jp.getCNames:
                        pass
                        # Geoc_jp.
                Geoc_jp.cfBool = False
                break
            except BaseException as error:
                    print(error)
                    print("Base Error Happened While getting the imput from the user | ChoicedLoop Method")
                    Geoc_jp.cfBool = int(input("Please Enter 1 for Continuing the loop (Try again),\n or 0 for ending the loop and go on with the error: "))

        print('ChoicedLoop Ended')

# /////////////////////////////////////NEW Method/////////////////////////////////////////////

Geoc_jp = GetData('http://www.geoc.jp/rashinban/dantai.php?from=0')

Geoc_jp.DirectHtmlParser(Geoc_jp.firstPageUrl, 'html.parser')

Geoc_jp.GetPgsUrlsByRGXandList("from=", 'http://www.geoc.jp/rashinban/', 1, 'html.parser', 'a')

Geoc_jp.GetSubPagesUrls(Geoc_jp.pagesUrls, 'dantai_detail', 'http://www.geoc.jp/rashinban/', 'td')

Geoc_jp.DataChoices()

ChoicedLoop()


# Geoc_jp.AllInOne()

# with open('emails.txt', 'a') as w:
#     for email in Geoc_jp.emailsList:
#         w.write(f'{email}\n')

for name in Geoc_jp.namesList:
    print(f'{name}\n')




