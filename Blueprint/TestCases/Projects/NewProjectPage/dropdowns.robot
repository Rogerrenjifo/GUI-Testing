*** Settings ***
Library    Blueprint.Steps.Actions.MainMenu.main_menu_actions.MainMenuActions
Library    Blueprint.Steps.Actions.Projects.new_request_actions.NewRequestActions
Library    Blueprint.Steps.Verifications.Projects.NewProjectPage.new_project_page_verifications.NewProjectPage
Resource    Blueprint/TestCasesResources/navigate.resource
Suite Setup    Navigate To Projects

*** Variables ***
${value}    3
${value2}    2
${section}    Delivering
${label}    Multiline Box 1


*** Test Cases ***
Verify Open Browser
    Log To Console    hola

Verify Open Project
    Navigate To Projects
    select_user_from_the_dropdown_in_new_request    ${section}    ${label}    ${value}
    ${content}    get_the_content_of_a_dropdown    ${section}   ${label}
    Option Should Be Equal   ${content}    ${value}

verify2
    select_user_from_the_dropdown_in_new_request    ${section}    ${label}    ${value}
    select_user_from_the_dropdown_in_new_request    ${section}    ${label}    ${value2}
    ${content}    get_the_content_of_a_dropdown    ${section}   ${label}
    Option Should Be Equal   ${content}    ${value2}
    

*** Keywords ***
Search An Specific Project
    [Arguments]   ${project_name}=AT19 - RM
    Sleep    8
    Go To Project Process In Main Menu   ${project_name}
    Sleep    3