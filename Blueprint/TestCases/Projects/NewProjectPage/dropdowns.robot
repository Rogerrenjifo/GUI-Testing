*** Settings ***
Documentation    Atomic tests to verify the functionality of dropdowns
...              in new project page of Blueprint.
Library    Blueprint.Steps.Actions.MainMenu.main_menu_actions.MainMenuActions
Library    Blueprint.Steps.Actions.Projects.new_project_actions.NewProjectActions
Library    Blueprint.Steps.Verifications.Projects.NewProjectPage.new_project_page_verifications.NewProjectPageVerifications
Resource    Blueprint/TestCasesResources/Projects/NewProjectPage/new_project.resource
Suite Setup    Search An Specific Project And Click On New Request Button
Force Tags     New_Project_Page    Dropdowns 

*** Variables ***
${user_to_select}    Roger Renjifo
${user_by_default}    Carolina Vacaflor
${section_new_history}    New history
${label_responsible}    responsible
${section_delivering}    Delivering
${label_Multiline Box 1 }    Multiline Box 1 
${purple_color}    rgba(117, 105, 255, 1)
${red_color}    rgba(255, 114, 105, 1)

*** Test Cases ***
Verify that dropdownbox has the default value
    ${content}    Get The Content Of A Dropdown    ${section_new_history}   ${label_responsible}
    Option Should Be Equal   ${content}    ${user_by_default} 

Verify that hover on the label of a dropdown the color change to purple
    The Rgb Color Of A Label Should Be As Expected    ${section_new_history}   ${label_responsible}   ${purple_color}

verify that it is possible to select one of the available options
    Select User From The Dropdown In New Project Page    ${section_new_history}    ${label_responsible}    ${user_to_select}
    ${content}    Get The Content Of A Dropdown    ${section_new_history}   ${label_responsible}
    Option Should Be Equal   ${content}    ${user_to_select}

Verify that it is not possible to select two options
    Select User From The Dropdown In New Project Page    ${section_new_history}    ${label_responsible}    ${user_by_default}
    Select User From The Dropdown In New Project Page    ${section_new_history}    ${label_responsible}    ${user_to_select}
    ${content}    Get The Content Of A Dropdown    ${section_new_history}   ${label_responsible}
    Option Should Be Equal   ${content}    ${user_to_select}

Verify when the box is clicked the list with the option is displayed 
    Click In The Dropdown    ${section_new_history}    ${label_responsible}
    The Options List In Dropdown Should Be Displayed

Verify that if the dropdown is a required field and it is empty the Field Required message is displayed in red color
    Remove The Content Of A Component In New Project Page    ${section_delivering}    ${label_Multiline Box 1 }
    Field Required Message Should Be Displayed

Verify that if the dropdown is a required field and it is empty error icon is displayed
    Remove The Content Of A Component In New Project Page    ${section_delivering}    ${label_Multiline Box 1 }
    Field Required Icon Should Be Displayed

Verify that if the dropdown is a required field and it is empty its label change to red color
    Remove The Content Of A Component In New Project Page    ${section_delivering}    ${label_Multiline Box 1 }
    The Rgb Color Of A Label Should Be As Expected    ${section_delivering}    ${label_Multiline Box 1 }   ${red_color}
