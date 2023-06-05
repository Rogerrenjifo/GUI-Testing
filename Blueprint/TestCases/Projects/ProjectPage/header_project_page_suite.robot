*** Settings ***
Resource    Blueprint/TestCasesResources/project_page.resource
Library    Blueprint.Steps.Verifications.Projects.ProjectPage.header_project_page_verifications.HeaderProjectPageVerifications
Suite Setup    Search An Specific Project And Open Export Dialog    ${project_name}
Force Tags    HEADER    PROJECT_PAGE

*** Variables ***
${project_name}    AT19-ProjectPage-X2P
${expected_export_dialog_title}    Export to CSV
${expected_label_text}    Filename
${expected_popup_text}    CSV exported.
${new_request_button_color}    rgba(0, 217, 194, 1)
${export_button_text}    Export

*** Test Cases ***

Verify that when clicking the “Export button”, a dialog is displayed.
    Export Dialog Should Be Displayed

Verify that the title of the export dialog matches with “Export to CSV”
    ${dialog_title}    Obtain Export Dialog Title Text In Project Page
    Verify Equal Ignore    ${dialog_title}    ${expected_export_dialog_title}

Verify that the input label of the export dialog matches with “Filename”
    ${input_label}    Obtain Export Dialog Input Label Text In Project Page
    Verify Equal Ignore    ${input_label}    ${expected_label_text}

Verify that the default value of the “Filename” label has the following pattern: “export_project_name_day_month_year”
    ${default_filename}    Obtain Export Dialog Input Value In Project Page
    Export File Name Should Follow The Format    ${default_filename}    ${flow_name}

Verify the export dialog contains a “Cancel” button
    ${button_text}    Obtain Export Dialog Cancel Button Text In Project Page
    Verify Equal Ignore    ${button_text}    ${cancel_button_text}

Verify the export dialog contains an “Export” button
    ${button_text}    Obtain Export Dialog Export Button Text In Project Page
    Verify Equal Ignore    ${button_text}    ${export_button_text}

Verify that when the “Export” button is clicked a popup message is displayed
    Click Export Dialog Button In Project Page
    Popup Message Should Be Displayed

Verify that popup message text matches with “CSV exported.”
    ${popup_text}    Obtain Popup Message Text In Project Page
    Verify Equal Ignore    ${popup_text}    ${expected_popup_text}

Verify that popup message color matches with “rgba(92, 184, 92, 1)”
    ${popup_color}    Obtain Popup Message Color In Project Page
    Verify Equal Ignore    ${popup_color}    ${expected_success_popup_color}

Verify that after click on "Cancel" button export dialog is no more displayed
    Click Export Button In Project Page
    Click Cancel Export Dialog Button In Project Page
    Export Dialog Should Not Be Displayed

Verify that after click on "Close" button export dialog is no more displayed
    Click Export Button In Project Page
    Click Close Export Dialog Button In Project Page
    Export Dialog Should Not Be Displayed

Verify that the project name is visible
    Project Name Should Be Displayed

Verify that when hovering on the “New Request“ button its background color changes to green (#00d9c3)
    Hover New Request Button
    ${button_color}    Obtain New Request Button Color
    Verify Equal Ignore    ${button_color}    ${new_request_button_color}

Verify that clicking on the "New Request" button redirects the user to the new-project endpoint
    Click On New Request Button
    Current Page Should Be New Project
