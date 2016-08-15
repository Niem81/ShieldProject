from system.core.model import Model

class Claim(Model):
    def __init__(self):
        super(Claim, self).__init__()
    def add_claim(self, new_claim):
        print "Add claim in model"
        print new_claim
        print new_claim['items_selected']
        print new_claim['items_selected'][0]
        print "Insert first the claim"
        query1 = "INSERT INTO claims (claim, created_at, updated_at) values (%s, NOW(), NOW())"
        data1 = [new_claim['claim']]
        self.db.query_db(query1, data1)
        print "Second: get the recent claim and insert into response with the user"
        query_sel = "SELECT id FROM claims ORDER BY id DESC LIMIT 1"
        last_claim_id = self.db.query_db(query_sel)
        print   last_claim_id, last_claim_id[0]
        query2 = "INSERT INTO responses (created_at, updated_at, claim_id, user_id) values (NOW(), NOW(), %s, %s)"
        data2 = [last_claim_id[0]['id'], 8] #session['id']
        self.db.query_db(query2, data2)
        print "Third: once created, get the last response id"
        query_res = "SELECT id FROM responses ORDER BY id DESC LIMIT 1"
        last_resp_id = self.db.query_db(query_res)
        cant = len(new_claim['items_selected'])
        for x in range(0, cant):
            query = "INSERT INTO assets_responses (responses_id, assets_id) values (%s, %s)"
            data = [last_resp_id[0]['id'], new_claim['items_selected'][x]]
            self.db.query_db(query, data)