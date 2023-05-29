*** Settings ***
Library            Libraries.Drivers.browser.Browser
Library            Blueprint.Steps.Actions.Flows.header_actions.HeaderActions

*** Variables ***
${flow_create_flow_tab}    https://test.blueprint.ses-unit.com/designer/4cdc8bfd-5b7d-4645-84da-72e304f4e442

*** Keywords ***
Navigate To Flows-Page-Create-Flow
    Navigate To Url                ${flow_create_flow_tab}
    Click Tab In Flow Header       Create Flow
