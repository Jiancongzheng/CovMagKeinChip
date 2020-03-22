import sys
from prettytable import PrettyTable
#reload (sys)
#sys.setdefaultencoding('aaa')

def tablePrint(infoList):
    table = PrettyTable(['国家','大洲','确诊','治愈','现存确诊'])
    for country in infoList:
        if 'confirmedCount' in country and 'curedCount' in country:
            table.add_row([country['provinceName'],country['continents'],country['confirmedCount'],country['curedCount'],country['confirmedCount']-country['curedCount']])

    print(table)


