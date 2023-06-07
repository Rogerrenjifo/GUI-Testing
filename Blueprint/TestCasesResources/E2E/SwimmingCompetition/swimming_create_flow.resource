*** Settings ***
Resource    Blueprint/TestCasesResources/E2E/SwimmingCompetition/swimming_importations.resource

*** Keywords ***
Move Components To Canvas
    Click Tab In Flow Header    Create Flow
    Sleep    2
    Move Component To Specific Position In Flow Main Panel    start    50    9
    Sleep    1
    Move Component To Specific Position In Flow Main Panel    first    50    21
    Sleep    1
    Click Component    first
    Change Component Name In Flow Properties   age to participate 
    Move Action To Board Position    37    29
    Sleep    1
    Change Component Name In Flow Properties    more than 15 years
    Set Owner Process In Flow Properties    AT19-GUI_Testing-dv
    Move Step To Board Position    37    37
    Sleep    1
    Change Component Name In Flow Properties    free style domain
    Move Action To Board Position    37    50
    Sleep    1
    Change Component Name In Flow Properties    domain free style
    Set Owner Process In Flow Properties    AT19-GUI_Testing-dv
    Move Step To Board Position    37    58
    Sleep    1
    Change Component Name In Flow Properties    butterfly and back style
    Move Action To Board Position    37    71
    Sleep    1
    Change Component Name In Flow Properties    domain butterfly and back style
    Set Owner Process In Flow Properties    AT19-GUI_Testing-dv
    Move Step To Board Position    37    79
    Sleep    1
    Change Component Name In Flow Properties    accepted
    Move Action To Board Position    6    19
    Sleep    1
    Change Component Name In Flow Properties    less than 15 years
    Set Owner Process In Flow Properties    AT19-GUI_Testing-dv
    Move Action To Board Position    70    39
    Sleep    1
    Change Component Name In Flow Properties    not domain free style
    Set Owner Process In Flow Properties    AT19-GUI_Testing-dv
    Move Action To Board Position    70    60
    Sleep    1
    Change Component Name In Flow Properties    not domain butterfly and back style
    Set Owner Process In Flow Properties    AT19-GUI_Testing-dv
    Move Step To Board Position    70    68
    Sleep    1
    Change Component Name In Flow Properties    butterfly and chest style
    Move Action To Board Position    70    81
    Sleep    1
    Change Component Name In Flow Properties    domain butterfly and chest style
    Set Owner Process In Flow Properties    AT19-GUI_Testing-dv
    Move Action To Board Position    109    70
    Sleep    1
    Change Component Name In Flow Properties    not domain butterfly and chest style
    Set Owner Process In Flow Properties    AT19-GUI_Testing-dv
    Move Step To Board Position    109    21
    Sleep    1
    Change Component Name In Flow Properties    continue training

Connect Components
    Click Component    first
    Connect Components In Flow Main Panel    first    002Added1     12    4
    Click Component    002Added1 
    Connect Components In Flow Main Panel    002Added1     001Added1     12    4
    Click Component    001Added1 
    Connect Components In Flow Main Panel    001Added1     002Added2     12    4
    Click Component    002Added2 
    Connect Components In Flow Main Panel    002Added2     001Added2     12    4
    Click Component    001Added2
    Connect Components In Flow Main Panel    001Added2     002Added3     12    4
    Click Component    002Added3
    Connect Components In Flow Main Panel    002Added3     001Added3     12    4
    Click Component    first
    Connect Components In Flow Main Panel    first     002Added4     16    8
    Click Component    002Added4
    Connect Components In Flow Main Panel    002Added4     001Added5     4    4
    Click Component    001Added1
    Connect Components In Flow Main Panel    001Added1     002Added5     8    16
    Click Component    002Added5
    Connect Components In Flow Main Panel    002Added5     001Added5     4    16
    Click Component    001Added2
    Connect Components In Flow Main Panel    001Added2     002Added6     8    16
    Click Component    002Added6
    Connect Components In Flow Main Panel    002Added6     001Added4     12    4
    Click Component    001Added4
    Connect Components In Flow Main Panel    001Added4     002Added7     12    4
    Click Component    002Added7
    Connect Components In Flow Main Panel    002Added7     001Added3     16    8
    Click Component    001Added4
    Connect Components In Flow Main Panel    001Added4     002Added8     8    16
    Click Component    002Added8
    Connect Components In Flow Main Panel    002Added8     001Added5     4    12
    Click Component    001Added3
    Click End Step Checkbox In Flow Properties    001Added3  
    Click Component    001Added5
    Click End Step Checkbox In Flow Properties    001Added5
    Sleep    3 

Verify Components Titles
    Component Title Should Be    age to participate                     first
    Component Title Should Be    free style domain                      001Added1
    Component Title Should Be    butterfly and back style               001Added2
    Component Title Should Be    accepted                               001Added3
    Component Title Should Be    butterfly and chest style              001Added4
    Component Title Should Be    continue training                      001Added5
    Component Title Should Be    more than 15 years                     002Added1
    Component Title Should Be    domain free style                      002Added2
    Component Title Should Be    domain butterfly and back style        002Added3
    Component Title Should Be    less than 15 years                     002Added4
    Component Title Should Be    not domain free style                  002Added5
    Component Title Should Be    not domain butterfly and back style    002Added6
    Component Title Should Be    domain butterfly and chest style       002Added7
    Component Title Should Be    not domain butterfly and chest style   002Added8

Verify Components Colors
    Component Color Should Be    001Added1   
    Component Color Should Be    001Added2
    Component Color Should Be    001Added4
    Component Color Should Be    002Added1
    Component Color Should Be    002Added2
    Component Color Should Be    002Added3
    Component Color Should Be    002Added4
    Component Color Should Be    002Added5
    Component Color Should Be    002Added6
    Component Color Should Be    002Added7
    Component Color Should Be    002Added8

Verify Components Connections
    Component Dot Should Be Connected    first        12
    Component Dot Should Be Connected    first        16
    Component Dot Should Be Connected    001Added1     4
    Component Dot Should Be Connected    001Added1     8
    Component Dot Should Be Connected    001Added1    12
    Component Dot Should Be Connected    001Added2     4
    Component Dot Should Be Connected    001Added2     8
    Component Dot Should Be Connected    001Added2    12
    Component Dot Should Be Connected    001Added4     4
    Component Dot Should Be Connected    001Added4     8
    Component Dot Should Be Connected    001Added4    12
    Component Dot Should Be Connected    002Added1     4
    Component Dot Should Be Connected    002Added1    12
    Component Dot Should Be Connected    002Added2     4
    Component Dot Should Be Connected    002Added2    12
    Component Dot Should Be Connected    002Added3     4
    Component Dot Should Be Connected    002Added3    12
    Component Dot Should Be Connected    002Added4     4
    Component Dot Should Be Connected    002Added4     8
    Component Dot Should Be Connected    002Added5     4
    Component Dot Should Be Connected    002Added5    16
    Component Dot Should Be Connected    002Added6    12
    Component Dot Should Be Connected    002Added6    16
    Component Dot Should Be Connected    002Added7     4
    Component Dot Should Be Connected    002Added7    16
    Component Dot Should Be Connected    002Added7     4
    Component Dot Should Be Connected    002Added7    16
    Component Dot Should Be Connected    002Added8     4
    Component Dot Should Be Connected    002Added8    16
