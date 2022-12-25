import allure
from allure_commons.types import Severity
from selene import be
from selene.support import by
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

browser.config.hold_browser_open = True

@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'K1LLsounDD')
@allure.link('https://github.com/', name='Url git')
@allure.story('Tests on clean Selene')
@allure.feature('Checking if a task is in the repository')
def test_search_github():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.open('https://github.com/')

    s('[name="q"]').click()
    s('[name="q"]').send_keys('K1LLsounDD/qa_guru_python_3_7_allure-reports')
    s('[name="q"]').submit()

    s(by.link_text('K1LLsounDD/qa_guru_python_3_7_allure-reports')).click()

    s('#issues-tab').click()

    s(by.partial_text('#1')).should(be.visible)
    browser.quit()
