*** Settings ***
Resource   Blueprint/TestCasesResources/E2E/electricity_supply/electricity_supply_create_form.resource
Resource   Blueprint/TestCasesResources/E2E/electricity_supply/electricity_supply_create_flow.resource
Resource   Blueprint/TestCasesResources/E2E/electricity_supply/electricity_supply_permissions.resource

Force Tags        e2e

*** Variables ***
${flow_name}   Electricity Supply-GUI DEMO
@{users}   Rocío Morales   Martin Alvarez   Celeste Palet
${electricity_departament_group}   Electricity Departament - GUI DEMO 3
${inspectors_group}   Inspectors - GUI DEMO 3
${technicians_group}   Technicians - GUI DEMO 3
${create_form_tab}   Create Form
${create_flow_tab}   Create Flow
${permission_tab}   Permissions
${publish_tab}   Publish

*** Test Cases ***
Verify that user is able to create and publish a complete flow process
    Create Groups If Not Exist
    ${flow_name}=   Create A New Flow With Random Code    ${flow_name}
    Flow Page Should Be Displayed   ${flow_name}
    Set Sections In Create Form
    Sections And Components Should Be Displayed
    Flow Tab Should Be Marked   ${create_form_tab}
    Click Tab In Flow Header    ${create_flow_tab}
    Set And Conect Actions And Steps In Board
    Actions And Steps Should Be Displayed
    Flow Tab Should Be Marked    ${create_flow_tab}
    Click Tab In Flow Header    ${permission_tab}
    Set Users In Permissions
    Selected Groups Should Be Displayed
    Flow Tab Should Be Marked    ${permission_tab}
    Click Tab In Flow Header    ${publish_tab}
    Click Save Publish Button
    Go To Project Process In Main Menu   ${flow_name}
    Project Title Should Be    ${flow_name}

*** Keywords ***
Create Groups If Not Exist
    Create Group If Not Exist   ${electricity_departament_group}     ${users}
    Create Group If Not Exist   ${inspectors_group}    ${users}
    Create Group If Not Exist   ${technicians_group}   ${users}

Set Sections In Create Form
    Set First Section In Create Form
    Set Second Section In Create Form
    Set Third Section In Create Form

Sections And Components Should Be Displayed
    First Section Components Should Be Displayed
    Second Section Components Should Be Displayed
    Third Section Components Should Be Displayed
    Sections Should Be Displayed

Set And Conect Actions And Steps In Board
    Set Components In Board
    Conect Components In Board
    Set End Step
