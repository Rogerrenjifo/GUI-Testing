*** Settings ***
Documentation            Setup Suite Resorce File For Home Repair Project
Library                  Blueprint.Steps.Actions.Flows.flow_page_actions.NewFlowActions
Library                  Blueprint.Steps.Actions.Logout.logout_actions.LogoutActions
Resource                 Blueprint/TestCasesResources/e2e/HomeRepair_dv/keywords.resource


*** Keywords ***
Sign Out And Close Browser
   Sing Out Process
   Sleep    5