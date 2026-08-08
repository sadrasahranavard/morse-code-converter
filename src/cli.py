import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.converter import MorseCodeConverter

class MorseCodeCLI:
    def __init__(self):
        self.converter = MorseCodeConverter()
    
    def display_banner(self):
        print("=" * 50)
        print("       MORSE CODE CONVERTER")
        print("=" * 50)
    
    def display_menu(self):
        print("\nMAIN MENU:")
        print("  1. Text to Morse Code")
        print("  2. Morse Code to Text")
        print("  3. Show Character Reference")
        print("  4. Exit")
        print("-" * 50)
    
    def text_to_morse_mode(self):
        print("\n" + "=" * 50)
        print("TEXT TO MORSE CODE")
        print("=" * 50)
        print("Type 'back' to return to menu, 'exit' to quit")
        
        while True:
            text = input("\nEnter text: ").strip()
            
            if text.lower() == 'back':
                break
            if text.lower() == 'exit' or text.lower() == 'quit':
                self.exit_program()
            
            if not text:
                print("Please enter some text!")
                continue
            
            result = self.converter.text_to_morse(text)
            
            if result['error']:
                print(f"Error: {result['error']}")
                continue
            
            print(f"\nOriginal: {text}")
            print(f"Morse:    {result['morse']}")
            
            # Show breakdown
            print("\nBreakdown:")
            for detail in result['details']:
                print(f"  '{detail['character']}' -> {detail['morse']}")
    
    def morse_to_text_mode(self):
        print("\n" + "=" * 50)
        print("MORSE CODE TO TEXT")
        print("=" * 50)
        print("Use dots (.) and dashes (-)")
        print("Separate letters with spaces, words with ' / '")
        print("Type 'back' to return to menu, 'exit' to quit")
        
        while True:
            morse = input("\nEnter Morse code: ").strip()
            
            if morse.lower() == 'back':
                break
            if morse.lower() == 'exit' or morse.lower() == 'quit':
                self.exit_program()
            
            if not morse:
                print("Please enter Morse code!")
                continue
            
            if not self.converter.validate_morse_input(morse):
                print("Invalid Morse code! Use only dots (.), dashes (-), spaces, and /")
                continue
            
            result = self.converter.morse_to_text(morse)
            
            if result['error']:
                print(f"Error: {result['error']}")
                continue
            
            print(f"\nMorse:    {morse}")
            print(f"Decoded:  {result['text']}")
            
            print("\nBreakdown:")
            for detail in result['details']:
                print(f"  {detail['morse']} -> '{detail['character']}'")
    
    def show_reference(self):
        print("\n" + "=" * 50)
        print("MORSE CODE REFERENCE")
        print("=" * 50)
        
        print("\nLETTERS:")
        letters = {k: v for k, v in self.converter.TEXT_TO_MORSE.items() if k.isalpha()}
        for i, (char, code) in enumerate(sorted(letters.items()), 1):
            print(f"  {char} = {code:<8}", end="")
            if i % 6 == 0:
                print()
        print()
        
        print("\nNUMBERS:")
        numbers = {k: v for k, v in self.converter.TEXT_TO_MORSE.items() if k.isdigit()}
        for i, (char, code) in enumerate(sorted(numbers.items()), 1):
            print(f"  {char} = {code:<8}", end="")
            if i % 5 == 0:
                print()
        print()
        
        input("\nPress Enter to continue...")
    
    def exit_program(self):
        """Exit the program gracefully."""
        print("\nThank you for using Morse Code Converter!")
        print("Goodbye!")
        sys.exit(0)
    
    def run(self):
        self.display_banner()
        
        while True:
            self.display_menu()
            choice = input("Select option (1-4): ").strip()
            
            if choice == '1':
                self.text_to_morse_mode()
            elif choice == '2':
                self.morse_to_text_mode()
            elif choice == '3':
                self.show_reference()
            elif choice == '4':
                self.exit_program()
            else:
                print("Invalid option! Please select 1-4.")

def main():
    cli = MorseCodeCLI()
    try:
        cli.run()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted.")
        cli.exit_program()

if __name__ == "__main__":
    main()