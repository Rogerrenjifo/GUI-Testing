*** Settings ***
Resource     Blueprint/TestCasesResources/Flow/CreateFlow/common_imports.resource
Library      Blueprint.Steps.Verifications.Flow.CreateFlow.create_flow_verifications.CreateFlowVerifications

Force Tags       CREATE_FLOW    NAME_FLOW_INPUT   CREATE_FLOW_DIALOG   FLOW
Suite Setup      Click On New Flow Button

*** Variables ***
${string_with_more_than_51_characters}   Believeinyourselfandpursueyourpassionwithdetermination!

*** Test Cases ***
Verify an error message is not displayed when entering special chracters in 'Name' field in 'Create Flow' dialog
    [Template]  Error Message Should Not Be Displayed
    @
    $
    %
    ^
    &
    *
    (
    )
    _
    +
    {
    }
    |
    :
    "
    <
    >
    ?
    ${string_with_more_than_51_characters}

*** Keywords ***
Error message should not be displayed
    [Arguments]    ${name_input}
        Insert New Flow Name        ${name_input}
        Click On Create New Flow Button
        Code Field Required Message Should Be Displayed
