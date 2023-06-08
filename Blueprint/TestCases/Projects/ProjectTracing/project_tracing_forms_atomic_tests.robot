*** Settings ***
Documentation    Tests to verify the functionality of each component
...              of the project tracing forms GUI.
Resource         Blueprint/TestCasesResources/Projects/ProjectTracing/project_tracing_forms_resources.robot
Suite Setup      Open project tracing forms webpage
Test Teardown    Click section title in project forms    Section 1
Force Tags        PROJECT
*** Test Cases ***
Verify edit button is visible when mouse is hover text field
    Put mouse hover field with title    Title    Section 1
    Edit Button Of Field Should Be Visible    Title    Section 1

Verify edit button is visible when mouse is hover dropdown field
    Put mouse hover field with title    Dropdown Box 1    Section 1
    Edit button of field should be visible    Dropdown Box 1    Section 1

Verify edit button is visible when mouse is hover numeric field
    Put mouse hover field with title    Numeric Box 1    Section 1
    Edit button of field should be visible    Numeric Box 1    Section 1

Verify edit button is visible when mouse is hover checkbox field
    Put mouse hover field with title    CheckBox 1    Section 1
    Edit button of field should be visible    CheckBox 1    Section 1

Verify edit button is visible when mouse is hover date field
    Put mouse hover field with title    Date 1    Section 1
    Edit button of field should be visible    Date 1    Section 1

Verify edit button is visible when mouse is hover multiline field
    Put mouse hover field with title    Multiline Box 1    Section 1
    Edit button of field should be visible    Multiline Box 1    Section 1

Verify edit button is visible when mouse is hover userlist field
    Put mouse hover field with title    User List 1    Section 1
    Edit button of field should be visible    User List 1    Section 1

Verify save button is visible when edit button is clicked on text field
    Put mouse hover field with title    Title    Section 1
    Click edit button of field    Title    Section 1
    Save button should be visible

Verify save button is visible when edit button is clicked on dropdown field
    Put mouse hover field with title    Dropdown Box 1    Section 1
    Click edit button of field    Dropdown Box 1    Section 1
    Save button should be visible

Verify save button is visible when edit button is clicked on numeric field
    Put mouse hover field with title    Numeric Box 1    Section 1
    Click edit button of field    Numeric Box 1    Section 1
    Save button should be visible

Verify save button is visible when edit button is clicked on checkbox field
    Put mouse hover field with title    CheckBox 1    Section 1
    Click edit button of field    CheckBox 1    Section 1
    Save button should be visible

Verify save button is visible when edit button is clicked on date field
    Put mouse hover field with title    Date 1    Section 1
    Click edit button of field    Date 1    Section 1
    Save button should be visible

Verify save button is visible when edit button is clicked on multiline field
    Put mouse hover field with title    Multiline Box 1    Section 1
    Click edit button of field    Multiline Box 1    Section 1
    Save button should be visible
    Click cancel changes in project forms

Verify save button is visible when edit button is clicked on userlist field
    Put mouse hover field with title    User List 1    Section 1
    Click edit button of field    User List 1    Section 1
    Save button should be visible

Verify cancel button is visible when edit button is clicked on text field
    Put mouse hover field with title    Title    Section 1
    Click edit button of field    Title    Section 1
    Cancel button should be visible

Verify cancel button is visible when edit button is clicked on dropdown field
    Put mouse hover field with title    Dropdown Box 1    Section 1
    Click edit button of field    Dropdown Box 1    Section 1
    Cancel button should be visible

Verify cancel button is visible when edit button is clicked on numeric field
    Put mouse hover field with title    Numeric Box 1    Section 1
    Click edit button of field    Numeric Box 1    Section 1
    Cancel button should be visible

Verify cancel button is visible when edit button is clicked on checkbox field
    Put mouse hover field with title    CheckBox 1    Section 1
    Click edit button of field    CheckBox 1    Section 1
    Cancel button should be visible

Verify cancel button is visible when edit button is clicked on date field
    Put mouse hover field with title    Date 1    Section 1
    Click edit button of field    Date 1    Section 1
    Cancel button should be visible

Verify cancel button is visible when edit button is clicked on multiline field
    Put mouse hover field with title    Multiline Box 1    Section 1
    Click edit button of field    Multiline Box 1    Section 1
    Cancel button should be visible
    Click cancel changes in project forms

Verify cancel button is visible when edit button is clicked on userlist field
    Put mouse hover field with title    User List 1    Section 1
    Click edit button of field    User List 1    Section 1
    Cancel button should be visible

Verify text field changes color when moused is hovered
    Click section title    Section 1
    Field border should be color    Title    Section 1    rgba(0, 0, 0, 0)
    Put mouse hover field with title    Title    Section 1
    Field border should be color    Title    Section 1    rgba(117, 105, 255, 1)

Verify dropdown field changes color when moused is hovered
    Click section title    Section 1
    Field border should be color    Dropdown Box 1    Section 1    rgba(0, 0, 0, 0)
    Put mouse hover field with title    Dropdown Box 1    Section 1
    Field border should be color    Dropdown Box 1    Section 1    rgba(117, 105, 255, 1)

Verify numeric field changes color when moused is hovered
    Click section title    Section 1
    Field border should be color    Numeric Box 1    Section 1    rgba(0, 0, 0, 0)
    Put mouse hover field with title    Numeric Box 1    Section 1
    Field border should be color    Numeric Box 1    Section 1    rgba(117, 105, 255, 1)

