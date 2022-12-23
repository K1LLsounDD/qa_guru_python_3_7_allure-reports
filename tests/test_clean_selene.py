from selene import be, have
from selene.support import by
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

browser.config.hold_browser_open = True


def test_search_github_eroshenko_allure():
    s('[name="q"]').click()
    s('[name="q"]').send_keys('eroshenkoam/allure-example')
    s('[name="q"]').submit()

    s(by.link_text('eroshenkoam/allure-example')).click()

    s('#issues-tab').click()

    s(by.partial_text('#76')).should(be.visible)
