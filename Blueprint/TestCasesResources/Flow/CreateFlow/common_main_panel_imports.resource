*** Settings ***
Library    Libraries.Drivers.browser.Browser
Library    Blueprint.Steps.Actions.Flows.header_actions.HeaderActions
Library    Blueprint.Steps.Actions.Flows.flow_components_actions.FlowComponentsActions
Library    Blueprint.Steps.Actions.Flows.flow_main_panel_actions.FlowMainPanelActions
Library    Blueprint.Steps.Actions.CommonElements.popup_messages_actions.PopUpMessagesActions
Library    Blueprint.Steps.Actions.Flows.flows_properties_actions.FlowPropertiesActions
Library    Blueprint.Steps.Verifications.Flow.CreateFlow.create_flow_main_panel_verification.CreateFlowMainPanelVerifications
Library    Blueprint.Steps.Actions.Flows.flow_page_actions.NewFlowActions
Resource   Blueprint/TestCasesResources/navigate.resource
