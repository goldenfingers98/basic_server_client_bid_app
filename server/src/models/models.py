from lib.entity.Entity import Entity
from datetime import datetime
        

class Buyer(Entity):
    FILE = "facture.txt"
    HEADERS = ["Identificateur Acheteur","Somme à payer"]
    def __init__(self,id=-1):
        super().__init__()
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

    __slot__ = {
        '__id':{
            'type':int,
            'getter':'getId',
            'setter':'setId'
        },
        '__bill_ammount':{
            'type':float,
            'getter':'getBillAmmount',
            'setter':'setBillAmmount'
        },
    }

class Asset(Entity):
    FILE = "bien.txt"
    HEADERS = ["Référence Objet","Prix Départ","Dernier Prix","Etat","Acheteur"]
    __next_ref = 0
    def __init__(self,ref=-1,buyer=None,starting_price=0):
        super().__init__()
        if ref == -1:
            self.__ref = Asset.__next_ref
            Asset.__next_ref += 1
        else:
            self.__ref = ref
        self.__starting_price = starting_price
        self.__last_price = starting_price
        self.__state = 'Disponible'
        self.__buyer = buyer

    def getRef(self):
        return self.__ref

    def getStartingPrice(self):
        return self.__starting_price

    def getLastPrice(self):
        return self.__last_price

    def getState(self):
        return self.__state

    def getBuyer(self):
        return self.__buyer

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
        if self.__buyer is None:
            return f'{self.__ref}\t{self.__starting_price}\t{self.__last_price}\t{self.__state}\t{self.__buyer}\n'
        return f'{self.__ref}\t{self.__starting_price}\t{self.__last_price}\t{self.__state}\t{self.__buyer.getId()}\n'

    __slot__ = {
        '__ref':{
            'type':int,
            'getter':'getRef',
            'setter':'setRef'
        },
        '__starting_price':{
            'type':float,
            'getter':'getStartingPrice',
            'setter':'setStartingPrice'
        },
        '__last_price':{
            'type':float,
            'getter':'getLastPrice',
            'setter':'setLastPrice'
        },
        '__state':{
            'type':str,
            'getter':'getState',
            'setter':'setState'
        },
        '__state':{
            'type':str,
            'getter':'getState',
            'setter':'setState'
        },
        '__buyer':{
            'type':Buyer,
            'getter':'getBuyer',
            'setter':'setBuyer'
        }
    }

class History(Entity):
    FILE = "historique.txt"
    HEADERS = ["Identificateur Acheteur","Bien","Proposition Valeur","Résultat"]
    def __init__(self,proposal=0,result='echec',asset=None,buyer=None):
        super().__init__()
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

    def setBuyer(self,buyer):
        self.__buyer = buyer

    def __str__(self):
        return f'{self.__date}\t{self.__buyer.getId()}\t{self.__asset.getRef()}\t{self.__proposal}\t{self.__result}\n'

    __slot__ = {
        '__date':{
            'type':datetime,
            'getter':'getDate',
            'setter':'setDate'
        },
        '__buyer':{
            'type':Buyer,
            'getter':'getBuyer',
            'setter':'setBuyer'
        },
        '__asset':{
            'type':Asset,
            'getter':'getAsset',
            'setter':'setAsset'
        },
        '__proposal':{
            'type':float,
            'getter':'getProposal',
            'setter':'setProposal'
        },
        '__result':{
            'type':str,
            'getter':'getResult',
            'setter':'setResult'
        }
    }
