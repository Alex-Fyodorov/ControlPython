from model import NoteBook
import text
import view

def search_note(pb: NoteBook):
    word = view.input_request(text.input_search_word)
    result = pb.find_note(word)
    view.show_book(result, text.not_find(word))     
    return result

def input_note_id(note_list: NoteBook, operation: str) -> int:
    note_id = int(view.input_request(operation))
    while note_id not in note_list.note_book:
        view.print_message(text.id_not_in_list)
        note_id = int(view.input_request(operation))
    return note_id        

def start():  
    nb = NoteBook()  
    nb.open_file()                
    view.print_message(text.load_successful)
    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                nb.open_file()                
                view.print_message(text.load_successful)
            case 2:
                nb.save_file()
                view.print_message(text.save_successful)
            case 3:                
                view.show_book(nb, text.empty_book_error)
            case 4:    
                view.show_book_by_date(nb, text.empty_book_error)
            case 5:
                new_note = view.input_note(text.input_note())
                nb.add_note(new_note)
                view.print_message(text.note_action(new_note.head, text.operation[0]))
            case 6:                
                search_list = search_note(nb)
                if search_list.note_book:                                        
                    note_id = input_note_id(search_list, text.input_read_note_id)
                    note = nb.note_book.get(note_id)
                    view.show_one_note(note_id, note)
            case 7:
                search_list = search_note(nb)
                if search_list.note_book:                                        
                    note_id = input_note_id(search_list, text.input_edit_note_id)
                    new_note = view.input_note(text.input_note(True))
                    head = nb.edit_note(note_id, new_note)
                    view.print_message(text.note_action(head, text.operation[1]))
            case 8:
                search_list = search_note(nb)
                if search_list.note_book:                                        
                    note_id = input_note_id(search_list, text.input_del_note_id)
                    head = nb.delete_note(note_id)
                    view.print_message(text.note_action(head, text.operation[2]))
            case 9:
                if nb.original_book.__eq__(nb.note_book):
                    if view.input_request(text.confirm_changes).lower() == 'y':
                        nb.save_file()
                        view.print_message(text.save_successful)
                view.print_message(text.exit_program)
                break            