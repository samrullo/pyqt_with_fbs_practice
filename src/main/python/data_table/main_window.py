from utils.data_table_utils import get_data_table_configs
import pathlib
from functools import partial
from PyQt5.QtWidgets import QMainWindow, QAction, QStackedLayout
from new_data_table import NewDataTableWidget


class MainWindow(QMainWindow):
    def __init__(self, appctxt):
        super().__init__()
        self.appctxt = appctxt
        self.data_table_configs = get_data_table_configs(
            pathlib.Path(
                self.appctxt.get_resource("data_tables/data_table_definitions")
            )
        )
        self.data_config_actions = {}
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 800, 700)
        self.setWindowTitle("New Data Table")
        self.stacked_layout = QStackedLayout()
        self.new_data_table_widget = NewDataTableWidget(self.appctxt)
        self.stacked_layout.addWidget(self.new_data_table_widget)
        self.createMenus()
        self.show()

    def createMenus(self):
        self.menu_bar = self.menuBar()
        self.file_menu = self.menu_bar.addMenu("File")
        self.data_table_menu = self.menu_bar.addMenu("Data Table")
        self.data_table_menu.addAction("New Data Table")
        self.data_table_menu.addSeparator()
        for data_config in self.data_table_configs:
            self.data_config_actions[data_config["data_table_name"]] = QAction(
                data_config["data_table_name"], self
            )
            self.data_config_actions[data_config["data_table_name"]].triggered.connect(
                partial(self.data_config_selected, data_config)
            )
            print(f"will create action with name ")
            self.data_table_menu.addAction(
                self.data_config_actions[data_config["data_table_name"]]
            )

    def data_config_selected(self, data_config):
        print(self)
        print(data_config)
