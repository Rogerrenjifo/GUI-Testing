*** Settings ***
Resource      Blueprint/TestCasesResources/E2E/OrderReception/order_reception_imports.resource
Force Tags    E2E   PROJECTS

*** Variables ***
@{first_section_list}    Customer name    Name of product    Number of order     Date of customer order     Product quantity
@{second_section_list}    Customer name    Name of the product   Name of the person in charge of receiving customer orders      Number of order     Date of customer order      Product quantity        Name of the warehouse clerk in charge of preparing the order        Date of order to warehouse

*** Test Cases ***
Verify that is posible create an Order Reception process flow and publish it
    ${flow_name}    Create A New Flow With Random Code       Order Reception Process -
    Log To Console       ${flow_name}
    Set Order Reception Section
    The Components Order Should Be    ${first_section_list}    section-1
    Set Order to warehouse Section
    The Components Order Should Be    ${second_section_list}    section-2
    Click Save Next Button In Flow Header
    New Section Should Be Displayed
    Click Save Next Button In Flow Header
    Popup Message Text Should Be Equal    Flow ${flow_name} updated.
    Move Components to Main Panel
    Components Should Be Displayed In The Main Panel
    Connect the components
    Click Save Next Button In Flow Header
    Popup Message Text Should Be Equal    Flow ${flow_name} updated.
    Set A User In Flow Admin Section
    Users Selected List Should Contain    Fabian Cabrejo
    Set A User In Process Permissions Section
    Users Selected List Process Permissions Should Contain    Denisse Cordova
    Set Users In Sections Visibility
    Users Selected should be visible
    Click Save Next Button In Flow Header
    Popup Message Text Should Be Equal    Flow ${flow_name} updated.
    Click Save Publish Button
    Popups Messages Text Should Contains    Flow ${flow_name} published.
    Go To Project Process In Main Menu   ${flow_name}
    Project Name Should Be As Expected    ${flow_name}

*** Keywords ***
Set Order Reception Section
    Define Section Name Process In Form Properties   Section 1    Order Reception
    Select Component In Form Main Panel    section-1_textbox-1
    Set Name In Form Properties Panel    Customer name
    Set Placeholder In Form Properties Panel    Enter the name of the customer
    Add Component To Column Section In Create Form    date       section-1-columnB
    Set Name In Form Properties Panel    Date of customer order
    Add Component Down Existent Component In Create Form    textbox   section-1_textbox-1
    Set Name In Form Properties Panel    Name of product
    Add Component Down Existent Component In Create Form    numericbox   section-1_date-1
    Set Name In Form Properties Panel    Product quantity
    Add Component Down Existent Component In Create Form    numericbox   section-1_textbox-2    2
    Set Name In Form Properties Panel    Number of order

Set Order to warehouse Section
    Add New Section In Create Form
    Set Section Name In Form Properties Panel    Order to warehouse
    Add Component To Column Section In Create Form    textbox   section-2-columnA
    Set Name In Form Properties Panel    Customer name
    Add Component To Column Section In Create Form    date   section-2-columnB
    Set Name In Form Properties Panel    Date of customer order
    Add Component To Column Section In Create Form    numericbox   section-2-columnA
    Set Name In Form Properties Panel    Number of order
    Add Component To Column Section In Create Form    numericbox   section-2-columnB
    Set Name In Form Properties Panel    Product quantity
    Add Component To Column Section In Create Form    textbox   section-2-columnA
    Set Name In Form Properties Panel    Name of the product
    Add Component To Column Section In Create Form    date   section-2-columnB
    Set Name In Form Properties Panel    Date of order to warehouse
    Add Component To Column Section In Create Form    textbox   section-2-columnA
    Set Name In Form Properties Panel    Name of the person in charge of receiving customer orders
    Add Component To Column Section In Create Form    textbox   section-2-columnB
    Set Name In Form Properties Panel    Name of the warehouse clerk in charge of preparing the order

Move Components to Main Panel
    Sleep    2s
    Move Component To Specific Position In Flow Main Panel    start      53    0
    Move Component To Specific Position In Flow Main Panel    first      53    15
    Click Component    first
    Change Component Name In Flow Properties   Order Reception
    Move Action To Board Position   45  25
    Sleep    2
    Change Component Name In Flow Properties   Responsible for receiving purchase order
    Set select owner and owner    1    Denisse Cordova
    Move Action To Board Position   75   40
    Sleep    2
    Change Component Name In Flow Properties   Check product in stock
    Set select owner and owner    1    Denisse Cordova
    Move Action To Board Position   20   40
    Sleep    2
    Change Component Name In Flow Properties   Check product not available
    Set select owner and owner    1    Denisse Cordova
    Move Action To Board Position   20   65
    Sleep    2
    Change Component Name In Flow Properties   Confirm order
    Set select owner and owner    1    Denisse Cordova
    Move Action To Board Position   65   65
    Sleep    2
    Change Component Name In Flow Properties   Customer accepts another product
    Set select owner and owner    1    Denisse Cordova
    Move Action To Board Position   90   65
    Sleep    2
    Change Component Name In Flow Properties   Customer rejects product
    Set select owner and owner    1    Denisse Cordova
    Move Step To Board Position   20   85
    Sleep    2
    Change Component Name In Flow Properties   Close the sale
    Click End Step Checkbox In Flow Properties    001Added1
    Move Step To Board Position   85   85
    Sleep    2
    Change Component Name In Flow Properties   Cancel order
    Click End Step Checkbox In Flow Properties    001Added2
    Move Step To Board Position   45   33
    Sleep    2
    Change Component Name In Flow Properties   Verify availability of the product
    Move Step To Board Position   20   55
    Sleep    2
    Change Component Name In Flow Properties   Order to warehousing for product preparation
    Move Step To Board Position   75   55
    Sleep    2
    Change Component Name In Flow Properties   Inform the customer
    Sleep  5

