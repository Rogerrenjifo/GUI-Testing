*** Settings ***
Documentation      This test Suite tests the actions of adding a 'step' and 'actions' component to the main board.
...                the position of the component is given by a percentage pair (x,y), where 0,0 is the top left corner
...                and (100,100) is the downright corner of the canvas board.
Library            Blueprint.Steps.Actions.Flows.flow_components_actions.FlowComponentsActions
Library            Blueprint.Steps.Actions.Flows.flow_main_panel_actions.FlowMainPanelActions
Library            Blueprint.Steps.Verifications.Flow.CreateFlow.add_components_verifications.AddComponentsVerification
Library            Blueprint.Steps.Verifications.Flow.CreateFlow.create_flow_main_panel_verification.CreateFlowMainPanelVerifications     
Resource           Blueprint/TestCasesResources/navigate.resource

Suite Setup        Navigate To Flows-Page-Create-Flow And Add Components
Suite Teardown     Delete Flow Process In Flow Header
Force Tags         ADD_COMPONENTS    CREATE_FLOW   FLOWS    ROGER

*** Variables ***
${red_color}              rgb(255, 114, 105)
${step_id}                001Added1
${action_id}              002Added1

*** Test Cases ***
Verify that the color of the "step" dropped is red.
    ${color}    Obtain Component Color In Flow Main Panel    ${step_id}
    Component Rgb Color Should Be Equal    ${color}    ${red_color}

Verify that the color of the "action" dropped is red.
    ${color}    Obtain Component Color In Flow Main Panel    ${action_id}
    Component Rgb Color Should Be Equal    ${color}    ${red_color}        

Verify that "step properties" are displayed when an step is dropped on a canvas board.
    Click Component    ${step_id}
    The Component Properties Should Be Displayed    New Step 1

Verify that "action properties" are displayed when an action is dropped on a canvas board.
    Click Component    ${action_id}
    The Component Properties Should Be Displayed    New Action 1

Verify that "the step name" is not repeated when an step is dropped on a canvas board.
    Move Step To Board Position           0    0
    Component Should Have Different Title   001Added1    001Added2
    
Verify that "the action name" is not repeated when an action is dropped on a canvas board.
    Move Action To Board Position         100    100
    Component Should Have Different Title   002Added1    002Added2

Verify that the "step" component can be dropped over other component.
    Move Step To Board Position           50    30
    The Component Should Be Added To The Main Board        001Added3

Verify that the "Action" component can be dropped over other component.
    Move Action To Board Position         80    60
    The Component Should Be Added To The Main Board        002Added3

*** Keywords ***
Navigate To Flows-Page-Create-Flow And Add Components
    Navigate To Flows-Page-Create-Flow
    Move Step To Board Position           50    30
    Move Action To Board Position         80    60
