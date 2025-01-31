from pytest_bdd import scenario
import step_definitions.test_login_steps  # ✅ Explicitly import step definitions

@scenario('C:/Users//aarti.kyama//Python_Selenium_Training//Shanaya_project//features//login.feature'
,"Successful Login with Valid Credentials")
def test_login():
    pass  # ✅ This links the steps in test_login_steps.py
