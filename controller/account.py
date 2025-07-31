from model.handle_db import HandleAccounts
from werkzeug.security import generate_password_hash

class Account:
    data_account = {}
    
    def __init__(self, data_account):
        self.db = HandleAccounts()
        self.data_account = data_account
    
    def create_account(self):
        self._add_id_account()
        self._pass_encrypt()
        self.db.insert_account(self.data_account)
        
    def _add_id_account(self):
        account = self.db.get_all_accounts()
        one_account = account[-1]
        id_account = int(one_account[0])
        self.data_account["id_account"] = str(id_account + 1)

    def _pass_encrypt(self):
        self.data_account["password_account"] = generate_password_hash(self.data_account["password_account"], "pbkdf2:sha256:30", 30)