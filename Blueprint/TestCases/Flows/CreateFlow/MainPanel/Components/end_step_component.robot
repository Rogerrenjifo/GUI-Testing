*** Settings ***
Resource            Blueprint/TestCasesResources/Flow/CreateFlow/common_main_panel_imports.Resource
Suite Setup         Navigate To Flows-Page-Create-Flow
Suite Teardown      Delete Flow Process In Flow Header
Test Setup          Move actions and steps to the main panel
Test Teardown       Clean Components Added
Force Tags          CREATE_FLOW

*** Variables ***
${red_color}          rgb(255, 114, 105)
${turquoise_color}    rgb(0, 217, 194)

*** Test Cases ***
Verify that a final step has a button dropdown
    Click Component    001Added1
    Click End Step Checkbox In Flow Properties    001Added1
    ${found_result}    Is Dropdown Not Found In Flow Main Panel    001END1
    Component Should Have A Button Dropdown    ${found_result}

Verify that a final step is red border color when it does not have incoming and outgoing connections
    Click Component    001Added1
    Click End Step Checkbox In Flow Properties    001Added1
    ${color}    Obtain Component Color In Flow Main Panel    001END1
    Component Rgb Color Should Be Equal    ${color}    ${red_color}

Verify that a final step border changes to turquoise color when it has incoming connection
    Click Component    001Added1
    Click End Step Checkbox In Flow Properties    001Added1
    Connect Components In Flow Main Panel    002Added1    001END1    2    12
    ${color}    Obtain Component Color In Flow Main Panel    001END1
    Component Rgb Color Should Be Equal    ${color}    ${turquoise_color}

Verify that a final step cannot have an outgoing connection    
    Click Component    001Added1
    Click End Step Checkbox In Flow Properties    001Added1
    Connect Components In Flow Main Panel    001END1    002Added1    5    8
    Component Dot Should Be Connected    001END1    5    False

Verify that a final step can have more than one incoming connection
    Click Component    001Added1
    Click End Step Checkbox In Flow Properties    001Added1
    Connect Components In Flow Main Panel    002Added1    001END1    5    6
    Connect Components In Flow Main Panel    002Added2    001END1    5    8
    Component Dot Should Be Connected    001END1    6
    Component Dot Should Be Connected    001END1    8

Verify that a final step can clone 
    Click Component    001Added1
    Click End Step Checkbox In Flow Properties    001Added1
    Clone Component In Flow Main Panel    001END1
    ${dictionary}    Obtain Dictionary Status In Flow Main Panel
    Dictionary Should Contain Component    ${dictionary}    001END2

Verify that a final step can delete
    Click Component    001Added1
    Click End Step Checkbox In Flow Properties    001Added1
    Delete Component In Flow Main Panel    001END1
    ${dictionary}    Obtain Dictionary Status In Flow Main Panel
    Dictionary Should Not Contain Component    ${dictionary}    001END1

Verify that a final step can move in the canvas
    Click Component    001Added1
    Click End Step Checkbox In Flow Properties    001Added1
    ${x_source}    ${y_source}    Obtain X And Y Position Component In Flow Main Panel    001END1
    Move Component To Specific Position In_flow_main_panel    001END1    100    0
    ${x_target}    ${y_target}    Obtain X And Y Position Component In Flow Main Panel    001END1
    Component Should Have Different Positions   ${x_source}    ${x_target}
    Component Should Have Different Positions    ${y_source}    ${y_target}

*** Keywords ***
Move actions and steps to the main panel
    Move Action To Board Position    55    35
    Move Step To Board Position    40    50
    Move Step To Board Position    70    50
    Move Action To Board Position    40    20
