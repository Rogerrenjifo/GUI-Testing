*** Settings ***
Resource    Blueprint/TestCasesResources/E2E/SwimmingCompetition/swimming_importations.resource

*** Variables ***
${flow_permission_user}   Rocío Morales
${process_permission_user}   Fabian Cabrejo
${applicant_information_section_user}   Rocío Morales 
${swimming_styles_section_user}    Denisse Cordova 

*** Keywords ***
Set Permissions
    Click Tab In Flow Header    Permissions
#    Sleep    1
#    Delete All Users In Dropdown In Flow Permissions
#    Add New Flow Admin By Typing Process In Flow Permission    ${flow_permission_user}
    Delete All Users In Dropdown In Process Permission
    Add User To Initiate Process By Typing Process In Process Permissions    ${process_permission_user}
    Delete All Users In Section Visibility     3
    Add User To Section Visibility By Typing Process In Section Visibility    ${applicant_information_section_user}    3
    Delete All Users In Section Visibility     4
    Add User To Section Visibility By Typing Process In Section Visibility   ${swimming_styles_section_user}   4
    Sleep   3

Verify Permissions
    User In Flow Permission Should Be    ${flow_permission_user}
    User In Process Permission Should Be    ${process_permission_user}
    User In Section Visibility Should Be    ${applicant_information_section_user}
    User In Section Visibility Should Be    ${swimming_styles_section_user}    4

Time To Save The Flow
    Sleep    12
