*** Settings ***
Resource           Blueprint/TestCasesResources/E2E/UniversityAdmisionProcess/university_admision_imports.resource

Suite Setup        Create A New Flow With Random Code
Suite Teardown     Delete Storage
Force Tags         E2E    UNIVERSITY_ADMISION    FLOWS

*** Variables ***
@{first_section_list}    Full Name    Identity Card    Nationality    Phone Number    Date of birth    Gender    Home Address
@{second_section_list}    Academic Aptitude Test   Pre-University Courses    English Language Assessment 
@{third_section_list}    Photocopy of Identity Card    Photocopy Of Birth Certificate    High School Diploma Legalized Photocopy    Student Photographs
@{section_list}    Student Basic Information    Aptitude Tests    Documentation

*** Test Cases ***
Verify that a flow scenario can be created and published
    Flow Tab Should Be Marked    Create Form
    Flow Tab Error Should Not Be Marked    Create Flow 
    ${flow_name}    Get Flow Name Text In Flow Header
    Create Form
    Click Save Button In Flow Header
    Click Tab In Flow Header    Create Flow
    Flow Tab Error Should Be Marked    Create Flow    
    Create Flow    
    Click Save Button In Flow Header
    Click Tab In Flow Header    Permissions
    Flow Tab Should Be Marked    Permissions 
    Click Tab In Flow Header    Publish
    Flow Tab Should Be Marked    Publish
    Click Save Publish Button
    Sleep   5
    Go To Project Process In Main Menu   ${flow_name}
    Project Name Should Be As Expected    ${flow_name}

*** Keywords ***
Create Form
    Add First Section
    The Components Order Should Be    ${first_section_list}    section-1
    Add Second Section
    The Components Order Should Be    ${second_section_list}    section-2
    Add Third Section
    The Components Order Should Be    ${third_section_list}    section-3
    Section Order Should Be    ${section_list}

Create Flow
    Move Component To Specific Position In Flow Main Panel    start    15    15
    Move Component To Specific Position In Flow Main Panel    first    15    25
    Click Component    first
    Change Component Name In Flow Properties    Request admission form    
    Add Action Component    30    23    first    002Added1    8    16    Complete form    Maria Mamani
    Add Step Component    53    21    002Added1    001Added1    8    16    Take aptitude tests    
    Add Action Component    76    23    001Added1    002Added2    8    16    Fail aptitude test    Maria Mamani
    Add Step Component    100    21    002Added2    001Added2    8    16    Not accepted
    Click End Step Checkbox In Flow Properties    001Added2
    Add Action Component    53    35    001Added1    002Added3    12    4    Pass aptitude test    Maria Mamani
    Add Step Component    30    34    002Added3    001Added3    16    8    Requests documents
    Add Action Component    6    35    001Added3    002Added4    16    8    Present documents    Maria Mamani
    Add Step Component    6    52    002Added4    001Added4    12    4    Review documents
    Add Action Component    30    54    001Added4    002Added5    8    16    Missing documents    Roger Renjifo
    Click Component    002Added5
    Connect Components In Flow Main Panel    002Added5    001Added3    4    12
    Add Action Component    6    70    001Added4    002Added6    12    4    Up to date documents    Roger Renjifo
    Add Step Component    30    68    002Added6    001Added5    8    16    Assign subjects
    Add Action Component    53    70    001Added5    002Added7    8    16    Enroll    Maria Mamani
    Add Step Component    75    68    002Added7    001Added6    8    16    Pay tuition
    Add Action Component    100    70    001Added6    002Added8     8    16    Sign registration form    Maria Mamani
    Add Step Component    100    82    002Added8    001Added7    12    4    Registered
    Click End Step Checkbox In Flow Properties    001Added7

Add First Section
    Define Section Name Process In Form Properties   Section 1    Student Basic Information
    Select Component In Form Main Panel   section-1_textbox-1
    Set Name And Placeholder From Properties Panel   Full Name   Enter full name
    Add Component To Column Section In Create Form    date   section-1-columnB
    Set Name In Form Properties Panel    Date of birth
    Add Component Down Existent Component In Create Form    textbox   section-1_textbox-1    2
    Set Name And Check As Required From Properties Panel    Identity Card
    Add Component Down Existent Component In Create Form    dropdown   section-1_date-1
    Set Name In Form Properties Panel    Gender
    Set Add Dropdown Value In Form Properties Panel    Male
    Click Add Dropdown Button In Form Properties Panel
    Set Add Dropdown Value In Form Properties Panel    Female
    Click Add Dropdown Button In Form Properties Panel    
    Add Component Down Existent Component In Create Form    textbox   section-1_textbox-2   3
    Set Name And Placeholder From Properties Panel   Nationality   Enter nationality
    Add Component Down Existent Component In Create Form    textbox   section-1_dropdown-1   4
    Set Name And Placeholder From Properties Panel   Home Address   Enter home address
    Add Component Down Existent Component In Create Form    textbox   section-1_textbox-3   5
    Set Name And Placeholder From Properties Panel   Phone Number   Enter phone number

