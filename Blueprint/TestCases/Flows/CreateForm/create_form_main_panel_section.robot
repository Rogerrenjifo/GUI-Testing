*** Settings ***
Resource     Blueprint/TestCasesResources/Flow/CreateForm/common_imports.resource
Library      Blueprint.Steps.Verifications.Flow.CreateForm.create_form_main_panel_section_verification.CreateFormMainPanelSectionsVerifications
Library      Blueprint.Steps.Verifications.Flow.CreateForm.create_form_add_section_verification.CreateFormAddSectionVerifications

Suite Setup       Create A New Flow With Random Code
Suite Teardown    Delete Flow Process In Flow Header
Force Tags        CREATE_F0RM    MAIN_PANEL   SECTION   FLOWS

*** Test Cases ***
Verify that default section cannot be deleted from main panel
    [Tags]    SMOKE
    Delete Section In Form Main Panel    Section 1
    Default Section Should Be Displayed   Section 1

Verify that trying to delete the default section a popup message is displayed
    
    Delete Section In Form Main Panel    Section 1
    Pop Up Error Message Should Be Displayed   You cannot delete this section

Verify that trying to delete the default section a popup message is displayed in orange (rgba(240, 173, 78, 1))
    
    Delete Section In Form Main Panel    Section 1
    Pop Up Message Should Be Displayed In Expected Color    rgba(240, 173, 78, 1)

Verify that default section cannot be moved
    
    Add New Section In Create Form
    Move Section Down Other In Form Main Panel   Section 1    Section 2
    ${expected_section_order}=   Create List   Section 1    Section 2
    Section Order Should Be   ${expected_section_order}
    Delete All Sections Created In Form Main Panel

Verify that hovering a section change its color to purple (rgba(117, 105, 255, 1))
    
    Hover Section In Form Main Panel   Section 1
    Section Should Be Displayed In Expected Color    rgba(117, 105, 255, 1)   1

Verify that hovering a section, its 3-dots button is displayed
    
    Hover Section In Form Main Panel   Section 1
    Section Dots Button Should Be Displayed   Section 1

Verify that selecting a section its properties are displayed
    
    Add New Section In Create Form
    Add New Section In Create Form
    Select Section In Form Main Panel    Section 2
    Selected Section Properties Should Be Displayed    Section 2
    Delete All Sections Created In Form Main Panel

Verify that clicking section 3-dots button, delete button is displayed
    [Tags]    SMOKE
    Display Section Delete Menu In Form Main Panel    Section 1
    Section Delete Option Should Be Displayed   Delete

Verify that a non-default section can be deleted.
    [Tags]    SMOKE
    Add New Section In Create Form
    Delete Section In Form Main Panel    Section 2
    New Section Should Not Be Displayed   Section 2
    Delete All Sections Created In Form Main Panel

Verify that deleting a section its component are deleted to
    
    Add New Section In Create Form
    Add Component To Column Section In Create Form    textbox   section-2-columnA
    Delete Section In Form Main Panel    Section 2
    Component Should Not Be Displayed   section-2_textbox-1

Verify that a section can be moved above another
    
    Add New Section In Create Form
    Add New Section In Create Form
    Move Section Up Other In Form Main Panel    Section 3   Section 2
    ${expected_result}=   Create List    Section 1   Section 3   Section 2
    Section Order Should Be   ${expected result}
    Delete All Sections Created In Form Main Panel

Verify that a section can be moved bellow another
    
    Add New Section In Create Form
    Add New Section In Create Form
    Move Section Down Other In Form Main Panel    Section 2   Section 3
    ${expected_result}=   Create List    Section 1   Section 3   Section 2
    Section Order Should Be   ${expected result}
    Delete All Sections Created In Form Main Panel

Verify that a section cannot be moved above default section
    [Tags]    SMOKE
    Add New Section In Create Form
    Move Section Up Other In Form Main Panel    Section 2   Section 1
    ${expected_result}=   Create List    Section 1   Section 2
    Section Order Should Be    ${expected result}
    Delete All Sections Created In Form Main Panel

Verify that an empty section displayed an error message
    
    Add New Section In Create Form
    Select Section And Add Component To Section In Create Form  textbox    section-2-columnA
    Delete Components Added In Section In Form Main Panel   section-2
    Error Message Should Be Displayed   Section 2    Section must contain at least one component
    Delete All Sections Created In Form Main Panel

Verify that sections with repeated name display an error message
    
    Add New Section In Create Form
    Add New Section In Create Form
    Set Section Name In Form Properties Panel    Section 2
    Error Message Should Be Displayed   Section 2    Section must have a unique name
    Delete All Sections Created In Form Main Panel

Verify that sections whit repeated name are displayed in red color (rgba(213, 111, 151, 1))
    
    Add New Section In Create Form
    Add New Section In Create Form
    Set Section Name In Form Properties Panel    Section 2
    Section Should Be Displayed In Expected Color   rgba(117, 105, 255, 1)   2
    Delete All Sections Created In Form Main Panel
