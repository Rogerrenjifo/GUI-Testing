*** Settings ***
Resource            Blueprint/TestCasesResources/Flow/CreateFlow/common_main_panel_imports.resource
Suite Setup         Navigate To Flows-Page-Create-Flow
Suite Teardown      Delete Flow Process In Flow Header
Test Teardown       Clean Components Added
Test Setup          Edit the main panel
Force Tags          CREATE_FLOW   FLOW

*** Variables ***
${red_color}          rgb(255, 114, 105)
${turquoise_color}    rgb(0, 217, 194)

*** Test Cases ***
Verify that the initial step has red border when it has not outgoing connections
    ${color}    Obtain Component Color In Flow Main Panel    first
    Component Rgb Color Should Be Equal    ${color}    ${red_color}

Verify that the initial step border color changes to turquoise when an arrow outgoing of it
    Connect Components In Flow Main Panel    first    002Added1    6    16
    ${color}    Obtain Component Color In Flow Main Panel    first
    Component Rgb Color Should Be Equal    ${color}    ${turquoise_color}

Verify that the initial step does not have a button dropdown
    ${found_result}    Is Dropdown Not Found In Flow Main Panel    first
    Component Should Not Have A Button Dropdown    ${found_result}

Verify that the initial step can move in the canvas
    ${x_source}    ${y_source}    Obtain X And Y Position Component In Flow Main Panel    first
    Move Component To Specific Position In Flow Main Panel    first    60    30
    ${x_target}    ${y_target}    Obtain X And Y Position Component In Flow Main Panel    first
    Component Should Have Different Positions    ${x_source}    ${x_target}
    Component Should Have Different Positions    ${y_source}    ${y_target}

*** Keywords ***
Edit the main panel
    Move Action To Board Position    55    35
    Move Step To Board Position    40    50
