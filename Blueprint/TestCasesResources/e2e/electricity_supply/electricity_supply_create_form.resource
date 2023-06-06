*** Settings ***
Resource    Blueprint/TestCasesResources/E2E/electricity_supply/electricity_supply_importation.resource

*** Keywords ***
Set First Section In Create Form
    Define Section Name Process In Form Properties   Section 1    Documentation
    Select Component In Form Main Panel   section-1_textbox-1
    Set Name And Placeholder From Properties Panel   User   Enter user name
    Add Component To Column Section In Create Form    checkbox   section-1-columnB
    Set Name In Form Properties Panel    Plans
    Add Component Down Existent Component In Create Form    date   section-1_textbox-1
    Set Name And Check As Required From Properties Panel    Date of application presentation
    Add Component Down Existent Component In Create Form    checkbox   section-1_checkbox-1   2
    Set Name In Form Properties Panel    Inscription Form
    Add Component Down Existent Component In Create Form    date   section-1_date-1   2
    Set Name And Check As Required From Properties Panel    Due date for submission of documents
    Add Component Down Existent Component In Create Form    checkbox   section-1_checkbox-2   3
    Set Name In Form Properties Panel    House Deeds

First Section Components Should Be Displayed
    ${expected_titles}=   Create List    User  Date of application presentation   Due date for submission of documents   Plans   Inscription Form   House Deeds
    Components Order Should Be    ${expected_titles}
    ${expected_types}=   Create List   Date   Date   Checkbox   Checkbox   Checkbox
    Component type should be   ${expected_types}

Second Section Components Should Be Displayed
    ${expected_titles}=   Create List    Inspector Selection   Notes
    Components Order Should Be    ${expected_titles}   section-2
    ${expected_types}=   Create List   Userlist   Multi
    Component type should be   ${expected_types}   section-2

Third Section Components Should Be Displayed
    ${expected_titles}=   Create List    Folio   User Number   Date of supply discharge   Technician selection
    Components Order Should Be    ${expected_titles}   section-3
    ${expected_types}=   Create List   Text   Number   Date   Userlist
    Component type should be   ${expected_types}   section-3

Set Second Section In Create Form
    Add New Section In Create Form
    Set Section Name In Form Properties Panel    Revision of plans
    Add Component To Column Section In Create Form    userlist   section-2-columnA
    Set Name And User Values From Main Panel    Inspector Selection   Inspectors - GUI DEMO 3
    Set Placeholder In Form Properties Panel       Select a Inspector
    Add Component To Column Section In Create Form    multilinebox   section-2-columnB
    Set Name And Placeholder From Properties Panel    Notes   Enter your notes here

Set Third Section In Create Form
    Add New Section In Create Form
    Set Section Name In Form Properties Panel    User Registration
    Add Component To Column Section In Create Form    textbox   section-3-columnA
    Set Name And Placeholder From Properties Panel    Folio   Enter folio of approval certificate
    Add Component To Column Section In Create Form    date   section-3-columnB
    Set Name In Form Properties Panel    Date of supply discharge
    Add Component Down Existent Component In Create Form    numericbox    section-3_textbox-1
    Set Name And Placeholder From Properties Panel    User Number   Enter user number for billing
    Add Component Down Existent Component In Create Form    userlist    section-3_date-1
    Set Name And User Values From Main Panel    Technician selection   Technicians - GUI DEMO 3
    Set Placeholder In Form Properties Panel    Select a Technician

Sections Should Be Displayed
    ${expected_result}=   Create List    Documentation   Revision of plans   User Registration
    Section Order Should Be   ${expected_result}
