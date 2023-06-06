*** Settings ***
Resource     Blueprint/TestCasesResources/Flow/MainMenu/main_menu_imports.resource
Library      Blueprint.Steps.Verifications.Flow.MainMenu.main_menu_verifications.MainMenuVerifications
Force Tags    MAIN_MENU     SEARCH_BAR
Suite Setup      Click On Flows Button
Suite Teardown   Click On Flows Button

*** Variables ***
${String_with_more_than_51_characters}      Believeinyourselfandpursueyourpassionwithdetermination!
${no_data_match_found_message}    No data match found

*** Test Cases ***
Verify the results are displayed when enter special characters in the flow search bar input
    [Template]    Test Flow Search Bar Input
    @
    $
    %
    ^
    &
    *
    (
    )
    _
    +
    {
    }
    |
    :
    "
    <
    >
    ?

Verify the flow search bar input has no limit characters
    [Tags]    BUG-235
    Insert Flow Name Into The Search Bar     ${String_with_more_than_51_characters}
    Message Not Data Match Found Should Be Displayed     ${no_data_match_found_message}


*** Keywords ***
Test Flow Search Bar Input
    [Arguments]    ${search_input}
    Insert Flow Name Into The Search Bar    ${search_input}
    Result Should Be Displayed
