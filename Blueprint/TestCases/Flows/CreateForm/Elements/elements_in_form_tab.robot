*** Settings ***
Resource     Blueprint/TestCasesResources/Flow/CreateForm/common_imports.resource
Library      Blueprint.Steps.Verifications.Flow.CreateForm.create_form_elements_verification.CreateFormElementsVerifications

Suite Setup       Create A New Flow With Random Code
Suite Teardown    Delete Flow Process In Flow Header
Force Tags        CREATE_F0RM    TAB_ELEMENTS   FLOWS

*** Test Cases ***
Verify that text input is displayed in Create Form tab
    [Tags]    SMOKE
    Input Text Should Be Displayed

Verify that date input is displayed in Create Form tab
    
    Input Date Should Be Displayed

Verify that dropdown input is displayed in Create Form tab
    
    Input Dropdown Should Be Displayed

Verify that multiline input is displayed in Create Form tab
    
    Input Multiline Should Be Displayed

Verify that numbers input is displayed in Create Form tab
    
    Input Numbers Should Be Displayed

Verify that checkbox input is displayed in Create Form tab
    
    Input Checkbox Should Be Displayed

Verify that user list input is displayed in Create Form tab
    
    Input User List Should Be Displayed

Verify that section input is displayed in Create Form tab
    [Tags]    SMOKE
    Input Section Should Be Displayed

Verify that components title label is displayed in Create Form tab
    
    Components Title Should Be Displayed    Components

Verify that section title label is displayed in Create Form tab
    
    Section Title Should Be Displayed    Section

Verify that default section is displayed in Create Form tab
    
    Default Section Should Be Displayed    Section 1

Verify that default component label is displayed in Create Form tab
    
    Default Component Should Be Displayed   section-1_textbox-1

Verify that default component title is "Title"
    
    Default Component Title Should Be   Title   section-1_textbox-1

Verify that default component is displayed in default section
    
    Component Should Be In Default Section   section-1_textbox-1
