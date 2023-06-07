*** Settings ***
Library             Libraries.Drivers.browser.Browser
Library             Blueprint.Steps.Actions.Login.login_page_actions.LoginPageActions
Library             Blueprint.Steps.Actions.MainMenu.main_menu_actions.MainMenuActions
Library             Blueprint.Steps.Utils.main_menu_manager.MainMenuManager
Library             Blueprint.Steps.Actions.Flows.flow_page_actions.NewFlowActions
Library             Blueprint.Steps.Verifications.Flow.CreateFlow.create_flow_verifications.CreateFlowVerifications
Library             Blueprint.Steps.Actions.Flows.create_form_elements_actions.CreateFormElementsActions
Library             Blueprint.Steps.Actions.Flows.create_form_main_panel_actions.FormMainPanelActions
Library             Blueprint.Steps.Actions.Flows.create_form_properties_panel_actions.PropertiesPanelActions
Library             Blueprint.Steps.Actions.Flows.header_actions.HeaderActions
Library             Blueprint.Steps.Actions.Flows.flow_components_actions.FlowComponentsActions
Library             Blueprint.Steps.Actions.Flows.flow_main_panel_actions.FlowMainPanelActions
Library             Blueprint.Steps.Actions.Flows.flows_properties_actions.FlowPropertiesActions
Library             Blueprint.Steps.Actions.Flows.publish_tab_actions.PublishTabActions
Library             Blueprint.Steps.Verifications.Flow.CreateForm.create_form_add_component_verification.CreateFormAddComponentVerifications
Library             Blueprint.Steps.Verifications.Flow.CreateFlow.add_components_verifications.AddComponentsVerification

*** Variables ***
${url}    https://test.blueprint.ses-unit.com/my-inbox
@{form_order}    First name    ID    Residence country    Time availability    Last name    Birth date    Cellphone number

*** Keywords ***
Login to blueprint
    Get Driver
    Navigate To Url    ${url}
    Login

Return to previous page
    Go Back To Previous Page

Create new flow if does not exist and go to flow page
    [Arguments]    ${title}    ${code}
    ${exist}=    flow exists    ${title}
    IF    ${exist}
        Click on flows button
        Insert flow name into the search bar    ${title}
        Click on flow result
    ELSE
        Click on flows button
        Blueprint.Steps.Actions.Flows.flow_page_actions.NewFlowActions.Click on new flow button
        Insert new flow name    ${title}
        Insert new flow code    ${code}
        Click on create new flow button
    END

Verify title of flow is 
    [Arguments]    ${title}
    Name label should be    ${title}    

Add field component on column 2 
    [Arguments]    ${component_type}
    add_component_to_column_section_in_create_form    ${component_type}    section-1-columnB

Add field component under field 1
    [Arguments]    ${component_type}
    add_component_down_existent_component_in_create_form    ${component_type}    section-1_textbox-1

Add field component under field 2
    [Arguments]    ${component_type}
    add_component_down_existent_component_in_create_form    ${component_type}    section-1_textbox-2

Add field component under field 3
    [Arguments]    ${component_type}
    add_component_down_existent_component_in_create_form    ${component_type}    section-1_textbox-3
    
Add field component under field 4
    [Arguments]    ${component_type}
    add_component_down_existent_component_in_create_form    ${component_type}    section-1_date-1

Add field component under field 5
    [Arguments]    ${component_type}
    add_component_down_existent_component_in_create_form    ${component_type}    section-1_textbox-4

Configure first field as First Name
    select_component_in_form_main_panel    section-1_textbox-1
    set_name_in_form_properties_panel    First name

Configure second field as Last Name
    select_component_in_form_main_panel    section-1_textbox-2
    set_name_in_form_properties_panel    Last name
    click_required_field_label_in_form_properties_panel

Configue third field as ID
    select_component_in_form_main_panel    section-1_textbox-3
    set_name_in_form_properties_panel    ID
    click_required_field_label_in_form_properties_panel

Configure date field as Birth date
    select_component_in_form_main_panel    section-1_date-1
    set_name_in_form_properties_panel    Birth date
    click_required_field_label_in_form_properties_panel

Configure fifth field as Residence Country
    select_component_in_form_main_panel    section-1_textbox-4
    set_name_in_form_properties_panel    Residence country
    click_required_field_label_in_form_properties_panel

Configure numeric field as Cellphone number
    select_component_in_form_main_panel    section-1_numericbox-1
    set_name_in_form_properties_panel    Cellphone number
    click_required_field_label_in_form_properties_panel

Configure dropdown as time-availability
    select_component_in_form_main_panel    section-1_dropdown-1
    set_name_in_form_properties_panel    Time availability
    click_required_field_label_in_form_properties_panel
    add_dropdown_single_value_process_in_form_properties    section-1_dropdown-1    No availability
    add_dropdown_single_value_process_in_form_properties    section-1_dropdown-1    Part-time
    add_dropdown_single_value_process_in_form_properties    section-1_dropdown-1    Full-time

Verify order of components on form
    the_components_order_should_be    ${form_order}    section 1

Connect given components using given points
    [Arguments]    ${component_1}    ${component_2}    ${point_1}    ${point_2}
    click_component    ${component_1}
    connect_components_in_flow_main_panel    ${component_1}    ${component_2}    ${point_1}    ${point_2}

Configure information validation step
    click_component    first
    change_component_name_in_flow_properties    Information Validation

Configure rejected action
    click_component    002Added1
    change_component_name_in_flow_properties    Rejected
    click_add_comment_checkbox_in_flow_properties

Configure disqualified step
    click_component    001Added1
    change_component_name_in_flow_properties    Disqualified
    click_end_step_checkbox_in_flow_properties    001Added1

Configure information validated action
    click_component    002Added2
    change_component_name_in_flow_properties    Information Validated
    click_select_owner_menu_in_flow_properties
    select_owner_from_list_in_flow_properties    position=1
    click_owner_combobox_in_flow_properties
    select_owner_in_menu_in_flow_properties

Configure technical test step
    click_component    001Added2
    change_component_name_in_flow_properties    Technical tests

Configure tests passed action
    click_component    002Added3
    change_component_name_in_flow_properties    Tests passed
    click_select_owner_menu_in_flow_properties
    select_owner_from_list_in_flow_properties    position=1
    click_owner_combobox_in_flow_properties
    select_owner_in_menu_in_flow_properties

Configure english interview step
    click_component    001Added3
    change_component_name_in_flow_properties    English interview

Configure english interview passed action
    click_component    002Added4
    change_component_name_in_flow_properties    Interview passed

Configure accepted step
    click_component    001Added4
    change_component_name_in_flow_properties    Accepted
    click_end_step_checkbox_in_flow_properties    001Added4

Search for project and go
    [Arguments]    ${title}
    click_on_projects_button
    insert_project_name_into_the_search_bar    ${title}
    click_on_a_project_result

Delete Storage
    Clean Dictionary
    Delete Form Storage
