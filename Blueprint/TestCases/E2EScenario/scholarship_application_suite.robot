*** Settings ***
Resource    Blueprint/TestCasesResources/E2E/scholarship_application_scenario.resource

Force Tags    SCHOLARSHIP_APPLICATION
Suite Setup    Search Flow
Suite Teardown    Delete Flow Process In Flow Header

*** Variables ***
${expected_success_popup_color}    rgba(92, 184, 92, 1)
${color_component_with_error}   rgb(255, 114, 105)
${expected_text_popup}    Flow AT19-Scenario-Scholarship-RM-6NC updated.
${user_group}   AT19-GUITESTING-SCENARIO-SCHOLARSHIP

*** Test Cases ***
#Verify a form can be created and its elements properties modified
#    #Section 1
#    Create Applicant Information Section
#    Components Order Should Be    ${component_names_section_1}
#    Components Type In Section Should Be    ${component_types_section_1}
#    #Section 2
#    Create Documentation Section
#    Components Order Should Be    ${component_names_section_2}    section-2
#    Components Type In Section Should Be    ${component_types_section_2}    section-2
#    #Section 3
#    Create Academic Performance Section
#    Components Order Should Be    ${component_names_section_3}    section-3
#    Components Type In Section Should Be    ${component_types_section_3}    section-3
#    Flow Header Title Should Be The Same As The Title Set In Create Flow    ${flow_name_for_edit}
#    Click Save Button In Flow Header
#    Popup Message Should Be Displayed
#    Pop Up Message Should Be Displayed In Expected Color    ${expected_success_popup_color}
#    Popup Message Text Should Be    Flow ${flow_name_for_edit} updated.
#
#Verify a flow can be created and its components edited
#    Click Tab In Flow Header    Create Flow
#    Move Component To Specific Position In Flow Main Panel    start    ${60}    ${5}
#    Move Component To Specific Position In Flow Main Panel    first    ${60}    ${20}
#    Change Component Name In Flow Properties    Scholarship Application
#    Add Action With Name To Board    Application form is not complete    ${5}    ${17}    1
#    Add Step With Name To Board    Ask applicant for send complete form    ${5}    ${30}    1
#    Add Action With Name To Board   Documentiation is not complete    ${85}    ${17}    2
#    Add Step With Name To Board    Review Documentation    ${85}    ${30}   2
#    Add Action With Name To Board   Application form is complete    ${85}    ${45}    3
#    Add Step With Name To Board    Ask appliant for send the complete documentation    ${85}    ${55}    3
#    Add Action With Name To Board   Documentiation is complete    ${43}    ${33}    4
#    Add Step With Name To Board    Review Applicant's Academic Performance    ${43}    ${43}    4
#    Add Action With Name To Board   Does not meet academic requirements    ${5}    ${45}    5
#    Add Step With Name To Board    Decline Scholarship Application    ${5}    ${57}    5
#    Add Action With Name To Board   Meets Academic Requirements    ${43}    ${60}   6
#    Add Step With Name To Board    Accept Scholarship Application    ${43}    ${70}    6
#    Add Action With Name To Board    Recive the Scholarship Application    ${5}   ${7}    7
#    Add Action With Name To Board    Recive Applicant documentation    ${85}    ${70}    8
#    Connect Initial Step With Action 1 From Point 16 To Point 8
#    Connect Initial Step With Action 2 From Point 8 To Point 16
#    Connect Action 1 With Step 1 From Point 12 To Point 4
#    Connect Action 2 With Step 2 From Point 12 To Point 4
#    Connect Step 2 With Action 3 From Point 12 To Point 4
#    Connect Action 3 With Step 3 From Point 12 To Point 4
#    Connect Step 2 With Action 4 From Point 16 To Point 8
#    Connect Action 4 With Step 4 From Point 12 To Point 4
#    Connect Step 4 With Action 6 From Point 12 To Point 4
#    Connect Action 6 With Step 6 From Point 12 To Point 4
#    Connect Step 4 With Action 5 From Point 16 To Point 8
#    Connect Action 5 With Step 5 From Point 12 To Point 4
#    Connect Action 7 With Initial Step From Point 8 To Point 2
#    Connect Step 1 With Action 7 From Point 16 To Point 16
#    Connect Step 3 With Action 8 From Point 12 To Point 4
#    Connect Action 8 With Step 2 From Point 8 To Point 8
#    Components Titles Should Be    ${steps}
#    Components Titles Should Be    ${actions}
#    Check Step 5 As End Step
#    Check Step 6 As End Step
#    Components Titles Should Not Have Errors    ${actions}      ${color_component_with_error}

