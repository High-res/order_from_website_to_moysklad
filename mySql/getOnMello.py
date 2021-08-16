from bs4 import BeautifulSoup
import requests


def getOnMello() :
    r = requests.get('https://mello.kz/db_mello.php')
    messages = r.content
    return messages

def parseMello() :
    # Получаем с сылки данные
    soup = BeautifulSoup(getOnMello(), 'html.parser')
    items = soup.findAll('tr')

    results = []
    for item in items:
        results.append({
            # Делим получаемые данные для записи
            'name' : item.find('td', class_ = 'name').get_text(strip=True),
            'value' : item.find('td', class_ = 'value').get_text(strip=True),
        })

    mello_names = []
    mello_emails = []
    mello_phones = []
    mello_countries = []
    submit_time = []
    to_mysql = []
    for i in range(len(results)):
        # Сохраняем каждую запись в массив
        if results[i]['name'] == 'your-name':
            mello_names.append(results[i]['value'])
        if results[i]['name'] == 'your-email':
            mello_emails.append(results[i]['value'])
        if results[i]['name'] == 'tel-797':
            mello_phones.append(results[i]['value'])
        if results[i]['name'] == 'menu-387':
            mello_countries.append(results[i]['value'])
        if results[i]['name'] == 'submit_time':
            submit_time.append(results[i]['value'])

    # print(allItems[1]['id'])
    for j in range(0, len(mello_names)) :
        # Подготавливаем массив данных для записи в базу
        to_sql = {
            'id' : j+1,
            'name': mello_names[j],
            'email' : mello_emails[j],
            'phone' : mello_phones[j],
            'country' : mello_countries[j],
            'date' : submit_time[j]
        }
        to_mysql.append(to_sql)
    return to_mysql
