*** Settings ***
Library            Blueprint.Steps.Actions.Flows.header_actions.HeaderActions
Library            Blueprint.Steps.Actions.Flows.overwrite_dialog_actions.OverwriteDraftDialogActions
Library            Blueprint.Steps.Actions.Flows.create_form_elements_actions.CreateFormElementsActions
Library            Blueprint.Steps.Verifications.Flow.Header.header_verifications.HeaderVerifications
Library            Blueprint.Steps.Verifications.Flow.Header.overwrite_draft_dialog_verifications.OverwriteDraftDialogVerifications
Resource           Blueprint/TestCasesResources/navigate.resource

Suite Setup        Create Draft Version
Force Tags         FLOWS    OVERWRITE_DRAFT_DIALOG

*** Variables ***
${deprecated_flow_version}      v1

*** Test Cases ***
Verify overwrite draft dialog is displayed when 'Save' button is clicked after a change was made
    [Tags]    P1
    Make A Change In Create Form
    Click Save Button In Flow Header
    Overwrite Draft Dialog Should Be Displayed
    Click Close Button In Overwrite Draft Dialog

Verify overwrite draft dialog is displayed when 'Save & next' button is clicked after a change was made
    [Tags]    P1
    Make A Change In Create Form
    Click Save Next Button In Flow Header
    Overwrite Draft Dialog Should Be Displayed
    Click Close Button In Overwrite Draft Dialog

Verify overwrite draft dialog title is displayed
    [Tags]    P2
    Make A Change In Create Form
    Click Save Button In Flow Header
    Overwrite Draft Title Should Be Displayed

Verify overwrite draft dialog question is displayed
    [Tags]    P2
    Overwrite Draft Question Should Be Displayed

Verify close button is displayed
    [Tags]    P2
    Overwrite Draft Dialog Close Button Should Be Displayed

Verify cancel button is displayed
    [Tags]    P2
    Overwrite Draft Dialog Cancel Button Should Be Displayed

Verify confirm button is displayed
    [Tags]    P2
    Overwrite Draft Dialog Confirm Button Should Be Displayed

Verify 'Overwrite draft' title text is displayed
    [Tags]    P2
    Overwrite Draft Dialog Title Text Should Be Equal    Overwrite draft

Verify 'A draft for this flow exists. Do you want to overwrite?' question text is displayed
    [Tags]    P2
    Overwrite Draft Dialog Question Text Should Be Equal    A draft for this flow exists. Do you want to overwrite?
    Click Close Button In Overwrite Draft Dialog

Verify overwrite draft dialog is closed when 'Close' button is clicked
    [Tags]    P2
    Make A Change In Create Form
    Click Save Button In Flow Header
    Click Close Button In Overwrite Draft Dialog
    Overwrite Draft Should Not Be Displayed

Verify overwrite draft dialog is closed when 'Cancel' button is clicked
    [Tags]    P2
    Make A Change In Create Form
    Click Save Button In Flow Header
    Click Cancel Button In Overwrite Draft Dialog
    Overwrite Draft Should Not Be Displayed

Verify 'Flow updated.' pop-up message is displayed when 'Confirm' button is clicked after 'Save' button was clicked
    [Tags]    P3
    Make A Change In Create Form
    Click Save Button In Flow Header
    Click Confirm Button In Overwrite Draft Dialog
    Popup Message Text Should Be Equal    Flow AT19-CV updated.

*** Keywords ***
Create Draft Version
    Navigate To A Flow
    Click Tab In Flow Header    Create Form
    Add Component To Column Section In Create Form    numericbox   section-2-columnA
    Click Save Button In Flow Header

Make A Change In Create Form
    Display Header Dropdown In Flow Header
    Display Select Version In Flow Header
    Click Version In Flow Header    ${deprecated_flow_version}
    Click Tab In Flow Header    Create Form
    Add Component To Column Section In Create Form    numericbox   section-2-columnA    
