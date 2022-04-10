from Config import *

class Write(Variables):
    def __init__(self, firstPageUrl):
        Variables.__init__(self, firstPageUrl)


# /////////////////////////////////////NEW Method/////////////////////////////////////////////

    def writeFromListofLists(self, ListofLists, dest, filename, sheetName):
        Book = writeWorkbook()
        sheet = Book.active
        sheet.title = sheetName
        if str(dest).endswith("\\"):
            self.filename = f'{filename}.xlsx'
        else:
            self.filename = f'\{filename}.xlsx'

        # List Loop to append
        print('Writing on the sheet')
        x = int()
        for row in ListofLists:
            x+=1
            try:
                sheet.append(row)
            except BaseException as error:
                print('Error while writing a row | writeFromListofLists Methode')
            print(f'Row N.{x} has been written')
        
        Book.save(f'{dest}{self.filename}')
        print('sheet has been written')

        return 

# /////////////////////////////////////NEW Method/////////////////////////////////////////////

    def writeFromListofStrings(self, ListofData, dest, filename, sheetName):
        Book = writeWorkbook()
        sheet = Book.active
        sheet.title = sheetName
        if str(dest).endswith("\\"):
            self.filename = f'{filename}.xlsx'
        else:
            self.filename = f'\{filename}.xlsx'

        # List Loop to append
        print('Writing on the sheet')
        x = int()
        for row in ListofData:
            x+=1
            try:
                sheet.append([row])
            except BaseException as error:
                print('Error while writing a row | writeFromListofStrings Methode')
            print(f'Row N.{x} has been written')
        
        Book.save(f'{dest}{self.filename}')
        print('sheet has been written')
        print('sheet has been written')

        return 

# /////////////////////////////////////NEW Method/////////////////////////////////////////////

