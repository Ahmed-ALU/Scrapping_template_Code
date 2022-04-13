from black import InvalidInput
from Config import *
from GetUrls import GetUrls

class GetData(GetUrls):
    def __init__(self, firstPageUrl):
        GetUrls.__init__(self, firstPageUrl)
    

    def DataChoices(self):
        
        """
        This method is a simple method, it asks the user which type of data you want to have
        from the choices we have, then it store  the boolean value of each type has been chosen.
        No arguments, run first.... 
        """
        print('DataChoice Started')
        #Loop Variable
        self.cfBool = True

        listOfQuestions = ['Do You want to add Companies Names? ', 'Do You want to add Emails? ', 'Do You want to add Urls? ', 'Do You want to add Phones? ', 'Do You want to add Contacts Names? ']
        qCounter = int()
        for q in listOfQuestions:
            qCounter +=1
            while self.cfBool:
                try:
                    if qCounter == 1:
                        print('please enter 1 or 0')
                        self.getNames = int(input(listOfQuestions[qCounter-1]))
                        if self.getNames == 1 or self.getNames == '1':
                            self.attributesNames = self.AttrSelection()
                        qCounter +=1
                    if qCounter == 2:
                        print('please enter 1 or 0')
                        self.getMailes = int(input(listOfQuestions[qCounter-1]))
                        if self.getMailes == 1 or self.getMailes == '1':
                            self.attributesEmails = self.AttrSelection()
                        qCounter +=1
                    if qCounter == 3:
                        print('please enter 1 or 0')
                        self.getUrls = int(input(listOfQuestions[qCounter-1]))
                        if self.getUrls == 1 or self.getUrls == '1':
                            self.attributesUrls = self.AttrSelection()
                        qCounter +=1
                    if qCounter == 4:
                        print('please enter 1 or 0')
                        self.getPhones = int(input(listOfQuestions[qCounter-1]))
                        if self.getPhones == 1 or self.getPhones == '1':
                            self.attributesPhones = self.AttrSelection()
                    if qCounter == 5:
                        print('please enter 1 or 0')
                        self.getCNames = int(input(listOfQuestions[qCounter-1]))
                        if self.getCNames == 1 or self.getCNames == '1':
                            self.attributesCNames = self.AttrSelection()
                    
                    # break the loop if done
                    self.cfBool = False
                    break
                except ValueError as error:
                    print(error)
                    print("Please enter a number not a character or a set of characters | DataChoices Method")
                    self.cfBool = int(input("Please Enter 1 for Continuing the loop (Try again),\n or 0 for ending the loop and go on with the error: "))
                except BaseException as error:
                    print(error)
                    print("Base Error Happened While getting the imput from the user | DataChoices Method")
                    self.cfBool = int(input("Please Enter 1 for Continuing the loop (Try again),\n or 0 for ending the loop and go on with the error: "))
        
        print('DataChoice Ended')
# /////////////////////////////////////NEW Method/////////////////////////////////////////////

    def AttrSelection(self):

        """
        This method is just for storing the attriputes that the user want to filter his tag with in a variable.
        The arguments are as the following:
            - No arguments needed
        """

        print('AttrSelection Started')

        #Loop Variables
        self.cfBool = True
        
        # empty the attriputes variables
        self.attributes = dict()

        while self.cfBool:
            try:
                print('Please Privide us with the attriputes you want to filter the container tag with')
                print('if you want to enter True, you just type it....')
                try:
                    tempCounter = int(input('How many attriputes you want to add?: ')) 
                except ValueError as error:
                    print(error)
                    print("Value Error Happened, Please enter a number not a character | AttrSelection Method")
                    tempCounter = int(input('How many attriputes you want to add?: ')) 

                tempkey = str()
                tempValue = str()
                for attr in range(tempCounter):
                    tempkey = input(f'Please enter the {attr+1}th attripute name here: ')
                    tempValue = input(f'Please enter the {attr+1}th attripute Value here: ')
                    if tempValue == '1' or tempValue == 1:
                        tempValue = True
                    self.attributes[tempkey] = tempValue

                self.cfBool = False
                break
            except BaseException as error:
                    print(error)
                    print("Base Error Happened While getting attriputes selection | AttrSelection Method")
                    self.cfBool = int(input("Please Enter 1 for Continuing the loop (Try again),\n or 0 for ending the loop and go on with the error: "))
        
        print('AttrSelection Ended')
        print(f'The attributes are: {self.attributes}')

        return self.attributes

