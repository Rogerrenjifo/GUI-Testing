*** Settings ***
Resource     Blueprint/TestCasesResources/Flow/CreateForm/common_imports.resource
Library      Blueprint.Steps.Verifications.Flow.CreateForm.create_form_add_component_verification.CreateFormAddComponentVerifications
Library      Blueprint.Steps.Verifications.Flow.CreateForm.create_form_add_section_verification.CreateFormAddSectionVerifications

Suite Setup       Create A New Flow With Random Code
Suite Teardown    Delete Flow Process In Flow Header
Force Tags        CREATE_F0RM    ADD_COMPONENT   DEFAULT_SECTION   FLOWS

*** Test Cases ***
Verify that a component can be dropped in default section
    [Tags]    P1
    [Template]    Add Component In Default Section
    textbox        section-1-columnB   2
    date           section-1-columnB
    checkbox       section-1-columnB
    dropdown       section-1-columnB
    multilinebox   section-1-columnB
    numericbox     section-1-columnB
    userlist       section-1-columnB
    textbox        section-1-columnA   2
    date           section-1-columnA
    checkbox       section-1-columnA
    dropdown       section-1-columnA
    multilinebox   section-1-columnA
    numericbox     section-1-columnA
    userlist       section-1-columnA

Verify that adding a component in a section, its properties are displayed
    [Tags]    P3
    [Template]    Adding Component Shows Its Properties
    textbox        Text Box 2        2
    date           Date 1
    checkbox       CheckBox 1
    dropdown       Dropdown Box 1
    multilinebox   Multiline Box 1
    numericbox     Numeric Box 1
    userlist       User List 1

Verify that a component cannot be added above default component in the main panel
    [Tags]    P1
    [Template]    Try to Add Component Above Default
    textbox        Text Box 2        2
    date           Date 1
    checkbox       CheckBox 1
    dropdown       Dropdown Box 1
    multilinebox   Multiline Box 1
    numericbox     Numeric Box 1
    userlist       User List 1

Verify that adding a component above default component a popup error message is displayed in the main panel
    [Tags]    P3
    [Template]    Try to Add Component Above Default Show A Popup Message
    textbox        2
    date
    checkbox
    dropdown
    multilinebox
    numericbox
    userlist

Verify that adding a component above default component the popup error message is displayed in orange. (rgba(240, 173, 78, 1))
    [Tags]    P3
    [Template]    Try To Add Component Above Default Show A Popup Message In Orange
    textbox        2
    date
    checkbox
    dropdown
    multilinebox
    numericbox
    userlist

Verify that adding a component in a section, the component is displayed in expected color
    [Tags]    P3
    [Template]    Adding Component Is Displayed In Expected Color
    textbox        section-1_textbox-2        2
    date           section-1_date-1
    checkbox       section-1_checkbox-1
    dropdown       section-1_dropdown-1
    multilinebox   section-1_multilinebox-1
    numericbox     section-1_numericbox-1
    userlist       section-1_userlist-1

*** Keywords ***
Add Component In Default Section
    [Arguments]    ${component_type}    ${defatul_section}   ${component_number}=1
    Add Component To Column Section In Create Form    ${component_type}    ${defatul_section}   ${component_number}
    New Component Should Be Displayed In Default Section
    Delete Components And Sections Added In Form Main Panel

Adding Component Shows Its Properties
    [Arguments]    ${component_type}   ${component_name}   ${component_number}=1
    Add Component To Column Section In Create Form    ${component_type}    section-1-columnB   ${component_number}
    Component Properties Should Be Displayed   ${component_name}
    Delete Components And Sections Added In Form Main Panel

Try To Add Component Above Default
    [Arguments]    ${component_type}   ${second_component_name}   ${component_number}=1
    Add Component Up To Existent Component In Create Form      ${component_type}    section-1_textbox-1   ${component_number}
    New Component Should Not Be Displayed In Default Section   ${second_component_name}
    Delete Components And Sections Added In Form Main Panel

Try To Add Component Above Default Show A Popup Message
    [Arguments]    ${component_type}   ${component_number}=1
    Add Component Up To Existent Component In Create Form      ${component_type}    section-1_textbox-1   ${component_number}
    Pop Up Error Message Should Be Displayed   You cannot move the first field
    Delete Components And Sections Added In Form Main Panel

Try To Add Component Above Default Show A Popup Message In Orange
    [Arguments]   ${component_type}   ${component_number}=1
    Add Component Up To Existent Component In Create Form      ${component_type}    section-1_textbox-1   ${component_number}
    Pop Up Message Should Be Displayed In Expected Color    rgba(240, 173, 78, 1)
    Delete Components And Sections Added In Form Main Panel

Adding Component Is Displayed In Expected Color
    [Arguments]    ${component_type}   ${component_id}   ${component_number}=1
    Add Component To Column Section In Create Form    ${component_type}    section-1_textbox-1   ${component_number}
    Component Should Be Displayed In Expected Color   rgba(117, 105, 255, 1)   ${component_id}
    Delete Components And Sections Added In Form Main Panel
