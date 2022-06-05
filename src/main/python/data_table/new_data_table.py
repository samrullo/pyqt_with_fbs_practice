import os
import pathlib
import json
from PyQt5.QtWidgets import (
    QWidget,
    QFormLayout,
    QPushButton,
    QMessageBox,
    QLabel,
    QLineEdit,
    QVBoxLayout,
    QHBoxLayout,
)
from PyQt5.QtGui import QFont

from utils.my_pyqt_utils import deleteItemsOfLayout


class NewDataTableWidget(QWidget):
    def __init__(self, appctxt) -> None:
        super().__init__()
        self.appctxt = appctxt
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 800, 700)
        self.setWindowTitle("New Data Table")
        self.form_layout = QFormLayout()

        data_table_name_lbl = QLabel("Data Table Name")
        data_table_name_lbl.setObjectName("big_lbl")
        self.data_table_name_le = QLineEdit()
        self.data_table_name_le.setObjectName("big_le")
        no_of_cols_lbl = QLabel("Number of columns")
        no_of_cols_lbl.setObjectName("big_lbl")
        self.no_of_cols_le = QLineEdit()
        self.no_of_cols_le.setObjectName("big_le")
        no_of_cols_btn = QPushButton("Populate form")
        no_of_cols_btn.setObjectName("special_button")
        no_of_cols_btn.clicked.connect(self.populate_columns_name_fields)

        dt_form_layout = QFormLayout()
        dt_form_layout.addRow(data_table_name_lbl, self.data_table_name_le)
        dt_form_layout.addRow(no_of_cols_lbl, self.no_of_cols_le)
        dt_form_layout.addRow(no_of_cols_btn)

        v_box = QVBoxLayout()
        v_box.addLayout(dt_form_layout)
        self.col_form_layout = QFormLayout()
        v_box.addLayout(self.col_form_layout)
        self.v_box = v_box

        self.setLayout(v_box)
        self.show()

    def boxdelete(self, box):
        for i in range(self.vlayout.count()):
            layout_item = self.vlayout.itemAt(i)
            if layout_item.layout() == box:
                deleteItemsOfLayout(layout_item.layout())
                self.vlayout.removeItem(layout_item)
                break

    def populate_columns_name_fields(self):
        answer = QMessageBox.question(
            self,
            "Confirm",
            "Are you sure you want to populate columns name fields?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )
        if answer == QMessageBox.Yes:
            deleteItemsOfLayout(self.col_form_layout)

            self.column_names = []
            try:
                no_of_cols = int(self.no_of_cols_le.text())
                for i in range(no_of_cols):
                    _col_lbl = QLabel("Column {}".format(i + 1))
                    _col_lbl.setObjectName("big_lbl")
                    _col_le = QLineEdit()
                    _col_le.setObjectName("big_le")
                    self.column_names.append(_col_le)
                    self.col_form_layout.addRow(_col_lbl, _col_le)
                submit_btn = QPushButton("Submit")
                submit_btn.setObjectName("special_button")
                submit_btn.clicked.connect(self.submit_columns_name_fields)
                self.col_form_layout.addRow(submit_btn)
            except:
                QMessageBox.warning(self, "Error", "Please enter a valid number")
        else:
            pass

    def submit_columns_name_fields(self):
        datatable_def = {
            "datatable_name": self.data_table_name_le.text(),
            "no_cols": self.no_of_cols_le.text(),
            "column_names": [col_le.text() for col_le in self.column_names],
        }
        datatable_def_folder = pathlib.Path(
            self.appctxt.get_resource("datatables/datatable_definitions")
        )
        datatable_def_file = datatable_def_folder / (
            datatable_def["datatable_name"] + ".json"
        )
        print(f"attempting to save {datatable_def} into {datatable_def_file}")
        with open(datatable_def_file, "w") as f:
            json.dump(datatable_def, f)
        print(f"saved datatable def into {datatable_def_file}")
        QMessageBox.information(self, "Successfully saved", "Successfully saved")
        for col_le in self.column_names:
            print(col_le.text())
        deleteItemsOfLayout(self.col_form_layout)
