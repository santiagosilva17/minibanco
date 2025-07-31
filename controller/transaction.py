from model.handle_db import HandleTransactions

class Transaction:
    data_transaction = {}
    
    def __init__(self, data_transaction):
        self.db = HandleTransactions()
        self.data_transaction = data_transaction
    
    def create_transaction(self):
        self._add_id_transaction()
        self.db.insert_transaction(self.data_transaction)
        
    def _add_id_transaction(self):
        transaction = self.db.get_all_transactions()
        one_transaction = transaction[-1]
        id_transaction = int(one_transaction[0])
        self.data_transaction["id_transaction"] = str(id_transaction + 1)