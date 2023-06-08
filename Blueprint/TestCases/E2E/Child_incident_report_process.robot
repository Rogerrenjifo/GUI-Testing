*** Settings ***
Resource     Blueprint/TestCasesResources/E2E/ChildIncidentReportProcess/child_incident_report_process.resource

Force Tags    RESIZED SCREEN TEST
Suite Teardown    Delete Storage

*** Variables ***
${flow_name}    Child Incident Report Process
@{1_component_list}    Type of incident    Child name    Child lastname    Child age    Description    Reporter name    Date reported       
@{2_component_list}    Visitor    Description    Date scheduled    Was the child found?        
@{3_component_list}    Responsible    Supervisor

*** Test Cases ***
Verify that a flow template can be created, published and used in projects
    ${flow_name}   Create A New Flow With Random Code    Child Incident Report Process-
    Create Form For a Flow Template
    ${flow_name_created}    Get Flow Name Text In Flow Header
    Create A Flow Template
    Give Permissions For A Flow Template
    Save and publish A Flow Template
    Select Project Button In Main Menu
    Insert Project Name Into The Search Bar    ${flow_name_created}
    Create A New Project Using The Flow Template Created

*** Keywords ***
Create Form For a Flow Template
    Select Section In Form Main Panel    Section 1
    Set Section Name In Form Properties Panel    Child incident report
    Select Component In Form Main Panel    section-1_textbox-1
    Set Name In Form Properties Panel    Type of incident
    Add Component To Form    textbox    section-1-columnB    section-1_textbox-2    Description
    Add Component To Form    textbox    section-1-columnA    section-1_textbox-3    Child name
    Add Component To Form    userlist    section-1-columnB    section-1_userlist-1    Reporter name
    Select Userlist Value In Form Properties Panel    AT19-MAR
    Add Component To Form    textbox    section-1_textbox-3    section-1_textbox-4    Child lastname
    Add Component To Form    date    section-1-columnB    section-1_date-1     Date reported
    Add Component To Form    numericbox    section-1_textbox-4    section-1_numericbox-1     Child age
    The Components Order Should Be    ${1_component_list}    section-1
    Add Section Down Other In Form    Child incident report    Verification PDA
    Add Component To Form    userlist    section-2-columnA    section-2_userlist-1     Visitor
    Select Userlist Value In Form Properties Panel    AT19-MAR
    Add Component To Form    date    section-2-columnB    section-2_date-1     Date scheduled
    Add Component To Form    textbox    section-2-columnA    section-2_textbox-1     Description
    Add Component To Form    checkbox    section-2-columnB    section-2_checkbox-1     Was the child found?
    The Components Order Should Be    ${2_component_list}    section-2
    Add Section Down Other In Form    Verification PDA    Delivering & Verification OL
    Add Component To Form    userlist    section-3-columnA    section-3_userlist-1     Delivered by
    Select Userlist Value In Form Properties Panel    AT19-MAR
    Add Component To Form    userlist    section-3-columnB    section-3_userlist-2     Received by
    Select Userlist Value In Form Properties Panel    AT19-MAR
    Add Component To Form    date    section-3-columnA    section-3_date-1     Received Date
    Add Component To Form    numericbox    section-3-columnB    section-3_numericbox-1     Number of incidents reported
    Add Component To Form    checkbox    section-3_date-1    section-3_checkbox-1     Child history complete
    Add Component To Form    checkbox    section-3_numericbox-1    section-3_checkbox-2     Child medical history complete
    Add Section Down Other In Form    Delivering & Verification OL    Registration to Horizon System
    Add Component To Form    userlist    section-4-columnA    section-4_userlist-1     Responsible
    Select Userlist Value In Form Properties Panel    AT19-MAR
    Add Component To Form    userlist    section-4-columnB    section-4_userlist-2     Supervisor
    Select Userlist Value In Form Properties Panel    AT19-MAR
    The Components Order Should Be    ${3_component_list}    section-4

