*** Settings ***
Documentation    Atomic tests to verify the functionality of checkbox
...              in new project page of Blueprint.
Library    Blueprint.Steps.Actions.MainMenu.main_menu_actions.MainMenuActions
Library    Blueprint.Steps.Actions.Projects.new_project_actions.NewProjectActions
Library    Blueprint.Steps.Verifications.Projects.NewProjectPage.new_project_page_verifications.NewProjectPageVerifications
Library    Blueprint.Steps.Utils.main_menu_manager.MainMenuManager
Resource    Blueprint/TestCasesResources/Projects/NewProjectPage/new_project.resource
Suite Setup    Search An Specific Project And Click On New Request Button
Force Tags     NEW_PROJECT    CHECKBOX    PROJECT

*** Variables ***
${section_new_history}    New history
${section_delivering}    Delivering
${label_go_to_school}    Go to school
${label_photo_and_video_done}    Photo and video done
${label_has_identity_card}    Has identity card
${purple_color}    rgba(117, 105, 255, 1)

*** Test Cases ***
Verify that hover on the label of a checkbox the color change to purple "rgba(117, 105, 255, 1)"
    The Rgb Color Of A Label Should Be As Expected    ${section_new_history}   ${label_go_to_school}   ${purple_color}

Verify that a checkbox not marked like “Default Checked” in flow page is not marked by default
    [Tags]    NEGATIVE
    Checkbox Should Not Be Marked    ${section_new_history}   ${label_go_to_school}

Verify that clicking on the label of checkbox it gets marked
    Click A Checkbox Label Inside A Section In New Project Page    ${section_new_history}   ${label_go_to_school}
    Checkbox Should Be marked    ${section_new_history}   ${label_go_to_school}

Verify that clicking the checkbox it gets marked
    [Tags]    SMOKE
    Click A Checkbox Inside A Section In New Project Page    ${section_new_history}    ${label_photo_and_video_done}
    Checkbox Should Be marked    ${section_new_history}    ${label_photo_and_video_done}

Verify that the checkbox marked like “Default Checked” in flow page is marked by default
    Checkbox Should Be marked    ${section_delivering}    ${label_has_identity_card}

Verify that clicking a marked checkbox it gets unmarked
    Click A Checkbox Inside A Section In New Project Page    ${section_delivering}    ${label_has_identity_card}
    Checkbox Should Not Be Marked    ${section_delivering}    ${label_has_identity_card}

Verify that clicking the label of a marked checkbox it gets unmarked
    [Tags]    SMOKE
    Click A Checkbox Label Inside A Section In New Project Page    ${section_new_history}   ${label_go_to_school}
    Checkbox Should Not Be Marked    ${section_new_history}   ${label_go_to_school}
