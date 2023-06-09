*** Settings ***
Documentation       Home Repair Project e2e Testing
Resource            Blueprint/TestCasesResources/e2e/HomeRepair_dv/setup_suite.resource

Suite Teardown      Sign Out And Close Browser

Force Tags          FLOWS    E2E    DVC

*** Variables ***
${flow}             HomeRepair_dv-


*** Test Cases ***
Verify That A Flow Can Be Created
    ${flow_name}    Create A New Flow With Random Code    ${flow}
    Page Header Title Shoul Be Flow Title                 ${flow_name}
    Set Suite Variable                                    ${flow_title}    ${flow_name}

Verify That The Default Section Can Be Set Up
    [Documentation]             Steps and verifications to set up the default section.
    Define Starting Section
    Add "Ticket" Field In Starting Section
    Add "Work Request" In Starting Section
    Add "Clients list" In Starting Section
    Add "Client address" Field In Starting Section
    Add "Clients phone number" In Starting Section    
    Add "Cost" In Starting Section    
    The Starting Section Should Contains Those Fields 
    Click Save Button In Flow Header

Verify That The Workers Section Can Be Created
    [Documentation]             Steps and verifications to set up the Workers section.
    Add "Workers" Section
    Add "Complete Name" Field
    Add "References" Field
    Add "Workers Phone" Field    
    Add "Status" Field    
    Add "Worker address" Field
    Add "Work" Field
    The Workers Form Should Contains Those Fields      
    Click Save Button In Flow Header

Verify That The Form Request Section Can Be Created
    [Documentation]             Steps and verifications to set up the Workers section.
    Add Section "Form Request"
    Add "Ticket" Field In Form
    Add "Worker" list In Form
    Add "Start Date" 
    Add "End Date"
    Add "Supervisor" Field
    The Request Form Should Contains Those Fields
    Click Save Button In Flow Header

Verify That The Complete Flow Is CReated
    [Documentation]                 Steps and verifications to create the project flow
    Click Tab In Flow Header        Create Flow
    Change Initial Step Name To "Repair Request"
    Add And Connect Action Component "Not Available worker" 
    Add And Connect Action Component "Available worker"
    Add And Connect Step Component "Ask client to wait"
    Add And Connect Action Component "Client decide to wait"
    Add And Connect Step Component "Update hold on list"
    Add And Connect Action Component "Perform new request" 
    Add And Connect Action Component "Client decided not to wait"
    Add And Connect Step Component "Update request database"
    Add And Connect Step Component "Fill form request"
    Add And Connect Action Component "Repair work"
    Add And Connect Step Component "Reschedule"     
    Add And Connect Action Component "Finished"
    Add And Connect Step Component "Work status"
    Add And Connect Action Component "Not finished"
    Add And Connect Step Component "Ask payment"
    Set "Update Request Database" As Component As End Step
    Set "Ask payment" Component As End Step
    Click Save Button In Flow Header

Verify Permissions Are Set
    Click Tab In Flow Header          Permissions
    Set Flow Admin User
    Set Supervisor User
    User Should Be Visible
    Click Save Next Button In Flow Header
    Popup Message Text Should Be Equal           Flow ${flow_title} updated.

Verify The Flow Is Published As Project
    Sleep    5s
    Click Save Publish Button
    Sleep    4s
    Popups Messages Text Should Contains         Flow ${flow_title} published.
    Go To Project Process In Main Menu           ${flow_title}
    Project Name Should Be As Expected           ${flow_title}
    Sleep    10s