Verify the permissions of a flow can be edited
    Click Tab In Flow Header    Permissions
    Set Flow Permissions
    Set Process Permissions
    Set Visibility Section In Applicant Information, Documentation And Academic Performance
    Sleep    10
    User Selected In Flow Permissions Should Be    ${user_group}
    Sleep    20


*** Keywords ***
Create Applicant Information Section
    Define Section Name Process In Form Properties    Section 1    Applicant Information
    Define Element Name Process In Form Properties    section-1_textbox-1    Applicant Full Name
    Set Placeholder In Form Properties Panel    Insert the applicant full name
    Add Component To Column Section In Create Form    dropdown    section-1-columnB
    Set Name In Form Properties Panel    University
    Set Placeholder In Form Properties Panel    Select an university option
    ${universities}    Create List    University 1    University 2    University 3    University 4
    Add Dropdown Values Process In Form Properties    section-1_dropdown-1    ${universities}
    Add Component Down Existent Component In Create Form    checkbox   section-1_textbox-1
    Set Name In Form Properties Panel    Personal Information complete
    Add Component Down Existent Component In Create Form    checkbox   section-1_dropdown-1    2
    Set Name In Form Properties Panel    Academic information complete
    ${component_names_section_1}    Create List    Applicant Full Name    Personal Information complete    University    Academic information complete
    ${component_types_section_1}    Create List    Checkbox    Dropdown    Checkbox
    Set Suite Variable    ${component_names_section_1}
    Set Suite Variable    ${component_types_section_1}

Create Documentation Section
    Add New Section In Create Form
    Set Section Name In Form Properties Panel    Documentation
    Add Component To Column Section In Create Form    checkbox    section-2-columnA
    Set Name In Form Properties Panel    Id Copy
    Add Component To Column Section In Create Form    checkbox    section-2-columnB    2
    Set Name In Form Properties Panel    Regular student certificate
    Add Component Down Existent Component In Create Form    checkbox    section-2_checkbox-1    3
    Set Name In Form Properties Panel    Analitical certificate
    Add Component Down Existent Component In Create Form    checkbox    section-2_checkbox-2    4
    Set Name In Form Properties Panel    Certificates of extra curricular activities
    ${component_names_section_2}    Create List    Id Copy    Analitical certificate    Regular student certificate    Certificates of extra curricular activities
    ${component_types_section_2}    Create List    Checkbox    Checkbox    Checkbox    Checkbox
    Set Suite Variable    ${component_names_section_2}
    Set Suite Variable    ${component_types_section_2}

Create Academic Performance Section
    Add New Section In Create Form
    Set Section Name In Form Properties Panel    Academic Performance
    Add Component To Column Section In Create Form    numericbox    section-3-columnA
    Set Name In Form Properties Panel    Average
    Set Placeholder In Form Properties Panel    Enter the applicant average
    Select Number Format In Form Properties Panel    comma
    Add Component To Column Section In Create Form    checkbox    section-3-columnB
    Set Name In Form Properties Panel    Extra curricular activities
    Add Component Down Existent Component In Create Form    multilinebox    section-3_numericbox-1
    Set Name In Form Properties Panel    Additional information
    Set Placeholder In Form Properties Panel    Please enter additional information relevant for the process
    ${component_names_section_3}    Create List    Average    Additional information    Extra curricular activities
    ${component_types_section_3}    Create List    Number    Multi    Checkbox
    Set Suite Variable    ${component_names_section_3}
    Set Suite Variable    ${component_types_section_3}

Set Flow Permissions
    Delete All Users In Dropdown In Flow Permissions
    Add New Flow Admin By Typing Process In Flow Permission    ${user_group}

Set Process Permissions
    Delete All Users In Dropdown In Flow Process Permission
    Add User To Initiate Process By Typing Process In Process Permissions    ${user_group}

Set Visibility Section In Applicant Information, Documentation And Academic Performance
    Delete All Users In Section Dropdown    3
    Add User To Section Visibility By Typing Process    ${user_group}   3
    Delete All Users In Section Dropdown    4
    Add User To Section Visibility By Typing Process    ${user_group}   4
    Delete All Users In Section Dropdown    5
    Add User To Section Visibility By Typing Process    ${user_group}   5
