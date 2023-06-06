*** Settings ***
Resource    Blueprint/TestCasesResources/E2E/scholarship_application_scenario.resource

Force Tags    SCHOLARSHIP_APPLICATION
Suite Setup    Search Flow

*** Test Cases ***
Verify a form can be created and its elements properties modified
    #Section 1
    Create Applicant Information Section
    Components Order Should Be    ${component_names_section_1}
    #Section 2
    Create Documentation Section
    #Section 3
    Create Academic Peerformance Section
    Click Save Next Button In Flow Header

#Verify a flow can be created and its components edited
#    Click Tab In Flow Header    Create Flow
#    Move Component To Specific Position In Flow Main Panel    start    ${60}    ${5}
#    Move Component To Specific Position In Flow Main Panel    first    ${60}    ${20}
#    Change Component Name In Flow Properties    Scholarship Application
#    Add Action With Name To Board    Application form is not complete    ${5}    ${17}
#    Add Step With Name To Board    Ask applicant for send complete form    ${5}    ${30}
#    Add Action With Name To Board   Application form is complete    ${85}    ${17}
#    Add Step With Name To Board    Review Documentation    ${85}    ${30}
#    Add Action With Name To Board   Application form is complete    ${85}    ${45}
#    Add Step With Name To Board    Ask appliant for send the complete documentation    ${85}    ${55}
#    Add Action With Name To Board   Documentiation is complete    ${43}    ${33}
#    Add Step With Name To Board    Review Applicant's Academic Performance    ${43}    ${43}
#    Add Action With Name To Board   Does not meet academic requirements    ${5}    ${45}
#    Add Step With Name To Board    Decline Scholarship Application    ${5}    ${57}
#    Add Action With Name To Board   Meets Academic Requirements    ${43}    ${60}
#    Add Step With Name To Board    Accept Scholarship Application    ${43}    ${70}
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
#    Check Step 1 As End Step
#    Check Step 3 As End Step
#    Check Step 5 As End Step
#    Check Step 6 As End Step

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
    ${component_types_section_1}    Create List    Text    Checkbox    Dropdown    Checkbox
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

Create Academic Peerformance Section
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


Add ${component} In Column ${column} Of Section ${section}, With ${name} As Name And ${placeholder} As Placeholder
    Add Component To Column Section In Create Form    ${component}    section-${section}-column${column}
    Set Name In Form Properties Panel    ${name}
    Set Placeholder In Form Properties Panel    ${placeholder}

Add ${component} ${component_number} Down ${existent_component_type} ${existent_component_number} In Section ${section_number}, With ${name} As Name And ${placeholder} As Placeholder
    Add Component Down Existent Component In Create Form    ${component}    section-${section_number}_${existent_component_type}-${existent_component_number}    ${component_number}
    Set Name In Form Properties Panel    ${name}
    Set Placeholder In Form Properties Panel    ${placeholder}

