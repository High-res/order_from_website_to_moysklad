import json
import requests
from datetime import date
import configure as config
import moySklad
import mySql


today = date.today()
day = today.strftime('%Y-%m-%d')
def newKontragents() :
    newKontragents = json.loads(moySklad.getAllKontragentsToday(config.moy_login, config.moy_password, day))

    return newKontragents

def allKontragents() :
    allKontragents = json.loads(moySklad.getAllKontragents(config.moy_login, config.moy_password))

    return allKontragents

def addKontragentIntoMello() :
    if len(mySql.parseMello()) > len(mySql.getData()) :
        print('Добавили в базу контрагента')
        # Здесь идет проверка нет ли в базе новой заявки если нет то записать в базу
        mySql.addData(mySql.parseMello()[-1]['name'], mySql.parseMello()[-1]['email'], mySql.parseMello()[-1]['phone'], mySql.parseMello()[-1]['country'], mySql.parseMello()[-1]['date'])
        # Здесь же создать новую завку на moysklad.ru и отправить ее
    else :
        print('Контрагента в базу не добавили!')

def lastPhone() :
    lastPhone = mySql.getData()[-1]['phone']

    return lastPhone


def dataToMoysklad() :
    dataes = moySklad.addKontragent(mySql.getData()[-1]['name'], mySql.getData()[-1]['email'], mySql.getData()[-1]['phone'], mySql.getData()[-1]['country'])

    return dataes

def createKontragent():
    addKontragentIntoMello()
    # addKontragentIntoMello берет последнего пользователя с заказа сайта 
    # mello.kz  и отправляет в базу данных reg.ru
    # Create Kontragent
    url = 'https://online.moysklad.ru/api/remap/1.2/entity/counterparty'
    


    allForKontr = []
    for i in allKontragents()['rows'] :
        if 'phone' in i :
            allForKontr.append(i['phone'])

    if lastPhone() in allForKontr :
        print('Есть совпадение Здесь 46:')
    else : 
        print('Совпадений нету!')
        r = requests.post(url, data = json.dumps(dataToMoysklad()), auth=(config.moy_login, config.moy_password), headers={'Content-type':'application/json', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.3;Win64;x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'})
        return r
        
def allOrdersToday() :
    allOrdersToday = moySklad.getAllOrders(config.moy_login, config.moy_password, day)

    return allOrdersToday