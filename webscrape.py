import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

baseUrl = "https://www.euroleaguebasketball.net/"

def getTeams():
    baseUrl = "https://www.euroleaguebasketball.net/"
    #headers = {
    #'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    #}
    r = requests.get('https://www.euroleaguebasketball.net/en/euroleague/teams/')
    soup = BeautifulSoup(r.content, 'lxml')
    teamlist = soup.find_all('ul', class_='teams-list_list__VcpE5')
    teamlinks = []
    for item in teamlist:
        for link in item.find_all('a', href=True):
            teamlinks.append(baseUrl + link['href'])
    return teamlinks

def getTeamStatsLink(teamlink):
    r = requests.get(f'{teamlink}')
    soup = BeautifulSoup(r.content, 'lxml')
    teamstatslink = soup.find_all('a', class_='page-subnavigation_link__X1cny')
    team_stats_link = teamstatslink[3]['href']
    return team_stats_link

#def getTeamPlayerStats(team_page):
#    r = requests.get(f'{team_page}')
#    soup = BeautifulSoup(r.content, 'lxml')
#    playerStats = soup.find_all('div', class_='complex-stat-table_row__XPRhI')
#    return playerStats

#team_stats_links = []

#for item in getTeams():
#    team_stats_links.append(baseUrl + getTeamStatsLink(f'{item}'))

#print(team_stats_links[17])
#print(getTeamPlayerStats(team_stats_links[17]))

url = 'https://www.euroleaguebasketball.net/en/euroleague/teams/paris-basketball/statistics/prs/?season=2024-25&phase=All%20phases'

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("user-data-dir=C:/Users/Martynas/AppData/Local/Google/Chrome/User Data")
options.add_argument("profile-directory=Default")
driver = webdriver.Chrome(options=options)

driver.get(url)
print("Waiting")
WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, 'complex-stat-table_row__XPRhI'))
)
print("Finished waiting")
teamstats = driver.find_elements(By.CLASS_NAME, 'complex-stat-table_row__XPRhI')
print(teamstats[0].text)
print(len(teamstats))
for stats in teamstats:
    print(stats.text)
    print("---")
