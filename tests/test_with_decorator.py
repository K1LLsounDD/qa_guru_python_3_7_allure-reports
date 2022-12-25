import allure
from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


@allure.tag('web')
@allure.label('owner', 'K1LLsounDD')
@allure.severity(Severity.NORMAL)
@allure.link('https://github.com/', name='Github url')
@allure.story('Test with decoration')
@allure.feature('Checking if a task is in the repository')
def test_decorator_steps():
    open_main_page()
    search_for_repository('K1LLsounDD/qa_guru_python_3_7_allure-reports')
    go_to_repository('K1LLsounDD/qa_guru_python_3_7_allure-reports')
    go_to_issue()
    check_issue('#1')
    browser.quit()


@allure.step('Open github in a browser with a screen resolution of 1920x1080.')
def open_main_page():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.open('https://github.com/')


@allure.step('Enter the name of the repository in the search {repo}')
def search_for_repository(repo):
    s('[name="q"]').click()
    s('[name="q"]').send_keys(repo).press_enter()


@allure.step('Go to the repository itself {repo}')
def go_to_repository(repo):
    s(by.link_text(repo)).click()


@allure.step('Go to the issue tab')
def go_to_issue():
    s('#issues-tab').click()


@allure.step('Checking for a issue {number}')
def check_issue(number):
    s(by.partial_text(number)).should(be.visible)
