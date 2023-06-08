*** Settings ***
Library            Blueprint.Steps.Actions.Flows.publish_tab_actions.PublishTabActions
Library            Blueprint.Steps.Verifications.Flow.Publish.publish_verifications.PublishVerifications
Library            Blueprint.Steps.Actions.Flows.header_actions.HeaderActions
Library            Blueprint.Steps.Actions.CommonElements.popup_messages_actions.PopUpMessagesActions
Library            Blueprint.Steps.Actions.Flows.flow_components_actions.FlowComponentsActions
Library            Blueprint.Steps.Actions.Flows.flows_properties_actions.FlowPropertiesActions
Library            Blueprint.Steps.Actions.Flows.create_form_elements_actions.CreateFormElementsActions
Library            Blueprint.Steps.Actions.Flows.section_visibility_permissions_actions.SectionsVisibilityActions
Resource           Blueprint/TestCasesResources/navigate.resource

Suite Setup        Navigate to Flows-page-Publish
Suite Teardown     Delete Flow Process In Flow Header
Force Tags         FLOWS    PUBLISH    holi2


*** Test Cases ***
Verify that 'Save and Publish' button is displayed
    [Tags]    P1
    Save And Publish Button Should Be Displayed

Verify 'Flow was not published.' pop-up message is displayed when 'Save and Publish' button is clicked and the flow has errors
    [Tags]    P2
    Click Save Publish Button
    Popup Message Should Be In List    Flow was not published.

Verify 'Publish error: Create Flow tab has errors. Missing end step' pop-up message is displayed when 'Save and Publish' button is clicked
    [Tags]    P2
    Click Save Publish Button
    Popup Message Should Be In List    Publish error: Create Flow tab has errors. Missing end step 

Verify 'Flow published.' pop-up message is displayed when 'Save and Publish' button is clicked in a draft version
    [Tags]    P2
    ${flow_name}    Get Flow Name Text In Flow Header
    Prepare Flow For Publish
    Click Publish Tab
    Click Save Publish Button
    Popup Message Should Be In List    Flow ${flow_name} published.

Verify 'Flow is already up-to-date.' pop-up message is displayed when 'Save and Publish' button is clicked in a published version
    [Tags]    P2
    ${flow_name}    Get Flow Name Text In Flow Header
    Click Publish Tab
    Click Save Publish Button
    Popup Message Should Be In List    Flow ${flow_name} is already up-to-date.

Verify 'Publish error: Create Form tab has errors.' pop-up message is displayed when 'Save and Publish' button is clicked and Create Form tab has errors
    [Tags]    P2
    Click Tab In Flow Header    Create Form
    Add New Section In Create Form
    Click Publish Tab
    Click Save Publish Button
    Popup Message Should Be In List    Publish error: Create Form tab has errors.

Verify 'Publish error: Create Flow tab has errors.' pop-up message is displayed when 'Save and Publish' button is clicked and Create Flow tab has errors
    [Tags]    P2
    Click Tab In Flow Header    Create Flow
    Move Action To Board Position    70    70
    Click Publish Tab
    Click Save Publish Button
    Popup Message Should Be In List    Publish error: Create Flow tab has errors.

Verify 'Publish error: Permissions tab has errors.' pop-up message is displayed when 'Save and Publish' button is clicked and Permissions tab has errors
    [Tags]    P2
    Click Tab In Flow Header    Permissions
    Delete All Users In Section Visibility    3
    Click Publish Tab
    Click Save Publish Button
    Popup Message Should Be In List    Publish error: Permissions tab has errors.

*** Keywords ***
Prepare Flow For Publish
    Click Tab In Flow Header    Create Flow
    Move Action To Board Position    40    25
    Click Component    first
    Connect Components In Flow Main Panel    first    002Added1    8    16
    Move Step To Board Position    65    25
    Click Component    002Added1
    Connect Components In Flow Main Panel    002Added1    001Added1    8    16
    Click Component    001Added1
    Click End Step Checkbox In Flow Properties    001Added1
    Click Save Button In Flow Header

Click Publish Tab
    Click Tab In Flow Header    Publish
    Sleep    5
