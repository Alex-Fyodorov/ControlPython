import text
from datetime import datetime
import textwrap
from model import Note, NoteBook

def main_menu():    
    for i, item in enumerate(text.menu):
        if i == 0:
            print(item)
        else:
            print(f'\t{i}. {item}')
    while True:
        choice = input(text.input_menu)
        if choice.isdigit() and 0 < int(choice) < len(text.menu):
            return int(choice)
        else:
            print(text.input_menu_error)

def print_message(msg: str):
    print('\n' + '=' * len(msg))
    print(msg)
    print('=' * len(msg) + '\n')

def show_one_note(note_id: int, note: Note):
    date = note.get_str_from_date()
    print('\n' + '*' * (len(note.head) + len(date) + 9))
    print(f'{note_id:>3}. {note.head}  {date}')
    print(textwrap.fill(note.body, 50))
    print('\n' + '*' * (len(note.head) + len(date) + 9))               


def show_book(book: NoteBook, msg: str):      
    if book.note_book:
        print('\n' + '*' * (book.max_len("head") + book.max_len("date") + 9))
        for i, note in book.note_book.items():
            print(f'{i:>3}. {note.head:<{book.max_len("head")}}  '                  
                  f'{note.get_str_from_date():<{book.max_len("date")}}')
        print('*' * (book.max_len("head") + book.max_len("date") + 9) + '\n')
    else:
        print_message(msg)

def show_book_by_date(book: NoteBook, msg: str):      
    if book.note_book:
        print('\n' + '*' * (book.max_len("head") + book.max_len("date") + 9))
        id_list = [x for x in range(1, len(book.note_book) + 1)]        
        for j in range(len(book.note_book)):  
            min_id = id_list[0]
            min_note = book.note_book[min_id]             
            for i, note in book.note_book.items():                
                if note.date < min_note.date and i in id_list:                    
                    min_id = i                    
                    min_note = note
            id_list.remove(min_id)        
            print(f'{min_id:>3}. {min_note.head:<{book.max_len("head")}}  '
                  f'{min_note.get_str_from_date():<{book.max_len("date")}}')
        print('*' * (book.max_len("head") + book.max_len("date") + 9) + '\n')
    else:
        print_message(msg)

def input_note(msg: list[str]) -> Note: 
    head = input(msg[0])
    body = input(msg[1])
    now = datetime.now()
    date = f'{now.year}-{now.month}-{now.day} {now.hour}:{now.minute}:{now.second}'   
    return Note(head, body, date)

def input_request(msg: str) -> str:
    return input(msg)