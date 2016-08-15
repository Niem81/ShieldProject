from system.core.controller import *

class Claims(Controller):
	def __init__(self, action):
		super(Claims, self).__init__(action)
		self.load_model('User')
		self.load_model('Asset')
		self.load_model('Claim')
	def claim(self):
		print "Do claim"
		items = self.models['Asset'].get_all_items_by_id(session['user_id'])
		print items
		return self.load_view('6.html', items=items)
	def add_claim(self):
		print "Start add claim"
		new_claim = {
				   "items_selected": request.form.getlist('items'),
				   "claim": request.form['claim'],
				    "user_id": session['user_id']
				}
		print "got diction"
		# we create a quote with our existing model function
		self.models['Claim'].add_claim(new_claim)
		print "Done inserting claim, response, and assets_responses"
		return redirect('/users/home')