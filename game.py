from database import *
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QMessageBox, QLineEdit, QPushButton, QVBoxLayout, QWidget
from random import randint


class GameWidget(QWidget):
    switch_window = pyqtSignal()

    def __init__(self):
        super(GameWidget, self).__init__()

        self.word_list = []
        self.score = 0
        self.wrong = 0
        self.lang = 0
        self.mode = ""
        self.random_word = ""

        self.questionWord = QLineEdit()
        self.questionWord.setReadOnly(True)

        self.answerWord = QLineEdit()

        self.submitButton = QPushButton()
        self.submitButton.setText("Submit")
        self.submitButton.clicked.connect(self.is_right)
        self.submitButton.setShortcut("Return")

        self.exitButton = QPushButton()
        self.exitButton.setText("Exit")
        self.exitButton.clicked.connect(self.switch_window.emit)
        self.exitButton.setShortcut("Escape")

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.questionWord, alignment=Qt.AlignCenter)
        self.mainLayout.addWidget(self.answerWord, alignment=Qt.AlignCenter)
        self.mainLayout.addWidget(self.submitButton, alignment=Qt.AlignCenter)
        self.mainLayout.addWidget(self.exitButton, alignment=Qt.AlignCenter)

        self.setLayout(self.mainLayout)

    def set_start(self, mode):
        self.score = 0
        self.wrong = 0
        self.mode = mode
        self.create_word_list()
        self.set_question_word()

    def create_word_list(self):
        self.word_list = []
    # if self.nounCheck.isChecked():
    #     self.word_list += nouns
    # if self.verbCheck.isChecked():
        self.word_list += verbs
    # if self.adjCheck.isChecked():
    #     self.word_list += adjectives
    # if self.adverbCheck.isChecked():
    #     self.word_list += adverbs

    def set_question_word(self):
        self.random_word = self.get_random_word()
        if self.mode == "RUS->ENG":
            self.questionWord.setText(self.random_word.rus)
        elif self.mode == "ENG->RUS":
            self.questionWord.setText(self.random_word.eng)
        else:
            self.lang = randint(1, 2)
            if self.lang == 1:
                self.questionWord.setText(self.random_word.rus)
            elif self.lang == 2:
                self.questionWord.setText(self.random_word.eng)

    def get_random_word(self):
        return self.word_list[randint(0, len(self.word_list) - 1)]

    def is_right(self):
        if self.answerWord.text() == self.get_translation():
            self.word_list.remove(self.random_word)
            self.score += 1
            if len(self.word_list) == 0:
                QMessageBox.information(
                    None, "Info", "You've finished all words from vocabulary.\nWrong answers : " + str(self.wrong) + "."
                )
                self.switch_window.emit()
            else:
                self.set_question_word()
        # elif self.oneLifeCheck.isChecked():
        #     QMessageBox.critical(
        #         None, "Wrong", "Right translation is " + self.get_translation() + "\nScore : " + str(self.score) + "."
        #     )
        #     self.switch_window.emit()
        else:
            QMessageBox.critical(None, "Wrong", "Right translation is " + self.get_translation() + ".")
            self.wrong += 1
            self.set_question_word()
        self.answerWord.setText("")

    def get_translation(self):
        if self.mode == "RUS->ENG":
            return self.rus_to_eng()
        elif self.mode == "ENG->RUS":
            return self.eng_to_rus()
        elif self.lang == 1:
            return self.rus_to_eng()
        elif self.lang == 2:
            return self.eng_to_rus()

    def rus_to_eng(self):
        for word in self.word_list:
            if word.rus == self.questionWord.text():
                return word.eng

    def eng_to_rus(self):
        for word in self.word_list:
            if word.eng == self.questionWord.text():
                return word.rus
