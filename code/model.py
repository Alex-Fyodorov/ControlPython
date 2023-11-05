from copy import deepcopy
from datetime import datetime
    
class Note():

    def __init__(self, head: str, body: str, date: str):        
        self.head = head
        self.body = body
        self.date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")

    def full(self):
        return f'{self.head.lower()} {self.body.lower()}'
    
    def get_str_from_date(self) -> str:   
        date = self.date     
        return f'{date.year}-{date.month}-{date.day} {date.hour}:{date.minute}:{date.second}'

class NoteBook:

    def __init__(self, note_book: dict = None, path: str = 'notes.txt'):
        self.path = path
        if note_book is None:
            self.note_book: dict[int, Note] = {}
        else: 
            self.note_book = note_book
        self.original_book = {}

    def open_file(self):        
        with open(self.path, 'r', encoding = 'UTF-8') as file:
            data = file.readlines()
        for i, note in enumerate(data, 1):
            note = note.strip().split(';')
            self.note_book[i] = Note(*note)
        self.original_book = deepcopy(self.note_book)

    def save_file(self):        
        data = []
        for note in self.note_book.values():            
            data.append(f'{note.head};{note.body};{note.date}')
        data = '\n'.join(data)
        with open(self.path, 'w', encoding = 'UTF-8') as file:
            file.write(data)

    def add_note(self, new_note: list[str]):        
        note_id = max(self.note_book) + 1
        self.note_book[note_id] = new_note

    def find_note(self, word: str):        
        result = {}
        for note_id, note in self.note_book.items():            
            if word.lower() in note.full():
                result[note_id] = note                
        return NoteBook(result)
    
    def edit_note(self, note_id: int, new_note: Note):        
        current_note = self.note_book.get(note_id)        
        head = new_note.head if new_note.head else current_note.head
        body = new_note.body if new_note.body else current_note.body
        now = datetime.now()
        date = f'{now.year}-{now.month}-{now.day} {now.hour}:{now.minute}:{now.second}'
        self.note_book[note_id] = Note(head, body, date)
        return head
    
    def delete_note(self, note_id: int) -> str:        
        return self.note_book.pop(note_id).head
    
    def max_len(self, option: str):
        result = []
        for note in self.note_book.values():
            if option == "head":
                item = note.head
            elif option == "body":
                item = note.body
            else:
                item = note.get_str_from_date()
            result.append(item)
        return len(max(result, key = len))