Add Second Section
    Add New Section In Create Form
    Error Message Should Be Displayed   Section 2    Section must contain at least one component
    Set Section Name In Form Properties Panel    Aptitude Tests
    Add Component To Column Section In Create Form    checkbox   section-2-columnA
    Set Name In Form Properties Panel    Academic Aptitude Test
    Add Component To Column Section In Create Form    checkbox   section-2-columnB
    Set Name In Form Properties Panel    English Language Assessment
    Add Component Down Existent Component In Create Form    checkbox   section-2_checkbox-1
    Set Name In Form Properties Panel    Pre-University Courses

Add Third Section
    Add New Section In Create Form
    Error Message Should Be Displayed   Section 3    Section must contain at least one component
    Set Section Name In Form Properties Panel    Documentation
    Add Component To Column Section In Create Form    checkbox   section-3-columnA
    Set Name In Form Properties Panel    Photocopy of Identity Card
    Add Component To Column Section In Create Form    checkbox   section-3-columnB
    Set Name In Form Properties Panel    High School Diploma Legalized Photocopy 
    Add Component Down Existent Component In Create Form    checkbox   section-3_checkbox-1
    Set Name In Form Properties Panel    Photocopy Of Birth Certificate    
    Add Component Down Existent Component In Create Form    checkbox   section-3_checkbox-2
    Set Name In Form Properties Panel    Student Photographs

Add Step Component
    [Arguments]    ${x_value}    ${y_value}    ${source}    ${target}    ${dot_source}    ${dot_target}    ${component_name}
    Move Step To Board Position    ${x_value}    ${y_value}
    Click Component    ${source}
    Connect Components In Flow Main Panel    ${source}    ${target}    ${dot_source}    ${dot_target}
    Click Component    ${target}
    Change Component Name In Flow Properties    ${component_name}

Add Action Component
    [Arguments]    ${x_value}    ${y_value}    ${source}    ${target}    ${dot_source}    ${dot_target}    ${component_name}    ${owner}
    Move Action To Board Position    ${x_value}    ${y_value}
    Click Component    ${source}
    Connect Components In Flow Main Panel    ${source}    ${target}    ${dot_source}    ${dot_target}
    Click Component    ${target}
    Change Component Name In Flow Properties    ${component_name}
    Set Owner Process In Flow Properties    ${owner}

Set Permissions
    Set Flow Admin
    Set User In Initiate Process
    Set Users In Sections Visibility

Set Flow Admin
    Delete All Users In Dropdown In Flow Permissions
    Click Dropdown Arrow In Flow Permissions
    Select User From Dropdown In Flow Permissions    Carolina Vacaflor

Set User In Initiate Process
    Delete All Users In Dropdown In Process Permission
    Click Dropdown Arrow In Process Permission
    Select User From Dropdown In Process Permission    Carolina Vacaflor
    Click Dropdown Arrow In Process Permission
    Select User From Dropdown In Process Permission    Roger Renjifo

Set Users In Sections Visibility
    Delete All Users In Section Visibility    3
    Click Dropdown Arrow In Section Visibility    3
    Select User From Dropdown In Section Visibility    Roger Renjifo   3
    Users Selected List In Section Visibility Should Contain    Roger Renjifo    3
    Delete All Users In Section Visibility    4
    Click Dropdown Arrow In Section Visibility    4
    Select User From Dropdown In Section Visibility    Roger Renjifo   4
    Users Selected List In Section Visibility Should Contain    Roger Renjifo    4
    Click Dropdown Arrow In Section Visibility    4
    Select User From Dropdown In Section Visibility    Maria Mamani   4
    Users Selected List In Section Visibility Should Contain    Maria Mamani    4
    Delete All Users In Section Visibility    5
    Click Dropdown Arrow In Section Visibility    5
    Select User From Dropdown In Section Visibility    Roger Renjifo   5
    Users Selected List In Section Visibility Should Contain    Roger Renjifo    5

Delete Storage
    Clean Dictionary
    Delete Form Storage
