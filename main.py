from PyQt5.QtWidgets import QApplication, QMessageBox, QStackedWidget
import game
import settings
import sys


class MainWindow(QStackedWidget):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
        self.setWindowTitle("Dictionary")
        self.resize(360, 480)

        self.settingsWidget = settings.SettingsWidget()
        self.settingsWidget.switch_window.connect(self.to_game)
        self.addWidget(self.settingsWidget)
        self.to_settings()

        self.gameWidget = game.GameWidget()
        self.gameWidget.switch_window.connect(self.to_settings)
        self.addWidget(self.gameWidget)

    def to_settings(self):
        self.setCurrentWidget(self.settingsWidget)

    def to_game(self):
        self.setCurrentWidget(self.gameWidget)
        self.gameWidget.set_start(self.settingsWidget.get_settings())


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
