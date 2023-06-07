*** Settings ***
Library            Blueprint.Steps.Actions.Flows.header_actions.HeaderActions
Library            Blueprint.Steps.Actions.Flows.create_form_elements_actions.CreateFormElementsActions
Library            Blueprint.Steps.Actions.Flows.create_form_main_panel_actions.FormMainPanelActions
Library            Blueprint.Steps.Actions.CommonElements.popup_messages_actions.PopUpMessagesActions
Library            Blueprint.Steps.Verifications.Flow.Header.header_verifications.HeaderVerifications
Resource           Blueprint/TestCasesResources/navigate.resource

Suite Setup        Navigate To A Flow
Suite Teardown     Click On Flows Button
Force Tags         HEADER_ELEMENTS   FLOWS

*** Variables ***
${flow_version}        v1
${created_popup}       New version for flow AT19-CV created.
${updated_popup}       Flow AT19-CV updated.
${up-to-date_popup}    Flow AT19-CV is already up-to-date.

*** Test Cases ***
Verify that flow status is displayed
    Flow Status Should Be Displayed

Verify that flow version is displayed
    Flow Version Should Be Displayed

Verify that flow name is displayed
    Flow Name Should Be Displayed

Verify that 'Delete' and 'Select Version' options are displayed when dropdown button is clicked
    Display Header Dropdown In Flow Header
    Delete Option Should Be Displayed
    Select Version Option Should Be Displayed
    Display Header Dropdown In Flow Header

Verify version list is displayed when 'Select Version' option is hover from the dropdown menu
    Display Header Dropdown In Flow Header
    Display Select Version In Flow Header
    Version List Should Be Displayed
    Display Header Dropdown In Flow Header

Verify that when a version is clicked from the version list, the flow version selected is displayed
    Display Header Dropdown In Flow Header
    Display Select Version In Flow Header
    Click Version In Flow Header    ${flow_version}
    Flow Version Should Be Equal    ${flow_version}

Verify that last update text is displayed
    Flow Last Updated Text Should Be Displayed

Verify 'Save' button is displayed in white color (rgba(255, 255, 255, 1))
    Save Button Should Be Displayed
    Save Button Color Should Be Equal    rgba(255, 255, 255, 1)

Verify 'Save' button color change to green (rgba(0, 217, 194, 1)) when is hovered
    Hover Save Button In Flow Header
    Save Button Color Should Be Equal    rgba(0, 217, 194, 1)

Verify 'New version for flow created.' pop-up message is displayed when 'Save' button is clicked after a change was made in a published flow
    Add Component To Column Section In Create Form    checkbox   section-2-columnB
    Click Save Button In Flow Header
    Close Pop Up On Create Form Elements
    Popup Message Text Should Be Equal    ${created_popup}

Verify 'Flow updated.' pop-up message is displayed when 'Save' button is clicked after a change was made
    Add Component To Column Section In Create Form    numericbox   section-2-columnA
    Click Save Button In Flow Header
    Popup Message Text Should Be Equal    ${updated_popup}
    Click To Close Popup Message

Verify 'Flow is already up-to-date.' pop-up message is displayed when 'Save' button is clicked when no changes were made
    Click Save Button In Flow Header
    Popup Message Text Should Be Equal    ${up-to-date_popup}
    Delete Flow Process In Flow Header
    Click To Close Popup Message

Verify 'Save & next' button is displayed in green color (rgba(0, 217, 194, 1))
    Save Next Button Should Be Displayed
    Save Next Button Color Should Be Equal    rgba(0, 217, 194, 1)

Verify 'Save & next' button color change to dark green (rgba(5, 176, 158, 1)) when is hovered
    Hover Save Next Button In Flow Header
    Save Next Button Color Should Be Equal    rgba(5, 176, 158, 1)

Verify 'New version for flow created.' pop-up message is displayed when 'Save & next' button is clicked after a change was made in a published flow
    Add Component To Column Section In Create Form    checkbox   section-2-columnB
    Click Save Next Button In Flow Header
    Popup Message Text Should Be Equal    ${created_popup}

Verify 'Flow updated.' pop-up message is displayed when 'Save & next' button is clicked after a change was made
    Click Tab In Flow Header    Create Form
    Add Component To Column Section In Create Form    numericbox   section-2-columnA
    Click Save Next Button In Flow Header
    Popup Message Text Should Be Equal    ${updated_popup}
    Click To Close Popup Message 

Verify 'Flow is already up-to-date.' pop-up message is displayed when 'Save & next' button is clicked when no changes were made  
    Click Save Next Button In Flow Header
    Popup Message Text Should Be Equal    ${up-to-date_popup}
    Delete Flow Process In Flow Header
