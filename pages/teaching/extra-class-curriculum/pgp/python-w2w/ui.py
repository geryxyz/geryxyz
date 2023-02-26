import pdb
import colorama

colorama.init()

def annotated(text, icon=''):
	return '[%s] %s' % (icon, text)

def info(text):
	print(annotated(colorama.Fore.CYAN + text + colorama.Fore.RESET, icon='i'))

def warning(text):
	print(annotated(colorama.Fore.YELLOW + text + colorama.Fore.RESET, icon='w'))

def error(text):
	print(annotated(colorama.Fore.RED + text + colorama.Fore.RESET, icon='!'))

def question(text):
	print(annotated(colorama.Fore.GREEN + text + colorama.Fore.RESET, icon='?'))
	print(annotated('', icon=':'), end='')
	return input()

if __name__ == '__main__':
	pdb.set_trace()