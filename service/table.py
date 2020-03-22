import sys
from prettytable import PrettyTable
#reload (sys)
#sys.setdefaultencoding('aaa')


def table_print(info_list):
    table = PrettyTable(['国家', '大洲', '确诊', '治愈', '现存确诊'])
    for country in info_list:
        if 'confirmedCount' in country and 'curedCount' in country:
            table.add_row([country['provinceName'], country['continents'], country['confirmedCount'],
                           country['curedCount'], country['activeCount']])
    print(table)


def confirmed_sort(element):
    return element['confirmedCount']


def cured_sort(element):
    return element['curedCount']


def active_sort(element):
    return element['activeCount']


def continent_sort(element):
    return element['continents']


def country_sort(element):
    return element['provinceName']