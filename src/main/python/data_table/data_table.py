import pathlib
import json
from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QComboBox,
    QTableWidget,
    QTableWidgetItem,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QFormLayout,
)

from PyQt5.QtCore import Qt


class DataTable(QWidget):
    def __init__(self, data_config, appctxt) -> None:
        super().__init__()
        self.appctxt = appctxt
        self.data_config = data_config
        self.data_table_contents_folder = self.appctxt.get_resource(
            "data_tables/data_table_contents"
        )

        self.data_table_name = self.data_config["data_table_name"]
        self.data_table_path = pathlib.Path(self.data_table_contents_folder) / (
            self.data_table_name + ".json"
        )
        if not self.data_table_path.exists():
            with open(self.data_table_path, "w") as f:
                json.dump([{}], f)
        self.data_table_contents = self.read_data_table_contents()
        self.initializeUI()

    def read_data_table_contents(self):
        with open(self.data_table_path, "r") as f:
            data_table_contents = json.load(f)
        return data_table_contents

    def initializeUI(self):
        self.setGeometry(100, 100, 800, 700)
        self.setWindowTitle("Data Table")
        self.form_layout = QHBoxLayout()
        self.v_box = QVBoxLayout()
        self.data_table_widget = QTableWidget()

        title = QLabel(self.data_config["data_table_name"])
        title.setAlignment(Qt.AlignCenter)
        title.setObjectName("big_lbl")

        # search section
        search_label = QLabel("Search text")
        search_le = QLineEdit()
        self.search_le = search_le
        search_col_lbl = QLabel("Search column")
        search_col = QComboBox()
        search_col.addItems([col for col in self.data_config["column_names"]])
        self.search_col = search_col
        form_layout = QFormLayout()
        form_layout.addRow(search_label, search_le)
        form_layout.addRow(search_col_lbl, search_col)
        search_le.textChanged.connect(self.filter_data)

        self.populate_table_widget_data(self.data_table_contents)

        self.v_box.addWidget(title)
        self.v_box.addLayout(form_layout)
        self.v_box.addWidget(self.data_table_widget)
        self.setLayout(self.v_box)
        self.show()

    def populate_table_widget_data(self, data_table_contents):
        table_columns = self.data_config["column_names"]
        tableWidgetColumnsDict = {col: i for i, col in enumerate(table_columns)}
        self.data_table_widget.setColumnCount(len(tableWidgetColumnsDict))
        self.data_table_widget.setRowCount(len(data_table_contents))

        # set table column names
        self.data_table_widget.setHorizontalHeaderLabels(
            [col.upper() for col in tableWidgetColumnsDict.keys()]
        )

        for row_idx, data_table_content in enumerate(data_table_contents):
            for col in tableWidgetColumnsDict:
                item = QTableWidgetItem(data_table_content[col])
                self.data_table_widget.setItem(
                    row_idx, tableWidgetColumnsDict[col], item
                )
                if tableWidgetColumnsDict[col] == 0:
                    item.setFlags((item.flags()) & (~Qt.ItemIsEditable))

    def filter_data(self):
        filter_by = self.search_col.currentText()
        search_txt = self.search_le.text().lower()
        filtered_data_list = [
            data_item
            for data_item in self.data_table_contents
            if search_txt.lower() in data_item[filter_by].lower()
        ]
        self.data_table_widget.clear()
        self.populate_table_widget_data(filtered_data_list)
