#Script only for defining the bare flow of the program
import os
import sys
import environment
import loader.main as loader

def module_start():
	environment.debug('Starting module ' + environment.current_module)
	sys.path.append(environment.current_module)
	import sourcing
	loader.load(environment, sourcing)
	del sourcing

def module_stop():
	environment.debug('Stopping module '+environment.current_module)
	sys.path.remove(environment.current_module)

def parse_cli_args():
	#The CLI arguments only provide info for global vars
	for i in sys.argv:
		if i == 'debug':
			environment.debug_enabled = True
		if i == 'help':
			with open(os.path.abspath(__file__)[:-11]+'help.txt') as help_txt:
				for i in help_txt.readlines():
					print(i)
			return True
	return False

def apf_startup():
	environment.debug('Starting ASF')
	if parse_cli_args():
		apf_shutdown()
	for i in os.listdir(environment.cwd):
		if os.path.isdir(i):
			if 'sourcing.py' in os.listdir(i):
				environment.modules.append(os.path.join(environment.cwd, i))
	
	environment.debug('List of all modules that will be analyzed by the auto learner/model maker:')
	for module in environment.modules:
		environment.debug(module)
	environment.debug()
	for module in environment.modules:
		environment.current_module = module
		module_start()
		module_stop()

def apf_shutdown(code=0):
	#Will be properly rewritten later for a graceful shutdown
	environment.debug('ASF shutdown')
	exit(code)
	
if __name__ == '__main__':
	environment.cwd = os.getcwd()
	environment.modules = []
	environment.current_module = ''
	environment.debug_enabled = False
	apf_startup()
	apf_shutdown()