from system.core.model import Model

class Asset(Model):
    def __init__(self):
        super(Asset, self).__init__()
    def add(self, new_asset):
        print "Add in model"
        query = "INSERT INTO assets (asset_name, asset_id, description, value, quantity, created_at, updated_at, user_id) VALUES (%s, %s, %s, %s, %s, NOW(),NOW(), %s)"
        print "past query"
        data = [new_asset['asset_name'], new_asset['asset_id'], new_asset['desc'], new_asset['value'], new_asset['quantity'], new_asset['user_id']]
        print data
        return self.db.query_db(query, data)
    def get_all_items_by_id(self, id):
        print "Getting item by id"
        query = "SELECT * FROM assets where user_id = %s"
        # htmlTxt.encode('ascii', 'ignore')
        data = [id]
        return self.db.query_db(query, data)