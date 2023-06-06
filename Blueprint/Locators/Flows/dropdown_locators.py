permissions = {"TITLE": "(//ng-select[@bindlabel='name'])[<<number>>]//preceding-sibling::label",
               "INPUT_TEXT_BOX": "(//ng-select[@bindlabel='name']//input)[<<number>>]",
               "TEXT_BOX": "(//ng-select[@bindlabel='name'])[<<number>>]/child::div",
               "DELETE_ALL_USERS": "(//ng-select[@ bindlabel='name'])[<<number>>]/descendant::span[@title]",
               "SELECT_USER": "//span[@title='<<user>>'] | //label[@title='<<user>>']",
               "EMPTY_MESSAGE": "(//ng-select[@bindlabel='name'])[<<number>>]/following-sibling::span",
               "DROPDOWN_ARROW": "(//span[@class='ng-arrow-wrapper'])[<<number>>]",
               "DELETE_ONE_USER": "(//div[contains(@class, 'ng-has')])[<<number>>]//span[text()='<<user>>']/ \
               preceding-sibling::span",
               "CONTENT_TEXT_BOX": "(//div[@class='ng-value-container'])[<<number>>]",
               "MESSAGE_IN_TEXT_BOX": "(//div[@class='ng-value-container'])[<<number>>]/child::div",
               "USER_SELECTED": "(//div[@class='ng-value-container'])[<<number>>]/ \
                descendant::span[contains(@class, 'ng-value-label')]",
               "DROPDOWN_LIST": "//div[contains(@class, 'ng-dropdown')]"
               }

projects_tracing_system = {"OPTION": "//span[normalize-space()='<<option>>']",
                           "ARROW_LOCATOR": "//span[@class='ng-arrow-wrapper']",
                           "CLEAR_ALL": "//span[@class='ng-clear-wrapper']",
                           "DROPDOWN_LIST": "//div[contains(@class, 'ng-dropdown')]"
                           }

projects_new_project = {"SELECT_USER": "//span[@title='<<user>>'] | //label[@title='<<user>>'] | //div[@title='<<user>>']",
                        "REMOVE_USER_LOCATOR": "//h3[@title='<<section_name>>']//following-sibling::div//descendant:: \
                        label[@title='<<label_name>>']//following-sibling::div//descendant::span[@title='Clear all']",
                        "TEXT_USER_NUMBER_DATE_BOX": "//h3[@title='<<section_name>>']//following-sibling:: \
                        div//descendant::label[@title='<<label_name>>']//following-sibling::div//child::input"
                        }
