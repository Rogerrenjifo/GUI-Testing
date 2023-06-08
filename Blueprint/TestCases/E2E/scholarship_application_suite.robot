*** Settings ***
Documentation    E2E Scenario that reprecents the process of a scholraship application
Resource    Blueprint/TestCasesResources/E2E/ScholarshipApplication/scholarship_application_scenario_importations.resource

Force Tags    SCHOLARSHIP_APPLICATION   E2E
Suite Setup    Set Steps and Actions Dictionaries
Suite Teardown    Delete Storage

*** Variables ***
${expected_success_popup_color}    rgba(92, 184, 92, 1)
${color_component_with_error}   rgb(255, 114, 105)
${expected_text_popup}    Flow AT19-Scenario-Scholarship-RM-6NC updated.
${user_group}   AT19-GUITESTING-SCENARIO-SCHOLARSHIP

*** Test Cases ***
Verify a flow can be created, from form creation, flow creation, and permissions assignation, to publish
    ${flow_name_for_edit}    Create A New Flow With Random Code    ${flow_name}
    Create Applicant Information Section
    Components Order Should Be    ${component_names_section_1}
    Components Type In Section Should Be    ${component_types_section_1}
    Create Documentation Section
    Components Order Should Be    ${component_names_section_2}    section-2
    Components Type In Section Should Be    ${component_types_section_2}    section-2
    Create Academic Performance Section
    Components Order Should Be    ${component_names_section_3}    section-3
    Components Type In Section Should Be    ${component_types_section_3}    section-3
    Flow Header Title Should Be The Same As The Title Set In Create Flow    ${flow_name_for_edit}
    Click Save Button In Flow Header
    Popup Message Should Be Displayed
    Pop Up Message Should Be Displayed In Expected Color    ${expected_success_popup_color}
    Popup Message Text Should Be    Flow ${flow_name_for_edit} updated.
    Click Tab In Flow Header    Create Flow
    Add Steps And Actions To Diagram
    Conncet Actions And Steps
    Components Titles Should Be    ${steps}
    Components Titles Should Be    ${actions}
    Check Step 5 As End Step
    Check Step 6 As End Step
    Components Titles Should Not Have Errors    ${actions}      ${color_component_with_error}
    Click Tab In Flow Header    Permissions
    Set Flow Permissions
    Set Process Permissions
    Set Visibility Section In Applicant Information, Documentation And Academic Performance
    User Selected In Flow Permissions Should Be    ${user_group}
    User Selected In Process Permissions Should Be    ${user_group}
    User Selected In Section Visibility Should Be    ${user_group}    3
    User Selected In Section Visibility Should Be    ${user_group}    4
    User Selected In Section Visibility Should Be    ${user_group}    5
    Verify Dropdown Titles For Sections Applicant Information, Documentation And Academic Performance
    Click Save Button In Flow Header
    Popup Message Should Be Displayed
    Pop Up Message Should Be Displayed In Expected Color    ${expected_success_popup_color}
    Popup Message Text Should Be    Flow permissions of ${flow_name_for_edit} updated.
    Click Tab In Flow Header    Publish
    Click Save Publish Button
    Click Save Continue Button
    Log To Console    ${flow_name_for_edit}
    New Project Should Exist    ${flow_name_for_edit}
