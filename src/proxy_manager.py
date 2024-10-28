import random

def load_proxies(file_path="config/proxies.txt"):
    with open(file_path, "r") as file:
        proxies = file.read().splitlines()
    return proxies

def get_random_proxy(proxies):
    return random.choice(proxies)
