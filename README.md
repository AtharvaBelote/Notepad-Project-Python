# Python Notepad Application

A lightweight Notepad application built using Python and Tkinter. This project replicates core text-editing functionalities found in standard notepad software, providing a simple and intuitive interface for everyday writing and editing tasks.

---

## Features

* **New File, Open File & Save**
* **Cut, Copy, Paste**
* **Select All (Ctrl+A support)**
* **Keyboard Shortcuts (Ctrl+N, Ctrl+O, Ctrl+S, etc.)**
* **Clean and minimal UI**

---

## Technologies Used

* **Python 3.x**
* **Tkinter (Standard Python GUI Library)**

---

## Project Structure

```
project-folder/
│
├── main.py
└── README.md
```

---

## How to Run

1. Install Python 3.x
2. Run the script:

```
python main.py
```

The Notepad application window will open immediately.

---

## Key Functionalities Explained

### 1. File Operations

* **New:** Clears the current text area.
* **Open:** Loads content from a `.txt` file.
* **Save:** Saves current modifications to the same file.

### 2. Editing Operations

Uses built-in Tkinter event bindings:

* `<<Cut>>`
* `<<Copy>>`
* `<<Paste>>`
* `<<SelectAll>>`

### 3. Keyboard Shortcuts

| Action     | Shortcut     |
| ---------- | ------------ |
| New File   | Ctrl+N       |
| Open File  | Ctrl+O       |
| Save File  | Ctrl+S       |
| Select All | Ctrl+A       |

---

## Future Enhancements (Optional)

* Dark mode
* More Keyboard shortcuts
* Font size customization
* Autosave feature
* Tabbed notes
* Spell-check integration

---

## License

This project is open-source and free to use for learning and development.
