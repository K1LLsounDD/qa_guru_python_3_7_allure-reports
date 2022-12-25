import allure
from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

@allure.tag('web')
@allure.severity(Severity.BLOCKER)
@allure.label('owner', 'K1LLsounDD')
@allure.link('https://github.com/', name='Github url')
@allure.feature('Checking if a task is in the repository')
@allure.story('Tests with steps')
def test_github_search():
    with allure.step('Open github in a browser with a screen resolution of 1920x1080.'):
        browser.config.window_width = 1920
        browser.config.window_height = 1080
        browser.open('https://github.com/')

    with allure.step('Enter the name of the repository in the search'):
        s('[name="q"]').click()
        s('[name="q"]').send_keys('K1LLsounDD/qa_guru_python_3_7_allure-reports').press_enter()

    with allure.step('Go to the repository itself'):
        s(by.link_text('K1LLsounDD/qa_guru_python_3_7_allure-reports')).click()

    with allure.step('Go to the issue tab'):
        s('#issues-tab').click()

    with allure.step('Search issue #1'):
        s(by.partial_text('#1')).should(be.visible)

    browser.quit()