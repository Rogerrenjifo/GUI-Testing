*** Settings ***
Library            Blueprint.Steps.Actions.Flows.header_actions.HeaderActions
Library            Blueprint.Steps.Verifications.Flow.Header.header_verifications.HeaderVerifications
Library            Blueprint.Steps.Verifications.Flow.Header.delete_dialog_verifications.DeleteDialogVerifications
Resource           Blueprint/TestCasesResources/navigate.resource

Suite Setup        Navigate To A Flow
Force Tags         DELETE_DIALOG   FLOW

*** Test Cases ***
Verify that delete dialog is displayed when 'Delete' option is clicked from the dropdown menu
    Open Delete Dialog
    Delete Dialog Should Be Displayed

Verify delete dialog title is displayed
    Open Delete Dialog
    Delete Dialog Title Should Be Displayed

Verify delete dialog question is displayed
    Open Delete Dialog
    Delete Dialog Question Should Be Displayed

Verify close button is displayed
    Open Delete Dialog
    Delete Dialog Close Button Should Be Displayed

Verify cancel button is displayed
    Open Delete Dialog
    Delete Dialog Cancel Button Should Be Displayed

Verify delete button is displayed
    Open Delete Dialog
    Delete Dialog Delete Button Should Be Displayed

Verify 'Delete Process' title text is displayed
    Open Delete Dialog
    Delete Dialog Title Text Should Be Equal    Delete Process

Verify 'Do you want to delete this process?' question text is displayed
    Open Delete Dialog
    Delete Dialog Question Text Should Be Equal    Do you want to delete this process?

*** Keywords ***
Open Delete Dialog
    Display Header Dropdown In Flow Header
    Click Delete Option In Flow Header
