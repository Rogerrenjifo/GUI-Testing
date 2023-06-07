*** Settings ***
Resource     Blueprint/TestCasesResources/Flow/CreateFlow/common_imports.resource
Library      Blueprint.Steps.Verifications.Flow.CreateFlow.create_flow_verifications.CreateFlowVerifications

Suite Setup      Click On Flows Button
Test Teardown    Click On Cancel New Flow Button
Force Tags       CREATE_FLOW    DIALOG_FIELDS    CREATE_FLOW_DIALOG   FLOWS

*** Variables ***
${name_label}    Name
${code_label}    Code
${flow_code}     100
${flow_name}     my_flow_test1


*** Test Cases ***
Verify the 'Create flow' dialog contains the Name field label
    Click On New Flow Button
    Name Label Should Be    ${name_label}

Verify the 'Create flow' dialog contains the Code field label
    Click On New Flow Button
    Code Label Should Be    ${code_label}

Verify a error message is displayed when try to create a flow with empty fields in the 'Create Flow' dialog
    Click On New Flow Button
    Click On Create New Flow Button
    Name Field Required Message Should Be Displayed
    Code Field Required Message Should Be Displayed

Verify a error message is displayed when try to create a flow with empty name in the 'Create flow dialog'
    Click On Flows Button
    Create New Flow Without Name Process In Flow Page   ${flow_code}
    Name Field Required Message Should Be Displayed

Verify a error message is displayed when try to create a flow with empty code in the 'Create flow dialog'
    Click On Flows Button
    Create New Flow Without Code Process In Flow Page   ${flow_name}
    Code Field Required Message Should Be Displayed
