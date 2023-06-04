*** Settings ***
Library    Blueprint.Steps.Actions.MainMenu.main_menu_actions.MainMenuActions
Library    Blueprint.Steps.Actions.Projects.ProjectPage.project_page_actions.ProjectPageActions
Library    Blueprint.Steps.Actions.Projects.ProjectTracing.Header.project_tracing_header_actions.ProjectTracingHeaderActions
Library    Blueprint.Steps.Actions.Projects.ProjectPage.export_dialog_actions.ExportDialogActions
Library    Blueprint.Steps.Actions.CommonElements.delete_dialog_actions.DeleteDialogActions
Library    Libraries.Assertions.assertions.Verification
Library    Blueprint.Steps.Utils.instance_manager.InstanceManager

*** Variables ***
${flow_name}    AT19-ProjectPage-137
${section_name}    Section 1
${component_name}   Title
${cancel_button_text}    Cancel
${expected_success_popup_color}    rgba(92, 184, 92, 1)

*** Keywords ***

Create ${number} Instances And Open Delete Dialog
    Create List Of Project Instance    ${flow_name}    ${number}
    ${ids}    Get All Projects Ids Text In Project Page
    ${project_id}   Obtain Random Id    ${ids}
    Open Delete Dialog In Project Instance    ${project_id}
    Set Suite Variable    ${project_id}


Search An Specific Project And Open Export Dialog
    [Arguments]    ${project_name}=${flow_name}
    Go To Project Process In Main Menu    ${project_name}
    Sleep    3
    Click Export Button In Project Page

Delete Created instances
    ${ids}     Get All Projects Ids Text In Project Page
    Log To Console    ${ids}
    Delete List Of Instances    ${ids}