import requests
import json
import logging
import time

logging.basicConfig(
    filename="server.log",
    filemode='a',
    level=logging.INFO,
    format='{levelname} {asctime} {name} : {message}',
    style='{'
)
log = logging.getLogger(__name__)


def main(url):
    while True:
        try:
            r = requests.get(url)
            data = json.loads(r.content)
            logging.info("Server is available. Server time: %s", data['date'])
            logging.info("Requested page: : %s", data['current_page'])
            logging.info("Server response keys:")
            for key in data.keys():
                logging.info("Key: %s, Value: %s", key, data[key])
        except requests.exceptions.ConnectionError:
            logging.error("Server is unavailable :(")

        time.sleep(60)

if __name__ == '__main__':
    main("http://localhost:8000/health")