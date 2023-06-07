*** Settings ***
Resource    Blueprint/TestCasesResources/Flow/CreateForm/common_imports.resource
Resource    Blueprint/TestCasesResources/E2E/ScholarshipApplication/scholarship_application_scenario_create_form.resource
Resource    Blueprint/TestCasesResources/E2E/ScholarshipApplication/scholarship_application_scenario_create_flow.resource
Library    Blueprint.Steps.Actions.Flows.flow_permissions_actions.FlowPermissionsActions
Library    Blueprint.Steps.Actions.Flows.process_permissions_actions.ProcessPermissionsActions
Library    Blueprint.Steps.Actions.Flows.section_visibility_permissions_actions.SectionsVisibilityActions
Library    Blueprint.Steps.Verifications.E2E.scholarship_application.ScholarshipApplicationVerifications
Library    Blueprint.Steps.Verifications.Flow.CreateForm.create_form_add_component_verification.CreateFormAddComponentVerifications
Library    Blueprint.Steps.Verifications.Flow.CreateForm.create_form_add_section_verification.CreateFormAddSectionVerifications
Library    Blueprint.Steps.Actions.Flows.flow_main_panel_actions.FlowMainPanelActions
Library    Blueprint.Steps.Actions.Flows.flows_properties_actions.FlowPropertiesActions
Library    Blueprint.Steps.Actions.Flows.flow_components_actions.FlowComponentsActions
Library    Blueprint.Steps.Actions.MainMenu.main_menu_actions.MainMenuActions
Library    Blueprint.Steps.Utils.main_menu_manager.MainMenuManager
Library    Blueprint.Steps.Actions.Flows.publish_tab_actions.PublishTabActions
Library    Collections

*** Variables ***
${flow_name}    AT19-Scenario-Scholarship-RM-
${user_group}   AT19-GUITESTING-SCENARIO-SCHOLARSHIP

*** Keywords ***
Set Steps and Actions Dictionaries
    ${steps}    Create Dictionary
    ${actions}    Create Dictionary
    Set Suite Variable    ${steps}
    Set Suite Variable    ${actions}

Update Owner
    Click Select Owner Menu In Flow Properties
    Select Owner From List In Flow Properties   position=1
    Click Owner Combobox In Flow Properties
    Search Owner In Menu In Flow Properties    ${user_group}
    Select Owner In Menu In Flow Properties

Set Flow Permissions
    Delete All Users In Dropdown In Flow Permissions
    Add New Flow Admin By Typing Process In Flow Permission    ${user_group}

Set Process Permissions
    Delete All Users In Dropdown In Process Permission
    Add User To Initiate Process By Typing Process In Process Permissions    ${user_group}

Set Visibility Section In Applicant Information, Documentation And Academic Performance
    Delete All Users In Section Visibility    3
    Add User To Section Visibility By Scrolling Process In Section Visibility    ${user_group}   3
    Delete All Users In Section Visibility    4
    Add User To Section Visibility By Scrolling Process In Section Visibility    ${user_group}   4
    Delete All Users In Section Visibility    5
    Add User To Section Visibility By Scrolling Process In Section Visibility    ${user_group}   5

Verify Dropdown Titles For Sections Applicant Information, Documentation And Academic Performance
    Section Visibility Title Should Be    ${section_name_1}    3
    Section Visibility Title Should Be    ${section_name_2}    4
    Section Visibility Title Should Be    ${section_name_3}    5

Delete Storage
    Clean Dictionary
    Delete Form Storage