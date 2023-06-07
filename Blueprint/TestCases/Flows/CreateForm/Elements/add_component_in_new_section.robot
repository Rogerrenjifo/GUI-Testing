*** Settings ***
Resource     Blueprint/TestCasesResources/Flow/CreateForm/common_imports.resource
Library      Blueprint.Steps.Verifications.Flow.CreateForm.create_form_add_component_verification.CreateFormAddComponentVerifications
Library      Blueprint.Steps.Verifications.Flow.CreateForm.create_form_add_section_verification.CreateFormAddSectionVerifications

Suite Setup       Create A New Flow With Random Code
Suite Teardown    Delete Flow Process In Flow Header
Force Tags        CREATE_F0RM   ADD_COMPONENT   NEW_SECTION   FLOWS

*** Test Cases ***
Verify that a component can be added after add a new section
    [Tags]   BUG   BG-241
    [Template]    Add Component In A New Section
    textbox        Text Box 1        section-2-columnB
    date           Date 1            section-2-columnB
    checkbox       CheckBox 1        section-2-columnB
    dropdown       Dropdown Box 1    section-2-columnB
    multilinebox   Multiline Box 1   section-2-columnB
    numericbox     Numeric Box 1     section-2-columnB
    userlist       User List 1       section-2-columnB
    textbox        Text Box 1
    date           Date 1
    checkbox       CheckBox 1
    dropdown       Dropdown Box 1
    multilinebox   Multiline Box 1
    numericbox     Numeric Box 1
    userlist       User List 1

Verify that a component can be added above another
    [Template]    Add Component Above Another
    textbox        section-2_textbox-1        Text Box 1        Text Box 2
    date           section-2_date-1           Date 1            Date 2
    checkbox       section-2_checkbox-1       CheckBox 1        CheckBox 2
    dropdown       section-2_dropdown-1       Dropdown Box 1    Dropdown Box 2
    multilinebox   section-2_multilinebox-1   Multiline Box 1   Multiline Box 2
    numericbox     section-2_numericbox-1     Numeric Box 1     Numeric Box 2
    userlist       section-2_userlist-1       User List 1       User List 2

Verify that a component can be added below another
    [Template]    Add Component Bellow Another
    textbox        section-2_textbox-1        Text Box 1        Text Box 2
    date           section-2_date-1           Date 1            Date 2
    checkbox       section-2_checkbox-1       CheckBox 1        CheckBox 2
    dropdown       section-2_dropdown-1       Dropdown Box 1    Dropdown Box 2
    multilinebox   section-2_multilinebox-1   Multiline Box 1   Multiline Box 2
    numericbox     section-2_numericbox-1     Numeric Box 1     Numeric Box 2
    userlist       section-2_userlist-1       User List 1       User List 2

Verify that a component cannot be dropped in the page header
    [Template]    Try To Add A Component In Header
    textbox        Text Box 2
    date           Date 1
    checkbox       CheckBox 1
    dropdown       Dropdown Box 1
    multilinebox   Multiline Box 1
    numericbox     Numeric Box 1
    userlist       User List 1

Verify that a component cannot be dropped in the page menu
    [Template]    Try To Add A Component Main Menu
    textbox        Text Box 2
    date           Date 1
    checkbox       CheckBox 1
    dropdown       Dropdown Box 1
    multilinebox   Multiline Box 1
    numericbox     Numeric Box 1
    userlist       User List 1

Verify that a component cannot be added in main panel
    [Template]    Try To Add A Component In Main Panel
    textbox        Text Box 1
    date           Date 1
    checkbox       CheckBox 1
    dropdown       Dropdown Box 1
    multilinebox   Multiline Box 1
    numericbox     Numeric Box 1
    userlist       User List 1

*** Keywords ***
Add Component In A New Section
    [Arguments]   ${component_type}   ${component_name}   ${column_section_id}=section-2-columnA
    Add New Section In Create Form
    Add Component To Column Section In Create Form    ${component_type}    ${column_section_id}
    Run Keyword And Continue On Failure    New Component Should Be Displayed In New Section   Section 2   ${component_name}
    Delete Components And Sections Added In Form Main Panel

Try To Add A Component In Main Panel
    [Arguments]    ${component_type}    ${component_name}
    Add Component In Main Panel In Create Form   ${component_type}
    New Component Should Not Be Displayed In Main Panel    ${component_name}

Add Component Above Another
    [Arguments]    ${component_type}   ${first_component_id}   ${firts_component_name}   ${second_component_name}
    Add New Section In Create Form
    Select Section And Add Component To Section In Create Form    ${component_type}    section-2-columnA
    Add Component Up To Existent Component In Create Form   ${component_type}    ${first_component_id}   2
    ${expected_result}=   Create List   ${second_component_name}   ${firts_component_name}
    The Components Order Should Be   ${expected_result}    Section 2
    Delete Components And Sections Added In Form Main Panel

Add Component Bellow Another
    [Arguments]   ${component_type}   ${first_component_id}   ${firts_component_name}   ${second_component_name}
    Add New Section In Create Form
    Select Section And Add Component To Section In Create Form    ${component_type}    section-2-columnB
    Add Component Down Existent Component In Create Form    ${component_type}    ${first_component_id}   2
    ${expected_result}=   Create List   ${firts_component_name}   ${second_component_name}
    The Components Order Should Be   ${expected_result}   Section 2
    Delete Components And Sections Added In Form Main Panel

Try To Add A Component In Header
    [Arguments]    ${component_type}   ${component_name}
    Add New Component In Flow Page Header    ${component_type}
    New Component Should Not Be Displayed In Default Section   ${component_name}
    Delete Components And Sections Added In Form Main Panel

Try To Add A Component Main Menu
    [Arguments]    ${component_type}   ${component_name}
    Add New Component In Page Menu    ${component_type}
    New Component Should Not Be Displayed In Default Section   ${component_name}
    Delete Components And Sections Added In Form Main Panel
