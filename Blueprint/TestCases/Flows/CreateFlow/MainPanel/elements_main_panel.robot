*** Settings ***
Resource            Blueprint/TestCasesResources/Flow/CreateFlow/common_main_panel_imports.resource
Suite Setup         Navigate To Flows-Page-Create-Flow
Suite Teardown      Delete Flow Process In Flow Header
Test Teardown       Clean Components Added
Test Setup          Redirect and move components to the main panel
Force Tags          CREATE_FLOW   FLOW

*** Variables ***
${dropdown_color}    rgb(117, 105, 255)
${already_connected_message}    These elements are already connected.

*** Test Cases ***
Verify that a button dropdown color changes when the cursor is over it
    [Tags]    BG-237   BUG
    ${color_dropdown}    Obtain Dropdown Color In Flow Main Panel    001Added1
    Component Rgb Color Should Be Equal    ${color_dropdown}    ${dropdown_color}

Verify that a button dropdown displays the menu with clone and delete options
    ${options}    Obtains Dropdown Options In Flow Main Panel    001Added1
    Dropdown Options Should Be Displayed    ${options}

Verify that an arrow cannot connect to an endpoint already connected
    Connect Components In Flow Main Panel    001Added1    002Added2    4    9
    Connect Components In Flow Main Panel    001Added2    002Added2    4    9
    Component Dot Should Be Connected    001Added2    4    False

Verify that an arrow can be deleted
    Connect Components In Flow Main Panel    001Added1    002Added2    4    9
    Connect Components In Flow Main Panel    001Added1    first    4    4
    Component Dot Should Be Connected    001Added1    4    False

Verify that an arrow cannot connect twice to the between components already connected
    Connect Components In Flow Main Panel    001Added1    002Added2    4    9
    Connect Components In Flow Main Panel    001Added1    002Added2    5    8
    ${text}    Get Popup Message Text
    Message Pop Up Should Be Equal    ${text}      ${already_connected_message}   
  
Verify that the main panel has the start component and the initial step
    ${dictionary}    Obtain Dictionary Status In Flow Main Panel
    Dictionary Should Contain Component    ${dictionary}    start
    Dictionary Should Contain Component    ${dictionary}    first

*** Keywords ***
Redirect and move components to the main panel
    Move Action To Board Position    55    35
    Move Step To Board Position    40    50
    Move Action To Board Position    70    50
    Move Step To Board Position    55    65
