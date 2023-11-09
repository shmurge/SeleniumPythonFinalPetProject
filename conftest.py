import pytest
from selenium import webdriver


def pytest_addoption(parser):
    # параметр выбора браузера --browser_name=chrome/firefox указываем при запуске из терминала
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    # параметр выбора языка браузера --language=ru/es/fr etc указываем при запуске из терминала
    parser.addoption('--language', action='store', default=None,
                     help='Choose language: ru, en, ... (etc.)')

@pytest.fixture(scope="class")
def browser(request):
    user_language = request.config.getoption("language") # присваиваем переменной значение параметра языка
    browser_name = request.config.getoption("browser_name") # # присваиваем переменной значение параметра браузера
    browser = None
    if browser_name == "chrome":
        from selenium.webdriver.chrome.options import Options   # импорт опций для chrome
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        from selenium.webdriver.firefox.options import Options    # импорт опций для firefox
        print("\nstart firefox browser for test..")
        fp = Options()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(options=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()