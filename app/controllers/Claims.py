from system.core.controller import *

class Claims(Controller):
    def __init__(self, action):
        super(Claims, self).__init__(action)
        self.load_model('User')
        self.load_model('Asset')
        self.load_model('Claim')
    def claim(self):
    	return self.load_view('6.html')
