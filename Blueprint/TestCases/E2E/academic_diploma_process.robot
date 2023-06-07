*** Settings ***
Resource      Blueprint/TestCasesResources/E2E/AcademicDiploma/academic_diploma_imports.resource
Force Tags    e2e
Suite Teardown    Delete Storage

*** Variables ***
@{first_section_list}    Student Name    Start Process Form    Score Certify    Due date for receipt of requirements
...    Kardex    Identication Certify   Start date for receipt of requirements  Voucher of payment
@{second_section_list}    Dean Signature    Manager   Rector Signature   

*** Test Cases ***
Verify that is posible create Academic Diploma process flow and publish it
    ${flow_name}   Create A New Flow With Random Code    Academic Diploma Process - 
    Set Documentation Section
    The Components Order Should Be    ${first_section_list}    section-1
    Set Signatures Section
    The Components Order Should Be    ${second_section_list}    section-2 
    New Section Should Be Displayed
    Click Save Next Button In Flow Header
    Popup Message Text Should Be Equal    Flow ${flow_name} updated.
    Move Components to Main Panel
    Components Shoul Be Displayed In The Main Panel
    Connect the components
    Components should be connected
    Click Save Next Button In Flow Header
    Popup Message Text Should Be Equal    Flow ${flow_name} updated.
    Set A User In Flow Admin Section
    Users Selected List Should Contain    Fabian Cabrejo
    Set A User In Process Permissions Section
    Users Selected List Process Permissions Should Contain    Telma Rios
    Set Users In Sections Visibility
    Users Selected should be visible
    Click Save Next Button In Flow Header
    Popup Message Text Should Be Equal    Flow ${flow_name} updated.
    Sleep    5s
    Click Save Publish Button
    Sleep    4s
    Popups Messages Text Should Contains    Flow ${flow_name} published.
    Go To Project Process In Main Menu   ${flow_name}
    Project Name Should Be As Expected    ${flow_name}

*** Keywords ***
Set Documentation Section
    Define Section Name Process In Form Properties   Section 1    Documentation
    Select Component In Form Main Panel    section-1_textbox-1
    Set Name In Form Properties Panel    Student Name
    Set Placeholder In Form Properties Panel    Enter name
    Add Component To Column Section In Create Form    checkbox       section-1-columnB
    Set Name In Form Properties Panel    Kardex
    Add Component Down Existent Component In Create Form    checkbox   section-1_textbox-1
    Set Name In Form Properties Panel    Start Process Form
    Add Component Down Existent Component In Create Form    checkbox   section-1_checkbox-1    2
    Set Name In Form Properties Panel    Identication Certify
    Add Component Down Existent Component In Create Form    checkbox   section-1_checkbox-2    3
    Set Name In Form Properties Panel    Score Certify
    Add Component Down Existent Component In Create Form    date   section-1_checkbox-3    4
    Set Name In Form Properties Panel    Start date for receipt of requirements
    Add Component Down Existent Component In Create Form    date   section-1_checkbox-4    5
    Set Name In Form Properties Panel    Due date for receipt of requirements
    Add Component Down Existent Component In Create Form    checkbox   section-1_date-1
    Set Name In Form Properties Panel    Voucher of payment

Set Signatures Section
    Add New Section In Create Form
    Set Section Name In Form Properties Panel    Signatures
    Add Component To Column Section In Create Form    checkbox   section-2-columnA
    Set Name In Form Properties Panel    Dean Signature
    Add Component To Column Section In Create Form    checkbox   section-2-columnB
    Set Name In Form Properties Panel    Rector Signature
    Add Component To Column Section In Create Form    dropdown   section-2-columnA
    Set Name In Form Properties Panel    Manager
    Set Add Dropdown Value In Form Properties Panel    Secretary
    Click Add Dropdown Button In Form Properties Panel
    Set Add Dropdown Value In Form Properties Panel    Rector
    Click Add Dropdown Button In Form Properties Panel
    Set Add Dropdown Value In Form Properties Panel    Dean
    Click Add Dropdown Button In Form Properties Panel

Move Components to Main Panel
    Sleep    2s
    Click Component    first
    Change Component Name In Flow Properties   Request Requirements
    Move Action To Board Position   33   30
    Change Component Name In Flow Properties   Bill Payment
    Set select owner and owner    1    Telma Rios
    Move Action To Board Position   83   30
    Change Component Name In Flow Properties   Not meet requirements
    Set select owner and owner    1    Fabian Cabrejo
    Move Action To Board Position   60   40
    Change Component Name In Flow Properties   Meet requirements
    Set select owner and owner    1    Fabian Cabrejo
    Move Action To Board Position   20   50
    Change Component Name In Flow Properties   Verify the Kardex
    Set select owner and owner    1    Fabian Cabrejo
    Move Action To Board Position   64   60
    Change Component Name In Flow Properties   First Signature
    Set select owner and owner    1    Denisse Cordova
    Move Action To Board Position   68   70
    Change Component Name In Flow Properties   Second Signature
    Set select owner and owner    1    Roger Renjifo
    Move Action To Board Position   20   80
    Change Component Name In Flow Properties   Request Academic Diploma
    Set select owner and owner    1    Telma Rios
    Move Step To Board Position   40   90
    Change Component Name In Flow Properties   Receive Academic Diploma
    Click End Step Checkbox In Flow Properties    001Added1
    Move Step To Board Position   60   28
    Change Component Name In Flow Properties   Review documents
    Move Step To Board Position   33   40
    Change Component Name In Flow Properties   Generate report
    Move Step To Board Position   39   57
    Change Component Name In Flow Properties   Print Academic Diploma
    Move Step To Board Position   90   65
    Change Component Name In Flow Properties   Receive and review signatures
    Move Step To Board Position   39   71
    Change Component Name In Flow Properties   Save Academic Diploma

