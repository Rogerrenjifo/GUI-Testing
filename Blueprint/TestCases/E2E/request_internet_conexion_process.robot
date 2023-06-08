*** Settings ***
Documentation      This 2e2 create a flow proccess to request a new internet conection.
...                the steps represents the responsibility of every department and the actions the validation 
...                to go to the next step
Resource           Blueprint/TestCasesResources/E2E/e2e.resource
Suite Setup        Create A New Flow
Suite Teardown     Delete Storage
Force Tags         E2E    INTERNET_CONECTION   FLOWS

*** Variables ***
${start_id}                start
${first_id}                first
@{section_list}            Client name    Address    Internet plan    Client id    Coverage
@{second_section_list}     Details        Process completed

*** Test Cases ***
Verify that a Template Can Be Created, Published, and Used.
    Create Form
    Click Tab In Flow Header        Create Flow
    Create Flow
    Click Tab In Flow Header        Permissions
    Add Permitions
    Click Tab In Flow Header        Publish
    Click Save Publish Button
    Click Save Continue Button
    Verify The Flow Was Created

*** Keywords ***
Create Form
    Fill First Section
    Add Section 2 with name Sales department
    Add Section 3 with name Finance department
    Add Section 4 with name Back office department
    Add Section 5 with name Instalation department
    Add Section 6 with name NOC department

Create Flow
    Move Start Component                                100   85
    Rename First Component  Sales department            100   98
    Add Step Component      Service not installed       0     94    
    Add Step Component      Finance department          0     83
    Add Step Component      Back office department      30    59
    Add Step Component      Instalation department      60    39
    Add Step Component      NOC department              90    19
    Add Step Component      Service installed           0     0
    Add Action Component    Without coverage            50    96    Telma Rios
    Add Action Component    With coverage               50    85    Telma Rios
    Add Action Component    Payment done                15    70    Fabian Cabrejo
    Add Action Component    Schedule the instalation    45    50    Denisse Cordova
    Add Action Component    Hardware installed          75    30    Carolina Vacaflor
    Add Action Component    Installed successfully      70    2     Maria Mamani
    Add Action Component    Installed with errors       70    8     Maria Mamani
    Connect Components      Sales department             Without coverage            16    8
    Connect Components      Sales department             With coverage               2     8
    Connect Components      Without coverage             Service not installed       16    8
    Connect Components      With coverage                Finance department          16    8
    Connect Components      Finance department           Payment done                2     16
    Connect Components      Payment done                 Back office department      2     16
    Connect Components      Back office department       Schedule the instalation    2     16
    Connect Components      Schedule the instalation     Instalation department      2     16
    Connect Components      Instalation department       Hardware installed          2     16
    Connect Components      Hardware installed           NOC department              2     16
    Connect Components      NOC department               Installed successfully      6     8
    Connect Components      NOC department               Installed with errors       5     8
    Connect Components      Installed with errors        Instalation department      16    1
    Connect Components      Installed successfully       Service installed           16    8
    Set End Step            Service installed
    Set End Step            Service not installed

Add Permitions
    Set A User In Process Permissions Section         Telma Rios
    Set Users In Sections Visibility             3    Fabian Cabrejo
    Set Users In Sections Visibility             4    Denisse Cordova
    Set Users In Sections Visibility             5    Carolina Vacaflor
    Set Users In Sections Visibility             6    Maria Mamani
    Set Users In Sections Visibility             7    Roger Renjifo

Rename First Component
    [Arguments]                                               ${name}          ${x_position}    ${y_position}
    Move Component To Specific Position In Flow Main Panel    ${first_id}      ${x_position}    ${y_position}
    ${x_target}    ${y_target}    Obtain X And Y Position Component In Flow Main Panel          ${first_id}
    Component Should Have Different Positions                 ${x_position}    ${x_target}
    Component Should Have Different Positions                 ${y_position}    ${y_target}
    Change Component Name In Flow Properties                  ${name}
    Component Title Should Be                                 ${first_id}      ${name}
    
Move Start Component 
    [Arguments]                                               ${x_position}    ${y_position}
    Move Component To Specific Position In Flow Main Panel    ${start_id}      ${x_position}    ${y_position}
    ${x_target}    ${y_target}    Obtain X And Y Position Component In Flow Main Panel          ${start_id}
    Component Should Have Different Positions                 ${x_position}    ${x_target}
    Component Should Have Different Positions                 ${y_position}    ${y_target}

