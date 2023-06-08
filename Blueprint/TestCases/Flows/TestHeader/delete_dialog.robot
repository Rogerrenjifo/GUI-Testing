*** Settings ***
Library            Blueprint.Steps.Actions.Flows.header_actions.HeaderActions
Library            Blueprint.Steps.Verifications.Flow.Header.header_verifications.HeaderVerifications
Library            Blueprint.Steps.Verifications.Flow.Header.delete_dialog_verifications.DeleteDialogVerifications
Library            Blueprint.Steps.Actions.CommonElements.popup_messages_actions.PopUpMessagesActions
Resource           Blueprint/TestCasesResources/navigate.resource

Suite Setup        Navigate To A Flow
Force Tags         DELETE_DIALOG   FLOWS
Suite Teardown     Click On Flows Button

*** Variables ***
${deprecated_flow_version}      v1
${published_flow_version}       v4
${draft_flow_version}           v5

*** Test Cases ***
Verify that delete dialog is displayed when 'Delete' option is clicked from the dropdown menu
    
    Open Delete Dialog
    Delete Dialog Should Be Displayed
    Click Close Button In Delete Dialog

Verify delete dialog title is displayed
    
    Open Delete Dialog
    Delete Dialog Title Should Be Displayed
    Click Close Button In Delete Dialog

Verify delete dialog question is displayed
    [Tags]    SMOKE
    Open Delete Dialog
    Delete Dialog Question Should Be Displayed
    Click Close Button In Delete Dialog

Verify close button is displayed
    
    Open Delete Dialog
    Delete Dialog Close Button Should Be Displayed
    Click Close Button In Delete Dialog

Verify cancel button is displayed
    
    Open Delete Dialog
    Delete Dialog Cancel Button Should Be Displayed
    Click Close Button In Delete Dialog

Verify delete button is displayed
    
    Open Delete Dialog
    Delete Dialog Delete Button Should Be Displayed
    Click Close Button In Delete Dialog

Verify 'Delete Process' title text is displayed
    
    Open Delete Dialog
    Delete Dialog Title Text Should Be Equal    Delete Process
    Click Close Button In Delete Dialog

Verify 'Do you want to delete this process?' question text is displayed
    
    Open Delete Dialog
    Delete Dialog Question Text Should Be Equal    Do you want to delete this process?
    Click Close Button In Delete Dialog

Verify delete dialog is closed when 'Close' button is clicked
    
    Open Delete Dialog
    Click Close Button In Delete Dialog
    Delete Dialog Should Not Be Displayed

Verify delete dialog is closed when 'Cancel' button is clicked
    
    Open Delete Dialog
    Click Cancel Button In Delete Dialog
    Delete Dialog Should Not Be Displayed

Verify 'It is not possible to delete a deprecated flow version.' pop-up message is displayed when 'Delete' button is clicked in a deprecated flow version
    
    Change Flow Version Process In Flow Header    ${deprecated_flow_version}
    Delete Flow Process In Flow Header
    Click To Close Popup Message
    Popup Message Text Should Be Equal    It is not possible to delete a deprecated flow version.

*** Keywords ***
Open Delete Dialog
    Display Header Dropdown In Flow Header
    Click Delete Option In Flow Header
