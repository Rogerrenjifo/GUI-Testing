*** Settings ***
Library            Blueprint.Steps.Actions.Flows.header_actions.HeaderActions
Library            Blueprint.Steps.Verifications.Flow.Header.flow_tabs_verifications.FlowTabsVerifications
Resource           Blueprint/TestCasesResources/navigate.resource

Suite Setup        Navigate To A Flow
Force Tags         FLOW_TABS   FLOW
Suite Teardown     Click On Flows Button

*** Variables ***
${create_form_tab}     Create Form
${create_flow_tab}     Create Flow
${permissions_tab}     Permissions
${publish_tab}         Publish

*** Test Cases ***
Verify 'Create Form' tab bar and icon are displayed
    Tab Bar Should Be Displayed     ${create_form_tab}
    Tab Icon Should Be Displayed    ${create_form_tab}

Verify 'Create Form' tab bar and icon are marked by default
    Flow Tab Should Be Marked    ${create_form_tab}

Verify 'Create Form' tab bar and icon are marked when 'Create Form' tab is clicked
    Click Tab In Flow Header     ${create_form_tab}
    Flow Tab Should Be Marked    ${create_form_tab}

Verify tab bar and icon of other tabs are not marked when 'Create Form' tab is clicked
    Click Tab In Flow Header     ${create_form_tab}
    Flow Tab Should Not Be Marked    ${create_flow_tab}
    Flow Tab Should Not Be Marked    ${permissions_tab}
    Flow Tab Should Not Be Marked    ${publish_tab}

Verify 'Create Form' tab bar and icon change to not marked when another tab is clicked
    Click Tab In Flow Header     ${create_form_tab}
    Flow Tab Should Be Marked    ${create_form_tab}
    Click Tab In Flow Header     ${permissions_tab}
    Flow Tab Should Not Be Marked    ${create_form_tab}

Verify 'Create Form' tab bar and icon change to not marked when 'Save & next' button is clicked
    Click Tab In Flow Header    ${create_form_tab}
    Click Save Next Button In Flow Header
    Flow Tab Should Not Be Marked    ${create_form_tab}

Verify 'Create Flow' tab bar and icon are displayed
    Tab Bar Should Be Displayed     ${create_flow_tab}
    Tab Icon Should Be Displayed    ${create_flow_tab}

Verify 'Create Flow' tab bar and icon are marked when 'Create Flow' tab is clicked
    Click Tab In Flow Header     ${create_flow_tab}
    Flow Tab Should Be Marked    ${create_flow_tab}

Verify tab bar and icon of other tabs are not marked when 'Create Flow' tab is clicked
    Click Tab In Flow Header     ${create_flow_tab}
    Flow Tab Should Not Be Marked    ${create_form_tab}
    Flow Tab Should Not Be Marked    ${permissions_tab}
    Flow Tab Should Not Be Marked    ${publish_tab}

Verify 'Create Flow' tab bar and icon change to not marked when another tab is clicked
    Click Tab In Flow Header     ${create_flow_tab}
    Flow Tab Should Be Marked    ${create_flow_tab}
    Click Tab In Flow Header     ${publish_tab}
    Flow Tab Should Not Be Marked    ${create_flow_tab}

Verify 'Create Flow' tab bar and icon change to not marked when 'Save & next' button is clicked
    Click Tab In Flow Header    ${create_flow_tab}
    Click Save Next Button In Flow Header
    Flow Tab Should Not Be Marked    ${create_flow_tab}

Verify 'Create Flow' tab bar and icon change to marked when 'Save & next' button is clicked from the 'Create Form' tab
    Click Tab In Flow Header     ${create_form_tab}
    Click Save Next Button In Flow Header
    Flow Tab Should Be Marked    ${create_flow_tab}

Verify 'Permissions' tab bar and icon are displayed
    Tab Bar Should Be Displayed     ${permissions_tab}
    Tab Icon Should Be Displayed    ${permissions_tab}

Verify 'Permissions' tab bar and icon are marked when 'Permissions' tab is clicked
    Click Tab In Flow Header     ${permissions_tab}
    Flow Tab Should Be Marked    ${permissions_tab}

Verify tab bar and icon of other tabs are not marked when 'Permissions' tab is clicked
    Click Tab In Flow Header     ${permissions_tab}
    Flow Tab Should Not Be Marked    ${create_form_tab}
    Flow Tab Should Not Be Marked    ${create_flow_tab}
    Flow Tab Should Not Be Marked    ${publish_tab}

Verify 'Permissions' tab bar and icon change to not marked when another tab is clicked
    Click Tab In Flow Header     ${permissions_tab}
    Flow Tab Should Be Marked    ${permissions_tab}
    Click Tab In Flow Header     ${create_form_tab}
    Flow Tab Should Not Be Marked    ${permissions_tab}

Verify 'Permissions' tab bar and icon change to not marked when 'Save & next' button is clicked
    Click Tab In Flow Header    ${permissions_tab}
    Click Save Next Button In Flow Header
    Flow Tab Should Not Be Marked    ${permissions_tab}

Verify 'Permissions' tab bar and icon change to marked when 'Save & next' button is clicked from the 'Create Flow' tab
    Click Tab In Flow Header     ${create_flow_tab}
    Click Save Next Button In Flow Header
    Flow Tab Should Be Marked    ${permissions_tab}

Verify 'Publish' tab bar and icon are displayed
    Tab Bar Should Be Displayed     ${publish_tab}
    Tab Icon Should Be Displayed    ${publish_tab}

Verify 'Publish' tab bar and icon are marked when 'Publish' tab is clicked
    Click Tab In Flow Header     ${publish_tab}
    Flow Tab Should Be Marked    ${publish_tab}

Verify tab bar and icon of other tabs are not marked when 'Publish' tab is clicked
    Click Tab In Flow Header     ${publish_tab}
    Flow Tab Should Not Be Marked    ${create_form_tab}
    Flow Tab Should Not Be Marked    ${create_flow_tab}
    Flow Tab Should Not Be Marked    ${permissions_tab}

Verify 'Publish' tab bar and icon change to not marked when another tab is clicked
    Click Tab In Flow Header     ${publish_tab}
    Flow Tab Should Be Marked    ${publish_tab}
    Click Tab In Flow Header     ${create_flow_tab}
    Flow Tab Should Not Be Marked    ${publish_tab}

Verify 'Publish' tab keeps marked when 'Save & next' button is clicked from 'Publish' tab
    [Tags]     BUG    BG-105
    Click Tab In Flow Header     ${publish_tab}
    Click Save Next Button In Flow Header
    Flow Tab Should Be Marked    ${publish_tab}

Verify 'Publish' tab bar and icon change to marked when 'Save & next' button is clicked from the 'Permissions' tab
    Click Tab In Flow Header     ${permissions_tab}
    Click Save Next Button In Flow Header
    Flow Tab Should Be Marked    ${publish_tab}
