*** Settings ***
Library    Blueprint.Steps.Actions.Flows.publish_tab_actions.PublishTabActions
Library    Blueprint.Steps.Actions.MainMenu.main_menu_actions.MainMenuActions
Resource    Blueprint/TestCasesResources/E2E/SwimmingCompetition/swimming_create_form.resource
Resource    Blueprint/TestCasesResources/E2E/SwimmingCompetition/swimming_create_flow.resource
Resource    Blueprint/TestCasesResources/E2E/SwimmingCompetition/swimming_permissions.resource

Force Tags    E2E    Swimming_Competition    PROJECT
Suite Teardown    Delete Storage

*** Variables ***
${flow_name_without_code}   AT19-SWIMMING

*** Test Cases ***
Verify a new flow can be created
    Sleep    10
    ${flow_name_with_code}    Create A New Flow With Random Code    ${flow_name_without_code}
    Flow Page Title Should Be Displayed    ${flow_name_with_code}
    Set Suite Variable    ${flow_name_with_code}

Verify that the form can be created
    Create Applicant Information Section
    Applicant Information Section Should Be Displayed
    Create Swimming Styles Section
    Swimming Styles Section Should Be Displayed

Verify flow can be created
    Move Components To Canvas
    Verify Components Titles
    Connect Components
    Verify Components Colors
    Verify Components Connections

Verify Permissions can be set
    Set Permissions
    Verify Permissions

Verify project is created
    Click Tab In Flow Header    Publish
    Click Save Publish Button
    Time To Save The Flow
    Go To Project Process In Main Menu    ${flow_name_with_code}    
    Project Title Should Be    ${flow_name_with_code}
