import pymysql
import configure



def addData(name, email, phone, country, date) :
    try :
        connection = pymysql.connect(
            host=configure.host, 
            port=3306,
            user=configure.user,
            password=configure.password,
            database=configure.db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        print('Connected')
        try :
            with connection.cursor() as cursor :
                insert_query = "INSERT INTO `mello.kz_to_moysklad` (name, email, phone, country, date) VALUES (%s,%s,%s,%s,%s);" 
                cursor.execute(insert_query, (name, email, phone, country, date))
                connection.commit()
                print('Данные переданы смотреть таблицу')
        finally:
            connection.close()
    except Exception as ex :
        print("Не подключилось")
        print(ex)
        

def getData() :
    try :
        connection = pymysql.connect(
            host=configure.host, 
            port=3306,
            user=configure.user,
            password=configure.password,
            database=configure.db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        # print('Connected')
        try :
            with connection.cursor() as cursor :
                select_all_rows = "SELECT * FROM `mello.kz_to_moysklad`"
                cursor.execute(select_all_rows)
                rowItems = cursor.fetchall()
        finally:
            connection.close()
    except Exception as ex :
        print("Не подключилось")
        print(ex)
    return rowItems