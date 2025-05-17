#подключение библиотек
from random import randint
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
def show_winner():
    random_number = randint(1, 100)
    number.setText(str(random_number))
    text.setText('Вот столько я битков наманил ы')
#создание элементов интерфейса
app = QApplication([])
window = QWidget()
#привязка элементов к вертикальной линии
window.setWindowTitle('Симулятор травы 4к')
window.resize(500, 400)
text = QLabel('Нажми кнопку паже')
number = QLabel('?')
btn = QPushButton('Да, эту')
btn.clicked.connect(show_winner)
vline = QVBoxLayout()
vline.addWidget(text, alignment=Qt.AlignCenter)
vline.addWidget(number, alignment=Qt.AlignCenter)
vline.addWidget(btn, alignment=Qt.AlignCenter)
window.setLayout(vline)
#обработка событий

window.show()
app.exec()
#запуск приложения