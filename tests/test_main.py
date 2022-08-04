import time

import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


from GenerateUser import User
from .locators import *


class TestStellarBurgers:
    FirstName, Email, Password = User().generation_of_user_data()

    def __wait_element(self, driver, xpath_element):
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located((By.XPATH, xpath_element)))

    def __login(self, driver, email_value='EvgeniyGrekov231@mail.ru', password_value='123456'):
        if driver.current_url == "https://stellarburgers.nomoreparties.site/login":
            self.__wait_element(driver, ".//input[(@name='name')]")
            self.__wait_element(driver, ".//input[(@name='Пароль')]")
            self.__wait_element(driver, ".//*[text()='Войти']")

            located_email = driver.find_element(*LoginPageLocators.FIELD_NAME)
            located_password = driver.find_element(*LoginPageLocators.FIELD_PASSWORD)
            located_enter_button = driver.find_element(*LoginPageLocators.BUTTON_ENTER)

            # email_value = 'EvgeniyGrekov231@mail.ru'
            # password_value = '123456'

            # без этих задержек не передаются данные в поля
            located_email.send_keys(email_value)
            time.sleep(0.3)
            located_password.send_keys(password_value)
            time.sleep(0.3)
            located_enter_button.click()

    # @pytest.mark.skip
    @pytest.mark.registration
    def test_registration(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")

        located_name, located_email  = driver.find_elements(*RegistrationPageLocators.FIELD_NAME)
        located_password = driver.find_element(*RegistrationPageLocators.FIELD_PASSWORD)
        located_reg_button = driver.find_element(*RegistrationPageLocators.BUTTON_REGISTRATION)

        located_name.send_keys(TestStellarBurgers.FirstName)
        located_email.send_keys(TestStellarBurgers.Email)
        located_password.send_keys(TestStellarBurgers.Password)
        located_reg_button.click()
        time.sleep(1) # без этой задержки условие if не отрабатывает

        if driver.current_url == "https://stellarburgers.nomoreparties.site/login":
            self.__login(driver, TestStellarBurgers.Email, TestStellarBurgers.Password)

        self.__wait_element(driver, ".//p[text()='Личный Кабинет']")
        driver.find_element(*MainPageLocators.LOGIN_LINK).click()

        self.__wait_element(driver, f".//input[(@value='{TestStellarBurgers.Email.lower()}')]")
        assert driver.find_element(By.XPATH, f".//input[(@value='{TestStellarBurgers.Email.lower()}')]").is_displayed()

        self.__wait_element(driver, ".//button[text()='Выход']")
        driver.find_element(*ProfileLocators.BUTTON_EXIT).click()

    # @pytest.mark.skip
    @pytest.mark.registration
    def test_field_password_lower_6(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/login")

        self.__wait_element(driver, ".//input[(@name='name')]")
        self.__wait_element(driver, ".//input[(@name='Пароль')]")

        located_email = driver.find_element(*LoginPageLocators.FIELD_NAME)
        located_password = driver.find_element(*LoginPageLocators.FIELD_PASSWORD)

        located_password.send_keys("12345")
        located_email.click()

        self.__wait_element(driver, ".//p[text()='Некорректный пароль']")
        assert driver.find_element(*InfoLocators.FALSE_PASSWORD).is_displayed()

    # @pytest.mark.skip
    @pytest.mark.authorization
    def test_authorization_button_personal_account(self, driver):
        self.__wait_element(driver, ".//p[text()='Личный Кабинет']")
        driver.find_element(*MainPageLocators.LOGIN_LINK).click()

        self.__login(driver)

        self.__wait_element(driver, ".//p[text()='Личный Кабинет']")
        driver.find_element(*MainPageLocators.LOGIN_LINK).click()

        self.__wait_element(driver, f".//input[(@value='{'EvgeniyGrekov231@mail.ru'.lower()}')]")
        assert driver.find_element(By.XPATH, f".//input[(@value='{'EvgeniyGrekov231@mail.ru'.lower()}')]").is_displayed()

    # @pytest.mark.skip
    @pytest.mark.exit
    def test_exit_accout(self, driver):
        self.__wait_element(driver, ".//p[text()='Личный Кабинет']")
        driver.find_element(*MainPageLocators.LOGIN_LINK).click()

        self.__login(driver)

        self.__wait_element(driver, ".//p[text()='Личный Кабинет']")
        driver.find_element(*MainPageLocators.LOGIN_LINK).click()

        self.__wait_element(driver, ".//button[text()='Выход']")
        driver.find_element(*ProfileLocators.BUTTON_EXIT).click()

        self.__wait_element(driver, ".//p[text()='Личный Кабинет']")
        driver.find_element(*MainPageLocators.LOGIN_LINK).click()
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

    # @pytest.mark.skip
    @pytest.mark.authorization
    def test_authorization_button_login(self, driver):
        self.__wait_element(driver, ".//p[text()='Личный Кабинет']")
        driver.find_element(*MainPageLocators.LOGIN_ACCOUNT_BUTTON).click()

        self.__login(driver)

        self.__wait_element(driver, ".//p[text()='Личный Кабинет']")
        driver.find_element(*MainPageLocators.LOGIN_LINK).click()

        self.__wait_element(driver, f".//input[(@value='{'EvgeniyGrekov231@mail.ru'.lower()}')]")
        assert driver.find_element(By.XPATH, f".//input[(@value='{'EvgeniyGrekov231@mail.ru'.lower()}')]").is_displayed()

    # @pytest.mark.skip
    @pytest.mark.authorization
    def test_authorization_in_menu_password_recovery(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/forgot-password")

        self.__wait_element(driver, ".//*[text()='Войти']")
        driver.find_element(*LoginPageLocators.BUTTON_ENTER).click()

        self.__login(driver)

        driver.find_element(*MainPageLocators.LOGIN_LINK).click()

        self.__wait_element(driver, f".//input[(@value='{'EvgeniyGrekov231@mail.ru'.lower()}')]")
        assert driver.find_element(By.XPATH, f".//input[(@value='{'EvgeniyGrekov231@mail.ru'.lower()}')]").is_displayed()

    # @pytest.mark.skip
    @pytest.mark.authorization
    def test_authorization_menu_registration(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")

        self.__wait_element(driver, ".//*[text()='Войти']")
        driver.find_element(*LoginPageLocators.BUTTON_ENTER).click()

        self.__login(driver)

        self.__wait_element(driver, ".//p[text()='Личный Кабинет']")
        driver.find_element(*MainPageLocators.LOGIN_LINK).click()

        self.__wait_element(driver, f".//input[(@value='{'EvgeniyGrekov231@mail.ru'.lower()}')]")
        assert driver.find_element(By.XPATH, f".//input[(@value='{'EvgeniyGrekov231@mail.ru'.lower()}')]").is_displayed()

    # @pytest.mark.skip
    @pytest.mark.navigation
    def test_transition_to_personal_account(self, driver):
        self.__wait_element(driver, ".//p[text()='Личный Кабинет']")
        driver.find_element(*MainPageLocators.LOGIN_LINK).click()

        self.__login(driver)

        self.__wait_element(driver, ".//p[text()='Личный Кабинет']")
        driver.find_element(*MainPageLocators.LOGIN_LINK).click()

        self.__wait_element(driver, f".//input[(@value='{'EvgeniyGrekov231@mail.ru'.lower()}')]")
        assert driver.find_element(By.XPATH, f".//input[(@value='{'EvgeniyGrekov231@mail.ru'.lower()}')]").is_displayed()

    # @pytest.mark.skip
    @pytest.mark.navigation
    def test_transition_logo(self, driver):
        self.__wait_element(driver, ".//p[text()='Личный Кабинет']")
        driver.find_element(*MainPageLocators.LOGIN_LINK).click()

        self.__login(driver)

        self.__wait_element(driver, ".//p[text()='Личный Кабинет']")
        driver.find_element(*MainPageLocators.LOGIN_LINK).click()
        self.__wait_element(driver, ".//a[@href='/']")
        driver.find_element(*MainPageLocators.LOGO).click()

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

    # @pytest.mark.skip
    @pytest.mark.navigation
    def test_transition_constructor(self, driver):
        self.__wait_element(driver, ".//p[text()='Личный Кабинет']")
        driver.find_element(*MainPageLocators.LOGIN_LINK).click()

        self.__login(driver)

        self.__wait_element(driver, ".//p[text()='Личный Кабинет']")
        driver.find_element(*MainPageLocators.LOGIN_LINK).click()
        self.__wait_element(driver, ".//p[text()='Конструктор']")
        driver.find_element(*MainPageLocators.CONSTRUCTOR).click()

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

    # @pytest.mark.skip
    @pytest.mark.navigation
    def test_navigation_food_menu(self, driver):
        if driver.current_url != "https://stellarburgers.nomoreparties.site/":
            driver.get("https://stellarburgers.nomoreparties.site/")

        self.__wait_element(driver, ".//div/div/*[text()='Булки']")
        self.__wait_element(driver, ".//div/div/*[text()='Соусы']")
        self.__wait_element(driver, ".//div/div/*[text()='Начинки']")

        located_button_roll = driver.find_element(*MainPageLocators.BUTTON_ROLLS)
        located_button_sauces = driver.find_element(*MainPageLocators.BUTTON_SAUCES)
        located_button_stuffing = driver.find_element(*MainPageLocators.BUTTON_TOPPINGS)

        located_button_sauces.click()
        elem_sauces = []
        for i in driver.find_elements(*ListOfProducts.LIST_OF_SAUCES):
            elem_sauces.append(i)

        located_button_roll.click()
        elem_roll = []
        for i in driver.find_elements(*ListOfProducts.LIST_OF_ROLLS):
            elem_roll.append(i)

        located_button_stuffing.click()
        elem_stuffing = []
        for i in driver.find_elements(*ListOfProducts.LIST_OF_TOPPINGS):
            elem_stuffing.append(i)

        assert driver.find_element(*MainPageLocators.TEXT_SAUCES).is_displayed() \
               and driver.find_element(*MainPageLocators.TEXT_ROLLS).is_displayed() \
               and driver.find_element(*MainPageLocators.TEXT_TOPPINGS).is_displayed() \
               and len(elem_sauces) == 4 \
               and len(elem_roll) == 2 \
               and len(elem_stuffing) == 9
