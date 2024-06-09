import requests

# URL для получения списка пивоваренных заводов
url = "https://api.openbrewerydb.org/breweries"

# Отправляем GET-запрос к API
response = requests.get(url)

# Проверяем успешность запроса
if response.status_code == 200:
    # Получаем данные в формате JSON
    data = response.json()
    
    # Выводим информацию о первых 5 пивоваренных заводах
    for brewery in data[:5]:
        print(f"Название: {brewery['name']}")
        print(f"Тип: {brewery['brewery_type']}")
        print(f"Адрес: {brewery['street']}, {brewery['city']}, {brewery['state']} {brewery['postal_code']}")
        print("--------------------")
else:
    print("Ошибка при получении данных с сервера")
