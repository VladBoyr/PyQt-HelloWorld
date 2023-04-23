import keyboard
import sys
from PyQt6.QtWidgets import QApplication, QDialog
from ui_imagedialog import Ui_ImageDialog

keyboard.add_hotkey("ctrl+alt+j", lambda: print("ctrl+alt+j was pressed"))

app = QApplication(sys.argv)
window = QDialog()
ui = Ui_ImageDialog()
ui.setupUi(window)

window.show()
sys.exit(app.exec())
