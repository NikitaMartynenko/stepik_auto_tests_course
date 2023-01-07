import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException
import time
import math

def answer():
    return math.log(int(time.time()))

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1",
                                  "https://stepik.org/lesson/236896/step/1",
                                  "https://stepik.org/lesson/236897/step/1",
                                  "https://stepik.org/lesson/236898/step/1",
                                  "https://stepik.org/lesson/236899/step/1",
                                  "https://stepik.org/lesson/236903/step/1",
                                  "https://stepik.org/lesson/236904/step/1",
                                  "https://stepik.org/lesson/236905/step/1"])

def test_guest_should_see_login_link(browser, link):

    browser.get(link)
    browser.implicitly_wait(10)

    signin = browser.find_element(By.CSS_SELECTOR, "#ember33")
    signin.click()

    emailik = browser.find_element(By.CSS_SELECTOR, "#id_login_email")
    emailik.send_keys("niyoko4@mail.ru")
    password = browser.find_element(By.CSS_SELECTOR, "#id_login_password")
    password.send_keys("naruto44")
    button_sign = browser.find_element(By.CSS_SELECTOR, ".sign-form__btn")
    button_sign.click()

    try:
        time.sleep(1)
        input1 = browser.find_element(By.CSS_SELECTOR, ".textarea")
        time_now = answer()
        input1.send_keys(time_now)

        time.sleep(2)
        but1 = browser.find_element(By.CSS_SELECTOR, ".submit-submission")
        but1.click()

    except (ElementNotInteractableException, NoSuchElementException) as e:
        print(type(e))
        time.sleep(1)
        again_but = browser.find_element(By.CSS_SELECTOR, ".again-btn")
        again_but.click()
        time.sleep(1)
        input1 = browser.find_element(By.CSS_SELECTOR, ".textarea")
        time_now = answer()
        input1.send_keys(time_now)

        time.sleep(2)
        but2 = browser.find_element(By.CSS_SELECTOR, ".submit-submission")
        but2.click()

    feedback = browser.find_element(By.CSS_SELECTOR, "p.smart-hints__hint")
    print(f'feedback = = {feedback.text}')
    assert feedback.text == "Correct!", f"expected 'Correct!', got {feedback.text}"
