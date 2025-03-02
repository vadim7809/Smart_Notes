from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import*
from smart_file import*


app = QApplication([])

notes = read_in_file()

window = QWidget()
window.resize(600, 400)


main_line = QHBoxLayout(window)


text_edit = QTextEdit()
main_line.addWidget(text_edit)


v1 = QVBoxLayout()


notutku_list = QLabel("Список заміток")
v1.addWidget(notutku_list)


note_list = QListWidget()
note_list.addItems(notes)
v1.addWidget(note_list)


main_btn = QHBoxLayout()
add_note_btn = QPushButton("Створити замітку")
delete_note_btn = QPushButton("Видалити замітку")
save_note_btn = QPushButton("Зберегти замітку")
main_btn.addWidget(add_note_btn)
main_btn.addWidget(delete_note_btn)
v1.addWidget(save_note_btn)
v1.addLayout(main_btn)


tags_list = QLabel("Список тегів")
v1.addWidget(tags_list)


tag_list = QListWidget()
v1.addWidget(tag_list)


tag_input = QLineEdit()

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

def show_note():
    key = notutku_list.currentItem().text()
    text_edit.setText(notes[key]["текст"])
    tag_list.clear()
    tag_list.addItems(notes[key]["теги"])

notutku_list.itemClicked.connect(show_note)
window.setLayout(main_line)
window.show()
app.exec()
