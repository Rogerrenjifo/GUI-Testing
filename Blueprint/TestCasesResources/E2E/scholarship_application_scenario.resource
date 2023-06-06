*** Settings ***
Resource    Blueprint/TestCasesResources/Flow/CreateForm/common_imports.resource
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
Library    Collections

*** Variables ***
${flow_name}    AT19-Scenario-Scholarship-RM-

*** Keywords ***
Search Flow
    ${exists}   Flow Exists    ${flow_name}
    ${flow_name_for_edit}    Go To Flow For Edit    ${exists}    ${flow_name}
    ${steps}    Create Dictionary
    ${actions}    Create Dictionary
    Set Suite Variable    ${flow_name_for_edit}
    Set Suite Variable    ${steps}
    Set Suite Variable    ${actions}

Add Step With Name To Board
    [Arguments]    ${name}    ${x_coordenate}    ${y_coordenate}    ${component_number}
    Move Step To Board Position    ${x_coordenate}    ${y_coordenate}
    Sleep    1
    Change Component Name In Flow Properties    ${name}
    Set To Dictionary    ${steps}    001Added${component_number}    ${name}
Add Action With Name To Board
    [Arguments]    ${name}    ${x_coordenate}    ${y_coordenate}    ${component_number}
    Move Action To Board Position    ${x_coordenate}    ${y_coordenate}
    Sleep    1
    Change Component Name In Flow Properties    ${name}
    Update Owner
    Set To Dictionary    ${actions}    002Added${component_number}   ${name}

Update Owner
    Click Select Owner Menu In Flow Properties
    Select Owner From List In Flow Properties   position=1
    Click Owner Combobox In Flow Properties
    Search Owner In Menu In Flow Properties    AT19-GUITESTING-SCENARIO-SCHOLARSHIP
    Select Owner In Menu In Flow Properties

Connect Step ${step_number} With Action ${action_number} From Point ${a} To Point ${b}
    Click Component    001Added${step_number}
    Connect Components In Flow Main Panel    001Added${step_number}    002Added${action_number}   ${a}    ${b}

Connect Action ${action_number} With Step ${step_number} From Point ${a} To Point ${b}
    Click Component    002Added${action_number}
    Connect Components In Flow Main Panel    002Added${action_number}    001Added${step_number}   ${a}    ${b}

Connect Initial Step With Action ${action_number} From Point ${a} To Point ${b}
    Click Component    first
    Connect Components In Flow Main Panel    first    002Added${action_number}    ${a}    ${b}

Connect Action ${action_number} With Initial Step From Point ${a} To Point ${b}
    Click Component    002Added${action_number}
    Connect Components In Flow Main Panel    002Added${action_number}    first   ${a}    ${b}

Check Step ${step_number} As End Step
    ${step_id}    Set Variable    001Added${step_number}
    ${title}    Set Variable   ${steps}[${step_id}]
    Click Component    ${step_id}
    Click End Step Checkbox In Flow Properties    001Added${step_number}
    Remove From Dictionary    ${steps}    ${step_id}
    Set To Dictionary    ${steps}    001END${step_number}   ${title}
