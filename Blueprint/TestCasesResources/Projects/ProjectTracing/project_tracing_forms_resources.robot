*** Settings ***
Library    Libraries.Drivers.browser.Browser
Library    Blueprint.Steps.Actions.Login.login_page_actions.LoginPageActions
Library    Blueprint.Steps.Actions.Projects.ProjectTracing.project_tracing_forms_actions.FormsActions
Library    Blueprint.Steps.Verifications.Projects.ProjectTracing.project_tracing_forms_verifications.ProjectTracingFormsVerifications

*** Variables ***
${project_tracing_forms_page}    https://test.blueprint.ses-unit.com/project-tracing/d737c271-53fe-4481-a609-00c7324ccbf7


*** Keywords ***
Open project tracing forms webpage
    navigate_to_url    ${project_tracing_forms_page}
    wait_for_project_forms_page_to_load_in_project_forms    Section 1

Put mouse hover field with title
    [Arguments]    ${field_title}    ${section_title}
    move_mouse_hover_field_in_project_forms    ${field_title}    ${section_title}
    wait_for_edit_button_to_load_in_project_forms    ${field_title}    ${section_title}

Click edit button of field
    [Arguments]    ${field_title}    ${section_title}
    select_field_to_edit_in_project_forms    ${field_title}    ${section_title}
    wait_for_save_button_to_load_in_project_forms

Set empty text in field
    [Arguments]    ${field_title}    ${section_title}
    set_empty_input_in_project_forms    ${field_title}    ${section_title}

Click section title
    [Arguments]    ${section_title}
    click_section_title_in_project_forms    ${section_title}
