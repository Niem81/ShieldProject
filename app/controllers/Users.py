from system.core.controller import *

class Users(Controller):
	def __init__(self, action):
		super(Users, self).__init__(action)
		self.load_model('User')
		self.load_model('Asset')
		self.load_model('Claim')
	def index(self):
		return self.load_view("index.html")

	def register(self):

		registration = {
		'first_name' : request.form['first_name'],
		'last_name' : request.form['last_name'],
		'email' : request.form['email'],
		'password' : request.form['password'],
		'admin': 1
		}
		print registration
		print "You just registered"
		status = self.models['User'].register_user(registration)
		if status['status'] == True:
			message = "Succesfull registration"
			return jsonify({'status':'OK','user':status['user'],'message':message});
			#return redirect('/')
		else: 
			for message in status['errors']:
				flash(message)
			return redirect('/')
	def login(self):
		user_info = {
			'email' : request.form['email2'],
			'password' : request.form['password2']
		}
		login_status = self.models['User'].login_user(user_info)
		print "got login_status"
		if login_status['status'] == True:
			session['user_id'] = login_status['user']['id']
			session['first_name'] = login_status['user']['first_name']
			return redirect('/users/home')
		else:
			if login_status == False:
				return redirect('/')
	def home(self):
		items = self.models['Asset'].get_all_items_by_id(session['user_id'])
		numb = len(items)
		print numb
		return self.load_view('2.html', items=items, numb=numb)

	def update_plan(self):
		the_plan = {
		'plans_id' : request.form['plan'],
		'user_id' : session['user_id']
		}
		self.models['User'].select_plan(the_plan)
		return redirect('/users/home')
