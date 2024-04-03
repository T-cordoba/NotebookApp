import dataclasses
import random
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Note:
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"
    code: int
    title: str
    text: str
    importance: str
    creation_time: datetime = dataclasses.field(default_factory=datetime.now)
    creation_date: datetime = dataclasses.field(default_factory=datetime.now)
    tags: list = dataclasses.field(default_factory=list)

    def __str__(self):
        return f"Code: {self.code} \nCreation date: {self.creation_time} \n{self.title}: {self.text}"

    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)


@dataclass
class Notebook:
    notes: dict[int, Note] = dataclasses.field(default_factory=dict)

    def add_note(self, title: str, text: str, importance: str):
        note_code = len(self.notes) + 1
        self.notes[note_code] = Note(note_code, title, text, importance)
        return note_code

    def important_notes(self):
        return [note for note in self.notes.values() if note.importance in [Note.HIGH, Note.MEDIUM]]

    def tags_note_count(self):
        tags = {}
        for note in self.notes.values():
            for tag in note.tags:
                if tag not in tags:
                    tags[tag] = 1
                else:
                    tags[tag] += 1
        return tags
