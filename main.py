from database import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMessageBox, QLineEdit, QPushButton, QVBoxLayout, QWidget
from random import randint
import sys


class MainWindow(QWidget):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
        self.setWindowTitle("Dictionary")

        self.questionWord = QLineEdit()
        self.questionWord.setReadOnly(True)

        self.answerWord = QLineEdit()

        self.is_game = False
        self.submitButton = QPushButton("Start")
        self.submitButton.clicked.connect(self.is_right)

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.questionWord, alignment=Qt.AlignBaseline)
        self.mainLayout.addWidget(self.answerWord, alignment=Qt.AlignBaseline)
        self.mainLayout.addWidget(self.submitButton, alignment=Qt.AlignBaseline)

        self.setLayout(self.mainLayout)

    def is_right(self):
        if self.is_game:
            if self.answerWord.text() == self.get_translation():
                print("Right")
                self.answerWord.setText("")
                self.set_question_word()
            else:
                QMessageBox.critical(None, 'Wrong', 'Right translation is ' + adjectives[self.questionWord.text()])
                self.submitButton.setText("Start")
        else:
            self.submitButton.setText("Submit")
            self.is_game = True
            self.set_question_word()

    def set_question_word(self):
        rnd = randint(0, len(adjectives) - 1)
        self.questionWord.setText(adjectives[rnd].eng)

    def get_translation(self):
        for adjective in adjectives:
            if adjective.eng == self.questionWord.text():
                return adjective.rus


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
