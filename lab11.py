import requests
import json

API_KEY = "505480d7"
BASE_URL = "http://www.omdbapi.com/"

def search_movies(query):
    params = {
        "apikey": API_KEY,
        "s": query
    }
    try:
        response = requests.get(BASE_URL, params=params)  # формирование URL с параметрами
        if response.status_code == 200:  # обработка ошибок HTTP-запросов
            data = response.json()  # обработка JSON-ответов
            if data.get("Response") == "True":
                for movie in data.get("Search", []):
                    title = movie.get("Title", "N/A")
                    year = movie.get("Year", "N/A")
                    type_ = movie.get("Type", "N/A")
                    print(f"Название: {title}, Год: {year}, Тип: {type_}")  # форматированный вывод
            else:
                print(f"Ошибка поиска: {data.get('Error', 'Неизвестная ошибка')}")
        else:
            print(f"Ошибка соединения с API: {response.status_code}")  # обработка ошибок HTTP-запросов
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def main():
    while True:  # бесконечный цикл для CLI-программы
        query = input("Введите название фильма (или напишите 'выход' чтобы завершить работу): ")
        if query.lower() == "выход":
            print("Завершение работы...")
            break
        search_movies(query)

if __name__ == "__main__":
    main()