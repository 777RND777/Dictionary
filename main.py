from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow
import game
import settings
import sys


class MainWindow(QMainWindow):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
        self.setWindowTitle("Dictionary")
        self.resize(360, 480)

        self.settingsWidget = settings.SettingsWidget()
        self.settingsWidget.switch_window.connect(self.to_game)
        self.to_settings()

        self.gameWidget = game.GameWidget()
        self.gameWidget.switch_window.connect(self.to_settings)

    def to_settings(self):
        self.setCentralWidget(self.settingsWidget)

    def to_game(self):
        self.setCentralWidget(self.gameWidget)
        self.gameWidget.set_start(self.settingsWidget.modeBox.currentText())


def catch_exceptions(t, val, tb):
    QMessageBox.critical(None, "An exception was raised", "Exception type: {}".format(t))
    old_hook(t, val, tb)


if __name__ == "__main__":
    old_hook = sys.excepthook
    sys.excepthook = catch_exceptions

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
