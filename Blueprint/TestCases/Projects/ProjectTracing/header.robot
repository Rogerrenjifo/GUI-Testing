*** Settings ***
Documentation       Atomic test to verify the functionality of the header in project tracing page of Blueprint
Resource            Blueprint/TestCasesResources/Projects/ProjectTracing/common_header_imports.resource
Suite Setup         Navigate to Project Tracing
Force Tags          PROJECT_TRACING    HEADER

*** Variables ***
${url}  https://test.blueprint.ses-unit.com/project-tracing/686fd7ee-88a2-4ff9-b75b-83096c58b4e0
${expected_tag_tex}     847-1
${expected_project_name_text}      AT19-DC
${expected_rgb_delete_color}  rgba(0, 217, 194, 1)
${button_text}   action 2
${expected_rgb_action_color}     rgba(5, 176, 158, 1)

*** Test Cases ***
Verify that the Project tag text is displayed
    Project Tag Text Should Be Displayed        ${expected_tag_tex}

Verify that project name text title is displayed
    Project Name Text Should Be Displayed     ${expected_project_name_text}

Verify that Delete button is displayed
    Delete Button Should Be Displayed

Verify that the background of the Delete button changes to RGB:(0, 217, 194, 1) when the mouse is hovered over it.
    The Background Of The Delete Button Should Be Turquoise     ${expected_rgb_delete_color}

Verify that the background of the Action button changes to RGB:(5, 176, 158, 1) when the mouse is hovered over it.
    The Background Of The Action Button Should Be Highlighted    ${button_text}    ${expected_rgb_action_color}

Verify that when the delete button is clicked, the Delete process instance pop-up window is displayed.
    Click Delete Button In Project Tracing
    Popup Window Should Be Displayed

Verify that the Cancel
    Click Delete Button In Project Tracing
    Cancel Button Of Delete Process Instance Should Be Displayed

Verify that the Delete button is visible in the pop-up window Delete process instance.
    Click Delete Button In Project Tracing
    Delete Button Of Delete Process Instance Should Be Displayed

Verify that an instance of the process can be deleted in the Delete Process Instance pop-up window.
    Click Delete Button In Project Tracing
    Click Delete Button From Delete Dialog In Project Tracing
    Delete Button Should Be Displayed

Verify that you can cancel the deletion of a process instance in the Delete Process Instance pop-up window
    Click Delete Button In Project Tracing
    Click Cancel Button From Delete Dialog In Project Tracing
    Delete Button Should Be Displayed

*** Keywords ***
Navigate to Project Tracing
    Navigate To Url    ${url}
