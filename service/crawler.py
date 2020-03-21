#!/usr/bin/env python
# coding: utf-8



from bs4 import BeautifulSoup
from service.name_map import country_name_map, continent_name_map
from service.user_agent import user_agent_list
from requests_html import HTMLSession
import json
import re
from random import choice

class Crawler:
    
    def __init__(self):
        self.session = HTMLSession()
        
    def get_response(self):
        headers = {"User-Agent": choice(user_agent_list)}
        url = 'https://ncov.dxy.cn/ncovh5/view/pneumonia'
        r = self.session.get(url, headers=headers)
        soup = BeautifulSoup(r.content, 'lxml')
        overall_information = re.search(r'(\{"id".*\})\}', str(soup.find('script', attrs={'id': 'getStatisticsService'})))
        abroad_information = re.search(r'\[(.*)\]', str(soup.find('script', attrs={'id': 'getListByCountryTypeService2true'})))

        if overall_information:
            overall_information = self.restructure_overall(overall_information=overall_information)
        
        if abroad_information:
            abroad_information = self.restructure_abroad(abroad_information=abroad_information)
        
        return abroad_information
        
    def restructure_overall(self, overall_information):
        overall_information = json.loads(overall_information.group(1))
        return overall_information
        
    def restructure_abroad(self, abroad_information):
        countries = json.loads(abroad_information.group(0))
        for country in countries:
            delete country['id']
            delete country['createTime']
            delete country['modifyTime']
        return countries
        





