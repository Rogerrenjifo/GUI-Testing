*** Settings ***
Library            Libraries.Drivers.browser.Browser
Library            Blueprint.Steps.Actions.Flows.header_actions.HeaderActions
Library            Blueprint.Steps.Actions.Flows.flow_page_actions.NewFlowActions
Library            Blueprint.Steps.Actions.Flows.flow_main_panel_actions.FlowMainPanelActions

*** Variables ***
${new_project_page}        https://test.blueprint.ses-unit.com/new-project/81da6abe-8ec6-439a-bfb4-90ab70f6d55d
${flow}                    https://test.blueprint.ses-unit.com/designer/2f2f4494-96f1-4a39-8ee0-ec61da624112
${project_tracing}    https://test.blueprint.ses-unit.com/project-tracing/ab0ded4d-9bcc-4734-9d09-889fe94b9507

*** Keywords ***
Navigate To Flows-Page-Create-Flow
    Create A New Flow With Random Code
    Click Tab In Flow Header       Create Flow

Clean Components Added
    Clean Dictionary
    Reload Window
    Click Tab In Flow Header    Create Flow

Navigate To Project Tracing
    Navigate To Url                ${project_tracing}

Navigate To Projects
    Navigate To Url                 ${new_project_page}

Navigate To A Flow
    Navigate To Url                ${flow}
    
Navigate to Flows-page-Permission
    Create A New Flow With Random Code
    Click Tab In Flow Header    Permissions

Reload Permissions Tab
    Reload Window
    Click Tab In Flow Header    Permissions
