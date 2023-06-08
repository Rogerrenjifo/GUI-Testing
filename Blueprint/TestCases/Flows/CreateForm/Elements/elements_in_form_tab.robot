*** Settings ***
Resource     Blueprint/TestCasesResources/Flow/CreateForm/common_imports.resource
Library      Blueprint.Steps.Verifications.Flow.CreateForm.create_form_elements_verification.CreateFormElementsVerifications

Suite Setup       Create A New Flow With Random Code
Suite Teardown    Delete Flow Process In Flow Header
Force Tags        CREATE_F0RM    TAB_ELEMENTS   FLOWS

*** Test Cases ***
Verify that text input is displayed in Create Form tab
    [Tags]    P1
    Input Text Should Be Displayed

Verify that date input is displayed in Create Form tab
    [Tags]    P2
    Input Date Should Be Displayed

Verify that dropdown input is displayed in Create Form tab
    [Tags]    P2
    Input Dropdown Should Be Displayed

Verify that multiline input is displayed in Create Form tab
    [Tags]    P2
    Input Multiline Should Be Displayed

Verify that numbers input is displayed in Create Form tab
    [Tags]    P2
    Input Numbers Should Be Displayed

Verify that checkbox input is displayed in Create Form tab
    [Tags]    P2
    Input Checkbox Should Be Displayed

Verify that user list input is displayed in Create Form tab
    [Tags]    P2
    Input User List Should Be Displayed

Verify that section input is displayed in Create Form tab
    [Tags]    P1
    Input Section Should Be Displayed

Verify that components title label is displayed in Create Form tab
    [Tags]    P3
    Components Title Should Be Displayed    Components

Verify that section title label is displayed in Create Form tab
    [Tags]    P3
    Section Title Should Be Displayed    Section

Verify that default section is displayed in Create Form tab
    [Tags]    P2
    Default Section Should Be Displayed    Section 1

Verify that default component label is displayed in Create Form tab
    [Tags]    P2
    Default Component Should Be Displayed   section-1_textbox-1

Verify that default component title is "Title"
    [Tags]    P3
    Default Component Title Should Be   Title   section-1_textbox-1

Verify that default component is displayed in default section
    [Tags]    P3
    Component Should Be In Default Section   section-1_textbox-1
