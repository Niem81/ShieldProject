from system.core.model import Model

import re
from time import strftime
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class User(Model):
	def __init__(self):
		super(User, self).__init__()

	def register_user(self, users):
		EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
		password = users['password']
		hashed_pw = self.bcrypt.generate_password_hash(password)
		errors= []
		if len(users['password']) < 8:
			errors.append('Password cannot be less than 8 characters.')
		if errors:
			return {'status': False, 'errors': errors}
		else:
			query = 'INSERT INTO users (first_name, last_name, admin, email, password, created_at, updated_at) \
			 VALUES (:first_name, :last_name, :admin, :email, :password, NOW(), NOW())'
			data = {'first_name':users['first_name'],'last_name': users['last_name'] \
			,'admin': users['admin'],'email': users['email'],'password': hashed_pw }
			users = self.db.query_db(query, data)
			get_user = 'SELECT * FROM users order by id DESC LIMIT 1'
			get_user_query = self.db.query_db(get_user)
			return { 'status' : True, 'user': get_user_query[0] }
	def login_user(self, users):
		password = users['password']
		print password, "password 2222222222222222222"
		query = "SELECT * FROM users WHERE email = :user_email"
		user_data = {'user_email':users['email']}
		print user_data, "user_data 33333333333333333"
		users = self.db.query_db(query, user_data)
		errors = []
		print users, "users 44444444444444444"
		if users[0]:
			print "holalalalalal", users[0]
			if self.bcrypt.check_password_hash(users.password, password):
				return {'status': True, 'user': users[0]}
		return {'status' : False}
	def select_plan(self, plan):
		query = "INSERT into users_plans (users_id, plans_id) VALUES (%s,%s)"
		data = [plan['user_id'], plan['plans_id']]
		print query,"!!!!!!!!!!"
		return self.db.query_db(query, data)
