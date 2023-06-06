*** Settings ***
Resource    Blueprint/TestCasesResources/Flow/CreateForm/common_imports.resource
Library    Blueprint.Steps.Verifications.Flow.CreateForm.create_form_add_component_verification.CreateFormAddComponentVerifications
Library    Blueprint.Steps.Verifications.Flow.CreateForm.create_form_add_section_verification.CreateFormAddSectionVerifications
Library    Blueprint.Steps.Actions.Flows.flow_main_panel_actions.FlowMainPanelActions
Library    Blueprint.Steps.Actions.Flows.flows_properties_actions.FlowPropertiesActions
Library    Blueprint.Steps.Actions.Flows.flow_components_actions.FlowComponentsActions
Library    Blueprint.Steps.Actions.MainMenu.main_menu_actions.MainMenuActions
Library    Blueprint.Steps.Utils.main_menu_manager.MainMenuManager

*** Variables ***
${flow_name}    AT19-Scenario-Scholarship-RMWY3

*** Keywords ***
Search Flow
    ${exists}   Flow Exists    ${flow_name}
    ${flow_name_for_edit}    Go To Flow For Edit    ${exists}    ${flow_name}
    Set Suite Variable    ${flow_name_for_edit}

Add Step With Name To Board
    [Arguments]    ${name}    ${x_coordenate}    ${y_coordenate}
    Move Step To Board Position    ${x_coordenate}    ${y_coordenate}
    Sleep    1
    Change Component Name In Flow Properties    ${name}

Add Action With Name To Board
    [Arguments]    ${name}    ${x_coordenate}    ${y_coordenate}
    Move Action To Board Position    ${x_coordenate}    ${y_coordenate}
    Sleep    1
    Change Component Name In Flow Properties    ${name}

Connect Step ${step_number} With Action ${action_number} From Point ${a} To Point ${b}
    Click Component    001Added${step_number}
    Connect Components In Flow Main Panel    001Added${step_number}    002Added${action_number}   ${a}    ${b}

Connect Action ${action_number} With Step ${step_number} From Point ${a} To Point ${b}
    Click Component    002Added${action_number}
    Connect Components In Flow Main Panel    002Added${action_number}    001Added${step_number}   ${a}    ${b}

Connect Initial Step With Action ${action_number} From Point ${a} To Point ${b}
    Click Component    first
    Connect Components In Flow Main Panel    first    002Added${action_number}    ${a}    ${b}

Check Step ${step_number} As End Step
    Click Component    001Added${step_number}
    Click End Step Checkbox In Flow Properties    001Added${step_number}
