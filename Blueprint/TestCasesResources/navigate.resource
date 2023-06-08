*** Settings ***
Library            Libraries.Drivers.browser.Browser
Library            Blueprint.Steps.Actions.Flows.header_actions.HeaderActions
Library            Blueprint.Steps.Actions.Flows.flow_page_actions.NewFlowActions
Library            Blueprint.Steps.Actions.Flows.flow_main_panel_actions.FlowMainPanelActions
Library            Blueprint.Steps.Actions.MainMenu.main_menu_actions.MainMenuActions

*** Variables ***
${project_tracing}         https://test.blueprint.ses-unit.com/project-tracing/ab0ded4d-9bcc-4734-9d09-889fe94b9507
${search_flow}             AT19-CV

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

Return to previous page
    Go Back To Previous Page

Navigate To A Flow
    Reload Window
    Click On Flows Button
    Sleep    20s
    Insert Flow Name Into The Search Bar    ${search_flow}
    Click On Flow Result

Reload The Page
    Reload Window
    Sleep    45s    

Navigate to Flows-page-Permission
    Create A New Flow With Random Code
    Click Tab In Flow Header    Permissions

Reload Permissions Tab
    Reload Window
    Click Tab In Flow Header    Permissions

Navigate to Flows-page-Publish
    Create A New Flow With Random Code
    Click Tab In Flow Header    Publish
    Sleep    5
