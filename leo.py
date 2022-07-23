import urllib.request, bs4
web_page = urllib.request.urlopen('http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=13')
result_code = bs4.BeautifulSoup(web_page, 'html.parser')

regional_table = result_code.find('table', class_='num midsize')

# 리스트에 지역, 확진자, 사망자 순서대로 정보 저장


# regional
def regional_case():
    region_case_dict = {}
    for i in range(2, 19):
        rows = regional_table.select_one('tbody > tr:nth-child(' + str(i) + ')')
        region = rows.find('th').text
        case = int(rows.select_one('td:nth-child(5)').text.strip().replace(',', ''))
        region_case_dict[region] = case
    return region_case_dict

def regional_death():
    region_death_dict = {}
    for i in range(2, 19):
        rows = regional_table.select_one('tbody > tr:nth-child(' + str(i) + ')')
        region = rows.find('th').text
        death = int(rows.select_one('td:nth-child(6)').text.strip().replace(',', ''))
        region_death_dict[region] = death
    return region_death_dict