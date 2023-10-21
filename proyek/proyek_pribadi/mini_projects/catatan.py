import tkinter as tk
import sqlite3 as sql

# jendela utama
window = tk.Tk()
window.title("Notes")
window.geometry("400x600")

# kotak teks
note_entry = tk.Text(window)
note_entry.pack()

# tombol simpan
def save_note():
    note = note_entry.get("1.0", tk.END)
    conn = sql.connect("notes.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY AUTOINCREMENT, content TEXT)")
    cursor.execute("INSERT INTO notes (content) VALUES (?)", (note,))
    conn.commit()
    conn.close()
    
save_button = tk.Button(window, text="Save Note", command=save_note)
save_button.pack()

# tombol untuk notes tersimpan
def view_notes():
    conn = sql.connect("notes.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM notes")
    notes = cursor.fetchall()
    conn.close()
    
    view_window = tk.Toplevel(window)
    view_window.title("View Notes")
    view_text = tk.Text(view_window)
    for note in notes:
        view_text.insert(tk.END, note[1] + "\n")
    view_text.pack()
    
view_button = tk.Button(window, text="View Notes", command=view_notes)
view_button.pack()

# run app
window.mainloop()
