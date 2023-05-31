*** Settings ***
Library    Blueprint.Steps.Actions.MainMenu.main_menu_actions.MainMenuActions
Library    Blueprint.Steps.Actions.Projects.ProjectPage.project_page_actions.ProjectPageActions
Library    Blueprint.Steps.Actions.Projects.new_request_actions.NewRequestActions
Library    Blueprint.Steps.Actions.Projects.ProjectTracing.Header.project_tracing_header_actions.ProjectTracingHeaderActions
Library    Blueprint.Steps.Actions.Projects.ProjectPage.export_dialog_actions.ExportDialogActions
Library    Blueprint.Steps.Actions.CommonElements.delete_dialog_actions.DeleteDialogActions
Library    Libraries.Assertions.assertions.Verification
Resource    Blueprint/TestCasesResources/navigate.resource

*** Variables ***
${section_name}    Section 1
${component_name}   Title
${project_page_url}    https://test.blueprint.ses-unit.com/project/40f2de7e-83ea-4eb2-a641-4939d958da6c
${new_project_page}    https://test.blueprint.ses-unit.com/new-project/77a58eec-a584-4b57-a197-25a190a4f40a
${cancel_button_text}    Cancel
${expected_success_popup_color}    rgba(92, 184, 92, 1)

*** Keywords ***
Create New Instance
    Click On New Request Button
    Insert Text Or Number In A Component In New Request    Project to delete    ${section_name}    ${component_name}
    Click Create Button In New Request
    ${new_project_id}    Get Project Tag Text In Project Tracing
    Navigate To Url    ${project_page_url}
    Sleep    5
    Set Test Variable    ${new_project_id}

Search An Specific Project
    [Arguments]    ${project_name}=AT19 - RM
    Go To Project Process In Main Menu    ${project_name}

Cancel Export Process
    Click Cancel Export Dialog Button In Project Page
    ${export_dialog}    Get Export Dialog
    Set Test Variable    ${export_dialog}

Close Export Dialog
    ${export_dialog}    Get Export Dialog
    Click Close Export Dialog Button In Project Page
    Set Test Variable    ${export_dialog}
