import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
import MainWindow


class MainCode(QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        MainWindow.Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.savefile.clicked.connect(self.on_save)
        self.openfile.clicked.connect(self.on_open)

    def on_save(self):
        FullFileName, _ = QFileDialog.getSaveFileName(self, '文件另存为', r'./', 'TXT (*.txt)')
        set_text = self.textEdit.toPlainText()
        with open(FullFileName, 'wt') as f:
            print(set_text, file=f)

    def on_open(self):
        txtstr = ""
        FullFileName, _ = QFileDialog.getOpenFileName(self, '打开', r'./', 'TXT (*.txt)')
        with open(FullFileName, 'rt') as f:
            lines = f.readlines()
            for line in lines:
                txtstr = txtstr + line
        self.textEdit.setText(txtstr)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    md = MainCode()
    md.show()
    sys.exit(app.exec_())