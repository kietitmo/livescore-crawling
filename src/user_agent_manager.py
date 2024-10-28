import random

def load_user_agents(file_path="config/user_agents.txt"):
    with open(file_path, "r") as file:
        user_agents = file.read().splitlines()
    return user_agents

def get_random_user_agent(user_agents):
    return random.choice(user_agents)
