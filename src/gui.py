import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, filedialog
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.converter import MorseCodeConverter

class MorseCodeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Morse Code Converter")
        self.root.geometry("800x600")
        self.converter = MorseCodeConverter()
        
        self.colors = {
            'bg': '#2b2b2b',
            'fg': '#ffffff',
            'accent': '#00ff00',
            'secondary': '#404040'
        }
        
        self.root.configure(bg=self.colors['bg'])
    
        self.conversion_mode = tk.StringVar(value="text_to_morse")
        
        self.setup_ui()
    
    def setup_ui(self):
        main_frame = tk.Frame(self.root, bg=self.colors['bg'])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        title_label = tk.Label(
            main_frame,
            text="MORSE CODE CONVERTER",
            font=("Arial", 20, "bold"),
            bg=self.colors['bg'],
            fg=self.colors['accent']
        )
        title_label.pack(pady=10)
   
        mode_frame = tk.Frame(main_frame, bg=self.colors['bg'])
        mode_frame.pack(pady=10)
        
        tk.Radiobutton(
            mode_frame,
            text="Text to Morse",
            variable=self.conversion_mode,
            value="text_to_morse",
            command=self.clear_all,
            bg=self.colors['bg'],
            fg=self.colors['fg'],
            selectcolor=self.colors['secondary'],
            font=("Arial", 11)
        ).pack(side=tk.LEFT, padx=20)
        
        tk.Radiobutton(
            mode_frame,
            text="Morse to Text",
            variable=self.conversion_mode,
            value="morse_to_text",
            command=self.clear_all,
            bg=self.colors['bg'],
            fg=self.colors['fg'],
            selectcolor=self.colors['secondary'],
            font=("Arial", 11)
        ).pack(side=tk.LEFT, padx=20)
        
        input_label = tk.Label(
            main_frame,
            text="INPUT:",
            font=("Arial", 12, "bold"),
            bg=self.colors['bg'],
            fg=self.colors['fg']
        )
        input_label.pack(anchor=tk.W, pady=(10, 5))
        
        self.input_text = scrolledtext.ScrolledText(
            main_frame,
            height=6,
            font=("Courier", 11),
            bg=self.colors['secondary'],
            fg=self.colors['fg'],
            insertbackground=self.colors['fg']
        )
        self.input_text.pack(fill=tk.X, pady=5)
        
        self.convert_btn = tk.Button(
            main_frame,
            text="CONVERT",
            command=self.perform_conversion,
            font=("Arial", 12, "bold"),
            bg=self.colors['accent'],
            fg=self.colors['bg'],
            padx=30,
            pady=10,
            cursor="hand2"
        )
        self.convert_btn.pack(pady=15)
        
        output_label = tk.Label(
            main_frame,
            text="OUTPUT:",
            font=("Arial", 12, "bold"),
            bg=self.colors['bg'],
            fg=self.colors['fg']
        )
        output_label.pack(anchor=tk.W, pady=(10, 5))
        
        self.output_text = scrolledtext.ScrolledText(
            main_frame,
            height=6,
            font=("Courier", 11),
            bg=self.colors['secondary'],
            fg=self.colors['accent'],
            insertbackground=self.colors['fg']
        )
        self.output_text.pack(fill=tk.X, pady=5)
        
        button_frame = tk.Frame(main_frame, bg=self.colors['bg'])
        button_frame.pack(pady=10)
        
        tk.Button(
            button_frame,
            text="Clear",
            command=self.clear_all,
            bg=self.colors['secondary'],
            fg=self.colors['fg'],
            padx=15
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            button_frame,
            text="Copy Result",
            command=self.copy_result,
            bg=self.colors['secondary'],
            fg=self.colors['fg'],
            padx=15
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            button_frame,
            text="Load File",
            command=self.load_file,
            bg=self.colors['secondary'],
            fg=self.colors['fg'],
            padx=15
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            button_frame,
            text="Save Result",
            command=self.save_result,
            bg=self.colors['secondary'],
            fg=self.colors['fg'],
            padx=15
        ).pack(side=tk.LEFT, padx=5)
        
        self.status_label = tk.Label(
            main_frame,
            text="Ready",
            bg=self.colors['secondary'],
            fg=self.colors['fg'],
            anchor=tk.W
        )
        self.status_label.pack(fill=tk.X, pady=(10, 0))
    
    def perform_conversion(self):
        input_text = self.input_text.get("1.0", tk.END).strip()
        
        if not input_text:
            messagebox.showwarning("Warning", "Please enter text to convert!")
            return
        
        mode = self.conversion_mode.get()
        
        if mode == "text_to_morse":
            result = self.converter.text_to_morse(input_text)
            output = result['morse']
        else:
            if not self.converter.validate_morse_input(input_text):
                messagebox.showerror("Error", "Invalid Morse code input!")
                return
            result = self.converter.morse_to_text(input_text)
            output = result['text']
        
        if result['error']:
            messagebox.showerror("Error", result['error'])
            return
        
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert("1.0", output)
        self.status_label.config(text="Conversion complete!")
    
    def clear_all(self):
        self.input_text.delete("1.0", tk.END)
        self.output_text.delete("1.0", tk.END)
        self.status_label.config(text="Cleared")
    
    def copy_result(self):
        output = self.output_text.get("1.0", tk.END).strip()
        if output:
            self.root.clipboard_clear()
            self.root.clipboard_append(output)
            self.status_label.config(text="Result copied to clipboard!")
        else:
            messagebox.showwarning("Warning", "No result to copy!")
    
    def load_file(self):
        filename = filedialog.askopenfilename(
            title="Select file",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        
        if filename:
            try:
                with open(filename, 'r') as file:
                    content = file.read()
                self.input_text.delete("1.0", tk.END)
                self.input_text.insert("1.0", content)
                self.status_label.config(text=f"Loaded: {filename}")
            except Exception as e:
                messagebox.showerror("Error", f"Could not read file: {e}")
    
    def save_result(self):
        output = self.output_text.get("1.0", tk.END).strip()
        if not output:
            messagebox.showwarning("Warning", "No result to save!")
            return
        
        filename = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        
        if filename:
            try:
                with open(filename, 'w') as file:
                    file.write(output)
                self.status_label.config(text=f"Saved to: {filename}")
                messagebox.showinfo("Success", "File saved successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Could not save file: {e}")

def main():
    root = tk.Tk()
    app = MorseCodeGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()