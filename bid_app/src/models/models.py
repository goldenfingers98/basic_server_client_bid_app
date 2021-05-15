from datetime import datetime

class Buyer:
    def __init__(self,id):
        self.__id = id
        self.__bill_ammount = 0

    def getId(self):
        return self.__id

    def getBillAmmount(self):
        return self.__bill_ammount

    def setId(self,id):
        self.__id = id

    def setBillAmmount(self,ammount):
        self.__bill_ammount = ammount

    def __str__(self):
        return f'{self.__id}\t{self.__bill_ammount}\n'

    __slots__ = {'__id':int,'__bill_ammount':int}

class asset:
    def __init__(self,ref,starting_price):
        self.__ref = ref
        self.__starting_price = starting_price
        self.__last_price = starting_price
        self.__state = 'Vendu'
        self.__buyer = None

    def getRef(self):
        return self.__ref

    def getStartingPrice(self):
        return self.__starting_price

    def getLastPrice(self):
        return self.__last_price

    def getState(self):
        return self.__state

    def setRef(self,ref):
        self.__ref = ref

    def setStartingPrice(self,price):
        self.__starting_price = price
    
    def setLastPrice(self,price):
        self.__last_price = price

    def setState(self,state):
        self.__state = state
    
    def setBuyer(self,buyer):
        self.__buyer = buyer

    def __str__(self):
        return f'{self.__ref}\t{self.__starting_price}\t{self.__last_price}\t{self.__state}\t{self.__buyer}\n'

class history:
    def __init__(self,proposal,result,asset,buyer):
        self.__date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.__proposal = proposal
        self.__result = result
        self.__asset = asset
        self.__buyer = buyer

    def getDate(self):
        return self.__date

    def getProposal(self):
        return self.__proposal

    def getResult(self):
        return self.__result

    def getAsset(self):
        return self.__asset

    def getBuyer(self):
        return self.__buyer

    def setDate(self,date):
        self.__date = date

    def setProposal(self,proposal):
        self.__proposal = proposal

    def setResult(self,result):
        self.__result = result

    def setAsset(self,asset):
        self.__asset = asset

    def setBuyer(self,nuyer):
        self.__buyer = Buyer

    def __str__(self):
        return f'{self.__date}\t{self.__buyer.getId()}\t{self.__proposal}\t{self.__result}\n'
