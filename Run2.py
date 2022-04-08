from GetData import GetData
# from GetUrls import GetUrls


class Scrap(GetData):
    def __init__(self, firstPageUrl):
        GetData().__init__(self, firstPageUrl)
    

    """
    Here we will write a specific script for each website using the methods we wrote in other classes
    """
