*** Settings ***
Library            Libraries.Drivers.browser.Browser
Library            Blueprint.Steps.Actions.Flows.header_actions.HeaderActions

*** Variables ***
${flow_create_flow_tab}    https://test.blueprint.ses-unit.com/designer/4cdc8bfd-5b7d-4645-84da-72e304f4e442
${new_project_page}        https://test.blueprint.ses-unit.com/new-project/0f0be67e-9f60-4077-96ab-f4106187e20e

*** Keywords ***
Navigate To Flows-Page-Create-Flow
    Navigate To Url                ${flow_create_flow_tab}
    Click Tab In Flow Header       Create Flow

Navigate To Projects
    Navigate To Url                 ${new_project_page}
