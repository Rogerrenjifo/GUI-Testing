*** Settings ***
Resource            Blueprint/TestCasesResources/Flow/CreateFlow/common_main_panel_imports.resource
Suite Setup         Navigate To Flows-Page-Create-Flow
Suite Teardown      Delete Flow Process In Flow Header
Test Teardown       Clean Components Added
Test Setup          Enter Create Flow tab and move components to the main panel
Force Tags          CREATE_FLOW   FLOWS

*** Variables ***
${red_color}    rgb(255, 114, 105)
${turquoise_color}    rgb(0, 217, 194)
${connect_itself_message}    Element cannot be connected to itself.
${step_to_step_message}    Cannot connect a step to another step.
${already_connected_message}    These elements are already connected.

*** Test Cases ***
Verify that a step cannot connect to another step
    [Tags]    P1
    Connect Components In Flow Main Panel    001Added1    001Added2    5    4
    ${text}    Get Popup Message Text
    Message Pop Up Should Be Equal    ${text}    ${step_to_step_message} 

Verify that a step without connections has a red border
    [Tags]    P3
    ${color}    Obtain Component Color In Flow Main Panel    001Added1
    Component Rgb Color Should Be Equal    ${color}    ${red_color}

Verify that a step border changes to turquoise color when it has incoming and outgoing connections
    [Tags]    P3
    Connect Components In Flow Main Panel    002Added1    001Added1    5    4
    Connect Components In Flow Main Panel    001Added1    002Added2    2    12
    ${color}    Obtain Component Color In Flow Main Panel    001Added1
    Component Rgb Color Should Be Equal    ${color}    ${turquoise_color}

Verify that a step can clone
    [Tags]    P2
    Clone Component In Flow Main Panel    001Added1
    ${dictionary}    Obtain Dictionary Status In Flow Main Panel
    Dictionary Should Contain Component    ${dictionary}    001Added3

Verify that a step has a button dropdown
    [Tags]    P2
    ${found_result}    Is Dropdown Not Found In Flow Main Panel    001Added1
    Component Should Have A Button Dropdown    ${found_result}

Verify that a step can connect to an action
    [Tags]    P1
    Connect Components In Flow Main Panel    001Added1    002Added2    5    9
    Component Dot Should Be Connected    001Added1    5

Verify that a step can have more than one incoming and outgoing connections
    [Tags]    P1
    Connect Components In Flow Main Panel    002Added1    001Added1    5    6
    Connect Components In Flow Main Panel    001Added1    002Added2    2    12
    Connect Components In Flow Main Panel    002Added3    001Added1    5    8
    Connect Components In Flow Main Panel    001Added1    002Added4    4    9
    Component Dot Should Be Connected    001Added1    6
    Component Dot Should Be Connected    001Added1    2
    Component Dot Should Be Connected    001Added1    8
    Component Dot Should Be Connected    001Added1    4

Verify that a step can move in the canvas
    [Tags]    P1
    ${x_source}    ${y_source}    Obtain X And Y Position Component In Flow Main Panel    001Added1
    Move Component To Specific Position In Flow Main Panel    001Added1    20    100
    ${x_target}    ${y_target}    Obtain X And Y Position Component In Flow Main Panel    001Added1
    Component Should Have Different Positions    ${x_source}    ${x_target}
    Component Should Have Different Positions    ${y_source}    ${y_target}

Verify that a step cannot connect to itself
    [Tags]    P1
    Connect Components In Flow Main Panel    001Added1    001Added1    4    9
    ${text}    Get Popup Message Text
    Message Pop Up Should Be Equal    ${text}    ${connect_itself_message}

Verify that a step can delete
    [Tags]    P2
    Delete Component In Flow Main Panel    001Added1
    ${dictionary}    Obtain Dictionary Status In Flow Main Panel
    Dictionary Should Not Contain Component    ${dictionary}    001Added1

*** Keywords ***
Enter Create Flow tab and move components to the main panel
    Move Action To Board Position    55    35
    Move Step To Board Position    40    50
    Move Action To Board Position    70    50
    Move Step To Board Position    55    65
    Move Action To Board Position    55    80
    Move Action To Board Position    30    86
