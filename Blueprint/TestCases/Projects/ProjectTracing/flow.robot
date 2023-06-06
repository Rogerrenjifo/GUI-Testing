*** Settings ***
Documentation       Atomic test to verify the functionality of the flow in project tracing page of Blueprint
Resource            Blueprint/TestCasesResources/Projects/ProjectTracing/common_flow_imports.resource
Suite Setup         Navigate to Project Tracing
Force Tags          PROJECT_TRACING    FLOW

*** Variables ***
${url}  https://test.blueprint.ses-unit.com/project-tracing/e686e021-c399-4351-a450-975cab9c25df
${expected_flow_title}      Flow
${expected_start_text_component}  Start
${expected_final_text_component}  end step
${expected_step_text_component_by_order}  Second step
${number}  2
${turquoise_color}   rgba(232, 232, 232, 0.7)

*** Test Cases ***
Verify that the title “Flow” is displayed on the Project Tracing page
    Flow Title Should Be Displayed    ${expected_flow_title}

Verify that “Star component” text is displayed on the flow
    Start Text Component Should Be Displayed       ${expected_start_text_component}

Verify that “Final component” text is displayed on the flow
    Last Text Component Should Be Displayed    ${expected_final_text_component}

Verify that start component is displayed
    Start Component Should Be Displayed

Verify that last component is displayed
    Last Component Should Be Displayed

Verify that “Step component” text is displayed on the flow
    Step Text Component Should Be Displayed    ${number}    ${expected_step_text_component_by_order}

Verify that the “Steps components” are displayed by order on the flow
    Steps Components Are Displayed By Order   ${number}

Verify that the “Actions components” are displayed by order on the flow
    Actions Components Are Displayed By Order    ${number}

Verify that the data can be obtained from the actions pop-up window
    Data Text From Popup Action     ${number}

Verify that when hovering on the “Actions” label its background color changes
    Border Element Should Be Highlighted      ${number}    ${turquoise_color}

*** Keywords ***
Navigate to Project Tracing
    Navigate To Url    ${url}
    Sleep    10s
