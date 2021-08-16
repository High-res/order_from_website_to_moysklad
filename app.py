import requests
import json
import mySql
import configure as config
import moySklad
import actions



def addOrderToMoySklad() :
    actions.createKontragent()
    # createKontragent Создает контрагента в moysklad.ru
    url = 'https://online.moysklad.ru/api/remap/1.2/entity/customerorder'
    newKontrPhone = []
    
    order = ''
    for i in actions.newKontragents()['rows'] :
        print(i['meta']['href'])
        if 'phone' in i :
            print('Phone here!!!')
            newKontrPhone.append(i['phone'])

        if mySql.getData()[-1]['phone'] in newKontrPhone :
            # проверить все заказы на сегодня если в ['agent'] есть совпадение 
            while True :
                order = moySklad.addOrder(i['meta']['href'])
                if i['meta']['href'] in actions.allOrdersToday() :
                    print('Заказ существует!')
                    reAllFunc()
                else :
                    print('Заказа не существует')
                    r = requests.post(url, data = json.dumps(order), auth=(config.moy_login, config.moy_password), headers={'Content-type':'application/json', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.3;Win64;x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'})
                    print(r.text)
                    return r
        else :
            print('Совпадений нету')

def reAllFunc() :
    addOrderToMoySklad()


if __name__ == '__main__' :
    while True:
        addOrderToMoySklad()




# В этом файле понять как работает loop и включить возможно придется использовать aioshedule
# В самом конце очистить базу данных в mello.kz и reg.ru
# Убрать битрикс форму включить в попап CF7
