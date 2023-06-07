*** Settings ***
Documentation    Atomic test to verify the functionality of the system in project tracing page of Blueprint
Resource         Blueprint/TestCasesResources/Projects/ProjectTracing/common_system_imports.resource
Suite Setup      Navigate to Project Tracing
Force Tags       PROJECT_TRACING    SYSTEM    PROJECT

*** Variables ***
${url}    https://test.blueprint.ses-unit.com/project-tracing/026f3bb0-fcc7-4b44-bbbe-6f531f2484ea
${expected_system_title}        System
${expected_current_step_title}  Current step
${expected_creation_date}       Creation date
${expected_last_update}         Last update
${expected_closure_date}        Closure date
${expected_color_current_step}  rgb(117, 105, 255)
${expected_color_action_owner}  rgb(229, 231, 235)

*** Test Cases ***
Verify that the title “System” is displayed
    ${title}    Get System Title In Project Tracing System
    System Title Should Be Displayed    ${title}    ${expected_system_title}

Verify that the title “Current step” is displayed
    ${title_current_step}    Get Current Step Title In Project Tracing System
    Current Step Title Should Be Displayed   ${title_current_step}   ${expected_current_step_title}

Verify its possible edit the current step
    Click Edit Current Step Button In Project System
    ${obtain_save_button}   Obtain Save Button Element
    Button Should Be Visible    ${obtain_save_button}

Verify options are displayed when dropdown field is clicked
    Click Edit Current Step Button In Project System
    Display Dropdown In Project System
    ${option_list}  Get Options In Dropdown
    Log To Console    ${option_list}
    Dropdown List Should Not Be Empty         ${option_list}

Verify options are displayed when click down arrow button
    Click Edit Current Step Button In Project System
    Display Dropdown In Project System
    ${option_list}  Get Options In Dropdown
    Log To Console    ${option_list}
    Dropdown List Should Not Be Empty       ${option_list}

Verify options are not displayed when click up arrow button
    Click Edit Current Step Button In Project System
    Display Dropdown In Project System
    Display Dropdown In Project System
    ${dropdown_list}    Obtain All The Components Of The Dropdown
    Dropdown List Should Not Be Displayed    ${dropdown_list}

Verify selected step is displayed on the dropdown
    Click Edit Current Step Button In Project System
    Display Dropdown In Project System
    Select Specific Option In Project System    end step

Verify that save button is visible when edit button is clicked
    Click Edit Current Step Button In Project System
    ${obtain_save_button}   Obtain Save Button Element
    Button Should Be Visible    ${obtain_save_button}

Verify that clear button is visible when edit button is clicked
    Click Edit Current Step Button In Project System
    ${obtain_clear_button}   Obtain Clear Button Element
    Button Should Be Visible    ${obtain_clear_button}

Verify that cancel button is visible when edit button is clicked
    Click Edit Current Step Button In Project System
    ${obtain_cancel_button}   Obtain Cancel Button Element
    Button Should Be Visible   ${obtain_cancel_button}

Verify that clear button deletes assigned value
    Click Edit Current Step Button In Project System
    Delete Current Value In Project System
    ${field_required}   Get The Field Requirement Message
    Field Required Should Be Displayed    ${field_required}

Verify that “Field requirement element“ is displayed when the dropdown box is empty
    Click Edit Current Step Button In Project System
    Delete Current Value In Project System
    ${field_required}  Get The Field Requirement Message
    Field Required Should Be Displayed    ${field_required}

Veryfy current step dropdown changes color when mouse is hovered
    ${actual_color}     Get Current Step Button Color
    Border Element Should Be Equal    ${actual_color}   ${expected_color_current_step}

Veryfy action owner dropdown changes color when mouse is hovered
    ${actual_color}     Get Action Owner Button Color
    Border Element Should Be Equal    ${actual_color}   ${expected_color_action_owner}

Verify that the title “Creation Date” is displayed
    ${title_creation_date}    Get Creation Date Title In Project Tracing System
    Creation Date Title Should Be Displayed        ${title_creation_date}    ${expected_creation_date}

Verify “Creation date” data text is displayed
    ${data_creation_date}   Get Creation Date Data In Project Tracing System
    Data Text Should Be Displayed   ${data_creation_date}

Verify that the title “Last Update” is displayed
    ${title_last_update}    Get Last Update Title In Project Tracing System
    Last Update Title Should Be Displayed       ${title_last_update}   ${expected_last_update}

Verify “Last update” data text is displayed
    ${data_last_update}   Get Last Update Data In Project Tracing System
    Data Text Should Be Displayed   ${data_last_update}

Verify that the title “Closure Date” is displayed
    ${title_last_update}    Get Closure Date Title In Project Tracing System
    Closure Date Title Should Be Displayed      ${title_last_update}   ${expected_closure_date}

Verify “Closure date” data text is displayed
    ${data_closure_date}   Get Closure Date Data In Project Tracing System
    Data Text Should Be Displayed   ${data_closure_date}

*** Keywords ***
Navigate to Project Tracing
    Navigate To Url    ${url}
