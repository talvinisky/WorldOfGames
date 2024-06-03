from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import sys

def test_scores_service():
    driver = None
    try:
        # Set Chrome options for headless mode
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920x1080")


        driver = webdriver.Chrome(options=chrome_options)


        driver.get("http://127.0.0.1:8777/")


        score_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "score"))
        ).text
        print(f"Score element text: {score_element}")


        score = int(score_element)
        print(f"Score integer: {score}")


        if 1000 >= score >= 1:
            print("exit code 0")
            sys.exit(0)
            return True
        else:
            print("exit code -1")
            sys.exit(-1)
            return False

    except Exception as e:
        print(f"Error occurred: {e}")
        sys.exit(-1)
        return False
    finally:

        if driver:
            driver.quit()


if __name__ == "__main__":
    print(test_scores_service())
