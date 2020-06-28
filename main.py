from database import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QHBoxLayout, QMessageBox,
                             QLineEdit, QPushButton, QVBoxLayout, QWidget)
from random import randint
import sys


class MainWindow(QWidget):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
        self.setWindowTitle("Dictionary")
        self.resize(360, 480)

        self.is_game = False
        self.word_list = []

        self.modeBox = QComboBox()
        self.modeBox.addItems(["RUS->ENG", "ENG->RUS", "BOTH"])
        self.mode = 0

        self.nounCheck = QCheckBox()
        self.nounCheck.setText("Nouns")
        self.nounCheck.setChecked(True)

        self.adjCheck = QCheckBox()
        self.adjCheck.setText("Adjectives")
        self.adjCheck.setChecked(True)

        self.partOfSpeech = QHBoxLayout()
        self.partOfSpeech.addWidget(self.nounCheck, alignment=Qt.AlignCenter)
        self.partOfSpeech.addWidget(self.adjCheck, alignment=Qt.AlignCenter)

        self.questionWord = QLineEdit()
        self.questionWord.setReadOnly(True)

        self.answerWord = QLineEdit()

        self.submitButton = QPushButton()
        self.submitButton.clicked.connect(self.is_right)

        self.exitButton = QPushButton()
        self.exitButton.setText("Exit")
        self.exitButton.clicked.connect(self.set_start)

        self.set_start()

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.modeBox, alignment=Qt.AlignCenter)
        self.mainLayout.addLayout(self.partOfSpeech)
        self.mainLayout.addWidget(self.questionWord, alignment=Qt.AlignCenter)
        self.mainLayout.addWidget(self.answerWord, alignment=Qt.AlignCenter)
        self.mainLayout.addWidget(self.submitButton, alignment=Qt.AlignCenter)
        self.mainLayout.addWidget(self.exitButton, alignment=Qt.AlignCenter)

        self.setLayout(self.mainLayout)

    def set_start(self):
        self.nounCheck.show()
        self.adjCheck.show()
        self.modeBox.show()
        self.questionWord.hide()
        self.answerWord.hide()
        self.submitButton.setText("Start")
        self.exitButton.hide()
        self.is_game = False

    def start_game(self):
        self.nounCheck.hide()
        self.adjCheck.hide()
        self.modeBox.hide()
        self.questionWord.show()
        self.answerWord.show()
        self.submitButton.setText("Submit")
        self.exitButton.show()
        self.is_game = True
        self.create_word_list()

    def create_word_list(self):
        self.word_list = []
        if self.nounCheck.isChecked():
            self.word_list += nouns
        if self.adjCheck.isChecked():
            self.word_list += adjectives

    def is_right(self):
        if self.is_game:
            if self.answerWord.text() == self.get_translation():
                self.set_question_word()
            else:
                QMessageBox.critical(None, 'Wrong', 'Right translation is ' + self.get_translation())
                self.set_start()
            self.answerWord.setText("")
        else:
            self.start_game()
            self.set_question_word()

    def set_question_word(self):
        rnd = randint(0, len(self.word_list) - 1)
        if self.modeBox.currentText() == "RUS->ENG":
            self.questionWord.setText(self.word_list[rnd].rus)
        elif self.modeBox.currentText() == "ENG->RUS":
            self.questionWord.setText(self.word_list[rnd].eng)
        else:
            self.mode = randint(1, 2)
            if self.mode == 1:
                self.questionWord.setText(self.word_list[rnd].rus)
            elif self.mode == 2:
                self.questionWord.setText(self.word_list[rnd].eng)

    def get_translation(self):
        if self.modeBox.currentText() == "RUS->ENG":
            return self.rus_to_eng()
        elif self.modeBox.currentText() == "ENG->RUS":
            return self.eng_to_rus()
        elif self.mode == 1:
            return self.rus_to_eng()
        elif self.mode == 2:
            return self.eng_to_rus()

    def rus_to_eng(self):
        for word in self.word_list:
            if word.rus == self.questionWord.text():
                return word.eng

    def eng_to_rus(self):
        for word in self.word_list:
            if word.eng == self.questionWord.text():
                return word.rus


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
