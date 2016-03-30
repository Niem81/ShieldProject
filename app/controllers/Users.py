from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        self.load_model('User')
        self.load_model('Asset')
        self.load_model('Claim')
    def index(self):
        return self.load_view('index.html')
    def login(self):
    	return self.load_view('2.html')
    def home(self):
    	return self.load_view('2.html')

