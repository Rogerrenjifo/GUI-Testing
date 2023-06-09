*** Settings ***
Resource            Blueprint/TestCasesResources/e2e/HomeRepair_dv/imports.resource


*** Variables ***
@{jobs}                     Plumbery    Electrician    Constructor     Painter
@{status}                   busy        Free
@{expected_components_1}    Ticket      Clients        Client Phone    Work Request    Client Address    Cost
@{expected_components_2}    Complete Name   Workers Phone  Workers Address   References    Status   Work
@{expected_components_3}    Ticket   Start Date    Supervisor    Worker    End Date

*** Keywords ***
Define Starting Section
    Sleep  5
    Define Section Name Process In Form Properties             Section 1                    Repair Request

Add "Ticket" Field In Starting Section
    Select Component In Form Main Panel                        section-1_textbox-1
    Set Name In Form Properties Panel                          Ticket
    Set Placeholder In Form Properties Panel                   Enter ticket number

Add "Work Request" In Starting Section
    Add Component To Column Section In Create Form             dropdown                     section-1-columnB
    Select Component In Form Main Panel                        section-1_dropdown-1
    Set Name In Form Properties Panel                          Work Request
    Add Dropdown Values Process In Form Properties             section-1_dropdown-1         ${jobs}
    Click Required Field Label In Form Properties Panel

Add "Clients list" In Starting Section
    Add Component Down Existent Component In Create Form       userlist                     section-1_textbox-1
    Set Name In Form Properties Panel                          Clients
    Select Userlist Value In Form Properties Panel             Telma Rios

Add "Client address" Field In Starting Section
    Add Component Down Existent Component In Create Form       textbox                      section-1_dropdown-1
    Set Name In Form Properties Panel                          Client Address

Add "Clients phone number" In Starting Section    
    Add Component Down Existent Component In Create Form       numericbox                   section-1_userlist-1
    Set Name In Form Properties Panel                          Client Phone    

Add "Cost" In Starting Section    
    Add Component Down Existent Component In Create Form       numericbox                   section-1_textbox-2
    Set Name In Form Properties Panel                          Cost

The Starting Section Should Contains Those Fields    
    The Components Order Should Be                             ${expected_components_1}     section-1



Add "Workers" Section
    Sleep  5
    Add New Section In Create Form      
    Set Section Name In Form Properties Panel                  Workers

Add "Complete Name" Field
    Add Component To Column Section In Create Form             textbox                      section-2-columnA
    Set Name In Form Properties Panel                          Complete Name
    Set Placeholder In Form Properties Panel                   Enter workers name

Add "References" Field
    Add Component To Column Section In Create Form             multilinebox                 section-2-columnB
    Set Name In Form Properties Panel                          References
    Click Required Field Label In Form Properties Panel

Add "Workers Phone" Field    
    Add Component Down Existent Component In Create Form       numericbox                   section-2_textbox-1
    Set Name In Form Properties Panel                          Workers Phone    

Add "Status" Field    
    Add Component Down Existent Component In Create Form       dropdown                     section-2_multilinebox-1
    Select Component In Form Main Panel                        section-2_dropdown-1
    Set Name In Form Properties Panel                          Status
    Add Dropdown Values Process In Form Properties             section-2_dropdown-1         ${status}

Add "Worker address" Field
    Add Component Down Existent Component In Create Form       textbox                      section-2_numericbox-1
    Set Name In Form Properties Panel                          Workers Address

Add "Work" Field
    Add Component Down Existent Component In Create Form       dropdown                     section-2_dropdown-1
    Select Component In Form Main Panel                        section-2_dropdown-2
    Set Name In Form Properties Panel                          Work
    Add Dropdown Values Process In Form Properties             section-2_dropdown-2         ${jobs}
    Click Required Field Label In Form Properties Panel
    
The Workers Form Should Contains Those Fields    
    The Components Order Should Be                             ${expected_components_2}     section-2



Add Section "Form Request"
    Sleep    5
    Add New Section In Create Form      
    Set Section Name In Form Properties Panel                  Form Request

Add "Ticket" Field In Form
    Add Component To Column Section In Create Form             textbox                      section-3-columnA
    Set Name In Form Properties Panel                          Ticket
    Set Placeholder In Form Properties Panel                   Enter ticket code

Add "Worker" list In Form
    Add Component To Column Section In Create Form             userlist                     section-3-columnB
    Set Name In Form Properties Panel                          Worker
    Select Userlist Value In Form Properties Panel             Daniel Villarroel

Add "Start Date" 
    Add Component Down Existent Component In Create Form       date                         section-3_textbox-1
    Set Name In Form Properties Panel                          Start Date    
    
Add "End Date"
    Add Component Down Existent Component In Create Form       date                         section-3_userlist-1
    Set Name In Form Properties Panel                          End Date

Add "Supervisor" Field
    Add Component To Column Section In Create Form             userlist                     section-3-columnB
    Set Name In Form Properties Panel                          Supervisor
    Select Userlist Value In Form Properties Panel             Damian Villanueva

The Request Form Should Contains Those Fields
    The Components Order Should Be                             ${expected_components_3}     section-3



