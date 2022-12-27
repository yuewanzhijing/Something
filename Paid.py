import sys
from PyQt5.QtWidgets import QApplication
import test
class Test():
    def __init__(self) -> None:
        self.app=QApplication(sys.argv)
        self.ui=test.Ui_MainWindow()
        self.ui.show()
        self.connect_click()
        sys.exit(self.app.exec_())
    
    def connect_click(self):
        self.ui.pushButton.clicked.connect(lambda:self.showMsg("1"))
        self.ui.pushButton_2.clicked.connect(lambda:self.showMsg("2"))
    
    def showMsg(self,name):
        if "1" == name:
            self.ui.textEdit.setPlainText("Button被按下")
        elif "2" == name:
            self.ui.textEdit.setPlainText("Button2被按下")

if __name__=="__main__":
    UI=Test()