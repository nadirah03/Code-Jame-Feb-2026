import pytest
from time_selection_framework import TimeKeeperPage


def test_timer_options_displayed(driver):
    page = TimeKeeperPage(driver)
    page.open()

    timers = page.get_timer_texts()

    assert "15:00" in timers
    assert "25:00" in timer
    assert "45:00" in timers


@pytest.mark.parametrize("time_value", ["15:00", "25:00", "45:00"])
def test_timer_buttons_visible_clickable(driver, time_value):
    page = TimeKeeperPage(driver)
    page.oppyen()

    assert page.is_timer_visible_and_clickable(time_value)


@pytest.mark.parametrize("time_value", ["15:00", "25:00", "45:00"])
def test_user_can_select_timer(driver, time_value):
    page = TimeKeeperPage(driver)
    page.open()

    page.select_timer(time_value)
    assert time_value in page.get_active_timer()


def test_other_timers_inactive(driver):
    page = TimeKeeperPage(driver)
    page.open()

    page.select_timer("25:00")
    active = page.get_active_timer()

    assert "25:00" in active


def test_smaller_time_on_left(driver):
    page = TimeKeeperPage(driver)
    page.open()

    timers = page.get_timer_texts()
    timer_values = sorted(timers)
    assert timers[0] == timer_values[0]


def test_start_button_navigation_and_timer_starts(driver):
    page = TimeKeeperPage(driver)
    page.open()

    page.select_timer("15:00")
    page.click_start()

    assert page.get_current_url() != TimeKeeperPage.URL

    displayed_time = page.get_displayed_time()
    assert "15" in displayed_time
