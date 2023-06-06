*** Settings ***
Resource            Blueprint/TestCasesResources/Flow/CreateFlow/common_main_panel_imports.Resource
Suite Setup         Navigate To Flows-Page-Create-Flow
Suite Teardown      Delete Flow Process In Flow Header
Test Setup          Move components to the main panel
Test Teardown       Clean Components Added
Force Tags          CREATE_FLOW

*** Variables ***
${red_color}                     rgb(255, 114, 105)
${turquoise_color}               rgb(0, 217, 194)
${action_to_action_message}      Cannot connect an action to another action.
${action_connection_message}     Actions can only have a single outgoing connection.
${connect_itself_message}        Element cannot be connected to itself.

*** Test Cases ***
Verify that an action cannot connect to another action
    Connect Components In Flow Main Panel    002Added1    002Added2    5    4
    ${text}    Get Popup Message Text
    Message Pop Up Should Be Equal    ${text}    ${action_to_action_message}

Verify that an action without connections has a red border
    ${color}    Obtain Component Color In Flow Main Panel    002Added1
    Component Rgb Color Should Be Equal    ${color}    ${red_color}

Verify that an action border is red color when it has incoming and outgoing connections
    Connect Components In Flow Main Panel    002Added1    001Added1    5    4
    Connect Components In Flow Main Panel    001Added2    002Added1    2    12
    ${color}    Obtain Component Color In Flow Main Panel    002Added1
    Component Rgb Color Should Be Equal    ${color}    ${red_color}

Verify that an action has a button dropdown
    ${found_result}    is_dropdown_not_found_in_flow_main_panel    002Added1
    Component Should Have A Button Dropdown    ${found_result}

Verify that an action cannot have more than one outgoing connection    
    Connect Components In Flow Main Panel    002Added2    001Added1    5    6
    Connect Components In Flow Main Panel    002Added2    001Added2    2    8
    ${text}    Get Popup Message Text
    Message Pop Up Should Be Equal    ${text}    ${action_connection_message}

Verify that an action can connect to a step
    Connect Components In Flow Main Panel    002Added1    001Added1    5    4
    Component Dot Should Be Connected    002Added1    5

Verify that an action connected to a final step has a turquoise color    
    Click Component    001Added1
    Click End Step Checkbox In Flow Properties    001Added1
    Connect Components In Flow Main Panel    first    002Added2    5    14
    Connect Components In Flow Main Panel    002Added2    001END1    2    3
    ${color}    Obtain Component Color In Flow Main Panel    001END1
    Component Rgb Color Should Be Equal    ${color}    ${turquoise_color}

Verify that an action can move in the canvas
    ${x_source}    ${y_source}    Obtain X And Y Position Component In Flow Main Panel    002Added1
    Move Component To Specific Position In Flow Main Panel    002Added1    0    60
    ${x_target}    ${y_target}    Obtain X And Y Position Component In Flow Main Panel    002Added1
    Component Should Have Different Positions    ${x_source}    ${x_target}
    Component Should Have Different Positions    ${y_source}    ${y_target}

Verify that an action can clone    
    clone_component_in_flow_main_panel    002Added1
    ${dictionary}    Obtain Dictionary Status In Flow Main Panel
    Dictionary Should Contain Component    ${dictionary}    002Added3

Verify that an action can delete
    Delete Component In Flow Main Panel    002Added1
    ${dictionary}    Obtain Dictionary Status In Flow Main Panel
    Dictionary Should Not Contain Component    ${dictionary}    002Added1

Verify that an action cannot connect to itself
    Connect Components In Flow Main Panel    002Added2    002Added2    4    11
    ${text}    Get Popup Message Text
    Message Pop Up Should Be Equal    ${text}    ${connect_itself_message}   

*** Keywords ***
Move components to the main panel
    Move Action To Board Position    55    35
    Move Step To Board Position    40    50
    Move Action To Board Position    70    50
    Move Step To Board Position    55    65 
