*** Settings ***
Resource            Blueprint/TestCasesResources/e2e/HomeRepair_dv/imports.resource


*** Keywords ***
Add Action Component
    [Arguments]                             ${title}        ${x_position}    ${y_position}    ${user}=Daniel Villarroel
    Move Action To Board Position                           ${x_position}    ${y_position}
    Sleep    1
    Change Component Name In Flow Properties                ${title}
    Sleep    1
    Action Component Should Be Visible In Flow Panel        ${title}
    Set Owner Process In Flow Properties                    ${user}

Add Step Component
    [Arguments]                             ${title}        ${x_position}    ${y_position}
    Move Step To Board Position                             ${x_position}    ${y_position}
    Sleep    1
    Change Component Name In Flow Properties                ${title}
    Sleep    1
    Step Component Should Be Visible In Flow Panel          ${title}

