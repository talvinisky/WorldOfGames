# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import sys
#
# def test_scores_service():
#     driver = None
#     try:
#         # Initialize the WebDriver instance without specifying the path
#         driver = webdriver.Chrome()
#
#         # Navigate to the URL
#         driver.get("http://127.0.0.1:8777/")
#
#         # Wait for the score element to be visible and get its text
#         score_element = WebDriverWait(driver, 10).until(
#             EC.visibility_of_element_located((By.ID, "score"))
#         ).text
#         print(f"Score element text: {score_element}")  # Debugging statement
#
#         # Convert the score text to an integer
#         score = int(score_element)
#         print(f"Score integer: {score}")  # Debugging statement
#
#         # Check if the score is between 1 and 1000
#         if 1000 >= score >= 1:
#             print("exit code 0")
#             sys.exit(0)  # Exit with code 0
#             return True
#         else:
#             print("exit code -1")
#             sys.exit(-1)  # Exit with code -1
#             return False
#
#     except Exception as e:
#         print(f"Error occurred: {e}")
#         sys.exit(-1)  # Exit with code -1
#         return False
#     finally:
#         # Close the WebDriver instance
#         if driver:
#             driver.quit()
#
# # Test function
# if __name__ == "__main__":
#     print(test_scores_service())
#
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

        # Initialize the WebDriver instance with Chrome options
        driver = webdriver.Chrome(options=chrome_options)

        # Navigate to the URL
        driver.get("http://127.0.0.1:8777/")

        # Wait for the score element to be visible and get its text
        score_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "score"))
        ).text
        print(f"Score element text: {score_element}")  # Debugging statement

        # Convert the score text to an integer
        score = int(score_element)
        print(f"Score integer: {score}")  # Debugging statement

        # Check if the score is between 1 and 1000
        if 1000 >= score >= 1:
            print("exit code 0")
            sys.exit(0)  # Exit with code 0
            return True
        else:
            print("exit code -1")
            sys.exit(-1)  # Exit with code -1
            return False

    except Exception as e:
        print(f"Error occurred: {e}")
        sys.exit(-1)  # Exit with code -1
        return False
    finally:
        # Close the WebDriver instance
        if driver:
            driver.quit()

# Test function
if __name__ == "__main__":
    print(test_scores_service())
