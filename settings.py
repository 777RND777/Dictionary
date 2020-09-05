from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QCheckBox, QComboBox, QHBoxLayout, QPushButton, QVBoxLayout, QWidget


class Settings:
    def __init__(self, mode, one_life, noun, verb, adj, adverb):
        self.mode = mode
        self.oneLife = one_life
        self.noun = noun
        self.verb = verb
        self.adj = adj
        self.adverb = adverb


class SettingsWidget(QWidget):
    switch_window = pyqtSignal()

    def __init__(self):
        super(SettingsWidget, self).__init__()

        self.modeBox = QComboBox()
        self.modeBox.addItems(["RUS->ENG", "ENG->RUS", "BOTH"])

        self.oneLifeCheck = QCheckBox()
        self.oneLifeCheck.setText("One life")

        self.nounCheck = QCheckBox()
        self.nounCheck.setText("Nouns")
        self.nounCheck.setChecked(True)

        self.verbCheck = QCheckBox()
        self.verbCheck.setText("Verbs")
        self.verbCheck.setChecked(True)

        self.adjCheck = QCheckBox()
        self.adjCheck.setText("Adjectives")
        self.adjCheck.setChecked(True)

        self.adverbCheck = QCheckBox()
        self.adverbCheck.setText("Adverbs")
        self.adverbCheck.setChecked(True)

        self.partOfSpeech = QHBoxLayout()
        self.partOfSpeech.addWidget(self.nounCheck, alignment=Qt.AlignCenter)
        self.partOfSpeech.addWidget(self.verbCheck, alignment=Qt.AlignCenter)
        self.partOfSpeech.addWidget(self.adjCheck, alignment=Qt.AlignCenter)
        self.partOfSpeech.addWidget(self.adverbCheck, alignment=Qt.AlignCenter)

        self.startButton = QPushButton()
        self.startButton.setText("Start")
        self.startButton.clicked.connect(self.switch_window.emit)
        self.startButton.setShortcut("Return")

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.modeBox, alignment=Qt.AlignCenter)
        self.mainLayout.addWidget(self.oneLifeCheck, alignment=Qt.AlignCenter)
        self.mainLayout.addLayout(self.partOfSpeech)
        self.mainLayout.addWidget(self.startButton, alignment=Qt.AlignCenter)

        self.setLayout(self.mainLayout)

    def get_settings(self):
        return Settings(
            self.modeBox.currentText(),
            self.oneLifeCheck.isChecked(),
            self.nounCheck.isChecked(),
            self.verbCheck.isChecked(),
            self.adjCheck.isChecked(),
            self.adverbCheck.isChecked(),
        )
