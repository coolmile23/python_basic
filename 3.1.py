#!/usr/bin/python

# -*- coding: utf-8 -*-

width = input('Please input width:')

price_width = 10
item_width = width - price_width

header_format = '%-*s%*s'
formats = '%-*s%*.2f'

print '' * width

print header_format % (item_width, 'Item', price_width, 'Price')
print '-' * width

print formats % (item_width, 'Apples', price_width, 0.4)
print formats % (item_width, 'Pears', price_width, 0.5)
print formats % (item_width, 'Cantaloupes', price_width, 1.92)
print formats % (item_width, 'Dried Apricots (16 oz)', price_width, 8)
print formats % (item_width, 'Prunes (4 lbs)', price_width, 12)
