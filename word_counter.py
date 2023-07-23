# Quartzz Dev.

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QVBoxLayout, QFileDialog, QLabel, QWidget

def calculate_word_frequency(text):
    word_freq = {}
    words = text.split()
    for word in words:
        word = word.lower()
        word_freq[word] = word_freq.get(word, 0) + 1
    return word_freq

class WordFrequencyCounter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Qua Kelime Sayacı")
        self.setGeometry(100, 100, 500, 400)

        self.text_area = QTextEdit(self)
        self.text_area.setGeometry(10, 10, 480, 250)

        self.import_button = QPushButton("Dosya İçe Aktar", self)
        self.import_button.setGeometry(10, 270, 120, 30)
        self.import_button.clicked.connect(self.import_file)

        self.calculate_button = QPushButton("Hesapla", self)
        self.calculate_button.setGeometry(140, 270, 120, 30)
        self.calculate_button.clicked.connect(self.calculate_frequency)

        self.result_label = QLabel(self)
        self.result_label.setGeometry(10, 310, 480, 80)

        self.show()

    def import_file(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Dosya İçe Aktar", "", "Text Files (*.txt)", options=options)
        if file_path:
            with open(file_path, 'r', encoding='utf-8') as file:
                self.text_area.setPlainText(file.read())

    def calculate_frequency(self):
        text = self.text_area.toPlainText()
        word_freq = calculate_word_frequency(text)
        sorted_word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)

        result_text = "Kelime Sayıları:\n"
        for word, freq in sorted_word_freq:
            result_text += f"{word}: {freq}\n"

        with open("kelime.txt", 'w', encoding='utf-8') as result_file:
            result_file.write(result_text)

        self.result_label.setText("Rapor oluşturuldu. kelime.txt dosyasına kaydedildi.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WordFrequencyCounter()
    sys.exit(app.exec_())