# /////////////////////////////////////NEW Method/////////////////////////////////////////////

    def GetNameMethod(self, firstTagContainer, limitValue=1):
        """
        This method is for getting the names from the subpages htmls.
        The arguments needed are as the following:
            -firstTagContainer --> The tag that contains the neme
            -limitValue --> The order of the name in the tags of the same charactaristics ... (Defult = 1)
        """
        print('GetNameMethod Started')

        #Loop Variables
        self.cfBool = True
        while self.cfBool:
            try:
                tempName = list()
                for name in self.parsedHtml.find_all(firstTagContainer, attrs=self.attributesNames, limit = limitValue): #needs to find how to pass those last two
                    tempName.append((name.text).encode('iso-8859-1').decode('utf-8').strip())
                if len(tempName) > 0:
                    self.namesList.append(tempName[int(limitValue)-1]) # Stored as lists
                else:
                    self.namesList.append('No names Found')
                self.cfBool = False
                print(f'name added {len(self.namesList)}')
                print(self.namesList[-1])
                break
            except BaseException as error:
                    print(error)
                    print("Base Error Happened While getting the names | GetNameMethod Method")
                    self.cfBool = int(input("Please Enter 1 for Continuing the loop (Try again),\n or 0 for ending the loop and go on with the error: "))
        
        print('GetNameMethod Ended')
        # print(f'We have {len(self.namesList)} in our names list, lastName = {self.namesList[-1]}')

        return self.namesList
# /////////////////////////////////////NEW Method/////////////////////////////////////////////

    def GetEmailMethod(self, firstTagContainer, slice01=None, slice02=None, limitValue=1):
        """
        This method is for getting the emails from the subpages htmls.
        The arguments needed are as the following:
            -firstTagContainer --> The tag that contains the email
            -Slice01/02 --> for getting specific output from the matches (we have to try to see)
        """

        print('GetEmailMethod Started')

        #Loop Variable
        self.cfBool = True
        while self.cfBool:
            try:
                tempemailLIst = list()
                for a in self.parsedHtml.find_all(firstTagContainer, self.attributesEmails, limit = limitValue)[slice01:slice02]:
                    try:
                        tempemail = a.get('href')
                        if str(tempemail).startswith('mailto'):
                            tempemail = tempemail[7:]
                        else:
                            pass
                        tempemailLIst.append(tempemailLIst) #Stored as lists
                    except (AttributeError, BaseException)as error:
                        print(error)
                        self.emailsList.append('No Emails Found')  
                self.emailsList.append(tempemail)
                print(f'email added {len(self.emailsList)}')
                self.cfBool = False
                break
            except BaseException as error:
                    print(error)
                    print("Base Error Happened While getting the emails | GetEmailMethod Method")
                    self.cfBool = int(input("Please Enter 1 for Continuing the loop (Try again),\n or 0 for ending the loop and go on with the error: "))
        print('GetEmailMethod Ended')
        print(f'We have {len(self.emailsList)} in our names list, lastName = {self.emailsList[-1]}')

        return self.emailsList
# /////////////////////////////////////NEW Method/////////////////////////////////////////////

    def GetEmailByRGXMethod(self, url):
        self.cfBool = True
        while self.cfBool:
            try:
                self.DirectHtmlParser(url, 'html.parser')
                temp_list = list()
                for email in RGX.findall(self.EMAIL_REGEX, self.textHtml):
                    temp_list.append(email)
                    
                if len(temp_list) > 0:
                    print(f"Email added {self.emailCount}") 
                    self.emailCount += 1
                else:
                    print (f"No Emails found  {self.emailCount}")
                    self.emailCount+=1
                    temp_list.append("No Emails found")

                try:
                    self.emailsList.append(temp_list) #Add to the main list # Added as a list 
                except TypeError:
                    temp_list.append("Error Addin Email")
                    self.emailsList.append(temp_list) #Add to the main list
                    
                print(f'email added {len(self.emailsList)}')
                self.cfBool = False
                break
            except BaseException as error:
                    print(error)
                    print("Base Error Happened While getting the emails | GetEmailsByRGXMethod Method")
                    self.cfBool = int(input("Please Enter 1 for Continuing the loop (Try again),\n or 0 for ending the loop and go on with the error: "))
            
        return temp_list

# /////////////////////////////////////NEW Method/////////////////////////////////////////////

    def GetphoneByRGXMethod(self):
        self.cfBool = True
        while self.cfBool:
            try:
                temp_list = list()
                for email in RGX.findall(self.PHONE_REGEX, self.textHtml):
                    temp_list.append(email)
                    
                if len(temp_list) > 0:
                    print(f"Phone added {self.emailCount}") 
                    self.emailCount += 1
                else:
                    print (f"No Phone found  {self.emailCount}")
                    self.emailCount+=1
                    temp_list.append("No Phone found")

                try:
                    self.emailsList.append(temp_list) #Add to the main list
                except TypeError:
                    temp_list.append("Error Adding Phone")
                    self.emailsList.append(temp_list) #Add to the main list

                self.cfBool = False
                break
            except BaseException as error:
                    print(error)
                    print("Base Error Happened While getting the emails | GetphoneByRGXMethod Method")
                    self.cfBool = int(input("Please Enter 1 for Continuing the loop (Try again),\n or 0 for ending the loop and go on with the error: "))

# /////////////////////////////////////NEW Method/////////////////////////////////////////////

 
