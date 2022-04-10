import openpyxl as OPX
from openpyxl import load_workbook as readWorkbook
from openpyxl import Workbook as writeWorkbook
import re as RGX
import requests as REQ
from bs4 import BeautifulSoup as BS


class Variables():
    
    def __init__(self, firstPageUrl):
        # ReadHtml.__init__(self, firstPageUrl)
        # GetUrls.__init__(self, firstPageUrl)
        # GetData.__init__(self, firstPageUrl)
        self.EMAIL_REGEX = r"[\w\.-]+@[\w\.-]+"
        self.PHONE_REGEX = r"[\d]{2,4}-[\d]{2,4}-[\d]{2,4}"
        self.emailPattern = RGX.compile(self.EMAIL_REGEX)
        self.cfBool = True
        self.tagsList = list()
        self.row_list = list()
        self.collective_list = list()
        self.PIncrement = int(0)
        self.filename = str()
        self.pureHtml = None
        self.textHtml = None
        self.parsedHtml = None
        self.firstPageUrl = firstPageUrl
        self.pagesUrls = list()
        self.subpages = list()
        self.namesList = list()
        self.emailsList = list()
        self.phonesList = list()
        self.urlsList = list()
        #GetData Survey Here
        self.getNames = False
        self.getMailes = False
        self.getUrls = False
        self.getPhones = False
        self.getCNames = False
        self.currentSubpage = None
        self.emailCount = int(0)
        self.attributes = dict()
        self.attributesNames = dict()
        self.attributesEmails = dict()
        self.attributesUrls = dict()
        self.attributesPhones = dict()
        self.attributesCNames = dict()


