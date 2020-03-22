#!/usr/bin/env python
# coding: utf-8

from service.crawler import Crawler
import service.table as st


crawler = Crawler()
overall_info = crawler.get_overall()
abroad_info = crawler.get_abroad()

'''
print(overall_info)
'''

abroad_info.sort(key=st.active_sort, reverse=True)
st.table_print(info_list=abroad_info)

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
