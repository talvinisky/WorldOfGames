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

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep


def test_scores_service(app_url):
    driver = webdriver.Remote(
        command_executor='http://selenium-hub:4444/wd/hub',
        desired_capabilities=DesiredCapabilities.CHROME
    )

    try:
        driver.get(app_url)
        elem = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "score")))
        score = int(elem.text)
        sleep(2)
        driver.quit()
        return True if 1 <= score <= 1000 else False
    except Exception as ex:
        print(ex.args[0])
        driver.quit()
        return False


def main_function():
    result = test_scores_service('http://web:5000')
    if result:
        return 0
    return -1


if __name__ == '__main__':
    res = main_function()
    print(res)