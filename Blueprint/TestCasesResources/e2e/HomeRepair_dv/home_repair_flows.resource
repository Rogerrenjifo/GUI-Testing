*** Settings ***
Resource            Blueprint/TestCasesResources/e2e/HomeRepair_dv/imports.resource


*** Variables ***
${STEP_ID}                  001Added
${ACTION_ID}                002Added
${START_ID}                 start
${FIRST_ID}                 first
${END_ID}                   001END

*** Keywords ***
Change Initial Step Name To "Repair Request"
    Click Component                               ${FIRST_ID}
    Change Component Name In Flow Properties      Repair request

Add And Connect Action Component "Not Available worker" 
    Add Action Component             Not Available worker        10       42       
    Click Component                               ${FIRST_ID}
    Connect Components In Flow Main Panel         ${FIRST_ID}    ${ACTION_ID}1    12    4
    
Add And Connect Action Component "Available worker"
    Add Action Component             Available worker            10       55 
    Click Component                               ${FIRST_ID}
    Connect Components In Flow Main Panel         ${FIRST_ID}    ${ACTION_ID}2    16    16

Add And Connect Step Component "Ask client to wait"
    Add Step Component               Ask client to wait          40       42
    Click Component                               ${ACTION_ID}1
    Connect Components In Flow Main Panel         ${ACTION_ID}1    ${STEP_ID}1     8    16

Add And Connect Action Component "Client decide to wait"
    Add Action Component             Client decide to wait       70       42
    Click Component                               ${STEP_ID}1
    Connect Components In Flow Main Panel         ${STEP_ID}1     ${ACTION_ID}3    8    16

Add And Connect Step Component "Update hold on list"
    Add Step Component               Update hold on list         70       25
    Click Component                               ${ACTION_ID}3
    Connect Components In Flow Main Panel         ${ACTION_ID}3   ${STEP_ID}2      4    12

Add And Connect Action Component "Perform new request" 
    Add Action Component             Perform new request         40       25 
    Click Component                               ${STEP_ID}2
    Connect Components In Flow Main Panel         ${STEP_ID}2   ${ACTION_ID}4      16    8
    Click Component                               ${ACTION_ID}4
    Connect Components In Flow Main Panel         ${ACTION_ID}4   ${FIRST_ID}      16    8

Add And Connect Action Component "Client decided not to wait"
    Add Action Component             Client decided not to wait   40       55 
    Click Component                               ${STEP_ID}1
    Connect Components In Flow Main Panel         ${STEP_ID}1   ${ACTION_ID}5     12    4

Add And Connect Step Component "Update request database"
    Add Step Component               Update request database      70       55
    Click Component                               ${ACTION_ID}5
    Connect Components In Flow Main Panel         ${ACTION_ID}5   ${STEP_ID}3     8    16

Add And Connect Step Component "Fill form request"
    Add Step Component               Fill form request            10       65
    Click Component                               ${ACTION_ID}2
    Connect Components In Flow Main Panel         ${ACTION_ID}2   ${STEP_ID}4     12    4

Add And Connect Action Component "Repair work"
    Add Action Component             Repair work                  40       65        Damian Villanueva
    Click Component                               ${STEP_ID}4
    Connect Components In Flow Main Panel         ${STEP_ID}4   ${ACTION_ID}6     8    16

Add And Connect Step Component "Reschedule"     
    Add Step Component               Reschedule                   70       65
    Click Component                               ${STEP_ID}5
    Connect Components In Flow Main Panel         ${STEP_ID}5   ${ACTION_ID}6     16    8

Add And Connect Action Component "Finished"
    Add Action Component             Finished                     10       77

Add And Connect Step Component "Work status"
    Add Step Component               Work status                  40       77
    Click Component                               ${STEP_ID}6
    Connect Components In Flow Main Panel         ${STEP_ID}6   ${ACTION_ID}7    16    8
    Click Component                               ${ACTION_ID}6
    Connect Components In Flow Main Panel         ${ACTION_ID}6   ${STEP_ID}6    12    4

Add And Connect Action Component "Not finished"
    Add Action Component            Not finished                  70       77
    Click Component                               ${STEP_ID}6
    Connect Components In Flow Main Panel         ${STEP_ID}6   ${ACTION_ID}8    8    16
    Click Component                               ${ACTION_ID}8
    Connect Components In Flow Main Panel         ${ACTION_ID}8   ${STEP_ID}5    4    12

Add And Connect Step Component "Ask payment"
    Add Step Component              Ask payment                   10       88       
    Click Component                               ${ACTION_ID}7
    Connect Components In Flow Main Panel         ${ACTION_ID}7   ${STEP_ID}7    12    4

Set "Update Request Database" As Component As End Step
    Click Component                               ${STEP_ID}3
    Click End Step Checkbox In Flow Properties    ${STEP_ID}3

Set "Ask payment" Component As End Step
    Click Component                               ${STEP_ID}7
    Click End Step Checkbox In Flow Properties    ${STEP_ID}7



Set Flow Admin User
    Click Dropdown Arrow In Flow Permissions
    Select User From Dropdown In Flow Permissions               Maria Mamani

Set Supervisor User
    Delete All Users In Section Visibility                                           3
    Click Dropdown Arrow In Section Visibility                                       3
    Select User From Dropdown In Section Visibility             Damian Villanueva    3

User Should Be Visible
    Users Selected List In Section Visibility Should Contain    Damian Villanueva    3