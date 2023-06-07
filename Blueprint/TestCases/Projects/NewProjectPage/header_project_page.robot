*** Settings ***
Documentation    Atomic tests to verify the functionality of the create 
...              button in new project page of Blueprint.
Library    Blueprint.Steps.Actions.Projects.new_project_actions.NewProjectActions
Library    Blueprint.Steps.Verifications.Projects.NewProjectPage.new_project_page_verifications.NewProjectPageVerifications
Resource    Blueprint/TestCasesResources/Projects/projects.resource

Suite Setup    Search An Specific Project And Click On New Request Button
Force Tags     PROJECT

*** Variables ***
${create_button_color}    rgba(0, 217, 194, 1)
${template_title}    AT-19 Test-fc
${section_name}    New history
${label_name}    New Child
${new_value}    Maria Eugenia
${new_section}    Delivering
${new_component}    Multiline Box 1
${new_component_2}    received Date
${year}    2024
${month}    June
${day}    5

*** Test Cases ***
Verify the title of a flow template in project page be the same as created in flow page
    The Title Of A Flow Template Should Be As Expected    ${template_title}   

Verify the create button background color changes when the user hove over the button
    Create Button Rgb Color Should Be As Expected    ${create_button_color}

Verify it is not posible to create a project flow if there is a required field empty
    [Tags]    BG-240
    Remove The Content Of A Component In New Project Page    ${section_name}    ${label_name}
    Create Button Status Should Be Disabled

Verify the text of Create button
    Create Button Text Should Be As Expected    Create

Verify the create button goes to the next page
    Insert Text Or Number In A Component In New Project Page    ${section_name}    ${label_name}    ${new_value}
    Click Create Button In New Project Page
    Popup Message Should Be Displayed
    Select User From The Dropdown In New Project Page    ${new_section}    ${new_component}    1
    Click A Component Inside A Section In New Project Page    ${new_section}    ${new_component_2}
    Select A Complete Date In Datepicker    ${year}    ${month}    ${day}
    Return to previous page