Verify checkbox field changes color when moused is hovered
    Click section title    Section 1
    Field border should be color    CheckBox 1    Section 1    rgba(0, 0, 0, 0)
    Put mouse hover field with title    CheckBox 1    Section 1
    Field border should be color    CheckBox 1    Section 1    rgba(117, 105, 255, 1)

Verify date field changes color when moused is hovered
    Click section title    Section 1
    Field border should be color    Date 1    Section 1    rgba(0, 0, 0, 0)
    Put mouse hover field with title    Date 1    Section 1
    Field border should be color    Date 1    Section 1    rgba(117, 105, 255, 1)

Verify multiline field changes color when moused is hovered
    Click section title    Section 1
    Field border should be color    Multiline Box 1    Section 1    rgba(0, 0, 0, 0)
    Put mouse hover field with title    Multiline Box 1    Section 1
    Field border should be color    Multiline Box 1    Section 1    rgba(117, 105, 255, 1)

Verify user list field changes color when moused is hovered
    Click section title    Section 1
    Field border should be color    User List 1    Section 1    rgba(0, 0, 0, 0)
    Put mouse hover field with title    User List 1    Section 1
    Field border should be color    User List 1    Section 1    rgba(117, 105, 255, 1)

Verify text box is red when required field is empty
    Set empty text in field    Title    Section 1
    Editable text input border should be color    rgba(255, 114, 105, 1)

Verify "Field required" warning message appears when required field is empty
    Set empty text in field    Title    Section 1
    Required field div should be visible

Verify "Field required" warning message is red
    Set empty text in field    Title    Section 1
    Required field div should be color    rgba(255, 114, 105, 1)

Verify save button turns red when a required field is empty
    Set empty text in field    Title    Section 1
    Save button should be color    rgb(255, 114, 105)

Verify save button is disabled when a required field is empty
    Set empty text in field    Title    Section 1
    Save button should be disabled

Verify cancel button is enabled when a required field is empty
    Set empty text in field    Title    Section 1
    Cancel button should be enabled

Verify text fields can have alphanumeric characters
    Set text input in project forms    Title    Section 1    qwertyuiopasdfghjklzxcvbnm123456789
    Editable text input should be    qwertyuiopasdfghjklzxcvbnm123456789
    Click cancel changes in project forms

Verify text fields can have special characters
    Set text input in project forms    Title    Section 1    ñ^*!¨!$%&/|@#~€¬
    Editable text input should be    ñ^*!¨!$%&/|@#~€¬

Verify dropdown field options are displayed when field is clicked while being edited
    Select field to edit in project forms    Dropdown Box 1    Section 1
    Click input field in project forms    Dropdown Box 1    Section 1
    Dropdown box 1 options should be visible

Verify that writing on cleared dropdown input field filters options correctly
    Set text input in project forms    Dropdown Box 1    Section 1    x
    Dropdown box 1 x options should be visible

Verify that typing not matching information displays "No items found" label
    Set text input in project forms    Dropdown Box 1    Section 1    z
    Dropdown no items found label should be visible

Verify that typing not matching information disables save button
    [Tags]    BG-245    BUG
    Set text input in project forms    Dropdown Box 1    Section 1    z
    Save button should be disabled

Verify that only letter 'e' is allowed on a numeric field
    [Tags]    BG-254    BUG
    Set numeric input in project forms    Numeric Box 1    Section 1    abcdefghijklmnopqrstuvwxyz
    Editable numeric input should be    e

Verify that only '+' and '-' special character are allowed on a numeric field
    [Tags]    BG-254    BUG
    Set numeric input in project forms    Numeric Box 1    Section 1    +-ñ^*!¨!$%&/|@#~€¬
    Editable numeric input should be    +-

Verify that 'up' arrow adds 1 unit to the value on a numeric field
    Set numeric input in project forms    Numeric Box 1    Section 1    2
    Press up arrow on numeric field in project forms
    Editable numeric input should be    3

Verify that 'down' arrow adds 1 unit to the value on a numeric field
    Set numeric input in project forms    Numeric Box 1    Section 1    2
    Press down arrow on numeric field in project forms
    Editable numeric input should be    1

Verify that checkbox value changes when is clicked
    Click checkbox label in project forms    CheckBox 1    Section 1
    Checkbox value should be    CheckBox 1    Section 1    true

Verify multiline fields can have special characters
    Set multiline text input in project forms    Multiline Box 1    Section 1    ñ^*!¨!$%&/|@#~€¬
    Multiline value should be    Multiline Box 1    Section 1    ñ^*!¨!$%&/|@#~€¬
    
Verify multiline fields can have alphanumeric characters
    Set multiline text input in project forms    Multiline Box 1    Section 1    abcdefghijklmnopqrstuvwxyz0123456789
    Multiline value should be    Multiline Box 1    Section 1    abcdefghijklmnopqrstuvwxyz0123456789  

Verify multiline fields saves end of lines
    Set multiline text input in project forms    Multiline Box 1    Section 1    xdasda\nadsad\nAKLDA\nfgfd
    Multiline value should be    Multiline Box 1    Section 1    xdasda\nadsad\nAKLDA\nfgfd

Verify 'Please select user from user list' message is displayed when the user list options are cleared
    Select field to edit in project forms    User List 1    Section 1
    Click clear all dropdown button in project forms
    Please select user should be visible
