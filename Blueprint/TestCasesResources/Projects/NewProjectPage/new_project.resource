*** Settings ***
Library    Blueprint.Steps.Actions.MainMenu.main_menu_actions.MainMenuActions
Library    Blueprint.Steps.Actions.Projects.ProjectPage.project_page_actions.ProjectPageActions

*** Variables ***
${flow_name}    AT-19 Test-fc


*** Keywords ***
Search An Specific Project And Click On New Request Button
    [Arguments]    ${project_name}=${flow_name}
    Go To Project Process In Main Menu    ${project_name}
    Sleep    3
    Click On New Request Button
   