#*** Settings ***
#Library    Blueprint.Steps.Actions.MainMenu.main_menu_actions.MainMenuActions
#Library    Blueprint.Steps.Actions.Flows.flow_components_actions.FlowComponentsActions
#Library    Blueprint.Steps.Actions.Flows.flow_page_actions.NewFlowActions
#Library    Blueprint.Steps.Actions.Flows.create_form_elements_actions.CreateFormElementsActions
#Library    Blueprint.Steps.Actions.Flows.create_form_properties_panel_actions.PropertiesPanelActions
#Library    Blueprint.Steps.Actions.Flows.header_actions.HeaderActions
#Library    Blueprint.Steps.Actions.Flows.flow_main_panel_actions.FlowMainPanelActions
#Library    Blueprint.Steps.Actions.Flows.flows_properties_actions.FlowPropertiesActions
#Library    Blueprint.Steps.Actions.Flows.publish_tab_actions.PublishTabActions
#Library    Blueprint.Steps.Actions.Projects.ProjectPage.project_page_actions.ProjectPageActions
#Library    Libraries.Resources.instance_manager.InstanceGenerator
##Suite Setup    Create New Flow And List Of Instances
##Suite Teardown    Delete Created instances
#
#*** Variables ***
#${flow_name}    AT19-ProjectPage-137
##${flow_name}    AT19-Test Project Page 6
##${flow_code}    TPQ
#
#*** Keywords ***
#Create New Flow
#    ${flow_name}    ${flow_code}    Create A New Flow With Random Code
#    Click Tab In Flow Header    Create Flow
#    Move Action To Board Position    ${20}    ${60}
#    Click Component    first
#    Connect Components In Flow Main Panel    source_id=first    target_id=002Added1    source_point_number=${12}    target_point_number=${4}
#    Move Step To Board Position    ${70}    ${60}
#    Click Component    002Added1
#    Connect Components In Flow Main Panel    source_id=002Added1    target_id=001Added1    source_point_number=${8}    target_point_number=${16}
#    Click Component    001Added1
#    Click End Step Checkbox In Flow Properties
#    Click Tab In Flow Header    Publish
#    Click Save Publish Button
#    Sleep    8
#    Set Suite Variable    ${flow_name}
#    Log To Console    ${flow_name}
#
#Create New Flow And List Of Instances
##    Create New Flow
#    Create List Of Project Instance    ${flow_name}    ${4}
#    Set Suite Variable    ${flow_name}
#    Log To Console    salio del create
##    Go To Project Process In Main Menu    ${flow_name}
##    Set Suite Variable    ${flow_name}
#
#Delete Created Flow
#    Go To Flow Process In Main Menu    ${flow_name}
#    Delete Flow Process In Flow Header
#
#Delete Created instances
#    ${ids}     Get All Projects Ids Text In Project Page
#    Log To Console    ${ids}
#    Delete List Of Instances    ${ids}
