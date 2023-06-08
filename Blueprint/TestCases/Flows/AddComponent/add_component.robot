*** Settings ***
Documentation      This test Suite tests the actions of adding a 'step' and 'actions' component to the main board.
...                the position of the component is given by a percentage pair (x,y), where 0,0 is the top left corner
...                and (100,100) is the downright corner of the canvas board.

Library            Blueprint.Steps.Actions.Flows.flow_components_actions.FlowComponentsActions
Library            Blueprint.Steps.Actions.Flows.flow_main_panel_actions.FlowMainPanelActions
Library            Blueprint.Steps.Verifications.Flow.CreateFlow.add_components_verifications.AddComponentsVerification
Resource           Blueprint/TestCasesResources/navigate.resource

Suite Setup        Navigate To Flows-Page-Create-Flow
Suite Teardown     Delete Flow Process In Flow Header
Force Tags         ADD_COMPONENT    CREATE_FLOW   FLOWS

*** Test Cases ***
Verify that the "Step" component can be added to 0%, 0% position on canvas board.
    [Tags]    SMOKE
    Move Step To Board Position                0     0
    The Component Should Be Added To The Main Board        001Added1

Verify that the "Step" component can be added to 0%, 100% position on canvas board.
    
    Move Step To Board Position                0     100
    The Component Should Be Added To The Main Board        001Added2

Verify that the "Step" component can be added to 100%, 0% position on canvas board.
    
    Move Step To Board Position                100   0
    The Component Should Be Added To The Main Board        001Added3

Verify that the "Step" component can be added to 100%, 100% position on canvas board.
    
    Move Step To Board Position                100   100
    The Component Should Be Added To The Main Board        001Added4

Verify that the "Step" component can not be moved to the main menu.
    
    Move Step To Main Menu Position            50    50
    The Component Should Not Be Added To The Main Board    001Added5

Verify that the "step" is not added to the "canvas" board when it is dropped in the component section. use case 1.
    
    Move Step To Component Panel Position      50    50
    The Component Should Not Be Added To The Main Board    001Added5

Verify that the "step" is not added to the "canvas" board when it is dropped in the header section. use case 1.
    
    Move Step To Header Position               50    50
    The Component Should Not Be Added To The Main Board    001Added5

Verify that the "step" is not added to the "canvas" board when it is dropped in the properties section. use case 1.
    
    Move Step To Properties Position           50    50
    The Component Should Not Be Added To The Main Board    001Added5

Verify that the "step" is not added to the "canvas" board when it is dropped in the component section. use case 2.
    [Tags]        BUG_BG-244    
    Click And Hold Step Component
    Move Component To Target Position    canvas       50    50
    Move Component To Target Position    component    100   17
    Drop Component
    The Component Should Not Be Added To The Main Board    001Added5

Verify that the "step" is not added to the "canvas" board when it is dropped in the component section. use case 3.
    [Tags]        BUG_BG-244    
    Click And Hold Step Component
    Move Component To Target Position    canvas       50    50
    Move Component To Target Position    component    0     0
    Drop Component
    The Component Should Not Be Added To The Main Board    001Added6

Verify that the "step" is not added to the "canvas" board when it is dropped in the header section. use case 2.
    [Tags]        BUG_BG-244    
    Click And Hold Step Component
    Move Component To Target Position    canvas       50    50
    Move Component To Target Position    header       0     0
    Drop Component
    The Component Should Not Be Added To The Main Board    001Added7

Verify that the "step" is not added to the "canvas" board when it is dropped in the properties section. use case 2.
    [Tags]        BUG_BG-244    
    Click And Hold Step Component
    Move Component To Target Position    canvas       50    50
    Move Component To Target Position    properties       0     0
    Drop Component
    The Component Should Not Be Added To The Main Board    001Added8

Verify that the "Action" component can be added to 0%, 0% position on canvas board.
    [Tags]    SMOKE
    Move Action To Board Position              0     0
    The Component Should Be Added To The Main Board        002Added1

Verify that the "Action" component can be added to 0%, 100% position on canvas board.
    [Tags]    SMOKE
    Move Action To Board Position              0     100
    The Component Should Be Added To The Main Board        002Added2

Verify that the "Action" component can be added to the 100%, 0% position on canvas board.
    
    Move Action To Board Position              100   0
    The Component Should Be Added To The Main Board        002Added3

Verify that the "Action" component can be added to the 100%, 100% position on canvas board.
    
    Move Action To Board Position              100   100
    The Component Should Be Added To The Main Board        002Added4

Verify that the "Action" component can not be moved to the main menu.
    
    Move Action To Main Menu Position          50    50
    The Component Should Not Be Added To The Main Board    002Added5

Verify that the "action" is not added to the "canvas" board when it is dropped in the component section. use case 1.
    
    Move Action To Component Panel Position    50    50
    The Component Should Not Be Added To The Main Board    002Added5

Verify that the "action" is not added to the "canvas" board when it is dropped in the header section. use case 1.
    
    Move Action To Header Position             50    50
    The Component Should Not Be Added To The Main Board    002Added5

Verify that the "action" is not added to the "canvas" board when it is dropped in the properties section. use case 1.
    
    Move Action To Properties Position         50    50
    The Component Should Not Be Added To The Main Board    002Added5

Verify that the "action" is not added to the "canvas" board when it is dropped in the component section. use case 2.
    [Tags]        BUG_BG-244    
    Click And Hold Action Component
    Move Component To Target Position    canvas       50    50
    Move Component To Target Position    component    100   17
    Drop Component
    The Component Should Not Be Added To The Main Board    002Added5

Verify that the "action" is not added to the "canvas" board when it is dropped in the component section. use case 3.
    [Tags]        BUG_BG-244    
    Click And Hold Action Component
    Move Component To Target Position    canvas       50    50
    Move Component To Target Position    component    50    50
    Drop Component
    The Component Should Not Be Added To The Main Board    002Added6

Verify that the "action" is not added to the "canvas" board when it is dropped in the header section. use case 2.
    [Tags]        BUG_BG-244    
    Click And Hold Action Component
    Move Component To Target Position    canvas       50    50
    Move Component To Target Position    header       50    50
    Drop Component
    The Component Should Not Be Added To The Main Board    002Added7

Verify that the "action" is not added to the "canvas" board when it is dropped in the properties section. use case 2.
    [Tags]        BUG_BG-244    
    Click And Hold Action Component
    Move Component To Target Position    canvas       50    50
    Move Component To Target Position    properties    50    50
    Drop Component
    The Component Should Not Be Added To The Main Board    002Added8
