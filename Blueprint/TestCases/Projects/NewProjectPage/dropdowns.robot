*** Settings ***
Library    Blueprint.Steps.Actions.MainMenu.main_menu_actions.MainMenuActions
Library    Blueprint.Steps.Actions.Projects.new_project_actions.NewProjectActions
Library    Blueprint.Steps.Verifications.Projects.NewProjectPage.new_project_page_verifications.NewProjectPageVerifications
Resource    Blueprint/TestCasesResources/navigate.resource
Suite Setup    Navigate To Projects

*** Variables ***
${value}    Roger Renjifo
${value2}    Carolina Vacaflor
${section}    New history
${label}    responsible


*** Test Cases ***
Verify Open Browser
    Log To Console    hola

Verify Open Project
    Navigate To Projects
    select_user_from_the_dropdown_in_new_project_page    ${section}    ${label}    ${value}
    ${content}    get_the_content_of_a_dropdown    ${section}   ${label}
    Option Should Be Equal   ${content}    ${value}

verify2
    select_user_from_the_dropdown_in_new_project_page    ${section}    ${label}    ${value}
    select_user_from_the_dropdown_in_new_project_page    ${section}    ${label}    ${value2}
    ${content}    get_the_content_of_a_dropdown    ${section}   ${label}
    Option Should Be Equal   ${content}    ${value2}
    

*** Keywords ***
Search An Specific Project
    [Arguments]   ${project_name}=AT19 - RM
    Sleep    8
    Go To Project Process In Main Menu   ${project_name}
    Sleep    3