*** Settings ***
Resource            Blueprint/TestCasesResources/Flow/Permissions/common_flow_admin_imports.resource
Suite Setup         Navigate to Flows-page-Permission
Test Teardown       Reload Permissions Tab
Suite Teardown      Delete Flow Process In Flow Header
Force Tags          PERMISSIONS   FLOWS   HOLI

*** Variables ***
${red_label_color}        rgba(255, 114, 105, 1)
${red_border_color}       rgb(255, 114, 105)
${purple_border_color}    rgb(117, 105, 255)
${purple_button_color}    rgba(117, 105, 255, 1)
${required_message}       Permission Required
${text_box_message}       Select users for this role
${items_message}          No items found

*** Test Cases ***
Verify that the "Flow admin" label color changes to red when the box is empty
    Delete All Users In Dropdown In Flow Permissions
    Rgb Color Of Label Should Be As Expected    ${red_label_color}

Verify that the arrow displays the dropdown
    Click Dropdown Arrow In Flow Permissions
    Dropdown Should Be Visible

Verify that the box border color changes when clicking the arrow
    Click Dropdown Arrow In Flow Permissions
    Rgb Color Of Text Box Should Be As Expected    ${purple_border_color}

Verify that "x" button background color changes when the mouse hovers it
    ${user_list}    Obtain User List Selected In Text Box In Flow Permissions
    Mouse Hover Delete Button In Flow Permissions    ${user_list}[0]
    Rgb Color Of Delete Button Should As Expected    ${user_list}[0]    ${purple_button_color}

Verify that an option can be selected in the dropdown
    Click Dropdown Arrow In Flow Permissions
    Select User From Dropdown In Flow Permissions    Denisse Cordova
    Users Selected List Should Contain    Denisse Cordova

Verify that the message "No items found" is displayed when typing an option that does not match with dropdown options
    Click Dropdown Arrow In Flow Permissions
    Type Name User In Dropdown In Flow Permissions    de34rf
    Dropdown Should Contain    ${items_message}

Verify that the box border changes to red when the box is empty
    Delete All Users In Dropdown In Flow Permissions
    Rgb Color Of Text Box Should Be As Expected    ${red_border_color}

Verify that the message "Select user for this role" is displayed when the box is empty
    Delete All Users In Dropdown In Flow Permissions
    Message In Empty Text Box Should Be As Expected    ${text_box_message}

Verify that the message "Permission required" is displayed when the box is empty
    Delete All Users In Dropdown In Flow Permissions
    Message Empty Dropdow Should Be As Expected    ${required_message}

Verify that the box border is purple after choosing a dropdown option
    Click Dropdown Arrow In Flow Permissions
    Select User From Dropdown In Flow Permissions    Fabian Cabrejo
    Rgb Color Of Text Box Should Be As Expected    ${purple_border_color}

Verify that the dropdown is not visible after choosing a dropdown option
    Click Dropdown Arrow In Flow Permissions
    Select User From Dropdown In Flow Permissions    Denisse Cordova
    Dropdown Should Not Be Visible

Verify that the box border is purple after retracting the dropdown
    Click Dropdown Arrow In Flow Permissions
    Click Dropdown Arrow In Flow Permissions
    Rgb Color Of Text Box Should Be As Expected    ${purple_border_color}

Verify that the "Clear all" button erases all the selected options in the box
    Click Dropdown Arrow In Flow Permissions
    Delete All Users In Dropdown In Flow Permissions
    Users Selected List Should Be Empty

Verify that a selected option is not repeated in the dropdown options
    Click Dropdown Arrow In Flow Permissions
    Select User From Dropdown In Flow Permissions    Denisse Cordova
    Click Dropdown Arrow In Flow Permissions
    Dropdown Should Not Contain    Denisse Cordova

Verify that a user is selected by default in Flow Admin text box
    ${user_list}    Obtain User List Selected In Text Box In Flow Permissions
    Users Selected List Should Contain    ${user_list}[0]

Verify that a user can be deleted from the text box 
    Click Dropdown Arrow In Flow Permissions
    Select User From Dropdown In Flow Permissions    Fabian Cabrejo
    Delete One Selected User In Dropdown In Flow Permissions    Fabian Cabrejo
    Users Selected List Should Not Contain    Fabian Cabrejo

Verify that a user can be found by typing and being selected from the dropdown
    Click Dropdown Arrow In Flow Permissions
    Add New Flow Admin By Typing Process In Flow Permission    Maria Mamani
    Users Selected List Should Contain    Maria Mamani

Verify that a group can be selected in the dropdown
    Click Dropdown Arrow In Flow Permissions
    Select User From Dropdown In Flow Permissions    new_group_test
    Users Selected List Should Contain    new_group_test

Verify that text box allows alphanumeric characters
    [Template]    Try to type alphanumeric characters in the text box
    q
    w
    e
    r
    t
    y
    u
    i
    o
    p
    a
    s
    d
    f
    g
    h
    j
    k
    l
    z
    x
    c
    v
    b
    n
    m
    1
    2
    3
    4
    5
    6
    7
    8
    9
    0

Verify that text box allows special characters
    [Template]    Try to type special characters in the text box
    ~
    !
    @
    $
    %
    ^
    &
    *
    (
    )
    -
    _
    =
    +
    `
    {
    }
    [
    ]
    *
    |
    <
    >
    /
    ?
    
*** Keywords ***
Try to type alphanumeric characters in the text box
    [Arguments]    ${alphanumeric_characters}
    Type Name User In Dropdown In Flow Permissions    ${alphanumeric_characters}
    Text Box Should Not Be Empty

Try to type special characters in the text box
    [Arguments]    ${special_characters}
    Type Name User In Dropdown In Flow Permissions    ${special_characters}
    Text Box Should Not Be Empty
