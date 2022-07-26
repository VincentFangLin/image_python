import web
from datetime import datetime
from enum import Enum

dbConn = web.database(dbn='mysql', db='image_process', user='root', pw='root')


#  Duplicate entry   
# transaction ...
def insertPlateValue(position_name,
               chip_index,
               value,
               plate_barcode):

    sql = """
        INSERT  INTO  platevalue (position_name, chip_index, value, plate_barcode, datetime)
        VALUES ( $position_name, $chip_index,  $value,  $plate_barcode,  $datetime ) ON DUPLICATE KEY UPDATE
        position_name = position_name,chip_index=chip_index,plate_barcode=plate_barcode;
    """

    vars = {
        'position_name': position_name,
        'chip_index': chip_index,
        'value': value,
        'plate_barcode': plate_barcode,
        'datetime': datetime.now(),
    }

    plateResult = dbConn.query(sql, vars=vars)


    return plateResult != None
def getPlateValueByBarcode(barcode):

    sql = """
        SELECT * FROM platevalue WHERE plate_barcode = $barcode
    """

    vars = {
        'barcode': barcode
    }

    plateResult = dbConn.query(sql, vars=vars)


    return plateResult 



def isUser(username, password):
    sql = """
        SELECT email, password FROM User WHERE email = $username
        UNION
        SELECT nickname AS email, password FROM User WHERE nickname = $username
    """

    vars = {
        'username': username
    }

    results = dbConn.query(sql, vars=vars)

    for record in results:
        if record['email'] == username and record['password'] == password:
            return True
    else:
        return False
def emailOrNickname(username):
    sql = """
        SELECT email, nickname FROM User WHERE email = $username
        UNION
        SELECT email, nickname FROM User WHERE nickname = $username
    """

    vars = {
        'username': username
    }

    results = dbConn.query(sql, vars=vars)
    email = None
    nickname = None
    for record in results:
        email, nickname = record['email'], record['nickname']
    return email, nickname

def insertUser(email,
               firstname,
               lastname,
               password,
               nickname):

    sql = """
        INSERT  INTO  User (email, first_name, last_name, password, nickname)
        VALUES ( $email, $firstname,  $lastname,  $password,  $nickname );
    """

    vars = {
        'email': email,
        'firstname': firstname,
        'lastname': lastname,
        'password': password,
        'nickname': nickname,
    }

    userResult = dbConn.query(sql, vars=vars)

    sql = """
        INSERT  INTO  UserStatistics (email, number_of_completed_trade_proposer, number_of_completed_trade_counterparty, response_time, number_of_unaccepted_trade_counterparty, user_rank)
        VALUES ( $email, NULL , NULL , NULL , NULL  , 'None');
    """
    vars = {
        'email': email
    }

    statsResult = dbConn.query(sql, vars=vars)

    return (userResult != None) and (statsResult != None)


def emailExists(email):
    sql = """
        SELECT email FROM User WHERE email = $email
    """
    vars = {
        'email': email
    }

    results = dbConn.query(sql, vars=vars)
    return len(results) > 0


def nicknameExists(nickname):
    sql = """
        SELECT nickname FROM User WHERE nickname = $nickname
    """
    vars = {
        'nickname': nickname
    }

    results = dbConn.query(sql, vars=vars)
    return len(results) > 0


def getUserNames(email):
    sql = """
        SELECT
        first_name,
        last_name,
        nickname
        FROM User
        WHERE email = $email;
    """
    vars = {
        'email' : email
    }

    results = dbConn.query(sql, vars = vars)
    for record in results:
        first_name = record['first_name']
        last_name = record['last_name']
        nickname = record['nickname']
    return first_name, last_name, nickname
