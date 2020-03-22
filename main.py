#!/usr/bin/env python
# coding: utf-8

from service.crawler import Crawler
from service.table import tablePrint


crawler = Crawler()
overall_info = crawler.get_overall()
abroad_info = crawler.get_abroad()

'''
print(overall_info)
'''

def confirmedSort(element):
    return (element['confirmedCount'])


print(abroad_info)
abroad_info.sort(key=confirmedSort,reverse=True)
print(abroad_info)

tablePrint(infoList=abroad_info)

"""
print('# Active cases: ')

for country in abroad_info:
    if 'confirmedCount' in country and 'curedCount' in country:
        print(country['countryFullName'] + ': ' + str(country['confirmedCount'] - country['curedCount']))

for key, val in overall_info.items():
    if key != 'globalStatistics':
        print(key + ': ' + val)

print('Global Statistics:')
for key, val in overall_info['globalStatistics'].items():
    print(key + ': ' + str(val))

"""
