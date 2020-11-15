import requests
import ntplib
from datetime import datetime


def get_time_if_url_not_work():
    c = ntplib.NTPClient()
    response = c.request('0.ua.pool.ntp.org', version=3)
    t = datetime.fromtimestamp(response.tx_time).time().strftime('%H:%M:%S %p')
    d = datetime.fromtimestamp(response.tx_time).date().strftime('%Y-%m-%d')
    date = {"date": d, "time": t}
    return date


def check_time(d):
    if "time" in d.keys():
        print("Time is: ", d['time'])
    try:
        print("Date is: ", d['date'])
    except KeyError:
        print("No date in response!!!")
        raise KeyError


def main(url=''):
    if not url:
        print("No URL passed to function")
        return False

    try:
        r = requests.get(url=url)
    except requests.exceptions.RequestException as e:
        raise ConnectionError

    if r:
        check_time(r.json())
        home_work(url)
    else:
        check_time(get_time_if_url_not_work())
    return True


def home_work(url=''):
    date = requests.get(url=url).json()['time']
    if isDay(date):
        print("Доброго дня!")
    else:
        print("Доброго вечора!")

def isDay(dateStr):
    return dateStr.find("PM") == -1

def my_good_fun():
    return "success"


def my_good_fun():
    return "Success"


if __name__ == "__main__":
    a = "=" * 40
    print(a + "\nРезультат без параметрів: ")
    main()
    print(a + "\nРезультат з правильною URL: ")
    main('http://date.jsontest.com/')