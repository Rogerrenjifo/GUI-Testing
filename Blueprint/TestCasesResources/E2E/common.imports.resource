*** Settings ***
Library      Blueprint.Steps.Actions.Flows.create_form_elements_actions.CreateFormElementsActions
Library      Blueprint.Steps.Actions.Flows.create_form_main_panel_actions.FormMainPanelActions
Library      Blueprint.Steps.Actions.Flows.create_form_properties_panel_actions.PropertiesPanelActions
Library      Blueprint.Steps.Actions.Flows.flow_page_actions.NewFlowActions
Library      Blueprint.Steps.Actions.Flows.header_actions.HeaderActions
Library      Blueprint.Steps.Actions.Flows.flows_properties_actions.FlowPropertiesActions
Library      Blueprint.Steps.Actions.Flows.flow_main_panel_actions.FlowMainPanelActions
Library      Blueprint.Steps.Actions.Flows.flows_properties_actions.FlowPropertiesActions
Library      Blueprint.Steps.Actions.Flows.flow_components_actions.FlowComponentsActions
Library      Blueprint.Steps.Actions.MainMenu.main_menu_actions.MainMenuActions
Library      Blueprint.Steps.Verifications.Flow.CreateForm.create_form_add_section_verification.CreateFormAddSectionVerifications
Library      Blueprint.Steps.Verifications.Flow.CreateForm.create_form_add_component_verification.CreateFormAddComponentVerifications
Library      Blueprint.Steps.Verifications.Flow.Header.header_verifications.HeaderVerifications
Library      Blueprint.Steps.Verifications.Flow.CreateFlow.add_components_verifications.AddComponentsVerification
Library      Blueprint.Steps.Actions.UsersAndGroups.groups_actions.GroupsActions
Library      Blueprint.Steps.Actions.UsersAndGroups.available_users_actions.AvailableUsersActions
Library      Blueprint.Steps.Actions.Flows.header_actions.HeaderActions
Library      Blueprint.Steps.Verifications.Flow.Permissions.permissions_verifications.FlowAdminPermissionsVerifications
Library      Blueprint.Steps.Actions.Flows.flow_permissions_actions.FlowPermissionsActions
Library      Blueprint.Steps.Actions.Flows.publish_tab_actions.PublishTabActions
Library      Blueprint.Steps.Verifications.Projects.ProjectTracing.flow_project_tracing_verification.FlowProjectTracingVerifications
Library      Blueprint.Steps.Verifications.Projects.ProjectPage.header_project_page_verifications.HeaderProjectPageVerifications

*** Keywords ***
Add components to section 1 and verify order of them
    Select Component In Form Main Panel                 section-1_textbox-1
    Set Name In Form Properties Panel                   Name
    Set Placeholder In Form Properties Panel            Please insert your name
    Add Component To Column Section In Create Form      numericbox   section-1-columnB
    Select Component In Form Main Panel                 section-1_numericbox-1
    Set Name In Form Properties Panel                   Age
    Set Placeholder In Form Properties Panel            Please insert your age
    Click Required Field Label In Form Properties Panel
    Add Component Down Existent Component In Create Form      dropdown  section-1_textbox-1
    Select Component In Form Main Panel                 section-1_dropdown-1
    Set Name In Form Properties Panel                   Are you more than 18 years old?
    Add Dropdown Values Process In Form Properties      section-1_dropdown-1      ${age_dropdown}
    Click Required Field Label In Form Properties Panel
    The Components Order Should Be    ${expected_section_1_components}    Section 1

Add section 2 and set name
    Add New Section In Create Form
    Select Section In Form Main Panel    Section 2
    Set Section Name In Form Properties Panel    Exam

Add components to section 2 and verify order of them
    Add Component To Column Section In Create Form      dropdown   section-2-columnA
    Select Component In Form Main Panel                 section-2_dropdown-1
    Set Name In Form Properties Panel                   Did you pass the exam?
    Add Dropdown Values Process In Form Properties      section-2_dropdown-1      ${exam_dropdown}
    Click Required Field Label In Form Properties Panel
    The Components Order Should Be    ${expected_section_2_components}    Section 2

Add section 3 and set name
    Add Section Down Other In Create Form        Exam
    Select Section In Form Main Panel            Section 3
    Set Section Name In Form Properties Panel    Payment

Add components to section 3 and verify order of them
    Add Component To Column Section In Create Form      checkbox   section-3-columnA
    Select Component In Form Main Panel                 section-3_checkbox-1
    Set Name In Form Properties Panel                   Pay exam fees
    The Components Order Should Be    ${expected_section_3_components}    Section 3

Add Action To Board
    [Arguments]    ${x_position}   ${y_position}   ${title}
    Move Action To Board Position   ${x_position}   ${y_position}
    Sleep    1s
    Change Component Name In Flow Properties   ${title}
    Click Select Owner Menu In Flow Properties
    Select Owner From List In Flow Properties   position=1
    Click Owner Combobox In Flow Properties
    Search Owner In Menu In Flow Properties     ${group_name}
    Select Owner In Menu In Flow Properties

Add Step To Board
    [Arguments]     ${x_position}   ${y_position}   ${title}
    Move Step To Board Position   ${x_position}   ${y_position}
    Sleep    1s
    Change Component Name In Flow Properties   ${title}

Click and connect componet in flow main panel
    [Arguments]    ${from_component}      ${to_component}   ${from}  ${to}
    The Component Should Be Added To The Main Board    ${from_component}
    Click Component    ${from_component}
    Sleep    1s
    Connect Components In Flow Main Panel   ${from_component}   ${to_component}   ${from}   ${to}
    Sleep    1s

Add field to update an select given result
    [Arguments]    ${index}
    Click Add Fields Update Button In Flow Properties
    Click Field Combobox Arrow In Flow Properties
    Select Result In Field Combobox Arrow In Flow Properties  ${index}

Add user to a group
    [Arguments]    ${username}
    Insert Username Into The Search User Bar    ${username}
    Sleep    1s
    Click On Add Button Of User Result By Index

Delete Storage
    Clean Dictionary
    Delete Form Storage
