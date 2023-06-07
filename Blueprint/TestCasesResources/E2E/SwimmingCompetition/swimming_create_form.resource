*** Settings ***
Resource    Blueprint/TestCasesResources/E2E/SwimmingCompetition/swimming_importations.resource

*** Keywords ***
Change Name From "section 1" To "Applicant Information"
    Select Section In Form Main Panel    Section 1
    Set Section Name In Form Properties Panel    Applicant Information

Change The Title Of The Default Textbox To "Name"
    Select Component In Form Main Panel    section-1_textbox-1
    Set Name In Form Properties Panel    Name

Create "ID" Numericbox 
    Add Component To Column Section In Create Form    numericbox    section-1-columnB
    Select Component In Form Main Panel    section-1_numericbox-1
    Set Name In Form Properties Panel    ID

Create "Gender" Dropdown
    Add Component To Column Section In Create Form    dropdown    section-1-columnA
    Select Component In Form Main Panel    section-1_dropdown-1
    Set Name In Form Properties Panel    Gender   
    Set Add Dropdown Value In Form Properties Panel    male
    Click Add Dropdown Button In Form Properties Panel
    Set Add Dropdown Value In Form Properties Panel    female
    Click Add Dropdown Button In Form Properties Panel

Create "Age" Numericbox 
    Add Component To Column Section In Create Form    numericbox    section-1-columnB
    Select Component In Form Main Panel    section-1_numericbox-2
    Set Name In Form Properties Panel    Age

Add new section with name "Swimming Styles"
    Add New Section In Create Form
    Select Section In Form Main Panel    Section 2
    Set Section Name In Form Properties Panel    Swimming Styles

Create "Free" Checkbox
    Add Component To Column Section In Create Form    checkbox    section-2-columnA
    Select Component In Form Main Panel    section-2_checkbox-1
    Set Name In Form Properties Panel    Free

Create "Back" Checkbox
    Add Component To Column Section In Create Form    checkbox    section-2-columnB
    Select Component In Form Main Panel    section-2_checkbox-2
    Set Name In Form Properties Panel    Back

Create "Butterfly" Checkbox
    Add Component To Column Section In Create Form    checkbox    section-2-columnA
    Select Component In Form Main Panel    section-2_checkbox-3
    Set Name In Form Properties Panel    Butterfly

Create "Chest" Checkbox
    Add Component To Column Section In Create Form    checkbox    section-2-columnB
    Select Component In Form Main Panel    section-2_checkbox-4
    Set Name In Form Properties Panel    Chest

Create Applicant Information Section
    Change Name From "section 1" To "Applicant Information"
    Change The Title Of The Default Textbox To "Name"
    Create "ID" Numericbox 
    Create "Gender" Dropdown
    Create "Age" Numericbox 

Create Swimming Styles Section
    Add new section with name "Swimming Styles"
    Create "Free" Checkbox
    Create "Back" Checkbox
    Create "Butterfly" Checkbox
    Create "Chest" Checkbox

Applicant Information Section Should Be Displayed
    ${expected_labels}   Create List    Name  Gender   ID   Age   
    Components Order Should Be    ${expected_labels}
    ${expected_components}   Create List   Dropdown   Number    Number
    Component type should be   ${expected_components}    section-1

Swimming Styles Section Should Be Displayed
    ${expected_labels}   Create List    Free  Butterfly   Back   Chest  
    Components Order Should Be    ${expected_labels}    section-2
    ${expected_components}   Create List   Checkbox   Checkbox    Checkbox    Checkbox
    Component type should be   ${expected_components}    section-2
