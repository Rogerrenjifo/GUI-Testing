EDIT_COMMENT_BUTTON = "//preceding::button[2]"
DELETE_COMMENT_BUTTON = "//preceding::button[1]"
COMMENT_DATE = "//preceding::span[contains(@class, 'time-elapsed')][1]"
COMMENT_CONTENT = {
    "by_index":  "//div[@class='comment-content']",
    "by_content": "//div[normalize-space()='<<value>>']"
}
COMMENT_OWNER_NAME = "//preceding::span[@class='header-text'][1]"
COMMENT_OWNER_INITIALS = "//preceding::div[@class='initials normal'][1]"
COMMENT_EDITED_TAG = "//preceding::div[normalize-space()='(Edited)'][1]"
EDIT_COMMENT_TEXT_AREA = "//textarea[@formcontrolname='updateData']"
CANCEL_COMMENT_BUTTON = "//button[@class='bp-btn-action' and normalize-space()='Cancel']"
UPDATE_COMMENT_BUTTON = "//button[contains(@class,'bp-btn-action') and normalize-space()='Update']"
