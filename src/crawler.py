from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from src.utils import click_element, scroll_to_bottom
from src.logger import setup_logger

import time

logger = setup_logger('app.log') 

def get_match_links(driver, url):
    """Lấy danh sách các liên kết trận đấu từ trang chính."""
    driver.get(url)
    logger.info(f"Opening URL: {url}")

    time.sleep(2) 
    click_element(driver, By.CSS_SELECTOR, "div.TA > p")  # Nhấn nút đóng nếu có
    return scroll_to_bottom(driver)

def extract_match_data(driver, link):
    """Lấy dữ liệu chi tiết của một trận đấu."""
    driver.get(link)
    time.sleep(2)

    match_data = {}
    match_data['home_team'] = driver.find_element(By.ID, 'match-detail_team-name_home-link').text
    match_data['away_team'] = driver.find_element(By.ID, 'match-detail_team-name_away-link').text
    score = driver.find_element(By.ID, 'score-or-time').text
    match_data['home_score'], match_data['away_score'] = score.split(" ")[0], score.split(" ")[2]

    try:
        click_element(driver, By.ID, "info")
        content_info = driver.find_element(By.ID, "tab-content-Info")

        try:
            match_data['startTime'] = content_info.find_element(By.CSS_SELECTOR, '[data-testid="match-info-row_root-startTime"]').text
        except NoSuchElementException:
            match_data['startTime'] = None

        try:
            referee_country = content_info.find_element(By.XPATH, '//*[contains(@data-testid, "match-info-row_root-referee__")]').text
            match_data['referee'], ref_citizenship = referee_country.split(" (")
            match_data['ref_citizenship'] = ref_citizenship.rstrip(")")
        except (NoSuchElementException, ValueError):
            match_data['referee'] = match_data['ref_citizenship'] = None

        try:
            match_data['stadium'] = content_info.find_element(By.CSS_SELECTOR, '[data-testid="match-info-row_root-venue"]').text
        except NoSuchElementException:
            match_data['stadium'] = None

        try:
            match_data['spectators'] = content_info.find_element(By.CSS_SELECTOR, '[data-testid="match-info-row_root-spectators"]').text
        except NoSuchElementException:
            match_data['spectators'] = None

        # Lấy thống kê chi tiết của trận đấu
        click_element(driver, By.ID, "statistics")
        content_center = driver.find_element(By.ID, "content-center")

        stats = [
            {"id": "match-detail__statistic__shotsOnTarget", "key": "shots_on_target"},
            {"id": "match-detail__statistic__shotsOffTarget", "key": "shots_off_target"},
            {"id": "match-detail__statistic__shotsBlocked", "key": "shots_blocked"},
            {"id": "match-detail__statistic__possession", "key": "possession"},
            {"id": "match-detail__statistic__corners", "key": "corners"},
            {"id": "match-detail__statistic__offsides", "key": "offsides"},
            {"id": "match-detail__statistic__fouls", "key": "fouls"},
            {"id": "match-detail__statistic__throwIns", "key": "throw_ins"},
            {"id": "match-detail__statistic__yellowCards", "key": "yellow_cards"},
            {"id": "match-detail__statistic__goalkeeperSaves", "key": "goalkeeper_saves"},
            {"id": "match-detail__statistic__goalKicks", "key": "goalKicks"}
        ]

        for stat in stats:
            try:
                element = content_center.find_element(By.ID, stat["id"])
                home_stat = element.find_element(By.CSS_SELECTOR, '[data-testid="match-detail_statistic_home-stat"]').text
                away_stat = element.find_element(By.CSS_SELECTOR, '[data-testid="match-detail_statistic_away-stat"]').text
                match_data[f'home_{stat["key"]}'] = home_stat
                match_data[f'away_{stat["key"]}'] = away_stat
            except NoSuchElementException:
                match_data[f'home_{stat["key"]}'] = match_data[f'away_{stat["key"]}'] = None
                logger.warning(f"Failed to extract statistic {stat['key']}")
        logger.info(f"Match data extracted: {match_data}")
        return match_data
    except Exception as e:
        logger.error(f"Error extracting match data from {link}: {e}")