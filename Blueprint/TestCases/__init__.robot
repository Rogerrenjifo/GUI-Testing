*** Settings ***
Library             Libraries.Drivers.browser.Browser
Library             Blueprint.Steps.Actions.Login.login_page_actions.LoginPageActions
Suite Setup         Login To Blueprint
Suite Teardown      Close Browser


*** Variables ***
${url}     https://test.blueprint.ses-unit.com/my-inbox

*** Keywords ***
Login To Blueprint
    Get Driver
    Navigate To Url   ${url}
    Login
