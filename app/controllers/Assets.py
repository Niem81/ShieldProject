from system.core.controller import *

class Assets(Controller):
    def __init__(self, action):
        super(Assets, self).__init__(action)
        self.load_model('User')
        self.load_model('Asset')
        self.load_model('Claim')
    def description(self):
        return self.load_view('3.html')
    def add_view(self):
        items = self.models['Asset'].get_all_items_by_id(session['user_id'])
        return self.load_view('4.html', items=items)
    def add(self):
        # the form data is still accessed in the same way as when we normally submitted the form
        # $(this).serialize() helped us send this info over to this url
        print "Insert values"
        new_asset = {
                   "asset_name": request.form['product_name'],
                   "asset_id": request.form['product_id'],
                   "desc": request.form['product_desc'],
                   "value": request.form['product_price'],
                   "quantity": request.form['quantity'],
                   "user_id": session['user_id']
                }
        print "got diction"
        # we create a quote with our existing model function
        self.models['Asset'].add(new_asset)
        print "got or"
        # we then retrieve the updated list of items from the database which will include our new quote
        items = self.models['Asset'].get_all_items_by_id(session['user_id']) #session['id']
        print "got item"
        print items
        # finally we will respond to the AJAX request with a partial that will use the items
        # retreived from the database to generate the appropriate html
        return self.load_view('partials/items.html', items=items)
    def add_plan_view(self):
        
        return self.load_view('5.html')
