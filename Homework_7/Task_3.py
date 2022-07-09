"""Отримати прогноз погоди для Одеси на наступні 5 днів та записати у файл з ім'ям поточної дати"""

import csv
import requests
from requests import Response
from datetime import datetime as dt

city = str(input("Enter city: "))
days = int(input("Enter number of days for forecast: "))
APIkey = "f9ada9efec6a3934dad5f30068fdcbb8"
Weather_url = 'http://api.openweathermap.org/data/2.5/forecast/daily'


def create_file(city: str, days: int) -> str:
    ret = f'{dt.now().strftime("%d.%m.%Y")} {city.capitalize()} {days} days weather forecast.txt'
    return ret.replace(' ', '.')


def get_response_url_in_json(url: str, city, days, APIkey) -> Response:
    params = {'q': city, 'cnt': days, 'units': 'metric', 'appid': APIkey}
    return requests.get(url, params=params).json()


def data_dates(response: Response) -> list:
    result = []
    for date in response['list']:
        result.append(dt.fromtimestamp(date['dt']).strftime("%d.%m.%Y"))
    return result


def temperatures(response: Response, key: str) -> list:
    result = []
    for temp in response['list']:
        result.append(temp['temp'][key])
    return result


def temperatures_data(dates: list, t_days: list, t_nights: list) -> list:
    result = []
    for date, t_day, t_night in zip(dates, t_days, t_nights):
        result.append({"   "'date': date, "    " 'day': t_day, "   "'night': t_night})
    return result


def save_file(name_file: str, data: list):
    with open(name_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, delimiter='\t', fieldnames=data[0])
        writer.writeheader()
        for elem_dict in data:
            writer.writerow(elem_dict)


def main():
    weather_file = create_file(city, days)
    site_response = get_response_url_in_json(Weather_url, city, days, APIkey)
    dates_list = data_dates(site_response)

    temp_days = temperatures(site_response, 'day')
    temp_night = temperatures(site_response, 'night')
    temperatures_info = temperatures_data(dates_list, temp_days, temp_night)

    save_file(weather_file, temperatures_info)


if __name__ == '__main__':
    main()