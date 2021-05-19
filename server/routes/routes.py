from lib.server.Server import Server
from threading import Thread
from time import sleep
from src.controllers.controllers import *

time = 30
lock = Lock()
chrono = None

def chrono_decrementor():
    global time
    global chrono
    while 1:
        lock.acquire()
        if time == 0: # Bidding is finished ----- Critical ressource
            lock.release()
            temp = AssetController.checkAvailableAssets()
            if (len(temp) == 1): # Check if the asset exists
                asset = temp[0] # Getting the concerned asset
                try:
                    history = HistoryController.getLastHistoryByAsset(asset) # Getting last bid history of the concerned asset
                    buyer = history.getBuyer() # Getting the involved buyer ie bidder
                    buyer.setBillAmmount(buyer.getBillAmmount()+asset.getLastPrice()*1.2) # Adding charges to the bill
                    asset.setBuyer(buyer) # Affecting the buyer to the asset
                    asset.setState('Vendu') # asset is sold
                    history.setResult('Succes') # the bid is successfull, ie the buyer has bought the asset
                    AssetController.updateAsset(asset)
                    HistoryController.updateHistory(history)
                    BuyerController.updateBuyerData(buyer)
                except:pass
                break
        else:
            lock.release()
            sleep(1)
            lock.acquire()
            time -= 1
            lock.release()
    
chrono = Thread(target=chrono_decrementor)

def broadCast(obj):
    Server.broadcast(obj)

# Routes here

def checkAssetToBuy():
    global chrono
    lock.acquire()
    temp =  AssetController.checkAvailableAssets()
    response = None
    if (len(temp) == 1):
        response = {'asset':temp[0],'current_time':time}
        try:
            if not chrono.is_alive():
                chrono.start()
        except Exception as err:
            chrono = Thread(target=chrono_decrementor)
            chrono.start()
    lock.release()
    
    return response


def bid(request):
    global time
    # Changing the asset last price
    temp =  AssetController.checkAvailableAssets()
    if (len(temp) == 1): # Check if the asset exists
        asset = temp[0]
        asset.setLastPrice(request['proposition']) # Changing asset last price
        buyer = BuyerController.getBuyerById(request['buyer_id'])
        history = History(request['proposition'],'echec',asset,buyer)
        AssetController.updateAsset(asset)
        HistoryController.pushHistory(history)
        # BroadCasting the bid
        lock.acquire()
        time = 30
        obj = {
            'current_time' : time,
            'asset' : asset,
            'buyer_id':request['buyer_id']
        }
        lock.release()
        broadCastThread = Thread(target=broadCast,args=[obj])
        broadCastThread.start()
        

    return None


def buyerData(request):
    return BuyerController.getBuyerById(request['id'])


def pay(request):
    buyer = BuyerController.getBuyerById(request['id'])
    buyer.setBillAmmount(0)
    BuyerController.updateBuyerData(buyer)
    return None 


def getAssets():
    return AssetController.getAll()

def addAsset(request):
    if AssetController.exists(request['ref']):
        raise Exception("Cannot add asset.\nAsset exists already.")
    asset = Asset(
        ref=request['ref'],
        starting_price=request['startingPrice']
    )
    AssetController.add(asset)
    return asset

def getAsset(request):
    if AssetController.exists(request['ref']):
        return AssetController.getAssetByRef(request['ref'])
    raise Exception("Asset not found.")