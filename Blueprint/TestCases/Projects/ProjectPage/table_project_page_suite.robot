*** Settings ***
Documentation    This suite verifies the functionalities of the components in the table on project page
Resource    Blueprint/TestCasesResources/project_page.resource
Library    Blueprint.Steps.Verifications.Projects.ProjectPage.table_project_page_verifications.TableProjectPageVerifications
Suite Setup    Search Project and Create Instances    ${3}    ${project_name}
Suite Teardown    Delete Created Instances
Force Tags    INSTANCES_TABLE    PROJECT_PAGE

*** Variables ***
${project_name}    AT19-ProjectPage-9D6

*** Test Cases ***
Verify all projects have an Id
    ${projects_ids}    Get All Projects Ids Text In Project Page
    All Projects Should Have Id    ${projects_ids}

Verify that all instance ids are different
    ${projects_ids}    Get All Projects Ids Text In Project Page
    Verify All Elements Are Different    ${projects_ids}

Verify that all ids contains the codebase of the project
    ${projects_ids}    Get All Projects Ids Text In Project Page
    All Ids Should Have Same Base Code    ${projects_ids}

Verify all projects have a title
    ${projects_ids}    Get All Projects Ids Text In Project Page
    All Projects Should Have Title    ${projects_ids}

Verify all projects have a current step
    ${projects_ids}    Get All Projects Ids Text In Project Page
    All Projects Should Have Current Step    ${projects_ids}

Verify all projects have an owner
    ${projects_ids}    Get All Projects Ids Text In Project Page
    All Projects Should Have Owner    ${projects_ids}

Verify all projects have a creator
    ${projects_ids}    Get All Projects Ids Text In Project Page
    All Projects Should Have Creator    ${projects_ids}

Verify all projects have a "Date Created"
    ${projects_ids}    Get All Projects Ids Text In Project Page
    All Projects Should Have Date Created    ${projects_ids}

Verify the checkbox has an unchecked value by default
    ${projects_ids}    Get All Projects Ids Text In Project Page
    ${project_id}   Obtain Random Id    ${projects_ids}
    Checkbox Should Not Be Checked    ${project_id}

Verify the checkbox has a checked value when clicked
    ${projects_ids}    Get All Projects Ids Text In Project Page
    Click On Checkbox In A Project Instance    ${projects_ids}[0]
    Checkbox Should Be Checked    ${projects_ids}[0]

Verify the checkbox that has a checked value changes to unchecked when is clicked
    ${projects_ids}    Get All Projects Ids Text In Project Page
    Click On Checkbox In A Project Instance    ${projects_ids}[0]
    Checkbox Should Not Be Checked    ${projects_ids}[0]

Verify that when clicking on the actions button of a project the delete menu is visible
    [Teardown]    Click Action Button In Project Instance    ${project_id}
    ${projects_ids}    Get All Projects Ids Text In Project Page
    ${project_id}   Obtain Random Id    ${projects_ids}
    Click Action Button In Project Instance    ${project_id}
    Actions Menu Should Be Displayed    ${project_id}

Verify that when clicking on the delete button from actions, delete dialog is visible
    [Teardown]    Click Dialog Close Button In A Project Instance
    ${projects_ids}    Get All Projects Ids Text In Project Page
    ${project_id}   Obtain Random Id    ${projects_ids}
    Click Action Button In Project Instance    ${project_id}
    Click Action Delete Button Project Instance    ${project_id}
    Delete Dialog Should Be Displayed

Verify that when clicking on a project instance the site redirects to the project trace page of that instance
    [Teardown]    Go To Project Process In Main Menu    ${flow_name}
    ${projects_ids}    Get All Projects Ids Text In Project Page
    ${project_id}   Obtain Random Id    ${projects_ids}
    Click On Row In A Project Instance    ${project_id}
    Current Url Should Be Project Tracing Page    ${flow_name}    ${project_id}
