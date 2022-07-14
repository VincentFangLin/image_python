import web, hashlib, datetime, re

dbh = web.database(dbn='mysql', db='image_process', user='root', pw='root')


def isUserExists(username, password):
    sql = """
        SELECT user_name, password
        FROM users
        WHERE user_name = $username
    """

    vars = {
        'username':username
    }

    results = dbh.query(sql, vars = vars)

    for record in results:
        if record['user_name'] == username and record['password'] == password:
            print(record)
            print("===================================")
            return True
    else:
        return False