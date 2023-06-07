*** Settings ***
Resource    Blueprint/TestCasesResources/E2E/electricity_supply/electricity_supply_importation.resource

*** Variables ***
${electricity_departament_group}   Electricity Departament - GUI DEMO 3
${inspectors_group}   Inspectors - GUI DEMO 3
${technicians_group}   Technicians - GUI DEMO 3

*** Keywords ***
Set Users In Permissions
    Delete All Users In Dropdown In Flow Permissions
    Add New Flow Admin By Typing Process In Flow Permission   ${electricity_departament_group}
    Delete All Users In Dropdown In Process Permission
    Add User To Initiate Process By Typing Process In Process Permissions    ${electricity_departament_group}
    Delete All Users In Section Visibility     3
    Add User To Section Visibility By Typing Process In Section Visibility    ${electricity_departament_group}    3
    Delete All Users In Section Visibility     4
    Add User To Section Visibility By Typing Process In Section Visibility   ${inspectors_group}   4
    Delete All Users In Section Visibility     5
    Add User To Section Visibility By Typing Process In Section Visibility   ${technicians_group}    5

Selected Groups Should Be Displayed
    User In Flow Permission Should Be   ${electricity_departament_group}
    User In Process Permission Should Be   ${electricity_departament_group}
    User In Section Visibility Should Be   ${electricity_departament_group}
    User In Section Visibility Should Be   ${inspectors_group}   4
    User In Section Visibility Should Be   ${technicians_group}   5
