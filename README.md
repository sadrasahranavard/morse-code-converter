# Morse Code Converter

A bidirectional Morse code converter with CLI and GUI interfaces.

## Features

- Text to Morse Code conversion
- Morse Code to Text conversion
- Command Line Interface (CLI)
- Desktop GUI (Tkinter)
- Support for letters, numbers, and special characters
- File import/export (GUI)
- Character-by-character breakdown (CLI)
- Built-in Morse code reference table (CLI)

## Installation

```bash
git clone https://github.com/sadrasahranavard/morse-code-converter.git
cd morse-code-converter
python -m venv venv

# Windows:
venv\Scripts\activate

# Mac/Linux:
source venv/bin/activate

pip install -r requirements.txt
```

## Usage

### CLI Version
```bash
python src/cli.py
```

### GUI Version
```bash
python src/gui.py
```

## Running Tests
```bash
python -m pytest tests/ -v
```

## Project Structure
```
morse-code-converter/
├── src/
│   ├── __init__.py
│   ├── converter.py      # Core conversion logic
│   ├── cli.py            # Command-line interface
│   └── gui.py            # Desktop GUI (Tkinter)
├── tests/
│   ├── __init__.py
│   └── test_converter.py # Unit tests
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
