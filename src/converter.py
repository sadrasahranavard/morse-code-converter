class MorseCodeConverter:
    TEXT_TO_MORSE = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....', '7': '--...',
        '8': '---..', '9': '----.',
        '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.',
        '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
        '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-',
        '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
        '$': '...-..-', '@': '.--.-.', ' ': '/'
    }
    
    MORSE_TO_TEXT = {value: key for key, value in TEXT_TO_MORSE.items()}
    
    @classmethod
    def text_to_morse(cls, text):
        if not text:
            return {'morse': '', 'details': [], 'error': 'No input provided'}
        
        morse_code = []
        details = []
        
        for char in text.upper():
            if char in cls.TEXT_TO_MORSE:
                morse_char = cls.TEXT_TO_MORSE[char]
                morse_code.append(morse_char)
                details.append({
                    'character': char,
                    'morse': morse_char,
                    'type': 'space' if char == ' ' else 'letter' if char.isalpha() else 'number' if char.isdigit() else 'special'
                })
            else:
                morse_code.append('?')
                details.append({
                    'character': char,
                    'morse': '?',
                    'type': 'unknown'
                })
        
        return {
            'morse': ' '.join(morse_code),
            'details': details,
            'error': None
        }
    
    @classmethod
    def morse_to_text(cls, morse):
        if not morse:
            return {'text': '', 'details': [], 'error': 'No input provided'}
        
        morse = morse.strip()
        words = morse.split(' / ')
        morse_chars = []
        
        for word in words:
            chars = word.split()
            morse_chars.extend(chars)
            morse_chars.append('/')
        
        morse_chars.pop()
        
        text_chars = []
        details = []
        
        for code in morse_chars:
            if code == '/':
                text_chars.append(' ')
                details.append({
                    'morse': '/',
                    'character': ' ',
                    'type': 'space'
                })
            elif code in cls.MORSE_TO_TEXT:
                char = cls.MORSE_TO_TEXT[code]
                text_chars.append(char)
                details.append({
                    'morse': code,
                    'character': char,
                    'type': 'letter' if char.isalpha() else 'number' if char.isdigit() else 'special'
                })
            else:
                text_chars.append('?')
                details.append({
                    'morse': code,
                    'character': '?',
                    'type': 'unknown'
                })
        
        return {
            'text': ''.join(text_chars),
            'details': details,
            'error': None
        }
    
    @classmethod
    def get_supported_characters(cls):
        return sorted([k for k in cls.TEXT_TO_MORSE.keys() if k != ' '])
    
    @classmethod
    def validate_morse_input(cls, morse):
        valid_chars = set('.-/ ')
        return all(char in valid_chars for char in morse)