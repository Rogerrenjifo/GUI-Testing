*** Settings ***
Documentation    Tests to verify the functionality of each component
...              of the project tracing forms GUI.
Resource         ../../../TestCasesResources/Projects/ProjectTracing/project_tracing_forms_resources.robot
Suite Setup      Open project tracing forms webpage
Suite Teardown   Close browser

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
    Click cancel button

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
    Click cancel button

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
