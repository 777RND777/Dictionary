from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMessageBox, QLineEdit, QPushButton, QVBoxLayout, QWidget
import sys


class MainWindow(QWidget):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
        self.setWindowTitle("Dictionary")

        self.questionWord = QLineEdit()
        self.questionWord.setReadOnly(True)

        self.answerWord = QLineEdit()

        self.submitButton = QPushButton("Submit")

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.questionWord, alignment=Qt.AlignBaseline)
        self.mainLayout.addWidget(self.answerWord, alignment=Qt.AlignBaseline)
        self.mainLayout.addWidget(self.submitButton, alignment=Qt.AlignBaseline)

        self.setLayout(self.mainLayout)


def catch_exceptions(t, val, tb):
    QMessageBox.critical(None, 'An exception was raised', 'Exception type: {}'.format(t))
    old_hook(t, val, tb)


if __name__ == '__main__':
    old_hook = sys.excepthook
    sys.excepthook = catch_exceptions

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
