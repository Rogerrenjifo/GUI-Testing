*** Settings ***
Resource     Blueprint/TestCasesResources/E2E/common.imports.resource
Force Tags    E2E   DRIVERS_LICENSE
Suite Teardown    Delete Storage

*** Variables ***
${flow_name}    DL-GUI-10
${group_name}   DL-GUI-Group-10
@{age_dropdown}      Yes, I am      No, I am not
@{exam_dropdown}     Yes, I passed the exam      No, I did not pass the exam
@{expected_section_1_components}    Name  Are you more than 18 years old?   Age
@{expected_section_2_components}    Did you pass the exam?
@{expected_section_3_components}    Pay exam fees

*** Test Cases ***
Verify that is possible to create a group
    Click On Users And Groups Button
    Create New Group    ${group_name}
    ${message}    Get Pop Up Text Created Group
    Add User To A Group    Rocio.Morales
    Add User To A Group    Celeste.Palet
    Add User To A Group    Martin.Alvarez

Verify a is posible to create a flow with a given name
    Click On Flows Drop Down Button
    Sleep    2s
    Click On New Flow Button
    Insert New Flow Name    ${flow_name}
    Insert New Flow Code    D70
    Click On Create New Flow Button
    Pop Up Message Text Should Be    Process created

Verify that is possible to add sections and components
    Sleep    2s
    Define Section Name Process In Form Properties      Section 1   Information
    Add Components To Section 1 And Verify Order Of Them
    Add Section 2 And Set Name
    Add Components To Section 2 And Verify Order Of Them
    Add Section 3 And Set Name
    Add Components To Section 3 And Verify Order Of Them

Verify it is possible to create flow without errors
    Click Tab In Flow Header    Create Flow
    Sleep    1s
    Click Component                            first
    Change Component Name In Flow Properties   Age verification
    Add Field To Update An Select Given Result    3
    Add Field To Update An Select Given Result    1

    Add Action To Board    20   55   Less than 18 years old
    Add Action To Board    50   5    Have more than 18 years old
    Add Step To Board      20   65   Wait until have more than 18 years old
    Add Field To Update An Select Given Result    2
    Add Step To Board      70   20   Payment
    Add Field To Update An Select Given Result    5
    Add Action To Board    75   35   Pay the fees
    Add Step To Board      75   45   Have medical exam
    Add Field To Update An Select Given Result    4
    Add Action To Board    65   60   Fail the medical exam
    Add Action To Board    99   60   Pass the medical exam
    Add Step To Board      75   70   Have technical exam
    Add Field To Update An Select Given Result    4
    Add Action To Board    60   85   Pass the technical exam
    Add Action To Board    95   85   Fail the technical exam
    Add Step To Board      75   95   Request licence process
    Add Action To Board    20   98   Pick up driver's license
    Add Step To Board      20   80   Got driver's license

    Click and connect componet in flow main panel   first       002Added2   5   16
    Click and connect componet in flow main panel   first       002Added1   12   4
    Click and connect componet in flow main panel   002Added1   001Added1   12   4
    Click and connect componet in flow main panel   001Added1   002Added2   8   14
    Click and connect componet in flow main panel   002Added2   001Added2   8   16
    Click and connect componet in flow main panel   001Added2   002Added3   12   4
    Click and connect componet in flow main panel   002Added3   001Added3   12   4
    Click and connect componet in flow main panel   001Added3   002Added4   13   3
    Click and connect componet in flow main panel   002Added4   001Added2   16   15
    Click and connect componet in flow main panel   002Added5   001Added4   12   4
    Click and connect componet in flow main panel   001Added4   002Added6   13   3
    Click and connect componet in flow main panel   001Added3   002Added5   7   5
    Click and connect componet in flow main panel   001Added4   002Added7   11   5
    Click and connect componet in flow main panel   002Added6   001Added5   12   4
    Click and connect componet in flow main panel   002Added7   001Added2   8   8
    Click and connect componet in flow main panel   001Added5   002Added8   16   8
    Click and connect componet in flow main panel   002Added8   001Added6   4   12
    Click Component                                 001Added6
    Click End Step Checkbox In Flow Properties      001Added6
    Click Save Next Button In Flow Header
    Pop Up Message Text Should Be   Flow ${flow_name} updated.

Verify it is possible to publish a created flow
    Click Tab In Flow Header    Permissions
    Sleep    1s
    Delete All Users In Dropdown In Flow Permissions
    Add New Flow Admin By Typing Process In Flow Permission    ${group_name}
    Click Save Next Button In Flow Header
    Pop Up Message Text Should Be    Flow ${flow_name} updated.
    Sleep    5s
    Click Save Publish Button

Verify that flow created is published in projects
    Sleep    2s
    Click On Projects Button
    Sleep    5s
    Insert Project Name Into The Search Bar    ${flow_name}
    Click On A Project Result
    Sleep    20s
    Project Title Should Be    ${flow_name}
