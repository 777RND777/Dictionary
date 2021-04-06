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
        self.settings = {}
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

    def set_start(self, settings):
        self.score = 0
        self.wrong = 0
        self.settings = settings
        self.create_word_list()
        self.set_question_word()

    def create_word_list(self):
        self.word_list = []
        if self.settings['noun']:
            self.word_list += nouns
        if self.settings['verb']:
            self.word_list += verbs
        if self.settings['adj']:
            self.word_list += adjectives
        if self.settings['adverb']:
            self.word_list += adverbs

    def set_question_word(self):
        self.random_word = self.get_random_word()
        if self.settings['mode'] == "RUS->ENG":
            self.questionWord.setText(self.random_word['rus'])
        elif self.settings['mode'] == "ENG->RUS":
            self.questionWord.setText(self.random_word['eng'])
        elif randint(0, 1):
            self.questionWord.setText(self.random_word['rus'])
        else:
            self.questionWord.setText(self.random_word['eng'])

    def get_random_word(self):
        return self.word_list[randint(0, len(self.word_list) - 1)]

    def is_right(self):
        translation = self.get_translation()
        if self.answerWord.text() == translation:
            self.word_list.remove(self.random_word)
            self.score += 1
            if not self.word_list:
                QMessageBox.information(None, "Info", f"You've finished all words from vocabulary.\n"
                                                      f"Wrong answers : {self.wrong}.")
                self.switch_window.emit()
            else:
                self.set_question_word()
        elif self.settings['one_life']:
            QMessageBox.critical(None, "Wrong", f"Right translation is {translation}\n"
                                                f"Score : {self.score}.")
            self.switch_window.emit()
        else:
            QMessageBox.critical(None, "Wrong", f"Right translation is {translation}.")
            self.wrong += 1
            self.set_question_word()
        self.answerWord.setText("")

    def get_translation(self):
        for word in self.word_list:
            if word['rus'] == self.questionWord.text():
                return word['eng']
            elif word['eng'] == self.questionWord.text():
                return word['rus']
