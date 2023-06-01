*** Settings ***
Resource            Blueprint/TestCasesResources/Flow/CreateFlow/common_main_panel_imports.Resource
Suite Setup         Navigate To Flows-Page-Create-Flow
Suite Teardown      Delete Flow Process In Flow Header
Test Teardown       Clean Components Added
Test Setup          Initialize the main panel
Force Tags          CREATE_FLOW

*** Variables ***
${turquoise_color}    rgb(0, 217, 194)

*** Test Cases ***
Verify that the Start component does not have a button dropdown  
    ${found_result}    Is Dropdown Not Found In Flow Main Panel    start
    Component Should Not Have A Button Dropdown    ${found_result}

Verify that the Start component has turquoise border
    ${color}    ObtaiN Component Color In Flow Main Panel    start
    Component Rgb Color Should Be Equal    ${color}    ${turquoise_color}

Verify that the Start component can only have a single outgoing connection
    ${dots_list}    Obtain Dots List Of Start Component In Flow Main Panel 
    Component Should Have A Single Dot    ${dots_list}

Verify that the Start component cannot disconnect from the Initial Step
    Connect Components In Flow Main Panel    first    first    4    9
    Component Dot Should Be Connected    first    4

Verify that the Start component can move in the canvas
    ${x_source}    ${y_source}    Obtain X And Y Position Component In Flow Main Panel    start
    Move Component To Specific Position In Flow Main Panel    start    0    0
    ${x_target}    ${y_target}    Obtain X And Y Position Component In Flow Main Panel    start
    Component Should Have Different Positions    ${x_source}    ${x_target}
    Component Should Have Different Positions    ${y_source}    ${y_target}

*** Keywords ***
Initialize the main panel
    Move Action To Board Position    55    35
    Move Step To Board Position    40    50
