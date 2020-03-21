#!/usr/bin/env python
# coding: utf-8

from service.crawler import Crawler

crawler = Crawler()
overall_info = crawler.get_overall()
abroad_info = crawler.get_abroad()
print('# Active cases: ')
for country in abroad_info:
    if 'confirmedCount' in country and 'curedCount' in country:
        print(country['countryFullName'] + ': ' + str(country['confirmedCount'] - country['curedCount']))
