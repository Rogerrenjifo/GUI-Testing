*** Settings ***
Resource    Blueprint/TestCasesResources/Flow/MainMenu/main_menu_imports.resource
Library     Blueprint.Steps.Verifications.Flow.MainMenu.main_menu_verifications.MainMenuVerifications
Force Tags    MAIN_MENU
Suite Setup      Click On Flows Button


*** Variables ***
${Flows_label}      Flows
${search_without_match}     @$%^d
${no_data_match_found_message}    No data match found

*** Test Cases ***
Verify the Flows label is "Flows" in the Main Menu
    Flows Label Should Be    ${Flows_label}

Verify the flow search bar input display the results when is empty
    Result Should Be Displayed

Verify that the message 'No data match found' is displayed when there is no coincidences results in flow search bar
    Insert Flow Name Into The Search Bar    ${search_without_match}
    Message Not Data Match Found Should Be Displayed    ${no_data_match_found_message}

Verify that the 'New flow' button is displayed
    New Flow Button Should Be Displayed

Verify that click on 'New flow' button displays the 'Create flow' dialog
    Click On New Flow Button
    Create Flow Dialog Should Be Displayed
