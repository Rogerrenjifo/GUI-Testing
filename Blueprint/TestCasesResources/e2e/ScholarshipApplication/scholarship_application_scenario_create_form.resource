*** Settings ***
Resource    Blueprint/TestCasesResources/e2e/ScholarshipApplication/scholarship_application_scenario_importations.resource

*** Variables ***
@{universities}    University 1    University 2    University 3    University 4
${section_name_1}    Applicant Information
${section_name_2}    Documentation
${section_name_3}    Academic Performance
@{component_names_section_1}    Applicant Full Name    Personal Information complete    University    Academic information complete
@{component_types_section_1}    Checkbox    Dropdown    Checkbox
@{component_names_section_2}    Id Copy    Analitical certificate    Regular student certificate    Certificates of extra curricular activities
@{component_types_section_2}    Checkbox    Checkbox    Checkbox    Checkbox
@{component_names_section_3}    Average    Additional information    Extra curricular activities
@{component_types_section_3}    Number    Multi    Checkbox

*** Keywords ***
Create Applicant Information Section
    Define Section Name Process In Form Properties    Section 1    ${section_name_1}
    Define Element Name Process In Form Properties    section-1_textbox-1    Applicant Full Name
    Set Placeholder In Form Properties Panel    Insert the applicant full name
    Add Component To Column Section In Create Form    dropdown    section-1-columnB
    Set Name In Form Properties Panel    University
    Set Placeholder In Form Properties Panel    Select an university option
    Add Dropdown Values Process In Form Properties    section-1_dropdown-1    ${universities}
    Add Component Down Existent Component In Create Form    checkbox   section-1_textbox-1
    Set Name In Form Properties Panel    Personal Information complete
    Add Component Down Existent Component In Create Form    checkbox   section-1_dropdown-1    2
    Set Name In Form Properties Panel    Academic information complete

Create Documentation Section
    Add New Section In Create Form
    Set Section Name In Form Properties Panel   ${section_name_2}
    Add Component To Column Section In Create Form    checkbox    section-2-columnA
    Set Name In Form Properties Panel    Id Copy
    Add Component To Column Section In Create Form    checkbox    section-2-columnB    2
    Set Name In Form Properties Panel    Regular student certificate
    Add Component Down Existent Component In Create Form    checkbox    section-2_checkbox-1    3
    Set Name In Form Properties Panel    Analitical certificate
    Add Component Down Existent Component In Create Form    checkbox    section-2_checkbox-2    4
    Set Name In Form Properties Panel    Certificates of extra curricular activities

Create Academic Performance Section
    Add New Section In Create Form
    Set Section Name In Form Properties Panel    ${section_name_3}
    Add Component To Column Section In Create Form    numericbox    section-3-columnA
    Set Name In Form Properties Panel    Average
    Set Placeholder In Form Properties Panel    Enter the applicant average
    Select Number Format In Form Properties Panel    comma
    Add Component To Column Section In Create Form    checkbox    section-3-columnB
    Set Name In Form Properties Panel    Extra curricular activities
    Add Component Down Existent Component In Create Form    multilinebox    section-3_numericbox-1
    Set Name In Form Properties Panel    Additional information
    Set Placeholder In Form Properties Panel    Please enter additional information relevant for the process
