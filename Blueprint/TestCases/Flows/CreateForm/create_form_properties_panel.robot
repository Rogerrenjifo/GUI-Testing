*** Settings ***
Resource     Blueprint/TestCasesResources/Flow/CreateForm/common_imports.resource
Library      Blueprint.Steps.Verifications.Flow.CreateForm.create_form_properties_panel_verifications.CreateFormPropertiesPanelVerifications
Library      Blueprint.Steps.Verifications.Flow.CreateForm.create_form_elements_verification.CreateFormElementsVerifications
Library      Blueprint.Steps.Verifications.Flow.CreateForm.create_form_add_component_verification.CreateFormAddComponentVerifications

Suite Setup       Create A New Flow With Random Code
Suite Teardown    Delete Flow Process In Flow Header
Force Tags        FLOWS    CREATE_F0RM    PROPERTIES_PANEL   COMPONENT

*** Variables ***
${Placeholder}       This is the placeholder
${Default_Value}     This is the default value
@{dropdown}      Yes, I am      No, I am not

*** Test Cases ***
Verify that the textbox fields are enabled
    Add Component To Column Section In Create Form    textbox    section-1-columnB
    Textbox Should Has Its Appropriate Fields         Textbox1    ${Placeholder}   ${Default_Value}

Verify that the numericbox fields are enabled
    Add Component Down Existent Component In Create Form    numericbox    section-1_textbox-1
    Numeric Box Should Has Its Appropriate Fields     Numericbox1   ${Placeholder}  general   ${Default_Value}

Verify that Default Value Formatted Should Be The According To Format In Numeric Box
    [Template]    Default Value Formatted Should Be The According To Format In Numeric Box
    General             2.345       2.345
    Percent             0.345       34.50%
    Only Positives      2.345       +2.345
    Only Negatives      2.345       -2.345
    Comma               2124.55     2,124.55
    Dollar              2124.55     $2,124.55

Verify that the multilinebox fields are enabled
    Add Component Down Existent Component In Create Form    multilinebox  section-1_textbox-2
    Multiline Box Should Has Its Appropriate Fields   Multilinebox1   ${Placeholder}

Verify that the dropdown fields are enabled
    Add Component Down Existent Component In Create Form     dropdown  section-1_numericbox-1
    Dropdown Box Should Has Its Appropriate Fields    Dropdwon1    ${Placeholder}   ${dropdown[1]}    section-1_dropdown-1   ${dropdown}

Verify that the date fields are enabled
    Add Component Down Existent Component In Create Form     date    section-1_multilinebox-1
    Date Should Has Its Appropriate Fields            Date1    2023   June   9    MMMM DD, YYYY

Verify that the userlist fields are enabled
    Add Component Down Existent Component In Create Form     userlist    section-1_dropdown-1
    User List Should Has Its Appropriate Fields              Userlist1    ${Placeholder}   Martin Alvarez  section-1_userlist-1   Martin Alvarez

Verify that the Section field is enabled
    Add New Section In Create Form
    Select Section In Form Main Panel    Section 2
    Section Should Has Its Appropriate Field    This is a new Section
