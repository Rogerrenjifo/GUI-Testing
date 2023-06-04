*** Settings ***
Library            Libraries.Drivers.browser.Browser
Library            Blueprint.Steps.Actions.Flows.header_actions.HeaderActions
Library            Blueprint.Steps.Actions.Flows.flow_page_actions.NewFlowActions
Library            Blueprint.Steps.Actions.Flows.flow_main_panel_actions.FlowMainPanelActions

*** Variables ***
${new_project_page}        https://test.blueprint.ses-unit.com/new-project/81da6abe-8ec6-439a-bfb4-90ab70f6d55d

*** Keywords ***
Navigate To Flows-Page-Create-Flow
    Create A New Flow With Random Code
    Click Tab In Flow Header       Create Flow
Clean Components Added
    Clean Dictionary
    Reload Window
    Click Tab In Flow Header    Create Flow

Navigate To Projects
    Navigate To Url                 ${new_project_page}
