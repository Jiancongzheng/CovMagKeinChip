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
        headers = {"User-Agent": choice(user_agent_list)}
        url = 'https://ncov.dxy.cn/ncovh5/view/pneumonia'
        r = self.session.get(url, headers=headers)
        self.soup = BeautifulSoup(r.content, 'lxml')
        
    def get_overall(self):
        overall_information = re.search(r'(\{"id".*\})\}', str(self.soup.find('script', attrs={'id': 'getStatisticsService'})))
        if overall_information:
            overall_information = self.__restructure_overall(overall_information=overall_information)
        return overall_information

    def get_abroad(self):
        abroad_information = re.search(r'\[(.*)\]',str(self.soup.find('script', attrs={'id': 'getListByCountryTypeService2true'})))
        if abroad_information:
            abroad_information = self.__restructure_abroad(abroad_information=abroad_information)
        return abroad_information

    def __restructure_overall(self, overall_information):
        overall_information = json.loads(overall_information.group(1))
        return overall_information
        
    def __restructure_abroad(self, abroad_information):
        countries = json.loads(abroad_information.group(0))
        for country in countries:
            try:
                country.pop("incrVo")
            except KeyError:
                pass
            try:
                country.pop("id")
            except KeyError:
                pass
            try:
                country.pop("createTime")
            except KeyError:
                pass
            try:
                country.pop("modifyTime")
            except KeyError:
                pass
            try:
                country.pop("tags")
            except KeyError:
                pass
            try:
                country.pop("provinceShortName")
            except KeyError:
                pass
            try:
                country.pop("provinceId")
            except KeyError:
                pass
            try:
                country.pop("cityName")
            except KeyError:
                pass
            try:
                country.pop("currentConfirmedCount")
            except KeyError:
                pass
            try:
                country.pop("createTime")
            except KeyError:
                pass
            try:
                country.pop("comment")
            except KeyError:
                pass
            try:
                country.pop("sort")
            except KeyError:
                pass
            try:
                country.pop("operator")
            except KeyError:
                pass
            try:
                country.pop("locationId")
            except KeyError:
                pass
            try:
                country.pop("countryShortCode")
            except KeyError:
                pass
            try:
                country.pop("statisticsData")
            except KeyError:
                pass
            try:
                country.pop("countryType")
            except KeyError:
                pass
        return countries
        





