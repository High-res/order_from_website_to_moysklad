import requests


# Создание контрагента
def addKontragent(name, email, phone, country) :
    kontragent = {
        'name': name,
        'description': 'Новый пользователь с сайта mello.kz',
        'email': email,
        'phone': phone,
        'actualAddress': country,
        'legalTitle': country,
        'legalAddress': country,
        'state' : {
            'meta' : {
                'href' : 'https://online.moysklad.ru/api/remap/1.2/entity/customerorder/metadata/states/0ba51f6e-fa60-11eb-0a80-047000016723',
                'metadataHref' : 'https://online.moysklad.ru/api/remap/1.2/entity/customerorder/metadata',
                'type' : 'state',
                'mediaType' : 'application/json'
            }
        },
        'priceType': {
            'meta': {
                'href': 'https://online.moysklad.ru/api/remap/1.2/context/companysettings/pricetype/be1a74c4-d114-11e7-7a69-8f550005cfa4',
                'type': 'pricetype',
                'mediaType': 'application/json'
            }
        },
        'attributes' : [ {
            'meta' : {
                'href' : 'https://online.moysklad.ru/api/remap/1.2/entity/counterparty/metadata/attributes/9178fe6e-2880-11ea-0a80-00d6000feee1',
                'type' : 'attributemetadata',
                'mediaType' : 'application/json'
            },
            'id' : '9178fe6e-2880-11ea-0a80-00d6000feee1',
            'name' : 'Система оплаты',
            'type' : 'customentity',
            'value' : {
                'meta' : {
                'href' : 'https://online.moysklad.ru/api/remap/1.2/entity/customentity/d424d75e-287f-11ea-0a80-015d0010190d/6c0b7c88-2880-11ea-0a80-015d00102b75',
                'metadataHref' : 'https://online.moysklad.ru/api/remap/1.2/context/companysettings/metadata/customEntities/d424d75e-287f-11ea-0a80-015d0010190d',
                'type' : 'customentity',
                'mediaType' : 'application/json',
                'uuidHref' : 'https://online.moysklad.ru/app/#custom_d424d75e-287f-11ea-0a80-015d0010190d/edit?id=6c0b7c88-2880-11ea-0a80-015d00102b75'
                },
                'name' : 'Наличные'
            }
        } ],
    }
    return kontragent

def getAllKontragents(login, password) :
    url = f'https://online.moysklad.ru/api/remap/1.2/entity/counterparty'
    # url = f'https://online.moysklad.ru/api/remap/1.2/entity/counterparty?expand=state&filter=created>{month}'

    r = requests.get(url, auth=(login, password))
    # print(r.headers)
    return r.text


def getAllKontragentsToday(login, password, day) :
    url = f'https://online.moysklad.ru/api/remap/1.2/entity/counterparty?expand=state&filter=created>{day}'
    r = requests.get(url, auth=(login, password))

    return r.text


def getAllOrders(login, password, day) : 
    url = ("https://online.moysklad.ru/api/remap/1.2/entity/customerorder?expand=state&filter=moment>=" + day)
    r = requests.get(url, auth=(login, password))
    
    return r.text


def addOrder(contragent) :
    order = {
        # 'name': '000034',
            'owner': {
              'meta': {
                'href': 'https://online.moysklad.ru/api/remap/1.2/entity/employee/be0b92d1-d114-11e7-7a69-8f550005cf75',
                'metadataHref': 'https://online.moysklad.ru/api/remap/1.2/entity/employee/metadata',
                'type': 'employee',
                'mediaType': 'application/json'
              }
            },
            'group': {
              'meta': {
                'href': 'https://online.moysklad.ru/api/remap/1.2/entity/group/bdf529e4-d114-11e7-7a69-971100001c2d',
                'metadataHref': 'https://online.moysklad.ru/api/remap/1.2/entity/group/metadata',
                'type': 'group',
                'mediaType': 'application/json'
              }
            },
            'organization': {
              'meta': {
                'href': 'https://online.moysklad.ru/api/remap/1.2/entity/organization/be16f0a1-d114-11e7-7a69-8f550005cf9c',
                'type': 'organization',
                'mediaType': 'application/json'
              }
            },
            'agent': {
              'meta': {
                'href': contragent,
                'type': 'counterparty',
                'mediaType': 'application/json'
              }
            },
            'state': {
              'meta': {
                'href': 'https://online.moysklad.ru/api/remap/1.2/entity/customerorder/metadata/states/0ba51f6e-fa60-11eb-0a80-047000016723',
                'type': 'state',
                'mediaType': 'application/json'
              }
            }
    }
    return order