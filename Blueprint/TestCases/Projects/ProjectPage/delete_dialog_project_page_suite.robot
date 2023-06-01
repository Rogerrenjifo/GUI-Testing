*** Settings ***
Resource    Blueprint/TestCasesResources/project_page.resource
Library    Blueprint.Steps.Verifications.Projects.ProjectPage.delete_dialog_project_page_verifications.DeleteDialogProjectPageVerifications
Force Tags    DELETE_INSTANCE   PROJECT_PAGE
Suite Setup    Create ${4} Instances And Open Delete Dialog
Suite Teardown    Delete Created Instances

*** Variables ***
${delete_dialog_title}    Delete Process Instance
${delete_dialog_question}    Do you want to delete this process instance?
${delete_button_text}    Delete
${popup_message_text}    Process instance deleted

*** Test Cases ***
Verify that delete dialog title matches “Delete Process Insatance”
    Delete Dialog Title Should Be    ${delete_dialog_title}

Verify that delete dialog paragraph matches “Do you want to delete this process instance?”
    ${dialog_question}    Obtain Question In Delete In Project Instance
    Verify Equal Ignore    ${dialog_question}    ${delete_dialog_question}

Verify the delete dialog contains a “Cancel” button
    ${button_text}    Obtain Dialog Cancel Button Text In Project Instance
    Verify Equal Ignore    ${button_text}    ${cancel_button_text}

Verify the delete dialog contains a “Delete” button
    ${button_text}    Obtain Dialog Delete Button Text In Project Instance
    Verify Equal Ignore    ${button_text}    ${delete_button_text}

Verify that when click in close button of delete dialog, the project instance still exists in the list
    Click Dialog Close Button In A Project Instance
    Project Instance Should Still Exist    ${project_id}

Verify that when click in close button of delete dialog, the delete dialog is not displayed
    Close Delete Project Instance Process In Project Page    ${project_id}
    Delete Dialog Should Not Be Displayed

Verify that when canceling the deletion of a project instance it still exists in the list
    Cancel Delete Project Instance Process In Project Page    ${project_id}
    Project Instance Should Still Exist    ${project_id}

Verify that when click in cancel button of delete dialog, the delete dialog is not displayed
    Cancel Delete Project Instance Process In Project Page    ${project_id}
    Delete Dialog Should Not Be Displayed

Verify that when a project instance is deleted a pop up message is displayed
    Delete Project Instance Process In Project Page    ${project_id}
    Popup Message Should Be Displayed

verify that the delete pop up message color is green
    ${popup_color}    Obtain Popup Message Color In Project Page
    Verify Equal Ignore    ${popup_color}    ${expected_success_popup_color}

Verify the text of the pop up message matches “Process instance deleted”
    ${popup_text}    Obtain Popup Message Text In Project Page
    Verify Equal Ignore    ${popup_text}    ${popup_message_text}

Verify that when deleting a project instance, it is no longer found on any of the pages
    ${ids}     Get All Projects Ids Text In Project Page
    ${project_id}   Obtain Random Id    ${ids}
    Delete Project Instance Process In Project Page    ${project_id}
    Project Instance Should Not Exist    ${project_id}
