import dataclasses
import random
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Note:
    code: int
    title: str
    text: str
    importance: str
    creation_time: datetime = dataclasses.field(default_factory=datetime.now)
    tags: list = dataclasses.field(default_factory=list)

    def __str__(self):
        return f"Code: {self.code} \nCreation date: {self.creation_time} \n{self.title}: {self.text}"

    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)


@dataclass
class Notebook:

    def add_note(self, title: str, text: str, importance: str):
        note = Note(
            code=random.randint(1, 1000),
            title=title,
            text=text,
            importance=importance
        )
        self.notes.append(note)

    def important_notes(self):
        return [note for note in self.notes if note.importance == "HIGH" or note.importance == "MEDIUM"]

    def tags_note_count(self):
        tags = {}
        for note in self.notes:
            for tag in note.tags:
                if tag not in tags:
                    tags[tag] = 1
                else:
                    tags[tag] += 1
        return tags
