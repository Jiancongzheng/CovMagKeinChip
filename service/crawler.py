#!/usr/bin/env python
# coding: utf-8

# In[5]:


from bs4 import BeautifulSoup
from service.name_map import country_name_map, continent_name_map
from service.user_agent import user_agent_list
from requests_html import HTMLSession
import json
import re
from random import choice


# In[12]:


class Crawler:
    
    def __init__(self):
        self.session = HTMLSession()
        
    def get_response(self):
        headers = {"User-Agent": choice(user_agent_list)}
        url = 'https://ncov.dxy.cn/ncovh5/view/pneumonia'
        r = self.session.get(url, headers=headers)
        soup = BeautifulSoup(r.content, 'lxml')
        overall_information = re.search(r'(\{"id".*\})\}', str(soup.find('script', attrs={'id': 'getStatisticsService'})))
        '''re: 正则表达式模块'''
        if overall_information:
            self.restructure_overall(overall_information=overall_information)
        overall_information
        
    def restructure_overall(self, overall_information):
        overall_information = json.loads(overall_information.group(1))
        overall_information.pop('id')
        overall_information.pop('createTime')
        overall_information.pop('modifyTime')
        overall_information.pop('imgUrl')
        overall_information.pop('deleted')
        overall_information['countRemark'] = overall_information['countRemark'].replace(' 疑似', '，疑似').replace(' 治愈', '，治愈').replace(' 死亡', '，死亡').replace(' ', '')
        


# In[ ]:




