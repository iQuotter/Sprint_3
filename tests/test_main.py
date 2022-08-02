import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


from GenerateUser import User


class TestStellarBurgers:
    FirstName, Email, Password = User().generation_of_user_data()

    def __wait_element(self, driver, xpath_element):
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located((By.XPATH, xpath_element)))

    # @pytest.mark.skip()
    def test_registration(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")

        located_name, located_email  = driver.find_elements(By.XPATH, ".//input[(@name='name')]")
        located_password = driver.find_element(By.XPATH, ".//input[@name='Пароль']")
        located_reg_button = driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']")

        user_name = TestStellarBurgers.FirstName
        email_value = TestStellarBurgers.Email
        password_value = TestStellarBurgers.Password

        located_name.send_keys(user_name)
        located_email.send_keys(email_value)
        located_password.send_keys(password_value)
        located_reg_button.click()
        time.sleep(1)

        if driver.current_url == "https://stellarburgers.nomoreparties.site/login":
            located_email = driver.find_element(By.XPATH, ".//input[(@name='name')]")
            located_password = driver.find_element(By.XPATH, ".//input[@name='Пароль']")
            located_enter_button = driver.find_element(By.XPATH, "//button[text()='Войти']")

            located_email.send_keys(email_value)
            located_password.send_keys(password_value)
            located_enter_button.click()

        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
        time.sleep(1)
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/account/profile"
        assert driver.find_element(By.XPATH, f".//input[(@value='{email_value.lower()}')]").is_displayed()

        self.__wait_element(driver, ".//button[text()='Выход']")
        time.sleep(1)
        driver.find_element(By.XPATH, ".//button[text()='Выход']").click()
        time.sleep(1)

    # @pytest.mark.skip()
    def test_field_password_lower_6(self, driver):
        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
        if driver.current_url != "https://stellarburgers.nomoreparties.site/login":
            time.sleep(1)
            self.__wait_element(driver, ".//button[text()='Выход']")
            time.sleep(1)
            driver.find_element(By.XPATH, ".//button[text()='Выход']").click()
            time.sleep(1)
            driver.get("https://stellarburgers.nomoreparties.site/login")

        time.sleep(2)

        located_email = driver.find_element(By.XPATH, ".//input[(@name='name')]")
        located_password = driver.find_element(By.XPATH, ".//input[(@name='Пароль')]")

        located_password.send_keys("12345")
        time.sleep(1)
        located_email.click()
        time.sleep(1)

        self.__wait_element(driver, ".//p[text()='Некорректный пароль']")
        assert driver.find_element(By.XPATH, ".//p[text()='Некорректный пароль']").is_displayed()

    # @pytest.mark.skip()
    def test_authorization_button_personal_account(self, driver):
        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()

        located_email = driver.find_element(By.XPATH, ".//input[(@name='name')]")
        located_password = driver.find_element(By.XPATH, ".//input[(@name='Пароль')]")
        located_enter_button = driver.find_element(By.XPATH, ".//*[text()='Войти']")

        email_value = 'EvgeniyGrekov231@mail.ru'
        password_value = '123456'

        located_email.send_keys(email_value)
        located_password.send_keys(password_value)
        located_enter_button.click()

        time.sleep(1)

        driver.find_element(By.XPATH, "//p[text()='Личный Кабинет']").click()

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/account" \
               or driver.current_url == "https://stellarburgers.nomoreparties.site/account/profile"

    # @pytest.mark.skip()
    def test_exit_accout(self, driver):
        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
        time.sleep(1)
        if driver.current_url == "https://stellarburgers.nomoreparties.site/login":
            located_email = driver.find_element(By.XPATH, ".//input[(@name='name')]")
            time.sleep(1)
            located_password = driver.find_element(By.XPATH, ".//input[(@name='Пароль')]")
            time.sleep(1)
            located_enter_button = driver.find_element(By.XPATH, ".//*[text()='Войти']")
            time.sleep(1)

            email_value = 'EvgeniyGrekov231@mail.ru'
            password_value = '123456'

            located_email.send_keys(email_value)
            time.sleep(1)
            located_password.send_keys(password_value)
            time.sleep(1)
            located_enter_button.click()
            time.sleep(1)

        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
        time.sleep(1)

        driver.find_element(By.XPATH, ".//button[text()='Выход']").click()
        time.sleep(1)

        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
        assert driver.current_url != "https://stellarburgers.nomoreparties.site/account/profile"

    # @pytest.mark.skip()
    def test_authorization_button_login(self, driver):
        time.sleep(1)
        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
        time.sleep(1)
        if driver.current_url == "https://stellarburgers.nomoreparties.site/account/profile":
            time.sleep(1)
            self.__wait_element(driver, ".//button[text()='Выход']")
            time.sleep(1)
            driver.find_element(By.XPATH, ".//button[text()='Выход']").click()
            time.sleep(1)
        else:
            time.sleep(1)
            driver.get("https://stellarburgers.nomoreparties.site/")
            time.sleep(1)

        driver.find_element(By.XPATH, ".//button[contains(text(),'Войти')]").click()
        time.sleep(1)

        located_email = driver.find_element(By.XPATH, ".//input[(@name='name')]")
        time.sleep(1)
        located_password = driver.find_element(By.XPATH, ".//input[@name='Пароль']")
        time.sleep(1)
        located_enter_button = driver.find_element(By.XPATH, ".//*[text()='Войти']")
        time.sleep(1)

        email_value = 'EvgeniyGrekov231@mail.ru'
        password_value = '123456'

        located_email.send_keys(email_value)
        time.sleep(1)
        located_password.send_keys(password_value)
        time.sleep(1)
        located_enter_button.click()
        time.sleep(1)

        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
        time.sleep(2)
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/account" \
               or driver.current_url == "https://stellarburgers.nomoreparties.site/account/profile"
        assert driver.find_element(By.XPATH, ".//button[text()='Выход']").is_displayed()

    # @pytest.mark.skip()
    def test_authorization_in_menu_password_recovery(self, driver):
        time.sleep(1)
        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
        time.sleep(1)
        if driver.current_url == "https://stellarburgers.nomoreparties.site/account/profile":
            time.sleep(1)
            self.__wait_element(driver, ".//button[text()='Выход']")
            time.sleep(1)
            driver.find_element(By.XPATH, ".//button[text()='Выход']").click()
            time.sleep(1)
            driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
            time.sleep(1)
        else:
            driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
            time.sleep(1)

        self.__wait_element(driver, ".//*[text()='Войти']")
        time.sleep(1)
        located_enter = driver.find_element(By.XPATH, ".//*[text()='Войти']")
        time.sleep(1)
        driver.execute_script("arguments[0].scrollIntoView();", located_enter)
        time.sleep(1)

        driver.find_element(By.XPATH, ".//*[text()='Войти']").click()
        time.sleep(1)

        located_email = driver.find_element(By.XPATH, ".//input[(@name='name')]")
        time.sleep(1)
        located_password = driver.find_element(By.XPATH, ".//input[(@name='Пароль')]")
        time.sleep(1)
        located_enter_button = driver.find_element(By.XPATH, ".//*[text()='Войти']")
        time.sleep(1)

        email_value = 'EvgeniyGrekov231@mail.ru'
        password_value = '123456'

        located_email.send_keys(email_value)
        time.sleep(1)
        located_password.send_keys(password_value)
        time.sleep(1)
        located_enter_button.click()
        time.sleep(1)

        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
        time.sleep(2)
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/account" \
               or driver.current_url == "https://stellarburgers.nomoreparties.site/account/profile"
        assert driver.find_element(By.XPATH, ".//button[text()='Выход']").is_displayed()

    # @pytest.mark.skip()
    def test_authorization_menu_registration(self, driver):
        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
        if driver.current_url == "https://stellarburgers.nomoreparties.site/account/profile":
            self.__wait_element(driver, ".//button[text()='Выход']")
            driver.find_element(By.XPATH, ".//button[text()='Выход']").click()
            time.sleep(1)
            driver.get("https://stellarburgers.nomoreparties.site/register")
        else:
            driver.get("https://stellarburgers.nomoreparties.site/register")

        self.__wait_element(driver, ".//*[text()='Войти']")
        enter = driver.find_element(By.XPATH, ".//*[text()='Войти']")
        driver.execute_script("arguments[0].scrollIntoView();", enter)

        time.sleep(1)
        driver.find_element(By.XPATH, ".//*[text()='Войти']").click()

        time.sleep(3)
        located_email = driver.find_element(By.XPATH, ".//input[(@name='name')]")
        located_password = driver.find_element(By.XPATH, ".//input[(@name='Пароль')]")
        located_enter_button = driver.find_element(By.XPATH, ".//*[text()='Войти']")

        located_email.send_keys("EvgeniyGrekov231@mail.ru")
        time.sleep(1)
        located_password.send_keys("123456")
        time.sleep(1)
        located_enter_button.click()

        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
        time.sleep(2)
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/account" \
               or driver.current_url == "https://stellarburgers.nomoreparties.site/account/profile"
        assert driver.find_element(By.XPATH, ".//button[text()='Выход']").is_displayed()

    # @pytest.mark.skip()
    def test_transition_to_personal_account(self, driver):
        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
        time.sleep(1)
        if driver.current_url == "https://stellarburgers.nomoreparties.site/login":
            located_email = driver.find_element(By.XPATH, ".//input[(@name='name')]")
            time.sleep(1)
            located_password = driver.find_element(By.XPATH, ".//input[(@name='Пароль')]")
            time.sleep(1)
            located_enter_button = driver.find_element(By.XPATH, ".//*[text()='Войти']")
            time.sleep(1)

            email_value = 'EvgeniyGrekov231@mail.ru'
            password_value = '123456'

            located_email.send_keys(email_value)
            time.sleep(1)
            located_password.send_keys(password_value)
            time.sleep(1)
            located_enter_button.click()
            time.sleep(1)

        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
        time.sleep(1)

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/account" \
               or driver.current_url == "https://stellarburgers.nomoreparties.site/account/profile"
        assert driver.find_element(By.XPATH, ".//button[text()='Выход']").is_enabled()

    # @pytest.mark.skip()
    def test_transition_logo(self, driver):
        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
        time.sleep(1)
        if driver.current_url == "https://stellarburgers.nomoreparties.site/login":
            located_email = driver.find_element(By.XPATH, ".//input[(@name='name')]")
            time.sleep(1)
            located_password = driver.find_element(By.XPATH, ".//input[(@name='Пароль')]")
            time.sleep(1)
            located_enter_button = driver.find_element(By.XPATH, ".//*[text()='Войти']")
            time.sleep(1)

            email_value = 'EvgeniyGrekov231@mail.ru'
            password_value = '123456'

            located_email.send_keys(email_value)
            time.sleep(1)
            located_password.send_keys(password_value)
            time.sleep(1)
            located_enter_button.click()
            time.sleep(1)

        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
        time.sleep(1)

        driver.find_element(By.XPATH, ".//a[@href='/']").click()
        time.sleep(1)

        assert driver.find_element(By.XPATH, ".//section[1]/h1").text == "Соберите бургер"
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

    # @pytest.mark.skip()
    def test_transition_constructor(self, driver):
        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
        time.sleep(1)
        if driver.current_url == "https://stellarburgers.nomoreparties.site/login":
            located_email = driver.find_element(By.XPATH, ".//input[(@name='name')]")
            time.sleep(1)
            located_password = driver.find_element(By.XPATH, ".//input[(@name='Пароль')]")
            time.sleep(1)
            located_enter_button = driver.find_element(By.XPATH, ".//*[text()='Войти']")
            time.sleep(1)

            email_value = 'EvgeniyGrekov231@mail.ru'
            password_value = '123456'

            located_email.send_keys(email_value)
            time.sleep(1)
            located_password.send_keys(password_value)
            time.sleep(1)
            located_enter_button.click()
            time.sleep(1)

        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
        time.sleep(1)

        driver.find_element(By.XPATH, ".//p[text()='Конструктор']").click()
        time.sleep(1)

        assert driver.find_element(By.XPATH, ".//section[1]/h1").text == "Соберите бургер"
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

    # @pytest.mark.skip()
    def test_navigation_food_menu(self, driver):
        if driver.current_url != "https://stellarburgers.nomoreparties.site/":
            driver.get("https://stellarburgers.nomoreparties.site/")

        located_button_roll = driver.find_element(By.XPATH, ".//div/div/*[text()='Булки']")
        located_button_sauces = driver.find_element(By.XPATH, ".//div/div/*[text()='Соусы']")
        located_button_stuffing = driver.find_element(By.XPATH, ".//div/div/*[text()='Начинки']")

        located_button_sauces.click()
        elem_sauces = []
        time.sleep(1)
        for i in driver.find_elements(By.XPATH, ".//section/div/ul[2]/a"):
            elem_sauces.append(i)
            assert i.is_enabled()
        assert len(elem_sauces) == 4
        assert driver.find_element(By.XPATH, ".//h2[text()='Булки']").is_displayed()
        time.sleep(1)

        located_button_roll.click()
        elem_roll = []
        for i in driver.find_elements(By.XPATH, ".//section/div/ul[1]/a"):
            elem_roll.append(i)
            assert i.is_enabled()
        assert len(elem_roll) == 2
        assert driver.find_element(By.XPATH, ".//h2[text()='Булки']").is_displayed()
        time.sleep(1)

        located_button_stuffing.click()
        elem_stuffing = []
        for i in driver.find_elements(By.XPATH, ".//section/div/ul[3]/a"):
            elem_stuffing.append(i)
            assert i.is_enabled()
        assert len(elem_stuffing) == 9
        assert driver.find_element(By.XPATH, ".//h2[text()='Начинки']").is_displayed()
        time.sleep(1)
