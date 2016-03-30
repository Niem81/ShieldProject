from system.core.controller import *

class Assets(Controller):
    def __init__(self, action):
        super(Assets, self).__init__(action)
        self.load_model('User')
        self.load_model('Asset')
        self.load_model('Claim')

    def description(self):
    	return self.load_view('3.html')
    def add(self):
    	return self.load_view('4.html')
    def add_item(self):
    	return self.load_view('5.html')

