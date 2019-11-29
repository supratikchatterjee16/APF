#Module becomes a serving point for files within the environment

def identify_mime(extension):
	pass#start here

class Sourcing:
	def __init__(self):
		self.root = ''
		self.data_files = []
		self.data_info = []#Classifiers and load orders go here
		self.extensions = []
		self.filetype = []
	
	def identify_data_files(self):
		for i in self.data_files:
			extn = i[i.rfind('.') + 1 : ]
			self.extensions.append(extn)
		for i in self.extensions:
			self.filetype.append(identify_mime(i))
	
	def load(self, environment, sourcing):
		datapath = environment.current_module + sourcing.data_root
		self.data_files = sourcing.data
		self.identify_data_files()
	

sys.modules[__name__] = Sourcing()