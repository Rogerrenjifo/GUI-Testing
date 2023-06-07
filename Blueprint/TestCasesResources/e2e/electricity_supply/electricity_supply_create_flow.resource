*** Settings ***
Resource    Blueprint/TestCasesResources/e2e/electricity_supply/electricity_supply_importation.resource

*** Variables ***
${expected_action_color}   rgb(229, 231, 235)
${expected_step_color}    rgb(0, 217, 194)

*** Keywords ***
Conect Components
    [Arguments]     ${source}   ${target}   ${source_point}   ${target_point}
    Click Component    ${source}
    Connect Components In Flow Main Panel   ${source}   ${target}   ${source_point}   ${target_point}

Set End Step
    Click Component    001Added1
    Click End Step Checkbox In Flow Properties   001Added1

Add An Action To Board
    [Arguments]    ${x_position}   ${y_position}   ${title}   ${owner}=Electricity Departament - GUI DEMO
    Move Action To Board Position   ${x_position}   ${y_position}
    Sleep    1
    Change Component Name In Flow Properties   ${title}
    Set Owner Process In Flow Properties    ${owner}

Add A Step To Board
    [Arguments]     ${x_position}   ${y_position}   ${title}
    Move Step To Board Position   ${x_position}   ${y_position}
    Sleep    1
    Change Component Name In Flow Properties   ${title}

Set Components In Board
    Sleep    1
    Click Component    first
    Change Component Name In Flow Properties   Application - Presentation of documents
    Add A Step To Board       90   82   Technician discharges the service
    Add An Action To Board    35   27   Documentation submitted on time
    Add An Action To Board    8    50   Documentation not submitted on time
    Add A Step To Board       60   25   Revision of plans
    Add A Step To Board       8    59   Reapply for supply
    Add An Action To Board    85   27   Plans meet specifications
    Add An Action To Board    43   43   Plans do not meet specifications
    Add A Step To Board       85   38   On site inspection
    Add An Action To Board    90   52   Construction meet specifications
    Add An Action To Board    42   57   Construction does not meet specifications
    Add A Step To Board       90   62   Certification and approval of supply
    Add An Action To Board    90   75   Payment of taxes
    Add An Action To Board    8    70   Delete Documentation
    Add An Action To Board    42   80   Date is meet
    Add A Step To Board       42   67   Assignment of deadline for changes

Conect Components In Board
    Click Component     first
    Conect Components   first       002Added2   13   4
    Conect Components   002Added2   001Added3   12   4
    Conect Components   001Added3   002Added8   12   4
    Conect Components   002Added8   first       16   16
    Conect Components   first       002Added1   8   16
    Conect Components   002Added1   001Added2   8   16
    Conect Components   001Added2   002Added4   12   8
    Conect Components   002Added4   first       16   11
    Conect Components   001Added2   002Added3   8   16
    Conect Components   002Added3   001Added4   12   4
    Conect Components   001Added4   002Added6   16   8
    Conect Components   001Added4   002Added5   12   4
    Conect Components   002Added5   001Added5   12   4
    Conect Components   001Added5   002Added7   12   4
    Conect Components   002Added7   001Added1   12   4
    Conect Components   002Added6   001Added6   12   4
    Conect Components   001Added6   002Added9   12   4
    Conect Components   002Added9   001Added4   8   14

Actions And Steps Should Be Displayed
    Component Title And RGB Color Should Be   Documentation submitted on time             ${expected_action_color}   002Added1
    Component Title And RGB Color Should Be   Documentation not submitted on time         ${expected_action_color}   002Added2
    Component Title And RGB Color Should Be   Plans meet specifications                   ${expected_action_color}   002Added3
    Component Title And RGB Color Should Be   Plans do not meet specifications            ${expected_action_color}   002Added4
    Component Title And RGB Color Should Be   Construction meet specifications            ${expected_action_color}   002Added5
    Component Title And RGB Color Should Be   Construction does not meet specifications   ${expected_action_color}   002Added6
    Component Title And RGB Color Should Be   Payment of taxes                            ${expected_action_color}   002Added7
    Component Title And RGB Color Should Be   Delete Documentation                        ${expected_action_color}   002Added8
    Component Title And RGB Color Should Be   Date is meet                                ${expected_action_color}   002Added9
    Component Title And RGB Color Should Be   Revision of plans                           ${expected_step_color}     001Added2
    Component Title And RGB Color Should Be   Reapply for supply                          ${expected_step_color}     001Added3
    Component Title And RGB Color Should Be   On site inspection                          ${expected_step_color}     001Added4
    Component Title And RGB Color Should Be   Certification and approval of supply        ${expected_step_color}     001Added5
    Component Title And RGB Color Should Be   Assignment of deadline for changes          ${expected_step_color}     001Added6
