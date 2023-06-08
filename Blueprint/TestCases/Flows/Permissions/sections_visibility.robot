*** Settings ***
Resource            Blueprint/TestCasesResources/Flow/Permissions/sections_visibility_imports.resource
Suite Setup         Navigate to Flows-page-Permission
Test Teardown       Reload Permissions Tab
Suite Teardown      Delete Flow Process In Flow Header
Force Tags          PERMISSIONS    FLOWS

*** Variables ***
${red_border_color}       rgb(255, 114, 105)
${purple_border_color}    rgb(117, 105, 255)
${purple_button_color}    rgba(117, 105, 255, 1)
${required_message}       Permission Required
${text_box_message}       Select users able to see this section
${items_message}          No items found

*** Test Cases ***
Verify that the arrow displays the dropdown
    [Tags]    P2
    Click Dropdown Arrow In Section Visibility    3
    Dropdown In Section Visibility Should Be Visible    3

Verify that the box border color changes when clicking the arrow
    [Tags]    P3
    Click Dropdown Arrow In Section Visibility    3
    The Rgb Color Of Text Box Should Be As Expected    ${purple_border_color}    3

Verify that "x" button background color changes when the mouse hovers it
    [Tags]    P3
    ${user_list}    Obtain User List Selected In Text Box In Section Visibility    3
    Mouse Hover Delete Button In Section Visibility    ${user_list}[0]    3
    The Rgb Color Of Delete Button Should As Expected    ${user_list}[0]    ${purple_button_color}    3

Verify that an option can be selected in the dropdown
    [Tags]    P1
    Click Dropdown Arrow In Section Visibility    3
    Select User From Dropdown In Section Visibility    Denisse Cordova    3
    Users Selected List In Section Visibility Should Contain    Denisse Cordova    3

Verify that the message "No items found" is displayed when typing an option that does not match with dropdown options
    [Tags]    P2
    Click Dropdown Arrow In Section Visibility    3
    Type Name User From Dropdown In Section Visibility    de34rf5    3
    Dropdown In Section Visibility Should Contain    ${items_message}    3

Verify that the box border changes to red when the box is empty
    [Tags]    P3
    Delete All Users In Section Visibility    3
    The Rgb Color Of Text Box Should Be As Expected    ${red_border_color}    3

Verify that the message "Select user for this role" is displayed when the box is empty
    [Tags]    P2
    Delete All Users In Section Visibility    3
    Message In Empty Text Box In Section Visibility Should Be As Expected    ${text_box_message}    3

Verify that the message "Permission required" is displayed when the box is empty
    [Tags]    P2
    Delete All Users In Section Visibility    3
    Message Empty Dropdow In Section Visibility Should Be As Expected    ${required_message}    3

Verify that the box border is purple after choosing a dropdown option
    [Tags]    P3
    Click Dropdown Arrow In Section Visibility    3
    Select User From Dropdown In Section Visibility    Fabian Cabrejo    3
    The Rgb Color Of Text Box Should Be As Expected    ${purple_border_color}    3

Verify that the dropdown is not visible after choosing a dropdown option
    [Tags]    P2
    Click Dropdown Arrow In Section Visibility    3
    Select User From Dropdown In Section Visibility    Denisse Cordova    3
    Dropdown In Section Visibility Should Not Be Visible    3

Verify that the box border is purple after retracting the dropdown
    [Tags]    P3
    Click Dropdown Arrow In Section Visibility    3
    Click Dropdown Arrow In Section Visibility    3
    The Rgb Color Of Text Box Should Be As Expected    ${purple_border_color}    3

Verify that the "Clear all" button erases all the selected options in the box
    [Tags]    P2
    Click Dropdown Arrow In Section Visibility    3
    Delete All Users In Section Visibility    3
    Users Selected List In Section Visibility Should Be Empty    3

Verify that a selected option is not repeated in the dropdown options
    [Tags]    P2
    Click Dropdown Arrow In Section Visibility    3
    Select User From Dropdown In Section Visibility    Denisse Cordova    3
    Click Dropdown Arrow In Section Visibility    3
    Dropdown In Section Visibility Should Not Contain    Denisse Cordova    3

Verify that "Everyone" is selected by default
    [Tags]    P1
    ${user_list}    Obtain User List Selected In Text Box In Section Visibility    3
    Users Selected List In Section Visibility Should Contain    ${user_list}[0]    3

Verify that a user can be deleted from the text box 
    [Tags]    P2
    Click Dropdown Arrow In Section Visibility    3
    Select User From Dropdown In Section Visibility    Fabian Cabrejo    3
    Delete One Selected User In Dropdown In Section Visibility    Fabian Cabrejo    3
    Users Selected List In Section Visibility Should Not Contain    Fabian Cabrejo    3

Verify that a user can be found by typing and being selected from the dropdown
    [Tags]    P1
    Click Dropdown Arrow In Section Visibility    3
    Add User To Section Visibility By Typing Process In Section Visibility    Maria Mamani    3
    Users Selected List In Section Visibility Should Contain    Maria Mamani    3

Verify that a group can be selected in the dropdown
    [Tags]    P1
    Click Dropdown Arrow In Section Visibility    3
    Select User From Dropdown In Section Visibility    new_group_test    3
    Users Selected List In Section Visibility Should Contain    new_group_test    3

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
    Type Name User From Dropdown In Section Visibility     ${alphanumeric_characters}    3
    Text Box In Section Visibility Should Not Be Empty    3

Try to type special characters in the text box
    [Arguments]    ${special_characters}
    Type Name User From Dropdown In Section Visibility    ${special_characters}    3
    Text Box In Section Visibility Should Not Be Empty    3
