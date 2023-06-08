*** Settings ***
Resource     Blueprint/TestCasesResources/Flow/CreateForm/common_imports.resource
Library      Blueprint.Steps.Verifications.Flow.CreateForm.create_form_main_panel_components_verifications.CreateFormMainPanelComponentsVerifications
Library      Blueprint.Steps.Verifications.Flow.CreateForm.create_form_elements_verification.CreateFormElementsVerifications
Library      Blueprint.Steps.Verifications.Flow.CreateForm.create_form_add_component_verification.CreateFormAddComponentVerifications

Suite Setup       Create A New Flow With Random Code
Suite Teardown    Delete Flow Process In Flow Header
Force Tags        CREATE_F0RM    MAIN_PANEL    FLOWS

*** Test Cases ***
Verify that hovering a component change its color
    
    Hover Component In Form Main Panel   section-1_textbox-1
    Component Should Be Displayed In Expected Color   rgba(117, 105, 255, 1)  section-1_textbox-1

Verify that default component cannot be deleted
    [Tags]    SMOKE
    Delete Component In Form Main Panel   section-1_textbox-1
    Default Component Should Be Displayed    section-1_textbox-1

Verify that default component cannot be moved
    [Tags]    SMOKE
    Add Component To Column Section In Create Form   date   section-1-columnB
    Move Component Up Other In Form Main Panel   section-1_date-1   section-1_textbox-1
    ${expected_result}   Create List    Title   Date 1
    Component Order Should Be   ${expected_result}
    Delete Components Added In Section In Form Main Panel

Verify that hovering a component, its 3-dots button is displayed
    [Tags]    SMOKE
    Hover Component In Form Main Panel   section-1_textbox-1
    Component Dots Button Should Be Displayed    section-1_textbox-1

Verify that selecting a component its properties are displayed
    
    Select Component In Form Main Panel    section-1_textbox-1
    Selected Component Properties Should Be Displayed    Title

Verify that clicking component 3-dots button, delete button is displayed
    
    Add Component To Column Section In Create Form   date   section-1-columnB
    Display Component Delete Menu In Form Main Panel    section-1_date-1
    Component Delete Option Should Be Displayed   Delete   section-1_date-1
    Select Component Delete Button In Form Main Panel   section-1_date-1

Verify that a non-default component can be deleted
    [Tags]    SMOKE
    Add Component To Column Section In Create Form   date   section-1-columnB
    Delete Component In Form Main Panel    section-1_date-1
    Component Should Not Be Displayed   Date 1    section-1

Verify that a component can be moved above another
    
    Add New Section In Create Form
    Select Section And Add Component To Section In Create Form    date   section-2-columnA
    Add Component To Column Section In Create Form    textbox   section-2-columnB
    Move Component Up Other In Form Main Panel    section-2_textbox-1   section-2_date-1
    ${expected_result}   Create List    Text Box 1   Date 1
    Component Order Should Be   ${expected_result}   section-2
    Delete Components And Sections Added In Form Main Panel

Verify that a component cannot be moved above default component
    [Tags]    SMOKE
    Add Component To Column Section In Create Form   date   section-1-columnB
    Move Component Up Other In Form Main Panel    section-1_date-1    section-1_textbox-1
    ${expected_result}   Create List    Title   Date 1
    Component Order Should Be   ${expected_result}
    Delete Components Added In Section In Form Main Panel

Verify that a component cannot be moved outside a section
    
    Add Component To Column Section In Create Form    date   section-1-columnB
    Move Component In Main Panel In Create Form    section-1_date-1
    Component Should Be Displayed    Date 1  section-1
    Delete Component In Form Main Panel    section-1_date-1

Verify that a component can be moved inside another section
    
    Add New Section In Create Form
    Select Section And Add Component To Section In Create Form    date   section-2-columnA
    Move Component Between Sections In Form Main Panel    section-2_date-1    section-1-columnB
    Component Should Be Displayed    Date 1   section-1
    Delete Section In Form Main Panel    Section 2