Add Step Component
    [Arguments]                                       ${name}            ${x_position}    ${y_position}
    ${component_id}    Move Step To Board Position    ${x_position}      ${y_position}
    The Component Should Be Added To The Main Board   ${component_id}
    Click Component                                   ${component_id}
    Change Component Name In Flow Properties          ${name}
    Component Title Should Be                         ${component_id}    ${name}
    
Add Action Component
    [Arguments]                                         ${name}            ${x_position}    ${y_position}    ${owner}
    ${component_id}    Move Action To Board Position    ${x_position}      ${y_position}
    The Component Should Be Added To The Main Board     ${component_id}
    Click Component                                     ${component_id}
    Change Component Name In Flow Properties            ${name}
    Component Title Should Be                           ${component_id}    ${name}
    Set_Owner Process In Flow Properties                ${owner}

Connect Components
    [Arguments]                            ${source}       ${target}           ${source_point}    ${target_point}    
    ${source_id}    Get Component Id By Title              ${source}
    ${target_id}    Get Component Id By Title              ${target}
    Connect Components In Flow Main Panel  ${source_id}    ${target_id}        ${source_point}    ${target_point}
    Component Dot Should Be Connected      ${source_id}    ${source_point}

Set End Step
    [Arguments]    ${name}
    ${component_id}    Get Component Id By Title        ${name}
    Click Component                                     ${component_id}
    Click End Step Checkbox In Flow Properties          ${component_id}

Fill First Section
    Define Section Name Process In Form Properties          Section 1            Client Information
    Select Component In Form Main Panel                     section-1_textbox-1
    Set Name In Form Properties Panel                       Client name
    Set Placeholder In Form Properties Panel                client name
    Add Component To Column Section In Create Form          textbox              section-1-columnB
    Set Name In Form Properties Panel                       Client id
    Set Placeholder In Form Properties Panel                client id
    Add Component Down Existent Component In Create Form    textbox              section-1_textbox-1     2
    Set Name In Form Properties Panel                       Address
    Set Placeholder In Form Properties Panel                address
    Add Component Down Existent Component In Create Form    checkbox             section-1_textbox-2    3
    Set Name In Form Properties Panel                       Coverage
    Add Component Down Existent Component In Create Form    textbox              section-1_textbox-3     4
    Set Name In Form Properties Panel                       Internet plan
    Set Placeholder In Form Properties Panel                internet plan
    The Components Order Should Be                          ${section_list}      section-1
    
Add Section ${section} with name ${name}
    Add New Section In Create Form
    Set Section Name In Form Properties Panel         ${name}
    Add Component To Column Section In Create Form    multilinebox                section-${section}-columnA
    Set Name In Form Properties Panel                 Details    
    Set Placeholder In Form Properties Panel          client id
    Add Component To Column Section In Create Form    checkbox                    section-${section}-columnB
    Set Name In Form Properties Panel                 Process completed
    The Components Order Should Be                    ${second_section_list}      section-${section}

Set A User In Process Permissions Section
    [Arguments]    ${name}
    Delete All Users In Dropdown In Process Permission
    Click Dropdown Arrow In Process Permission
    Select User From Dropdown In Process Permission   ${name}

Set Users In Sections Visibility
    [Arguments]    ${positions}    ${name}
    Delete All Users In Section Visibility            ${positions}
    Click Dropdown Arrow In Section Visibility        ${positions}
    Select User From Dropdown In Section Visibility   ${name}           ${positions}

Users Selected should be visible
    Users Selected List In Section Visibility Should Contain    Telma Rios         3
    Users Selected List In Section Visibility Should Contain    Fabian Cabrejo     3
    Users Selected List In Section Visibility Should Contain    Roger Renjifo      4
    Users Selected List In Section Visibility Should Contain    Denisse Cordova    4

Verify The Flow Was Created
    Sleep    5
    Go To Project Process In Main Menu    ${flow_name}
    Project Name Should Be As Expected    ${flow_name}

Create A New Flow
    ${flow_name}    Create A New Flow With Random Code
    Set Global Variable                   ${flow_name}

Delete Storage
    Clean Dictionary
    Delete Form Storage
