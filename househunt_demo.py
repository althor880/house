import os
import logging
from househunt import House, Listing, RFAPI
from dotenv import load_dotenv

SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))
CACHE_PATH = os.path.join(SCRIPT_PATH, '.cache')

def SearchForBothellWA():
    rfapi = RFAPI(
        region_ids=[29439]
        , load_listings=True
        , get_zestimates=False
        , cahe_folder = CACHE_PATH)

    matches = []
    for listing in rfapi.listings:
        print(listing.detailed)
        if listing.house.matches_search(beds=2, baths=1.0, sq_ft=900):
            if listing.matches_search(list_price=5000000):
                matches.append(listing)

def load_test_env(env_path="", log=False):
    if env_path == "":
        env_path = os.path.join(SCRIPT_PATH, ".env")
    if os.path.isfile(env_path):
        load_dotenv(env_path)
        if log:
            logging.debug('env={}'.format(os.environ))

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    load_test_env()

    if not os.path.exists(CACHE_PATH):
        os.mkdir(CACHE_PATH)

    SearchForBothellWA()
