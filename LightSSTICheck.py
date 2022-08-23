#!/usr/bin/env python3

import sys
import requests

class bcolors:
	OK = '\033[92m'
	FAIL = '\033[91m'
	RESET = '\033[0m'	
	INFO = '\033[94m'

def main():
	payloads = ["{{7.7*7.7}}","${7.7*7.7}","<%= 7.7*7.7 %>","${{7.7*7.7}}","#{7.7*7.7}"]
	for line in sys.stdin:
		try:
			params = dict(x.split('=') for x in line.split('&'))
			for payload in payloads:
				for key, value in params.items():
						params[key]=payload
				url = '&'.join('{}={}'.format(key, value) for key, value in params.items())
				rq = requests.get(url)
				if '59.290000000000006' in rq.text:
					print(bcolors.FAIL+"[VULN] "+url+bcolors.RESET)
					if payload == "<%= 7.7*7.7 %>":
						print(bcolors.INFO+"[*] "+"Possible Template found: Mako, Ruby - ERB"+bcolors.RESET)
					elif payload == "{{7.7*7.7}}":
						print(bcolors.INFO+"[*] "+"Possible Template found: Jinjava, Jinja2, Pebble, Twig"+bcolors.RESET)
					elif payload == "${7.7*7.7}":
						print(bcolors.INFO+"[*] "+"Possible Template found: EL, Freemarker, Groovy, Java, Mako"+bcolors.RESET)
					elif payload == "${{7.7*7.7}}":
						print(bcolors.INFO+"[*] "+"Possible Template found: Java"+bcolors.RESET)
					elif payload == "#{7.7*7.7}":
						print(bcolors.INFO+"[*] "+"Possible Template found: EL, Freemarker, Jade/Codepen, Ruby - Slim"+bcolors.RESET)

				else:
					print(bcolors.OK+"[NOT VULN] "+url+bcolors.RESET)
		except KeyboardInterrupt:
			print("Script canceled.")
			sys.exit(0)
		except:
			pass

if __name__ == '__main__':
	try:
		main()
	except Exception as e:
		print("A problem has occured.")
		print("Error info:")
		print(e)
