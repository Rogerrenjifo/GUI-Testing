CONTAINER = "//app-properties//div[contains(@class'properties-container')]"
HEADER_TITLE = "//app-properties//h2"
BODY_PROPERTIES = "//div[@class='overflow-sidenav']"
BODY_UPPPER = "//app-properties//div[@class='mt-4']"
BODY_LOWER = "//app-properties//div[@class='mt-7']"
OWNER = "//input[@id='owner-type']"
CMB_ADD_FIELDS = "//ng-select[@formcontrolname='field']"
LST_ADD_FIELDS = "//ng-select[@formcontrolname='field']//ng-dropdown-panel[@role='listbox']"
LST_ADD_FIELDS_ITEM = "//div[@class='item-details']//span[contains(@class,'item-title') and text()='<<text>>']"
SEL_OWNER_BASE = "//label[text()=' Select Owner ']"
OWNER_BASE = "//label[text()=' Owner ']"
MAIN_PROP_TITLE = "//span[@class='text-sm' and text()='Update Owner']"
LBL_OWNER = "<<base>>/parent::div//input[@id='owner-type']"
CMB_OWNER = "<<base>>/parent::div//div[@role='combobox']"
LST_OWNER = "<<base>>/ancestor::div//ng-dropdown-panel[@role='listbox']"
LST_SEL_OWNER_FLAG = "aria-expanded='true'"
LST_SEL_OWNER_ITEMS = "<<base>>/ancestor::div//ng-dropdown-panel[@role='listbox']//div[@role='option']"
LST_SEL_OWNER_ITEMS_LBLS = "<<base>>/ancestor::div//ng-dropdown-panel[@role='listbox']//div[@role='option']//span[@class='ng-option-label' and text()='<<text>>']"
LST_SEL_OWNER_DEFAULT_ITEM = "<<base>>/ancestor::div//ng-dropdown-panel[@role='listbox']//div[@role='option' and @aria-selected='true']"
LST_SEL_OWNER_ITEM_FLAG = "aria-selected='true'"
MSG_REQUIRED_ERROR = "//span[@class='form-input-error-message']"
LST_OWNER_ITEMS = "<<base>>/ancestor::div//div[@role='option']"
LST_OWNER_ITEMS_LBLS = "<<base>>/ancestor::div//div[@role='option']//span[contains(@class,'item-title') and text()='<<text>>']"
LST_OWNER_DEFAULT_ITEM = "<<base>>/ancestor::div//div[@role='option' and @aria-selected='true']"
OWNER_CLEAR = "//app-properties//label[@for='owner-type' and text()=' Owner ']//following-sibling::ng-select//span[@class='ng-clear-wrapper']"
OWNER_ARROW = "//app-properties//label[@for='owner-type' and text()=' Owner ']//following-sibling::ng-select//span[@class='ng-arrow-wrapper']"
BODY_UPPER_HEADER_TITLE = "//span[@class='text-sm']"
PROPERTIES_ROOT = "//app-properties"
BTN_ADD_FIELDS = "//form[contains(@class,'ng-untouched')]/following::button[text()=' Add field to update ']"
BTN_REQ_FIELDS_TEXT = "//form[contains(@class,'ng-untouched')]/following::button[text()=' Add field to update ']/text()"
REQ_FIELDS_FRM = "//div[contains(@class,'mt-2')]"
REQ_FIELDS_FRM_LBL = "//div[contains(@class,'mt-2')]//label[@for='type']"
REQ_FIELDS_LBL = "//app-properties//div[contains(@class,'mt-7')]//span[@class='text-sm']"
REQ_FIELDS_BTN = "//app-properties//button[contains(@class,'btn-action')]"
REQ_FIELDS_TRASH = "//app-properties//img[@alt='TrashCanIcon']/parent::button"
REQ_FIELDS_FLD_LBL = "//app-properties//ng-select[@formcontrolname='field']/preceding-sibling::label"
REQ_FIELDS_FLD_CMB = "//app-properties//ng-select[@formcontrolname='field']"
REQ_FIELDS_FLD_CMB_ITEM = "//app-properties//ng-select[@formcontrolname='field']//div[@class='ng-option']"
REQ_FIELDS_FLD_CMB_ITEM_R = "//span[contains(@class,'item-title') and text()='<<text>>']"
REQ_FIELDS_FLD_CLEAR = "//app-properties//ng-select[@formcontrolname='field']//span[@class='ng-clear-wrapper']"
REQ_FIELDS_FLD_ARROW = "//app-properties//ng-select[@formcontrolname='field']//span[@class='ng-arrow-wrapper']"
REQ_FIELDS_FLD_ITEM = "//app-properties//ng-select[@formcontrolname='field']//div[@class='ng-option']"
REQ_FIELDS_VAL_LBL = "//app-properties//ng-select[@formcontrolname='value']/preceding-sibling::label"
REQ_FIELDS_VAL_CMB = "//app-properties//ng-select[@formcontrolname='value']"
REQ_FIELDS_VAL_CLEAR = "//app-properties//ng-select[@formcontrolname='value']//span[@class='ng-clear-wrapper']"
REQ_FIELDS_VAL_ARROW = "//app-properties//ng-select[@formcontrolname='value']//span[@class='ng-arrow-wrapper']"
REQ_FIELDS_VAL_SELECTED = "//app-properties//ng-select[@formcontrolname='value']//div[@class='ng-value']"
REQ_FIELDS_VAL_ITEM = "//app-properties//ng-select[@formcontrolname='value']//div[@role='option']"
REQ_FIELDS_VAL_TEXT = "//app-properties//ng-select[@formcontrolname='value']//span[@class='ng-value-label']"
REQ_FIELDS_FRM_VAL_ITEM = "//div[contains(@class,'mt-2')]//ng-select[@formcontrolname='value']//div[@class='ng-input']"
REQ_FIELDS_VAL_INPUTS = "//app-generic-field//div[@class='form-field-input']/child::*"
REQ_FIELDS_FRM_VAL_TEXT = "//app-generic-field//div[@class='form-field-input']/child::input[@type='text']"
REQ_FIELDS_FRM_VAL_NUMBER = "//app-generic-field//div[@class='form-field-input']/child::input[@type='number']"
REQ_FIELDS_FRM_VAL_DATE = "//app-generic-field//div[@class='form-field-input']/app-datepicker-input"
REQ_FIELDS_FRM_VAL_DROP = "//app-generic-field//div[@class='form-field-input']/descendant::div[@role='combobox']"
REQ_FIELDS_FRM_VAL_MULTI = "//app-generic-field//div[@class='form-field-input']/textarea"
REQ_FIELDS_FRM_VAL_USER = "//app-generic-field//div[@class='form-field-input']/ng-select"
REQ_FIELDS_FRM_VAL_CHECK = "//app-generic-field//div[@class='form-field-input']//label[@class='checkbox-edit-mode']"
ADD_COMMENT_CHK = "//label[@for='add-comment']"
ADD_COMMENT_LBL = "//label[@for='add-comment' and @class='properties-checkbox-text']"
END_STEP_CHK = "//label[@for='end-step']"
END_STEP_LBL = "//span[@class='properties-panel-text']"
UPDATE_FIELDS_CHK = "//label[@for='update-form-fields']"
UPDATE_FIELDS_LBL = "//label[@for='update-form-fields' and @class='properties-checkbox-text']"
NAME_TXT = "//input[@id='name']"
NAME_LBL = "//label[@for='name']"
TYPE_LBL = "//label[@for='type']"
TYPE_CMB = "//ng-select[@id='type']//div[@role='combobox']"
TYPE_CMB_ARROW = "//ng-select[@id='type']//span[@class='ng-arrow-wrapper']"
TYPE_CMB_OPTION = "//ng-select[@id='type']//div[@role='option']"
TYPE_CMB_DEFAULT = "//ng-select[@id='type']//span[@class='ng-value-label']"
DATE_PICKER = "//div[@id='datepicker']"
DATE_PICKER_MONTH = "//div[@id='datepicker']//div[@class='dropdown-selector'][1]"
DATE_PICKER_YEAR = "//div[@id='datepicker']//div[@class='dropdown-selector'][2]"
DATE_PICKER_DAY = "//div[@id='datepicker']//div[@class='calendar-table-cell' and text()='<<day>>']"
DATE_PICKER_MONTH_ADD = "//div[@id='datepicker']//div[@class='dropdown-selector'][1]//div[@class='item-container']/a[contains(@id,'<<month>>')]"
DATE_PICKER_YEAR_ADD = "//div[@id='datepicker']//div[@class='dropdown-selector'][2]//div[@class='item-container']/a[contains(text(),'<<year>>')]"
OWNER_COMBOBOX_MENU = "//input[@id='owner-type' and @readonly]/ancestor::ng-select"
SELECT_FIRST_USER = "//input[@id='owner-type' and not (@readonly)]//following::div[@role='option'][1]"
SEARCH_OWNER = "//input[@id='owner-type' and not (@readonly)]"
