from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.XPATH, ".//p[text()='Личный Кабинет']")
    LOGIN_ACCOUNT_BUTTON = (By.XPATH, ".//button[contains(text(),'Войти')]")
    CONSTRUTOR = (By.XPATH, ".//p[text()='Конструктор']")
    ORDER_FEED = (By.XPATH, ".//p[text()='Лента Заказов']")
    LOGO = (By.XPATH, ".//a[@href='/']")

    BUTTON_ROLLS = (By.XPATH, ".//div/div/*[text()='Булки']")
    BUTTIN_SAUCES = (By.XPATH, ".//div/div/*[text()='Соусы']")
    BUTTON_TOPPINGS =(By.XPATH, ".//div/div/*[text()='Начинки']")
    TEXT_ROLLS = (By.XPATH, ".//h2[text()='Булки']")
    TEXT_SAUCES = (By.XPATH, ".//h2[text()='Соусы']")
    TEXT_TOPPINGS = (By.XPATH, ".//h2[text()='Начинки']")


class LoginPageLocators:
    FIELD_NAME = (By.XPATH, ".//input[(@name='name')]")
    FIELD_PASSWORD = (By.XPATH, ".//input[(@name='Пароль')]")
    BUTTON_ENTER = (By.XPATH, ".//*[text()='Войти']")


class RegistrationPageLocators(LoginPageLocators):
    BUTTON_REGISTRATION = (By.XPATH, ".//button[text()='Зарегистрироваться']")


class ProfileLocators:
    BUTTON_EXIT = (By.XPATH, ".//button[text()='Выход']")
    FIELD_EMAIL = (By.XPATH, ".//input[(@value='{email_value.lower()}')]")


class InfoLocators:
    INFO_PASSWORD = (By.XPATH, ".//p[text()='Некорректный пароль']")
    ASSEMBLE_BURGER = (By.XPATH, ".//section[1]/h1")

class List_of_products:
    LIST_OF_ROLLS = (By.XPATH, ".//section/div/ul[1]/a")
    LIST_OF_SAUCES = (By.XPATH, ".//section/div/ul[2]/a")
    LIST_OF_TOPPINGS = (By.XPATH, ".//section/div/ul[3]/a")