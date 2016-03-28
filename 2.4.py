#!/usr/bin/python

# -*- coding: utf-8 -*-

database = [
	['albert', '1234'],
	['dilber', '4242'],
	['smith', '7524'],
	['jones', '9843']
]

username = raw_input('username:')
password = raw_input('password:')

if [username, password] in database:
	print 'Access granted'
