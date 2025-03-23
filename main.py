from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
from smart_file import *

app = QApplication([])
notes = read_in_file()

window = QWidget()
window.resize(600, 400)

main_line = QHBoxLayout()

text_edit = QTextEdit()
main_line.addWidget(text_edit)

v1 = QVBoxLayout()

notutku_list_label = QLabel("Список заміток")
v1.addWidget(notutku_list_label)

note_list = QListWidget()
note_list.addItems(notes.keys())
v1.addWidget(note_list)

main_btn = QHBoxLayout()
add_note_btn = QPushButton("Створити замітку")
delete_note_btn = QPushButton("Видалити замітку")
save_note_btn = QPushButton("Зберегти замітку")
main_btn.addWidget(add_note_btn)
main_btn.addWidget(delete_note_btn)
v1.addWidget(save_note_btn)
v1.addLayout(main_btn)

tags_list_label = QLabel("Список тегів")
v1.addWidget(tags_list_label)

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
    key = note_list.currentItem().text()
    text_edit.setText(notes[key]["текст"])
    tag_list.clear()
    tag_list.addItems(notes[key]["теги"])

def add_note():
    note_name, ok = QInputDialog.getText(window, "Нова нотатка", "Введіть назву нотатки")
    if ok == True:
        notes[note_name] = {
            "текст": "",
            "теги": [

            ]
        }
        note_list.clear()
        note_list.addItems(notes)
        write_in_file(notes)


def save_note_func():
    text = text_edit.toPlainText()
    note_key = note_list.currentItem().text()
    notes[note_key]["текст"] = text
    write_in_file(notes)


def delete_func():
    note_key = note_list.currentItem().text()
    notes.pop(note_key)
    note_list.clear()
    note_list.addItems(notes)
    write_in_file(notes)

def add_tag():
    text = tag_input.text()
    note_key = note_list.currentItem().text()
    notes[note_key]["теги"].append(text)
    write_in_file(notes)
    tag_input.clear()
    tag_input.addItems(notes[note_key]["теги"])


def remove_tag():
    note_key = note_list.currentItem().text()
    selected_tag = tag_list.currentItem()

    if selected_tag:
        tag_text = selected_tag.text()
        notes[note_key]["теги"].remove(tag_text)
        write_in_file(notes)
        tag_list.clear()
        tag_list.addItems(notes[note_key]["теги"])

def search_tag():
    tag = tag_input.text()

    for note in notes:
        if tag in notes[note]["теги"]:
            note_list.addItem(note)



search_btn.clicked.connect(search_tag)
remove_tag_btn.clicked.connect(remove_tag)
add_tag_btn.clicked.connect(add_tag)
delete_note_btn.clicked.connect(delete_func)
save_note_btn.clicked.connect(save_note_func)
add_note_btn.clicked.connect(add_note)
note_list.itemClicked.connect(show_note)

window.setLayout(main_line)
window.show()
app.exec()
