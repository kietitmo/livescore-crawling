from src.crawler import extract_match_data, get_match_links
from src.data_processor import *
from src.utils import setup_driver, setup_logger
from src.user_agent_manager import load_user_agents

logger = setup_logger('app.log') 
user_agents = load_user_agents()

def main():
    driver = setup_driver(user_agent=user_agents[1])
    url = "https://www.livescore.com/en/football/england/premier-league/results/"
    
    match_links = get_match_links(driver, url)
    save_data_to_json(match_links, 'output/match_links.json')
    logger.info(f"Total matches found: {len(match_links)}")

    match_data_list = []
    for link in match_links:
        logger.info(f"Extracting link: {link}")
        match_data = extract_match_data(driver, link)
        match_data_list.append(match_data)

    save_data_to_json(match_data_list, 'output/matchs_data.json')
    save_data_to_csv(match_data_list, 'output/matchs_data.csv')
    driver.quit()

if __name__ == "__main__":
    main()
