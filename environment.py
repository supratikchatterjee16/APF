#define parameters and common shared functions
#The environment gets passed around, for state maintenance and information passing
import sys
import collections

class Environment(collections.MutableMapping):
	def __init__(self, *args, **kwargs):
		self.__dict__.update(*args, **kwargs)
		self['store'] = {}
		self['cwd'] = ''
		self['modules'] = []
		self['current_module'] = ''
		self['debug_enabled'] = False
	def __setitem__(self, key, value):
		self.__dict__[key] = value
	def __getitem__(self, key):
		return self.__dict__[key]
	def __delitem__(self, key):
		del self.__dict__[key]
	def __iter__(self):
		return iter(self.__dict__)
	def __len__(self):
		return len(self.__dict__)
	def __str__(self):
		return str(self.__dict__)
	def __repr__(self):
		return '{}, D({})'.format(super(D, self).__repr__(), self.__dict__)
	def debug(self, msg=''):
		if self.debug_enabled:
			print(msg)
	def refresh(self):
		pass

sys.modules[__name__] = Environment()#Makes the class the representation of the module