Connect the components
    Click Component    first
    Connect Components In Flow Main Panel    first          002Added1   12      4
    Click Component    002Added1
    Connect Components In Flow Main Panel    002Added1      001Added3   12      4
    Click Component    001Added3
    Connect Components In Flow Main Panel    001Added3      002Added2    8      4
    Click Component    001Added3
    Connect Components In Flow Main Panel    001Added3      002Added3   16      4
    Click Component    002Added2
    Connect Components In Flow Main Panel    002Added2      001Added5   12      4
    Click Component    002Added3
    Connect Components In Flow Main Panel    002Added3      001Added4   11      4
    Click Component    001Added4
    Connect Components In Flow Main Panel    001Added4      002Added4   12      4
    Click Component    001Added5
    Connect Components In Flow Main Panel    001Added5      002Added5   14      2
    Click Component    001Added5
    Connect Components In Flow Main Panel    001Added5      002Added6   10      4
    Click Component    002Added4
    Connect Components In Flow Main Panel    002Added4      001END1     12      4
    Click Component    002Added5
    Connect Components In Flow Main Panel    002Added5      001Added4   16      8
    Click Component    002Added6
    Connect Components In Flow Main Panel    002Added6      001END2     12      4

Set select owner and owner
    [Arguments]    ${position}    ${user}
    Click Select Owner Menu In Flow Properties
    Select Owner From List In Flow Properties    position=${position}
    Click Owner Combobox In Flow Properties
    Search_owner In Menu In Flow Properties    ${user}
    Select Owner In Menu In Flow Properties

Components Should Be Displayed In The Main Panel
    ${components_list}    Obtain Dictionary Status In Flow Main Panel
    Dictionary Should Contain Component    ${components_list}    start
    Dictionary Should Contain Component    ${components_list}    first
    Dictionary Should Contain Component    ${components_list}    002Added1
    Dictionary Should Contain Component    ${components_list}    002Added2
    Dictionary Should Contain Component    ${components_list}    002Added3
    Dictionary Should Contain Component    ${components_list}    002Added4
    Dictionary Should Contain Component    ${components_list}    002Added5
    Dictionary Should Contain Component    ${components_list}    002Added6
    Dictionary Should Contain Component    ${components_list}    001END1
    Dictionary Should Contain Component    ${components_list}    001END2
    Dictionary Should Contain Component    ${components_list}    001Added3
    Dictionary Should Contain Component    ${components_list}    001Added4
    Dictionary Should Contain Component    ${components_list}    001Added5

Components Should Be Conected
    Dictionary Should Contain Component        first            12
    Dictionary Should Contain Component        002Added1        12
    Dictionary Should Contain Component        002Added2        4
    Dictionary Should Contain Component        002Added3        4
    Dictionary Should Contain Component        002Added4        14
    Dictionary Should Contain Component        002Added5        2
    Dictionary Should Contain Component        002Added6        4
    Dictionary Should Contain Component        001END1          4
    Dictionary Should Contain Component        001END2          4
    Dictionary Should Contain Component        001Added3        16
    Dictionary Should Contain Component        001Added4        8
    Dictionary Should Contain Component        001Added5        10

Set A User In Flow Admin Section
    Click Dropdown Arrow In Flow Permissions
    Select User From Dropdown In Flow Permissions    Fabian Cabrejo

Set A User In Process Permissions Section
    Delete All Users In Dropdown In Process Permission
    Click Dropdown Arrow In Process Permission
    Select User From Dropdown In Process Permission    Denisse Cordova

Set Users In Sections Visibility
    Delete All Users In Section Visibility    3
    Click Dropdown Arrow In Section Visibility    3
    Select User From Dropdown In Section Visibility    Denisse Cordova   3
    Click Dropdown Arrow In Section Visibility    3
    Select User From Dropdown In Section Visibility    Telma Rios   3
    Delete All Users In Section Visibility    4
    Click Dropdown Arrow In Section Visibility    4
    Select User From Dropdown In Section Visibility    Roger Renjifo   4
    Click Dropdown Arrow In Section Visibility    4
    Select User From Dropdown In Section Visibility    Denisse Cordova   4

Users Selected should be visible
    Users Selected List In Section Visibility Should Contain    Telma Rios    3
    Users Selected List In Section Visibility Should Contain    Denisse Cordova    3
    Users Selected List In Section Visibility Should Contain    Roger Renjifo    4
    Users Selected List In Section Visibility Should Contain    Denisse Cordova    4
