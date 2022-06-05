from fbs_runtime.application_context.PyQt5 import ApplicationContext
from data_table.data_table import DataTable
import pathlib
import sys

if __name__ == "__main__":
    appctxt = ApplicationContext()  # 1. Instantiate ApplicationContext
    style_sheet = pathlib.Path(appctxt.get_resource("styles/mystyles.qss")).read_text()
    appctxt.app.setStyleSheet(style_sheet)
    data_config = {
        "data_table_name": "gpc_tickets",
        "no_cols": "4",
        "column_names": ["client", "project", "ticket", "url"],
    }

    profile_widget = DataTable(data_config, appctxt)
    exit_code = appctxt.app.exec_()  # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)
