*** Settings ***
Library             Libraries.Drivers.browser.Browser
Library             Blueprint.Steps.Actions.Login.login_page_actions.LoginPageActions
Library             Blueprint.Steps.Actions.Logout.logout_actions.LogoutActions

*** Variables ***
${url}    https://test.blueprint.ses-unit.com/new-project/cf412b5e-8bbc-4b2b-a6f0-6a2f168efdb6

*** Keywords ***
Login To Blueprint
    Get Driver
    Navigate To Url    ${url}
    Login

Return to previous page
    Go Back To Previous Page

Logout from Blueprint
    Sing Out Process
    Close Browser