Connect the components
    Click Component    first
    Connect Components In Flow Main Panel    first    002Added1    11    16
    Click Component    002Added1
    Connect Components In Flow Main Panel    002Added1    001Added2    8    16
    Click Component    001Added2
    Connect Components In Flow Main Panel    001Added2    002Added2    8    16
    Click Component    001Added2
    Connect Components In Flow Main Panel    001Added2    002Added3    11    4
    Click Component    002Added2
    Connect Components In Flow Main Panel    002Added2    first    4    8
    Click Component    002Added3
    Connect Components In Flow Main Panel    002Added3    001Added3    16    8
    Click Component    001Added3
    Connect Components In Flow Main Panel    001Added3    002Added4    16    3
    Click Component    002Added4
    Connect Components In Flow Main Panel    002Added4    001Added4    12    16
    Click Component    001Added4
    Connect Components In Flow Main Panel    001Added4    002Added5    8    16
    Click Component    002Added5
    Connect Components In Flow Main Panel    002Added5    001Added5    8    16
    Click Component    001Added5
    Connect Components In Flow Main Panel    001Added5    002Added6    12    8
    Click Component    002Added6
    Connect Components In Flow Main Panel    002Added6    001Added6    16    8
    Click Component    001Added6
    Connect Components In Flow Main Panel    001Added6    002Added7    16    2
    Click Component    002Added7
    Connect Components In Flow Main Panel    002Added7    001END1    11    16

Set select owner and owner
    [Arguments]    ${position}    ${user}
    Click Select Owner Menu In Flow Properties
    Select Owner From List In Flow Properties    position=${position}
    Click Owner Combobox In Flow Properties
    Search_owner In Menu In Flow Properties    ${user}
    Select Owner In Menu In Flow Properties

Components Shoul Be Displayed In The Main Panel
    ${components_list}    Obtain Dictionary Status In Flow Main Panel
    Dictionary Should Contain Component    ${components_list}    start
    Dictionary Should Contain Component    ${components_list}    first
    Dictionary Should Contain Component    ${components_list}    002Added1
    Dictionary Should Contain Component    ${components_list}    002Added2
    Dictionary Should Contain Component    ${components_list}    002Added3
    Dictionary Should Contain Component    ${components_list}    002Added4
    Dictionary Should Contain Component    ${components_list}    002Added5
    Dictionary Should Contain Component    ${components_list}    002Added6
    Dictionary Should Contain Component    ${components_list}    002Added7
    Dictionary Should Contain Component    ${components_list}    001END1
    Dictionary Should Contain Component    ${components_list}    001Added2
    Dictionary Should Contain Component    ${components_list}    001Added3
    Dictionary Should Contain Component    ${components_list}    001Added4
    Dictionary Should Contain Component    ${components_list}    001Added5
    Dictionary Should Contain Component    ${components_list}    001Added6

Components should be connected
    Component Dot Should Be Connected    first    11
    Component Dot Should Be Connected    first    8
    Component Dot Should Be Connected    002Added1    16
    Component Dot Should Be Connected    002Added1    8
    Component Dot Should Be Connected    001Added2    16
    Component Dot Should Be Connected    001Added2    8
    Component Dot Should Be Connected    001Added2    11
    Component Dot Should Be Connected    002Added2    16
    Component Dot Should Be Connected    002Added2    4
    Component Dot Should Be Connected    002Added3    4
    Component Dot Should Be Connected    002Added3    16
    Component Dot Should Be Connected    001Added3    8
    Component Dot Should Be Connected    001Added3    16
    Component Dot Should Be Connected    002Added4    3
    Component Dot Should Be Connected    002Added4    12
    Component Dot Should Be Connected    001Added4    16
    Component Dot Should Be Connected    001Added4    8
    Component Dot Should Be Connected    002Added5    16
    Component Dot Should Be Connected    002Added5    8
    Component Dot Should Be Connected    001Added5    16
    Component Dot Should Be Connected    001Added5    12
    Component Dot Should Be Connected    002Added6    8
    Component Dot Should Be Connected    002Added6    16
    Component Dot Should Be Connected    001Added6    8
    Component Dot Should Be Connected    001Added6    16
    Component Dot Should Be Connected    002Added7    2
    Component Dot Should Be Connected    002Added7    11
    Component Dot Should Be Connected    001END1    16

Set A User In Flow Admin Section
    Click Dropdown Arrow In Flow Permissions
    Select User From Dropdown In Flow Permissions    Fabian Cabrejo

Set A User In Process Permissions Section
    Delete All Users In Dropdown In Process Permission
    Click Dropdown Arrow In Process Permission
    Select User From Dropdown In Process Permission    Telma Rios

Set Users In Sections Visibility
    Delete All Users In Section Visibility    3
    Click Dropdown Arrow In Section Visibility    3
    Select User From Dropdown In Section Visibility    Telma Rios   3
    Click Dropdown Arrow In Section Visibility    3
    Select User From Dropdown In Section Visibility    Fabian Cabrejo   3
    Delete All Users In Section Visibility    4
    Click Dropdown Arrow In Section Visibility    4
    Select User From Dropdown In Section Visibility    Roger Renjifo   4
    Click Dropdown Arrow In Section Visibility    4
    Select User From Dropdown In Section Visibility    Denisse Cordova   4

Users Selected should be visible
    Users Selected List In Section Visibility Should Contain    Telma Rios    3
    Users Selected List In Section Visibility Should Contain    Fabian Cabrejo    3
    Users Selected List In Section Visibility Should Contain    Roger Renjifo    4
    Users Selected List In Section Visibility Should Contain    Denisse Cordova    4

Delete Storage
    Clean Dictionary
    Delete Form Storage