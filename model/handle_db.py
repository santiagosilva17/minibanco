import sqlite3

class HandleUsers:
    def __init__(self) -> None:
        self._con = sqlite3.connect("minibanco.db", check_same_thread=False)
        self._cur = self._con.cursor()
    
    def get_all_users(self):
        data = self._cur.execute("SELECT * FROM users")
        return data.fetchall()

    def get_only_user(self, data_user):
        data = self._cur.execute("SELECT * FROM users WHERE username = '{}'".format(data_user))
        return data.fetchone()
    
    def insert_user(self, data_user):
        self._cur.execute("INSERT INTO users VALUES('{}','{}','{}','{}','{}','{}')".format(
            data_user["id"],
            data_user["firstname"],
            data_user["lastname"],
            data_user["username"],
            data_user["country"],
            data_user["password_user"]
        ))
        self._con.commit()
        
    def __del__(self):
        self._con.close()
    
class HandleAccounts:
    def __init__(self) -> None:
        self._con = sqlite3.connect("minibanco.db", check_same_thread=False)
        self._cur = self._con.cursor()
    
    def get_all_accounts(self):
        data = self._cur.execute("SELECT * FROM accounts")
        return data.fetchall()

    def get_only_account(self, data_account):
        data = self._cur.execute("SELECT * FROM accounts WHERE type_account = '{}'".format(data_account))
        return data.fetchone()
    
    def get_only_money_account(self,type_account):
        data = self._cur.execute("SELECT money_account FROM accounts WHERE type_account = '{}'".format(type_account))
        return data.fetchone()
    
    def insert_account(self, data_account):
        self._cur.execute("INSERT INTO accounts VALUES('{}','{}','{}','{}')".format(
            data_account["id_account"],
            data_account["type_account"],
            data_account["money_account"],
            data_account["password_account"]
        ))
        self._con.commit()
    
    def update_account(self,money_account ,type_account):
        data = self._cur.execute("UPDATE accounts SET money_account = '{}' WHERE type_account = '{}'".format(money_account,type_account))
        self._con.commit()
        return data.fetchone()
    
    def __del__(self):
        self._con.close()
        
class HandleTransactions:
    def __init__(self) -> None:
        self._con = sqlite3.connect("minibanco.db",check_same_thread=False)
        self._cur = self._con.cursor()
    
    def get_all_transactions(self):
        data = self._cur.execute("SELECT * FROM transactions")
        return data.fetchall()

    def get_only_transaction(self, data_transaction):
        data = self._cur.execute("SELECT * FROM transactions WHERE id_transaction = '{}'".format(data_transaction))
        return data.fetchone()
    
    def insert_transaction(self, data_transaction):
        self._cur.execute("INSERT INTO transactions VALUES('{}','{}','{}')".format(
            data_transaction["id_transaction"],
            data_transaction["id_receive"],
            data_transaction["money_transaction"]
        ))
        self._con.commit()
        
    def __del__(self):
        self._con.close()