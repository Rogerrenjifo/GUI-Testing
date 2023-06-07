*** Settings ***
Documentation    E2E test to simulate the use of Blueprint to implement a flow of the process
...              of the application to enter Jala's AT specialization.
Resource         Blueprint/TestCasesResources/e2e/JalaSpecializationAT/scenario_resources.resource
Suite Setup      Login to blueprint

*** Test Cases ***
E2E Scenario: Application for Jala AT Specialization
    Sleep    25
    Create new flow if does not exist and go to flow page    Leo E2E Scenario 2    L4E
    Sleep    2
    Add field component on column 2    textbox
    Add field component under field 1    textbox
    Add field component under field 2    date
    Add field component under field 3    textbox
    Add field component under field 4    numericbox
    Add field component under field 5    dropdown
    Configure first field as First Name
    Configure second field as Last Name
    Configue third field as ID
    Configure date field as Birth date
    Configure fifth field as Residence Country
    Configure numeric field as Cellphone number
    Configure dropdown as time-availability
    Verify order of components on form
    Click tab in flow header    Create Flow
    Sleep    1
    Move action to board position    35    28
    the_component_should_be_added_to_the_main_board    002Added1
    Move step to board position    60    26
    the_component_should_be_added_to_the_main_board    001Added1
    Move action to board position    12    36
    the_component_should_be_added_to_the_main_board    002Added2
    Move step to board position    12    44
    the_component_should_be_added_to_the_main_board    001Added2
    Move action to board position    12    54
    the_component_should_be_added_to_the_main_board    002Added3
    Move step to board position    12    62
    the_component_should_be_added_to_the_main_board    001Added3
    Move action to board position    12    72
    the_component_should_be_added_to_the_main_board    002Added4
    Move step to board position    12    80
    the_component_should_be_added_to_the_main_board    001Added4
    Connect given components using given points    first    002Added1    8    16
    Connect given components using given points    002Added1    001Added1    8    16
    Connect given components using given points    first    002Added2    12    4
    Connect given components using given points    002Added2    001Added2    12    4
    Connect given components using given points    001Added2    002Added1    8    14
    Connect given components using given points    001Added2    002Added3    12    4
    Connect given components using given points    002Added3    001Added3    12    4
    Connect given components using given points    001Added3    002Added1    8    10
    Connect given components using given points    001Added3    002Added4    12    4
    Connect given components using given points    002Added4    001Added4    12    4
    Configure information validation step
    Configure rejected action
    Configure disqualified step
    Configure information validated action
    Configure technical test step
    Configure tests passed action
    Configure english interview step
    Configure english interview passed action
    Configure accepted step
    Click tab in flow header    Publish
    Sleep    1
    Click save publish button
    Sleep    10
    Search for project and go    Leo
    Sleep    10
