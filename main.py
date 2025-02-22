from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import*


app = QApplication([])

window = QWidget()
window.resize(600, 400)


main_line = QHBoxLayout(window)


text_edit = QTextEdit()
main_line.addWidget(text_edit)


v1 = QVBoxLayout()

# Заголовок списку нотаток
v1.addWidget(QLabel("Список заміток"))


note_list = QListWidget()
v1.addWidget(note_list)


main_btn = QHBoxLayout()
add_note_btn = QPushButton("Створити замітку")
delete_note_btn = QPushButton("Видалити замітку")
save_note_btn = QPushButton("Зберегти замітку")
main_btn.addWidget(add_note_btn)
main_btn.addWidget(delete_note_btn)
v1.addWidget(save_note_btn)
v1.addLayout(main_btn)


v1.addWidget(QLabel("Список тегів"))


tag_list = QListWidget()
v1.addWidget(tag_list)


tag_input = QLineEdit()
tag_input.setPlaceholderText("Введіть тег...")
v1.addWidget(tag_input)


tag_btn_layout = QHBoxLayout()
add_tag_btn = QPushButton("Додати до замітки")
remove_tag_btn = QPushButton("Відкріпити від замітки")
tag_btn_layout.addWidget(add_tag_btn)
tag_btn_layout.addWidget(remove_tag_btn)
v1.addLayout(tag_btn_layout)

search_btn = QPushButton("Шукати замітки по тегу")
v1.addWidget(search_btn)

main_line.addLayout(v1)


window.setLayout(main_line)
window.show()
app.exec()
