from threading import Thread
from time import sleep
from urllib.request import urlopen

from PyQt5 import QtWidgets, uic
import sys

from form import Ui_Form


def thread_update_voice_synthesis_health(form: Ui_Form):
    while True:
        is_up = check_voice_synthesis_up()
        newStatus = "Working!" if is_up else "Stopped"
        newColor = "green" if is_up else "red"

        form.label_VoiceSynthesisStatus.setText(newStatus)
        form.label_VoiceSynthesisStatus.setStyleSheet(f"QLabel {{ color : {newColor}}}")
        form.button_VoiceSynthesisStart.setDisabled(is_up)

        sleep(5)


def check_voice_synthesis_up() -> bool:
    health_url = 'http://localhost:5050/'
    try:
        with urlopen(health_url) as response:
            if response.status == 200:
                return True
    except Exception:
        return False


if __name__ == "__main__":
    # Set up GUI
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)

    # Set up health checks
    Thread(target=thread_update_voice_synthesis_health, args=(ui,)).start()

    Form.show()
    sys.exit(app.exec_())
