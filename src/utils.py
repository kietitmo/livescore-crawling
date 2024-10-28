from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import random
import time

from src.logger import setup_logger

logger = setup_logger('app.log')

def setup_driver(proxy=None, user_agent=None):
    options = webdriver.ChromeOptions()
    
    if proxy:
        options.add_argument(f'--proxy-server={proxy}')
    
    if user_agent:
        options.add_argument(f"user-agent={user_agent}")
    
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])

    options.add_argument("--no-sandbox")   
    options.add_argument("--disable-dev-shm-usage") 
    options.add_argument("--enable-unsafe-swiftshade")
    driver = webdriver.Chrome(options=options)
    
    # Sử dụng Selenium Stealth
    stealth(driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
           )

    return driver

def click_element(driver, by, value, timeout=10):
    """Nhấn vào phần tử nếu có thể nhấp được."""
    try:
        element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, value)))
        element.click()
        logger.info(f"Clicked the close button: {value}")
        time.sleep(random.uniform(2, 4))
    except Exception as e:
        logger.error(f"Failed to click the close button: {e}")

def scroll_to_bottom(driver):
    """Cuộn đến cuối trang và thu thập liên kết các trận đấu."""
    match_links = []
    viewport_height = driver.execute_script("return window.innerHeight")
    scroll_position = 0 

    while True:
        matches = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'zr.Dr')))
        for match in matches:
            match_link = match.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
            if match_link not in match_links:
                match_links.append(match_link)

        scroll_position += viewport_height
        driver.execute_script(f"window.scrollTo(0, {scroll_position});")
        time.sleep(random.uniform(2, 4))

        new_scroll_height = driver.execute_script("return document.body.scrollHeight")
        if scroll_position >= new_scroll_height:
            logger.info("Reached the end of the page.")
            break
    return match_links
