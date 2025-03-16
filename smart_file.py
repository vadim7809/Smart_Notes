import json


def write_in_file(data):
    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def read_in_file():
    try:

        with open ("data.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            return data

    except:
        return {}


def search_by_tag():
    tag = tag_input.text()
    if not tag:
        return
    filtered_notes = {k: v for k, v in notes.items() if tag in v["теги"]}
    note_list.clear()
    note_list.addItems(filtered_notes.keys())


def search_tag():
    tag = tag_list.text()
    if search_btn.text() == "Шукати замітки по тегу" and tag:
        notes_filtered = {}
        for note in notes:
            if tag in notes[note]["теги"]:
                notes_filtered[note] = notes[note]
    search_btn.setText("Скинути пошук")
    note_list.clear()
    tag_list.clear()
    tag_list.addItems(notes_filtered)
