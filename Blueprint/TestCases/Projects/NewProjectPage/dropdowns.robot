*** Settings ***
Library    Blueprint.Steps.Actions.MainMenu.main_menu_actions.MainMenuActions
Library    Blueprint.Steps.Actions.Projects.new_project_actions.NewProjectActions
Library    Blueprint.Steps.Verifications.Projects.NewProjectPage.new_project_page_verifications.NewProjectPageVerifications
Resource    Blueprint/TestCasesResources/navigate.resource
Suite Setup    Navigate To Projects
Suite Teardown    Close Browser
Force Tags     new_project_page    dropdowns 

*** Variables ***
${default_value}    Maria Mamani
${value}    Roger Renjifo
${value2}    Carolina Vacaflor
${section_new_history}    New history
${label_responsible}    responsible
${section_delivering}    Delivering
${label_Multiline Box 1 }    Multiline Box 1 
${purple_color}    rgba(117, 105, 255, 1)
${red_color}    rgba(255, 114, 105, 1)

*** Test Cases ***
Verify that dropdownbox has the default value
    ${content}    get_the_content_of_a_dropdown    ${section_new_history}   ${label_responsible}
    Option Should Be Equal   ${content}    ${default_value} 

Verify that hover on the label of a dropdown the color change to purple
    the_rgb_color_of_a_label_should_be_as_expected    ${section_new_history}   ${label_responsible}   ${purple_color}

verify that it is possible to select one of the available options
    select_user_from_the_dropdown_in_new_project_page    ${section_new_history}    ${label_responsible}    ${value}
    ${content}    get_the_content_of_a_dropdown    ${section_new_history}   ${label_responsible}
    Option Should Be Equal   ${content}    ${value}

Verify that it is not possible to select two options
    select_user_from_the_dropdown_in_new_project_page    ${section_new_history}    ${label_responsible}    ${value2}
    select_user_from_the_dropdown_in_new_project_page    ${section_new_history}    ${label_responsible}    ${value}
    ${content}    get_the_content_of_a_dropdown    ${section_new_history}   ${label_responsible}
    Option Should Be Equal   ${content}    ${value}

Verify when the box is clicked the list with the option is displayed 
    click_in_the_drodown    ${section_new_history}    ${label_responsible}
    the_options_list_in_dropdown_should_be_displayed

Verify that if the dropdown is a required field and it is empty the Field Required message is displayed in red color
    remove_the_content_of_a_component_in_new_project_page    ${section_delivering}    ${label_Multiline Box 1 }
    field_required_message_should_be_displayed

Verify that if the dropdown is a required field and it is empty error icon is displayed
    remove_the_content_of_a_component_in_new_project_page    ${section_delivering}    ${label_Multiline Box 1 }
    field_required_icon_should_be_displayed

Verify that if the dropdown is a required field and it is empty its label change to red color
    remove_the_content_of_a_component_in_new_project_page    ${section_delivering}    ${label_Multiline Box 1 }
    the_rgb_color_of_a_label_should_be_as_expected    ${section_delivering}    ${label_Multiline Box 1 }   ${red_color}