index = 2
stats_list = []
for stats in teamstats:
    num_in_team = stats.find_element(By.XPATH, f'//*[@id="main"]/div/div[2]/div/div/div[2]/div[1]/div[3]/div[2]/div/div/div/div/div[{index}]/div[1]').text
    player_name = stats.find_element(By.XPATH, f'//*[@id="main"]/div/div[2]/div/div/div[2]/div[1]/div[3]/div[2]/div/div/div/div/div[{index}]/div[2]/a/span[2]').text
    games_played = stats.find_element(By.XPATH , f'//*[@id="main"]/div/div[2]/div/div/div[2]/div[1]/div[3]/div[2]/div/div/div/div/div[{index}]/div[3]').text
    games_started = stats.find_element(By.XPATH, f'//*[@id="main"]/div/div[2]/div/div/div[2]/div[1]/div[3]/div[2]/div/div/div/div/div[{index}]/div[4]').text
    minutes_played = stats.find_element(By.XPATH, f'//*[@id="main"]/div/div[2]/div/div/div[2]/div[1]/div[3]/div[2]/div/div/div/div/div[{index}]/div[5]').text
    points = stats.find_element(By.XPATH, f'//*[@id="main"]/div/div[2]/div/div/div[2]/div[1]/div[3]/div[2]/div/div/div/div/div[{index}]/div[6]').text
    two_point_percentage = stats.find_element(By.XPATH, f'//*[@id="main"]/div/div[2]/div/div/div[2]/div[1]/div[3]/div[2]/div/div/div/div/div[{index}]/div[7]').text
    three_point_percentage = stats.find_element(By.XPATH, f'//*[@id="main"]/div/div[2]/div/div/div[2]/div[1]/div[3]/div[2]/div/div/div/div/div[{index}]/div[8]').text
    free_throw_percentage = stats.find_element(By.XPATH, f'//*[@id="main"]/div/div[2]/div/div/div[2]/div[1]/div[3]/div[2]/div/div/div/div/div[{index}]/div[9]').text
    offensive_rebounds = stats.find_element(By.XPATH, f'//*[@id="main"]/div/div[2]/div/div/div[2]/div[1]/div[3]/div[2]/div/div/div/div/div[{index}]/div[10]').text
    defensive_rebounds = stats.find_element(By.XPATH, f'//*[@id="main"]/div/div[2]/div/div/div[2]/div[1]/div[3]/div[2]/div/div/div/div/div[{index}]/div[11]').text
    total_rebounds = stats.find_element(By.XPATH, f'//*[@id="main"]/div/div[2]/div/div/div[2]/div[1]/div[3]/div[2]/div/div/div/div/div[{index}]/div[12]').text
    assists = stats.find_element(By.XPATH, f'//*[@id="main"]/div/div[2]/div/div/div[2]/div[1]/div[3]/div[2]/div/div/div/div/div[{index}]/div[13]').text
    steals = stats.find_element(By.XPATH, f'//*[@id="main"]/div/div[2]/div/div/div[2]/div[1]/div[3]/div[2]/div/div/div/div/div[{index}]/div[14]').text
    turnover = stats.find_element(By.XPATH, f'//*[@id="main"]/div/div[2]/div/div/div[2]/div[1]/div[3]/div[2]/div/div/div/div/div[{index}]/div[15]').text
    blocks = stats.find_element(By.XPATH, f'//*[@id="main"]/div/div[2]/div/div/div[2]/div[1]/div[3]/div[2]/div/div/div/div/div[{index}]/div[16]').text
    blocks_against = stats.find_element(By.XPATH, f'//*[@id="main"]/div/div[2]/div/div/div[2]/div[1]/div[3]/div[2]/div/div/div/div/div[{index}]/div[17]').text
    fouls_commited = stats.find_element(By.XPATH, f'//*[@id="main"]/div/div[2]/div/div/div[2]/div[1]/div[3]/div[2]/div/div/div/div/div[{index}]/div[18]').text
    fouls_received = stats.find_element(By.XPATH, f'//*[@id="main"]/div/div[2]/div/div/div[2]/div[1]/div[3]/div[2]/div/div/div/div/div[{index}]/div[19]').text
    performance_index_rating = stats.find_element(By.XPATH, f'//*[@id="main"]/div/div[2]/div/div/div[2]/div[1]/div[3]/div[2]/div/div/div/div/div[{index}]/div[20]').text
    
    team_stats = {
        'num_in_team': num_in_team,
        'player_name': player_name,
        'games_played': games_played,
        'games_started': games_started,
        'minutes_played': minutes_played,
        'points': points,
        'two_point_percentage': two_point_percentage,
        'three_point_percentage': three_point_percentage,
        'free_throw_percentage': free_throw_percentage,
        'offensive_rebounds': offensive_rebounds,
        'defensive_rebounds': defensive_rebounds,
        'total_rebounds': total_rebounds,
        'assists': assists,
        'steals': steals,
        'turnover': turnover,
        'blocks': blocks,
        'blocks_against': blocks_against,
        'fouls_commited': fouls_commited,
        'fouls_received': fouls_received,
        'performance_index_rating': performance_index_rating,
    }
    stats_list.append(team_stats)
    if index == 10: break
    index += 1
    '''
    print(num_in_team, player_name, games_played, games_started, minutes_played, points, two_point_percentage, three_point_percentage, free_throw_percentage, offensive_rebounds, defensive_rebounds, total_rebounds, assists, steals, turnover, blocks, blocks_against)
    print(index-1)
    '''
df = pd.DataFrame(stats_list)
print(df)
df.to_csv('first_output.csv', index=False)

# print(get_team_stats_link('https://www.euroleaguebasketball.net/euroleague/teams/anadolu-efes-istanbul/roster/ist/?season=2024-25'))




# API FOR TEAM PLAYERS: https://feeds.incrowdsports.com/provider/euroleague-feeds/v2/competitions/E/seasons/E2024/clubs/zal/people/stats
# API FOR INDIVIDUAL WHOLE TEAM STATS: https://feeds.incrowdsports.com/provider/euroleague-feeds/v2/competitions/E/seasons/E2024/clubs/zal/stats
# API FOR PLAYER: https://www.euroleaguebasketball.net/_next/data/p2JiwrcWFdKcXIXG1EnUh/en/euroleague/players/lonnie-walker-iv/<007975>.json?name=lonnie-walker-iv&id=<007975>