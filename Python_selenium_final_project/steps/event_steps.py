from pytest_bdd import when, then, parsers
from pages.event_page import EventPage
import logging

logger = logging.getLogger(__name__)

@when(parsers.parse('the user creates an event with subject: "{subject}", date: "{date}", time: "{time}", and account: "{account}"'))
def create_event(browser, subject, date, time, account):
    event_page = EventPage(browser)
    event_page.create_event(subject, date, time, account)
    logger.info("Event created successfully")

@then(parsers.parse('the event should be created and validated with subject: "{subject}", date: "{date}", time: "{time}", and account: "{account}"'))
def validate_event(browser, subject, date, time, account):
    event_page = EventPage(browser)
    assert event_page.validate_event(subject, date, time, account), "Event validation failed"
    logger.info("Event validated successfully")
