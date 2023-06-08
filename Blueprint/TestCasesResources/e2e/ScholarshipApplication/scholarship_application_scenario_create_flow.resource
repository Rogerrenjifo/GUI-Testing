*** Settings ***
Resource    Blueprint/TestCasesResources/E2E/ScholarshipApplication/scholarship_application_scenario_importations.resource

*** Variables ***

*** Keywords ***
Add Steps And Actions To Diagram
    Move Component To Specific Position In Flow Main Panel    start    ${60}    ${5}
    Move Component To Specific Position In Flow Main Panel    first    ${60}    ${20}
    Change Component Name In Flow Properties    Scholarship Application
    Add Action With Name To Board    Application form is not complete    ${5}    ${17}    1
    Add Step With Name To Board    Ask applicant for send complete form    ${5}    ${30}    1
    Add Action With Name To Board   Documentiation is not complete    ${85}    ${17}    2
    Add Step With Name To Board    Review Documentation    ${85}    ${30}   2
    Add Action With Name To Board   Application form is complete    ${85}    ${45}    3
    Add Step With Name To Board    Ask appliant for send the complete documentation    ${85}    ${55}    3
    Add Action With Name To Board   Documentiation is complete    ${43}    ${33}    4
    Add Step With Name To Board    Review Applicant's Academic Performance    ${43}    ${43}    4
    Add Action With Name To Board   Does not meet academic requirements    ${5}    ${45}    5
    Add Step With Name To Board    Decline Scholarship Application    ${5}    ${57}    5
    Add Action With Name To Board   Meets Academic Requirements    ${43}    ${60}   6
    Add Step With Name To Board    Accept Scholarship Application    ${43}    ${70}    6
    Add Action With Name To Board    Recive the Scholarship Application    ${5}   ${7}    7
    Add Action With Name To Board    Recive Applicant documentation    ${85}    ${70}    8

Conncet Actions And Steps
    Connect Initial Step With Action 1 From Point 16 To Point 8
    Connect Initial Step With Action 2 From Point 8 To Point 16
    Connect Action 1 With Step 1 From Point 12 To Point 4
    Connect Action 2 With Step 2 From Point 12 To Point 4
    Connect Step 2 With Action 3 From Point 12 To Point 4
    Connect Action 3 With Step 3 From Point 12 To Point 4
    Connect Step 2 With Action 4 From Point 16 To Point 8
    Connect Action 4 With Step 4 From Point 12 To Point 4
    Connect Step 4 With Action 6 From Point 12 To Point 4
    Connect Action 6 With Step 6 From Point 12 To Point 4
    Connect Step 4 With Action 5 From Point 16 To Point 8
    Connect Action 5 With Step 5 From Point 12 To Point 4
    Connect Action 7 With Initial Step From Point 8 To Point 2
    Connect Step 1 With Action 7 From Point 16 To Point 16
    Connect Step 3 With Action 8 From Point 12 To Point 4
    Connect Action 8 With Step 2 From Point 8 To Point 8

Add Step With Name To Board
    [Arguments]    ${name}    ${x_coordenate}    ${y_coordenate}    ${component_number}
    Move Step To Board Position    ${x_coordenate}    ${y_coordenate}
    Sleep    1
    Change Component Name In Flow Properties    ${name}
    Set To Dictionary    ${steps}    001Added${component_number}    ${name}

Add Action With Name To Board
    [Arguments]    ${name}    ${x_coordenate}    ${y_coordenate}    ${component_number}
    Move Action To Board Position    ${x_coordenate}    ${y_coordenate}
    Sleep    1
    Change Component Name In Flow Properties    ${name}
    Update Owner
    Set To Dictionary    ${actions}    002Added${component_number}   ${name}

Connect Step ${step_number} With Action ${action_number} From Point ${a} To Point ${b}
    Click Component    001Added${step_number}
    Connect Components In Flow Main Panel    001Added${step_number}    002Added${action_number}   ${a}    ${b}

Connect Action ${action_number} With Step ${step_number} From Point ${a} To Point ${b}
    Click Component    002Added${action_number}
    Connect Components In Flow Main Panel    002Added${action_number}    001Added${step_number}   ${a}    ${b}

Connect Initial Step With Action ${action_number} From Point ${a} To Point ${b}
    Click Component    first
    Connect Components In Flow Main Panel    first    002Added${action_number}    ${a}    ${b}

Connect Action ${action_number} With Initial Step From Point ${a} To Point ${b}
    Click Component    002Added${action_number}
    Connect Components In Flow Main Panel    002Added${action_number}    first   ${a}    ${b}

Check Step ${step_number} As End Step
    ${step_id}    Set Variable    001Added${step_number}
    ${title}    Set Variable   ${steps}[${step_id}]
    Click Component    ${step_id}
    Click End Step Checkbox In Flow Properties    001Added${step_number}
    Remove From Dictionary    ${steps}    ${step_id}
    Set To Dictionary    ${steps}    001END${step_number}   ${title}
