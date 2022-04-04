from Config import *

class ReadHtml(Variables):
    def __init__(self, firstPageUrl):
        Variables.__init__(self, firstPageUrl)


    def ReadHtmlOnline(self, url) -> str:
        """
        This method is basically using the request module to get the HTML un-pure text
        From the url Provided in the arguments

        The needed arguments are as the following:
            1- URL --> The url of the page you want to read its html. 
        """
        # loop Var
        self.cfBool = True

        # Control Flow
        while self.cfBool:
            try:
                self.pureHtml = REQ.get(url)
                self.cfBool = False
                break
            except (ConnectionAbortedError, ConnectionError) as error:
                print(error)
                print("Connection Error Happened While trying to connect to the website | ReadHml Method")
                self.cfBool = int(input("Please Enter 1 for Continuing the loop (Try again),\n or 0 for ending the loop and go on with the error: "))
            except BaseException as error:
                print(error)
                print("Base Error Happened While trying to connect to the website | ReadHml Method")
                self.cfBool = int(input("Please Enter 1 for Continuing the loop (Try again),\n or 0 for ending the loop and go on with the error: "))
        
        # Return 
        return self.pureHtml

# /////////////////////////////////////NEW Method/////////////////////////////////////////////

    def htmlToText(self, pureHtml):
        """
        This loop is basically working on doing only one jop, which is 
        converting the un-pure read html from the ReadHtmlOnline method
        to text that we can parse / beautify later using Beautifulsoup

        The needed arguments are as the following:
            1- pureHtml --> The Read HTML from the requests module. 
        """
        
        # Loop Var
        self.cfBool = True

        # Control Flow 
        while self.cfBool:
            try:
                self.textHtml = pureHtml.text
                self.cfBool = False
                break
            except BaseException as error:
                print(error)
                print ("Base Error happened while trying to convert the Pure HTML to text | htmlToText Method ")
                self.cfBool = int(input("Please Enter 1 for Continuing the loop (Try again),\n or 0 for ending the loop and go on with the error: "))
        # Return
        return self.textHtml

# /////////////////////////////////////NEW Method/////////////////////////////////////////////

    def DirectHtmlToTextOnline(self, Url):
        """
        This method takes the url of the website and return back the text pure html text directly
        without passing through two methods.

        The needed arguments are as the following:
            1- URL --> The url of the page you want to read its html. 
        """

        # Loop Var
        self.cfBool = True
        while self.cfBool:
            try:
                self.textHtml = self.htmlToText(self.ReadHtmlOnline(Url))
                break
            except (ConnectionAbortedError, ConnectionError) as error:
                print(error)
                print("Connection Error Happened While trying to connect to the website | DirectHtmlToTextOnline Method")
                self.cfBool = int(input("Please Enter 1 for Continuing the loop (Try again),\n or 0 for ending the loop and go on with the error: "))
            except BaseException as error:
                print(error)
                print("Base Error Happened While trying to connect to the website | DirectHtmlToTextOnline Method")
                self.cfBool = int(input("Please Enter 1 for Continuing the loop (Try again),\n or 0 for ending the loop and go on with the error: "))
        
        # Return
        return self.textHtml


# /////////////////////////////////////NEW Method/////////////////////////////////////////////

    def HtmlParser(self, htmlText, readingMode) -> str:
        # Loop Var
        self.cfBool = True

        # Control Flow 
        while self.cfBool:
            try:
                self.parsedHtml = BS(htmlText, readingMode)
                self.cfBool = False
                break
            except BaseException as error:
                print(error)
                print ("Base Error happened while trying to convert the Pure HTML to text | htmlParser Method ")
                self.cfBool = int(input("Please Enter 1 for Continuing the loop (Try again),\n or 0 for ending the loop and go on with the error: "))
        # Return
        return self.parsedHtml

# /////////////////////////////////////NEW Method/////////////////////////////////////////////

    def DirectHtmlParser(self, Url, readingMode):
        """
        This method takes the url of the website and return back the parsed html directly
        without passing through 3 methods.

        The needed arguments are as the following:
            1- URL --> The url of the page you want to read its html. 
            2- readingMode --> reading mode for parsing html using beautiful soup
        """

        # Loop Var
        self.cfBool = True
        while self.cfBool:
            try:
                self.HtmlParser(self.htmlToText(self.ReadHtmlOnline(Url)), readingMode)
                break
            except (ConnectionAbortedError, ConnectionError) as error:
                print(error)
                print("Connection Error Happened While trying to connect to the website | DirectHtmlToTextOnline Method")
                self.cfBool = int(input("Please Enter 1 for Continuing the loop (Try again),\n or 0 for ending the loop and go on with the error: "))
            except BaseException as error:
                print(error)
                print("Base Error Happened While trying to connect to the website | DirectHtmlToTextOnline Method")
                self.cfBool = int(input("Please Enter 1 for Continuing the loop (Try again),\n or 0 for ending the loop and go on with the error: "))
        
        # Return
        return self.parsedHtml