Create A Flow Template
    Sleep    2
    Click Save Next Button In Flow Header
    Move Component To Specific Position In Flow Main Panel    start    38    0
    Move Component To Specific Position In Flow Main Panel    first    38   10
    Click Component    first
    Change Component Name In Flow Properties    Child incident report
    Add Action To The Flow    30    18    002Added1    Fill report
    Connect Two Components    first    002Added1    12    4
    Add Step To The Flow    30    25    001Added1    Verification PDA
    Connect Two Components    002Added1    001Added1    12    4
    Add Action To The Flow    17    35    002Added2    Schedule visit day
    Connect Two Components    001Added1    002Added2    13    4
    Add Action To The Flow    41    35    002Added3    Assign visitor
    Connect Two Components    001Added1    002Added3    11    4
    Add Step To The Flow    30    42    001Added2      Was the child found?
    Connect Two Components    002Added2    001Added2    12    3
    Connect Two Components    002Added3    001Added2    12    5
    Add Action To The Flow    70    41    002Added4    Child not found
    Connect Two Components    001Added2    002Added4    8    16
    Connect Two Components    002Added4    001Added1    4    8
    Add Action To The Flow    30    52    002Added5    Child found
    Connect Two Components    001Added2    002Added5    12    4
    Add Step To The Flow    30    60    001Added3      Delivering and verification OL
    Connect Two Components    002Added5    001Added3    12    4
    Add Action To The Flow    8    70    002Added6    Fill information
    Connect Two Components    001Added3    002Added6    13    4
    Add Action To The Flow    30    70     002Added7    Documentacion complete
    Connect Two Components    001Added3    002Added7    12    4
    Add Action To The Flow    50    70    002Added8      Incomplete documentation
    Connect Two Components    001Added3    002Added8    11    4
    Add Step To The Flow    50    86     001Added4    Wait until complete it
    Connect Two Components    002Added8    001Added4    12    4
    Add Step To The Flow    17    78    001Added5      Registration
    Connect Two Components    002Added6    001Added5    12    3
    Connect Two Components    002Added7    001Added5    12    5
    Add Action To The Flow    17    88     002Added9    Register to Horizon
    Connect Two Components    001Added5    002Added9    12    4
    Connect Two Components    001Added4    002Added9    16    8
    Add Step To The Flow    17    96    001Added6      Reported to Canada office
    Connect Two Components    002Added9    001Added6    12    4
    Click Component     001Added6    
    Click End Step Checkbox In Flow Properties    001Added6

Give Permissions For A Flow Template
    Sleep    2
    Click Tab In Flow Header    Permissions
    Delete All Users In Dropdown In Flow Permissions
    Click Dropdown Arrow In Flow Permissions
    Select User From Dropdown In Flow Permissions    AT19-MAR
    Users Selected List Should Contain    AT19-MAR
    Click Dropdown Arrow In Process Permission
    Select User From Dropdown In Process Permission    Roger Renjifo
    Users Selected List Process Permissions Should Contain    Roger Renjifo
    Delete All Users In Section Visibility    3
    Click Dropdown Arrow In Section Visibility    3
    Select User From Dropdown In Section Visibility    Carolina Vacaflor    3
    Users Selected List In Section Visibility Should Contain    Carolina Vacaflor    3
    Delete All Users In Section Visibility    4
    Click Dropdown Arrow In Section Visibility    4
    Select User From Dropdown In Section Visibility    Roger Renjifo    4
    Users Selected List In Section Visibility Should Contain    Roger Renjifo    4
    Delete All Users In Section Visibility    5
    Click Dropdown Arrow In Section Visibility    5
    Select User From Dropdown In Section Visibility    Carolina Vacaflor    5
    Users Selected List In Section Visibility Should Contain    Carolina Vacaflor    5
    Delete All Users In Section Visibility    6
    Click Dropdown Arrow In Section Visibility    6
    Select User From Dropdown In Section Visibility    Roger Renjifo    6
    Users Selected List In Section Visibility Should Contain    Roger Renjifo    6
    Sleep    2

Save and publish A Flow Template
    Click Tab In Flow Header    Publish
    Click Save Publish Button
    Click Save Continue Button
    Sleep    10  
    
Add Action To The Flow
    [Arguments]    ${x}    ${y}    ${component_id}    ${component_name}
    Move Action To Board Position    ${x}    ${y}
    Click Component    ${component_id}
    The Component Should Be Added To The Main Board    ${component_id}
    Sleep    2
    Change Component Name In Flow Properties    ${component_name}
    Click Select Owner Menu In Flow Properties
    Select Owner From List In Flow Properties    position=1
    Click Owner Combobox In Flow Properties
    Search Owner In Menu In Flow Properties    AT19-MAR
    Select Owner In Menu In Flow Properties
    Click Component    ${component_id}

Add Step To The Flow
    [Arguments]    ${x}    ${y}    ${component_id}    ${component_name}
    Move Step To Board Position    ${x}    ${y}
    Click Component    ${component_id}
    The Component Should Be Added To The Main Board    ${component_id}
    Sleep    2
    Change Component Name In Flow Properties    ${component_name}
    
Add Component To Form
    [Arguments]    ${form_component}    ${section}    ${component_id}    ${component_name}
    Add Component To Column Section In Create Form    ${form_component}    ${section}
    Sleep    2
    Select Component In Form Main Panel    ${component_id}
    Set Name In Form Properties Panel    ${component_name}

Add Section Down Other In Form
    [Arguments]    ${name_section_up}    ${name_section_added}
    Add Section Down Other In Create Form   ${name_section_up}
    Set Section Name In Form Properties Panel    ${name_section_added}
    Sleep    2

Connect Two Components
    [Arguments]    ${start_component_name}    ${to}    ${start_from}    ${end_to}
    Click Component    ${start_component_name}
    Connect Components In Flow Main Panel    ${start_component_name}    ${to}    ${start_from}    ${end_to}

Select Project Button In Main Menu
    Click On Projects Button
    Sleep    2

Create A New Project Using The Flow Template Created
    Sleep    5
    Click On A Project Result
    Sleep    5
    Click On New Request Button
    Sleep    5
    Insert Text Or Number In A Component In New Project Page    Child incident report    Type of incident    Child had an accident
    Click Create Button In New Project Page
    Sleep    8

Delete Storage
    Clean Dictionary
    Delete Form Storage
