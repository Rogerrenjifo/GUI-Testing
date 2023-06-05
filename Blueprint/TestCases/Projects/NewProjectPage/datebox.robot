*** Settings ***
Documentation    Atomic tests to verify the functionality of datebox
...              in new project page of Blueprint.
Library    Blueprint.Steps.Actions.MainMenu.main_menu_actions.MainMenuActions
Library    Blueprint.Steps.Actions.Projects.new_project_actions.NewProjectActions
Library    Blueprint.Steps.Verifications.Projects.NewProjectPage.new_project_page_verifications.NewProjectPageVerifications
Resource    Blueprint/TestCasesResources/navigate.resource
Suite Setup    Navigate To Projects
Force Tags     New_Project_Page    Datebox

*** Variables ***
${section_delivering}    Delivering
${label_received_date}    received Date
${label_date_2}    Date 2
${default_date}    June 03, 2023
${year_to_select}    2022
${month_to_select}    November
${day_to_select}    25
${date_to_compare}    November 25, 2022
${select_new_year}    2026
${select_new_month}    July
${select_new_day}    8
${purple_color_rgba}    rgba(117, 105, 255, 1)
${purple_color_rgb}    rgb(117, 105, 255)
${red_color}    rgba(255, 114, 105, 1)

*** Test Cases ***
Verify that hover on the label of a datebox the color change to purple "rgba(117, 105, 255, 1)"
    The Rgb Color Of A Label Should Be As Expected    ${section_delivering}   ${label_received_date}   ${purple_color_rgba}

Verify That clicking into a datebox its border change to purple "rgb(117, 105, 255)"
    Border Of A Component Should Be Highlighted    ${section_delivering}   ${label_received_date}   ${purple_color_rgb}

Verify that if the datebox is a required field and it is empty the Field Required message is displayed in red color
    Remove The Content Of A Component In New Project Page    ${section_delivering}    ${label_received_date}
    Field Required Message Should Be Displayed

Verify that if the datebox is a required field and it is empty error icon is displayed
    Remove The Content Of A Component In New Project Page    ${section_delivering}    ${label_received_date}
    Field Required Icon Should Be Displayed

Verify that if the datebox is a required field and it is empty its label change to red color
    Remove The Content Of A Component In New Project Page    ${section_delivering}    ${label_received_date}
    The Rgb Color Of A Label Should Be As Expected    ${section_delivering}    ${label_received_date}   ${red_color}

Verify if the input of datebox has a default value the default value is displayed
    ${content}    Get The Content Of A Component In New Project Page    ${section_delivering}   ${label_date_2}
    Option Should Be Equal   ${content}    ${default_date} 

Verify that clicking the input of datebox the calendar is displayed
    Click A Component Inside A Section In New Project Page    ${section_delivering}    ${label_received_date}
    The Datepicker In Datebox Should Be Displayed
    Click A Component Inside A Section In New Project Page    ${section_delivering}    ${label_received_date}

Verify that clicking the month in datapicker the month list is displayed 
    Click A Component Inside A Section In New Project Page    ${section_delivering}    ${label_received_date}
    Click To Display Months In Datepicker New Project Page
    Month Or Year In Datapicker Should Be Displayed
    Click A Component Inside A Section In New Project Page    ${section_delivering}    ${label_received_date}

Verify that clicking the year in datapicker the year list is displayed 
    Click A Component Inside A Section In New Project Page    ${section_delivering}    ${label_received_date}
    Click To Display Years In Datepicker New Project Page
    Month Or Year In Datapicker Should Be Displayed
    Click A Component Inside A Section In New Project Page    ${section_delivering}    ${label_received_date}

Verify the user is able to select a month in a datebox
    Click A Component Inside A Section In New Project Page    ${section_delivering}    ${label_received_date}
    Select A Month In Datepicker    ${month_to_select}
    Month Value Should Be The Selected    ${month_to_select}
    Click A Component Inside A Section In New Project Page    ${section_delivering}    ${label_received_date}

Verify the user is able to select a year in a datebox
    Click A Component Inside A Section In New Project Page    ${section_delivering}    ${label_received_date}
    Select A Year In Datepicker    ${year_to_select}
    Year Value Should Be The Selected    ${year_to_select}
    Click A Component Inside A Section In New Project Page    ${section_delivering}    ${label_received_date}

Verify the user is able to set a complete date in a datebox
    Click A Component Inside A Section In New Project Page    ${section_delivering}    ${label_received_date}
    Select A Complete Date In Datepicker    ${year_to_select}    ${month_to_select}    ${day_to_select}
    ${content}    Get The Content Of A Component In New Project Page    ${section_delivering}   ${label_received_date}
    Option Should Be Equal   ${content}    ${date_to_compare}

Verify user is able to change a selected date in a datebox
    Click A Component Inside A Section In New Project Page    ${section_delivering}    ${label_received_date}
    Select A Complete Date In Datepicker    ${select_new_year}    ${select_new_month}    ${select_new_day}
    Click A Component Inside A Section In New Project Page    ${section_delivering}    ${label_received_date}
    Select A Complete Date In Datepicker    ${year_to_select}    ${month_to_select}    ${day_to_select}
    ${content}    Get The Content Of A Component In New Project Page    ${section_delivering}   ${label_received_date}
    Option Should Be Equal   ${content}    ${date_to_compare}

Verify date can be deleted from a datebox
    Click A Component Inside A Section In New Project Page    ${section_delivering}    ${label_received_date}
    Select A Complete Date In Datepicker    ${select_new_year}    ${select_new_month}    ${select_new_day}
    Delete Date In A Datebox    ${section_delivering}   ${label_received_date}
    The Content Of A Component Should Be Empty    ${section_delivering}   ${label_received_date}

Verify when month is less than december and next month button is clicked month is increased but year not
    Click A Component Inside A Section In New Project Page    ${section_delivering}    ${label_Date_2}
    Select A Month In Datepicker    ${select_new_month}
    Select A Year In Datepicker    ${select_new_year}
    Click To Next Month Button
    Month Value Should Be The Selected    August
    Year Value Should Be The Selected    ${select_new_year}
    Click A Component Inside A Section In New Project Page    ${section_delivering}    ${label_Date_2}

Verify when month is december and next month button is clicked month is january and year is increased 
    Click A Component Inside A Section In New Project Page    ${section_delivering}    ${label_Date_2} 
    Select A Month In Datepicker    December
    Select A Year In Datepicker    ${select_new_year}
    Click To Next Month Button
    Month Value Should Be The Selected    January
    Year Value Should Be The Selected    2027
    Click A Component Inside A Section In New Project Page    ${section_delivering}    ${label_Date_2}

Verify when month is more than january and previous month button is clicked month is decreased but year not
    Click A Component Inside A Section In New Project Page    ${section_delivering}    ${label_Date_2}
    Select A Month In Datepicker    ${select_new_month}
    Select A Year In Datepicker    ${select_new_year}
    Click To Previous Month Button
    Month Value Should Be The Selected    June
    Year Value Should Be The Selected    ${select_new_year}
    Click A Component Inside A Section In New Project Page    ${section_delivering}    ${label_Date_2}

Verify when month is january and previous month button is clicked month is december and year is decreased 
    Click A Component Inside A Section In New Project Page    ${section_delivering}    ${label_Date_2} 
    Select A Month In Datepicker    January
    Select A Year In Datepicker    ${select_new_year}
    Click To Previous Month Button
    Month Value Should Be The Selected    December
    Year Value Should Be The Selected    2025
    Click A Component Inside A Section In New Project Page    ${section_delivering}    ${label_Date_2} 
