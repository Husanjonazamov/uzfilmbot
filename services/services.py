import requests
from utils.env import BASE_URL


def createUser(user):
    url = f"{BASE_URL}/users/"
    response = requests.post(url, json=user)
    return response.json()

    
    
def getUser(user_id):
    url = f"{BASE_URL}/users/{user_id}"
    try:
        response = requests.get(url)
        if response.status_code == 404: 
            return None
        response.raise_for_status() 
        return response.json() 
    except requests.exceptions.RequestException as e:
        print(f"Error during getUser: {e}")
        return None



def updateDownloadCount(code):
    url = f"{BASE_URL}/download_count/{code}/"
    try:
        response = requests.get(url)
        data = response.json()
        return data
    
    except requests.exceptions.RequestException as e:
        print(f"Error during updateDownloadCount: {e}")


def get_movie_by_code(code: str):
    response = requests.get(f'{BASE_URL}/movies/{code}/')
    if response.status_code == 200:
        movie = response.json()
        return movie
    else:
        print('error')
    return None


def get_episodes_by_series_code(code: str):
    response = requests.get(f'{BASE_URL}/series/{code}/episodes/')
    if response.status_code == 200:
        episodes = response.json().get('episodes', [])
        return episodes
    else:
        print('----')
    return None



def get_seasons_by_movie_code(code: str):
    response = requests.get(f'{BASE_URL}/movies/{code}/seasons/')
    if response.status_code == 200:
        seasons = response.json().get('seasons', [])
        return seasons
    else:
        print('---')
        
    return None



def get_movie_by_list():
    response = requests.get(f'{BASE_URL}/movies_list/')
    if response.status_code == 200:
        movies = response.json()
        return movies
    else:
        print('--')
    return None



def get_category_by_list():
    response = requests.get(f'{BASE_URL}/category_list/')
    if response.status_code == 200:
        movies = response.json()
        return movies
    else:
        print('--')
    return None


def get_movies_by_category(title):
    url = f"{BASE_URL}/movies_category/{title}"
    try:
        response = requests.get(url)
        print(response.status_code)
        if response.status_code == 200:
            movies = response.json() 
            return movies
        else:
            print(f"Error: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"{e}")
    return []


def get_search_movie(query):
    url = f'{BASE_URL}/search/?query={query}'  
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return [] 


def get_season_movies_and_episodes(season_id: str, code: str):
    try:
        response = requests.get(f'{BASE_URL}/seasons/{season_id}/?code={code}')
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            raise Exception(f"Failed to retrieve data, status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")
        return None