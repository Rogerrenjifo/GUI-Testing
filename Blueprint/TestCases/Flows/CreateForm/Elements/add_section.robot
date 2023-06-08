*** Settings ***
Resource     Blueprint/TestCasesResources/Flow/CreateForm/common_imports.resource
Library      Blueprint.Steps.Verifications.Flow.CreateForm.create_form_add_section_verification.CreateFormAddSectionVerifications

Suite Setup        Create A New Flow With Random Code
Suite Teardown     Delete Flow Process In Flow Header
Test Teardown      Delete All Sections Created In Form Main Panel
Force Tags       CREATE_F0RM    ADD_SECTION   FLOWS

*** Variables ***
${default_section_name}                         Section 1
${first_section_added_name}                     Section 2
${expected_message_move_first_section}          You cannot move the first section
${expected_message_empty_section}               Section must contain at least one component
${expected_section_color}                       rgba(117, 105, 255, 1)
${first_section_added_index}                    2
${expected_message_empty_section_color}         rgba(255, 114, 105, 1)
${expected_message_move_first_section_color}    rgba(240, 173, 78, 1)

*** Test Cases ***
Verify that a section can be added to main panel
    [Tags]    SMOKE
    Add New Section In Create Form
    New Section Should Be Displayed

Verify that adding a section in the main panel, the section is empty
    
    Add New Section In Create Form
    New Section Should Be Empty   ${first_section_added_name}

Verify that adding a section in the main panel, an error message indicating that the section is empty is displayed.
    
    Add New Section In Create Form
    Error Message Should Be Displayed   ${first_section_added_name}   ${expected_message_empty_section}

Verify that adding a section in the main panel, its properties are displayed
    
    Add New Section In Create Form
    New Section Properties Should Be Displayed  ${first_section_added_name}

Verify that a section cannot be added above default section in the main panel
    
    Add Section Up Other In Create Form   ${default_section_name}
    New Section Should Not Be Displayed   ${first_section_added_name}

Verify that adding a section above default section an popup error message is displayed in the main panel
    
    Add Section Up Other In Create Form   ${default_section_name}
    Pop Up Error Message Should Be Displayed   ${expected_message_move_first_section}

Verify that adding a section in the main panel, the section is displayed in purple (rgba(117, 105, 255, 1))
    
    Add New Section In Create Form
    Section Should Be Displayed In Expected Color   ${expected_section_color}   ${first_section_added_index}

Verify that a section can be added above another in the main panel
    [Tags]    SMOKE
    Add New Section In Create Form
    Add Section Up Other In Create Form    ${first_section_added_name}
    New Section Should Be Displayed Above Selected  ${first_section_added_name}

Verify that a section can be added below another in the main panel
    [Tags]    SMOKE
    Add New Section In Create Form
    Add Section Down Other In Create Form    ${first_section_added_name}
    New Section Should Be Displayed Below Selected  ${first_section_added_name}

Verify that adding a section above default section the popup message is displayed in orange (rgba(240, 173, 78, 1)9
    
    Add Section Up Other In Create Form   ${default_section_name}
    Pop Up Message Should Be Displayed In Expected Color   ${expected_message_move_first_section_color}

Verify that adding a section, the error message indicating that the section is empty is displayed in red (rgba(255, 114, 105, 1))
    
    Add New Section In Create Form
    Error Message Should Be Displayed In Expected Color  ${expected_message_empty_section_color}    ${first_section_added_name}

Verify that a section cannot be dropped in the flow page header
    
    Add New Section In Flow Page Header
    New Section Should Not Be Displayed   ${first_section_added_name}

Verify that a section cannot be dropped in the page menu
    
    Add New Section In Page Menu
    New Section Should Not Be Displayed   ${first_section_added_name}
