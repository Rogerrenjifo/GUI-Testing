*** Settings ***
Documentation    Atomic tests to verify the functionality of a text box and 
...              a numberic box in new project page of Blueprint.
Library    Blueprint.Steps.Actions.Projects.new_project_actions.NewProjectActions
Library    Blueprint.Steps.Verifications.Projects.NewProjectPage.new_project_page_verifications.NewProjectPageVerifications
Resource    Blueprint/TestCasesResources/Projects/NewProjectPage/new_project.resource

Suite Setup    Search An Specific Project And Click On New Request Button
Force Tags     COMPONENT_PROJECTS    PROJECT

*** Variables ***
${section_name}    New history
${label_new_child}    New Child
${label_title_number}    Grade
${text_number}    MariaE2345
${chars}    !"#$%&/?¡¡*¨_:;
${numbers}    5678098
${chars_text}    !"#$%&/?¡¡*¨_:;newtext
${highlighted_label_color}    rgba(117, 105, 255, 1)
${highlighted_border_color}    rgb(117, 105, 255)
${label_grade}    Grade
${label_email}    email
${label_lastname}    lastname
${label_age}    age
${new_email}    newemailcreated
${increased_number}    4
${decreased_number}    1
${final_number}    3
${number_updated}    4567

*** Test Cases ***
Verify the user is able to select the text box
    Click A Component Inside A Section In New Project Page    ${section_name}    ${label_grade}
    Border Of A Component Should Be Highlighted    ${section_name}    ${label_email}    ${highlighted_border_color}

Verify the user is able to type text or number in a text box
    Insert Text Or Number In A Component In New Project Page    ${section_name}    ${label_lastname}    ${text_number}
    The Text Or Number Should Be As Expected    ${section_name}    ${label_lastname}    ${text_number}

Verify the user is able to type special characters in a text box
    Insert Text Or Number In A Component In New Project Page    ${section_name}    ${label_email}    ${chars_text}
    The Text Or Number Should Be As Expected    ${section_name}    ${label_email}    ${chars_text}

Verify it is posible to remove the text in a text box
    Remove The Content Of A Component In New Project Page    ${section_name}    ${label_lastname}
    The Content Of A Component Should Be Empty    ${section_name}    ${label_lastname}

Verify the text can be updated in a text box
    Remove The Content Of A Component In New Project Page    ${section_name}    ${label_email}
    Insert Text Or Number In A Component In New Project Page    ${section_name}    ${label_email}    ${new_email}
    The Text Or Number Should Be As Expected    ${section_name}    ${label_email}    ${new_email}

Verify the user is able to type numbers in a numberic box
    Insert Text Or Number In A Component In New Project Page    ${section_name}    ${label_grade}    ${numbers}
    The Text Or Number Should Be As Expected    ${section_name}    ${label_grade}    ${numbers}

Verify it is posible to remove the value in a numberic box
    Remove The Content Of A Component In New Project Page    ${section_name}    ${label_grade}
    The Content Of A Component Should Be Empty    ${section_name}    ${label_grade}

Verify the user is not able to type letters or special characters in a numberic box
    Insert Text Or Number In A Component In New Project Page    ${section_name}    ${label_grade}    ${chars_text}
    The Content Of A Component Should Be Empty    ${section_name}    ${label_grade}    

Verify the spin button increase a numberic value in a numberic box
    Increase Numbericbox Value In New Project Page    ${section_name}    ${label_grade}   ${increased_number}
    The Numberic Box Value Should Change    ${section_name}    ${label_grade}   ${increased_number}

Verify the spin button decrease a numberic value in a numberic box
    Decrease Numbericbox Value In New Project Page    ${section_name}    ${label_grade}   ${decreased_number}
    The Numberic Box Value Should Change    ${section_name}    ${label_grade}    ${final_number}   

Verify the number can be updated in a numberic box
    Remove The Content Of A Component In New Project Page    ${section_name}    ${label_age}
    Insert Text Or Number In A Component In New Project Page    ${section_name}    ${label_age}    ${number_updated}    
    The Text Or Number Should Be As Expected    ${section_name}    ${label_age}    ${number_updated}

Verify the label of a component changes color when the mouse is over
    The Rgb Color Of A Label Should Be As Expected     ${section_name}    ${label_lastname}    ${highlighted_label_color}
    Border Of A Component Should Be Highlighted    ${section_name}    ${label_email}     ${highlighted_border_color}

Verify that an error message is displayed when the required field is empty
    Remove The Content Of A Component In New Project Page    ${section_name}    ${label_new_child}
    Field Required Message Should Be Displayed
    Field Required Icon Should Be Displayed
