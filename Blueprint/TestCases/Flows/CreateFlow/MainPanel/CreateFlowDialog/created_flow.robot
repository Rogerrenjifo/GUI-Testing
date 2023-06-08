*** Settings ***
Resource     Blueprint/TestCasesResources/Flow/CreateFlow/common_imports.resource
Library      Blueprint.Steps.Verifications.Flow.CreateFlow.create_flow_verifications.CreateFlowVerifications

Test Teardown    Click On Flows Button
Force Tags       CREATE_FLOW    CREATE_FLOW_DIALOG   FLOWS

*** Variables ***
${flow_name}     my_flow_name_1
${existant_code}    111

*** Test Cases ***
Verify click on 'Create' button with a valid flow inputs in 'Create flow' redirects to the flow page
    
    Create A New Flow With Random Code
    Process Created Pop Up Message Should Be Displayed
    Flow Name Should Be Displayed
    Delete Flow Process In Flow Header

Verify a pop-up error message is displayed when create a new flow with an existent code
    
    Click On New Flow Button
    Insert New Flow Name    ${flow_name}
    Insert New Flow Code    ${existant_code}
    Click On Create New Flow Button
    Pop Up Message A Flow With Code Already Exists Should Be Displayed
