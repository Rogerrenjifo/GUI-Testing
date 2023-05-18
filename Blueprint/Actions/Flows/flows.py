from Blueprint.Actions.Flows.create_form_elements_actions import CreateFormElementsActions
from Blueprint.Actions.Flows.create_form_main_panel_actions import FormMainPanelActions
from Blueprint.Actions.Flows.create_form_properties_panel_actions import PropertiesPanelActions
from Blueprint.Actions.Flows.flow_components_actions import ComponentsActions
from Blueprint.Actions.Flows.header_actions import HeaderActions
from Blueprint.Actions.Flows.permissions_actions import FlowPermissionsActions
from Blueprint.Actions.Flows.publish_tab_actions import PublishTabActions
from Blueprint.Actions.Flows.flow_main_panel_actions import FlowMainPanelActions
from Blueprint.Actions.Flows.flows_properties_actions import FlowPropertiesActions


class Flows():
    """This class represents all the actions in flow page"""

    def __init__(self, driver):
        self.driver = driver
        self.__create_form_elements = CreateFormElementsActions(self.driver)
        self.__create_form_main_panel = FormMainPanelActions(self.driver)
        self.__create_form_properties_panel = PropertiesPanelActions(self.driver)
        self.__create_flow_main_panel = FlowMainPanelActions(self.driver)
        self.__create_flow_properties = FlowPropertiesActions()
        self.__create_flow_components = ComponentsActions(self.driver)
        self.__header = HeaderActions(self.driver)
        self.__permissions_tab = FlowPermissionsActions(self.driver)
        self.__publish_tab = PublishTabActions(self.driver)

    @property
    def form_tab_elements(self):
        """This attribute contains the actions of the elements in create form tab - flow page"""
        return self.__create_form_elements
    
    @property
    def form_tab_properties(self):
        """This attribute contains the actions of properties panel in create form tab - flow page"""
        return self.__create_form_properties_panel
    
    @property
    def form_tab_main_panel(self):
        """This attribute contains the actions of the main panel in create form tab - flow page"""
        return self.__create_form_main_panel
     
    @property
    def flow_tab_components(self):
        """This attribute contains the actions of each component in create flow tab - flow page"""
        return self.__create_flow_components
    
    @property
    def flow_tab_properties(self):
        """This attribute contains the actions of properties panel in create flow tab - flow page"""
        return self.__create_flow_properties
    
    @property
    def flow_tab_main_panel(self):
        """This attribute contains the actions of the main panel in create flow tab - flow page"""
        return self.__create_flow_main_panel
    
    @property
    def permissions_tab(self):
        """This attribute contains the actions in permissions tab - flow page"""
        return self.__permissions_tab
    
    @property
    def publish_tab(self):
        """This attribute contains the actions in publish tab - flow page"""
        return self.__publish_tab
    
    @property   
    def header(self):
        """This attribute contains the actions in the header of flow page"""
        return self.__header
