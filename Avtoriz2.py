from PyQt6.QtWidgets import QWidget, QApplication, QMainWindow, QLabel, QHBoxLayout, QLineEdit, QComboBox, QPushButton, QVBoxLayout, QGridLayout

class Avtoriz2(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Автоизация")
        self.setFixedSize(500,500)

        self.lbl_0 = QLabel("Пройти тест на тему: животных ")
        self.btn_add = QPushButton("Пройти")
        self.btn_exit = QPushButton("вернутся назад")

        layout = QGridLayout()
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


        layout.addWidget(self.lbl_0, 0,0)
        layout.addWidget(self.btn_add, 2,1)
        layout.addWidget(self.btn_exit, 2,0 )
        self.btn_exit.clicked.connect(self.exit_clic)

    def exit_clic(self):
        self.close()