TITLE = "(//ng-select[@bindlabel='name'])[<<number>>]//preceding-sibling::label"
INPUT_TEXT_BOX = "(//ng-select[@bindlabel='name']//input)[<<number>>]"
TEXT_BOX = "(//ng-select[@bindlabel='name'])[<<number>>]"
DELETE_ALL_USERS = "(//ng-select[@ bindlabel='name'])[<<number>>]/descendant::span[@title]"
SELECT_USER = "//span[@title='<<user>>'] | //label[@title='<<user>>']"
EMPTY_MESSAGE = "(//ng-select[@bindlabel='name'])[<<number>>]/following-sibling::span"
DELETE_ONE_USER = "(//div[contains(@class, 'ng-has')])[<<number>>]//span[text()='<<user>>']/preceding-sibling::span"
