from PyQt6.QtWidgets import QApplication, QWidget

app = QApplication([])
window = QWidget(windowTitle='Waveform Generator')
window.show()

app.exec()