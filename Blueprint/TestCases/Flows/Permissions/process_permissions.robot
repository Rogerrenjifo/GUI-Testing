*** Settings ***
Resource            Blueprint/TestCasesResources/Flow/Permissions/process_permissions_imports.resource
Suite Setup         Navigate to Flows-page-Permission
Test Teardown       Reload Permissions Tab
Suite Teardown      Delete Flow Process In Flow Header
Force Tags          PERMISSIONS    FLOWS

*** Variables ***
${red_label_color}        rgba(255, 114, 105, 1)
${red_border_color}       rgb(255, 114, 105)
${purple_border_color}    rgb(117, 105, 255)
${purple_button_color}    rgba(117, 105, 255, 1)
${required_message}       Permission Required
${text_box_message}       Select users for this role
${items_message}          No items found

*** Test Cases ***
Verify that the "Initiate Process" label color changes to red when the box is empty
    [Tags]    P3
    Delete All Users In Dropdown In Process Permission
    The Rgb Color Of Label Should Be As Expected    ${red_label_color}

Verify that the arrow displays the dropdown
    [Tags]    P3
    Click Dropdown Arrow In Process Permission
    Dropdown Process Permissions Should Be Visible

Verify that the box border color changes when clicking the arrow
    [Tags]    P2
    Click Dropdown Arrow In Process Permission
    The Rgb Color Of Text Box Should Be As Expected    ${purple_border_color}

Verify that "x" button background color changes when the mouse hovers it
    [Tags]    P3
    ${user_list}    Obtain User List Selected In Text Box In Process Permissions
    Mouse Hover Delete Button In Process Permissions    ${user_list}[0]
    The Rgb Color Of Delete Button Should As Expected    ${user_list}[0]    ${purple_button_color}

Verify that an option can be selected in the dropdown
    [Tags]    P1
    Click Dropdown Arrow In Process Permission
    Select User From Dropdown In Process Permission    Denisse Cordova
    Users Selected List Process Permissions Should Contain    Denisse Cordova

Verify that the message "No items found" is displayed when typing an option that does not match with dropdown options
    [Tags]    P2
    Click Dropdown Arrow In Process Permission
    Type Name User In Dropdown In Process Permission    de34rf
    Dropdown Process Permissions Should Contain    ${items_message}

Verify that the box border changes to red when the box is empty
    [Tags]    P3
    Delete All Users In Dropdown In Process Permission
    The Rgb Color Of Text Box Should Be As Expected    ${red_border_color}

Verify that the message "Select user for this role" is displayed when the box is empty
    [Tags]    P1
    Delete All Users In Dropdown In Process Permission
    Message In Empty Text Box Process Permissions Should Be As Expected    ${text_box_message}

Verify that the message "Permission required" is displayed when the box is empty
    [Tags]    P1
    Delete All Users In Dropdown In Process Permission
    Message Empty Dropdow Process Permissions Should Be As Expected    ${required_message}

Verify that the box border is purple after choosing a dropdown option
    [Tags]    P3
    Click Dropdown Arrow In Process Permission
    Select User From Dropdown In Process Permission    Fabian Cabrejo
    The Rgb Color Of Text Box Should Be As Expected    ${purple_border_color}

Verify that the dropdown is not visible after choosing a dropdown option
    [Tags]    P2
    Click Dropdown Arrow In Process Permission
    Select User From Dropdown In Process Permission    Denisse Cordova
    Dropdown Process Permissions Should Not Be Visible

Verify that the box border is purple after retracting the dropdown
    [Tags]    P3
    Click Dropdown Arrow In Process Permission
    Click Dropdown Arrow In Process Permission
    The Rgb Color Of Text Box Should Be As Expected    ${purple_border_color}

Verify that the "Clear all" button erases all the selected options in the box
    [Tags]    P3
    Click Dropdown Arrow In Process Permission
    Delete All Users In Dropdown In Process Permission
    Users Selected List Process Permissions Should Be Empty

Verify that a selected option is not repeated in the dropdown options
    [Tags]    P2
    Click Dropdown Arrow In Process Permission
    Select User From Dropdown In Process Permission    Denisse Cordova
    Click Dropdown Arrow In Process Permission
    Dropdown Process Permissions Should Not Contain    Denisse Cordova

Verify that "Everyone" is selected by default
    [Tags]    P1
    ${user_list}    Obtain User List Selected In Text Box In Process Permissions
    Users Selected List Process Permissions Should Contain    ${user_list}[0]

Verify that a user can be deleted from the text box 
    [Tags]    P2
    Click Dropdown Arrow In Process Permission
    Select User From Dropdown In Process Permission    Fabian Cabrejo
    Delete One Selected User In Dropdown In Process Permission    Fabian Cabrejo
    Users Selected List Process Permissions Should Not Contain    Fabian Cabrejo

Verify that a user can be found by typing and being selected from the dropdown
    [Tags]    P1
    Click Dropdown Arrow In Process Permission
    Add User To Initiate Process By Typing Process In Process Permissions    Maria Mamani
    Users Selected List Process Permissions Should Contain    Maria Mamani

Verify that a group can be selected in the dropdown
    [Tags]    P1
    Click Dropdown Arrow In Process Permission
    Select User From Dropdown In Process Permission    new_group_test
    Users Selected List Process Permissions Should Contain    new_group_test

Verify that text box allows alphanumeric characters
    [Tags]    P2
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
    [Tags]    P2
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
    Type Name User In Dropdown In Process Permission    ${alphanumeric_characters}
    Text Box Process Permissions Should Not Be Empty

Try to type special characters in the text box
    [Arguments]    ${special_characters}
    Type Name User In Dropdown In Process Permission    ${special_characters}
    Text Box Process Permissions Should Not Be Empty
