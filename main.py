from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import*

app = QApplication([])
window = QWidget()
window.resize(500, 500)


main_line = QHBoxLayout()

# Тут ліва частина
text_edit = QTextEdit()
main_line.addWidget(text_edit)


#Тут права частина
v1 = QVBoxLayout()

notes_list_lbl = QLabel("Список заміток")
notes_list = QListWidget()

v1.addWidget(notes_list_lbl)
v1.addWidget(notes_list)

main_line.addLayout(v1)

main_btn = QHBoxLayout()
add_note_btn = QPushButton("Створити замітку")
delete_note_btn = QPushButton("Видалити замітку")
save_note_btn = QPushButton("Зберегти замітку")
main_btn.addWidget(add_note_btn)
main_btn.addWidget(delete_note_btn)
main_btn.addWidget(save_note_btn)
main_line.addLayout(main_btn)

notes_list_lbl2 = QLabel("Список тегів")
tag_list = QListWidget()
v1.addWidget(tag_list)
v1.addWidget(notes_list_lbl2)

tag_input = QLineEdit()

window.setLayout(main_line)
window.show()
app.exec()