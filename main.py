import requests
from bs4 import BeautifulSoup

def get_gamepass_list():
    url = "https://www.trueachievements.com/xbox-game-pass/games?page="
    page = 1
    games_names = []

    while(1):
        url_page = url + str(page)
        response = requests.get(url_page)
        soup = BeautifulSoup(response.content, 'html.parser')

        games_td = soup.find_all('td', class_='game')
        
        if len(games_td) == 0:
            break

        games_names.extend([game.text for game in games_td])
        page += 1
        



if __name__ == "__main__":

    get_gamepass_list()