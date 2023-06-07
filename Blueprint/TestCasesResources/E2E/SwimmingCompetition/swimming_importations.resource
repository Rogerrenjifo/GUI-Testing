*** Settings ***
Resource    Blueprint/TestCasesResources/Flow/CreateForm/common_imports.resource
Library    Blueprint.Steps.Verifications.Flow.CreateForm.create_form_add_section_verification.CreateFormAddSectionVerifications
Library    Blueprint.Steps.Actions.Flows.create_form_properties_panel_actions.PropertiesPanelActions
Library    Blueprint.Steps.Actions.Flows.flow_main_panel_actions.FlowMainPanelActions
Library    Blueprint.Steps.Actions.Flows.flows_properties_actions.FlowPropertiesActions
Library    Blueprint.Steps.Actions.Flows.flow_components_actions.FlowComponentsActions
Library      Blueprint.Steps.Actions.Flows.process_permissions_actions.ProcessPermissionsActions
Library      Blueprint.Steps.Actions.Flows.section_visibility_permissions_actions.SectionsVisibilityActions
Library      Blueprint.Steps.Actions.Flows.flow_permissions_actions.FlowPermissionsActions
Library    Blueprint.Steps.Verifications.Flow.CreateForm.create_form_main_panel_components_verifications.CreateFormMainPanelComponentsVerifications
Library    Blueprint.Steps.Verifications.E2E.swimming_verifications.SwimmingCompetitionVerifications
Library    Blueprint.Steps.Verifications.Flow.CreateFlow.create_flow_main_panel_verification.CreateFlowMainPanelVerifications
