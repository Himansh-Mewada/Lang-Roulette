import tkinter as tk
from tkinter import messagebox
import random
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DICT_FILE = os.path.join(BASE_DIR, "dict.txt")
CLEANED_CSV_FILE = os.path.join(BASE_DIR, "programming_languages_cleaned.csv")


class LanguageRouletteApp:
    def __init__(self, master):
        """
        Initializes the Language Roulette GUI application.

        Args:
            master: The root Tkinter window.
        """
        self.master = master
        master.title("Programming Language Roulette")
        master.geometry("600x400") # Set a default window size
        master.resizable(True, True) # Allow window resizing

        # Create a main frame to hold all widgets
        # This frame will be configured to expand with the window
        self.main_frame = tk.Frame(master, bg="#e0e0e0") # Slightly darker background for the frame
        self.main_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        # Configure the grid for the main window to make the main_frame expandable
        # These methods are correctly called on the master (Tkinter root window)
        # to configure its grid behavior.
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)


        # Configure grid for responsive layout within the main_frame
        # These methods are now called on self.main_frame
        self.main_frame.rowconfigure(0, weight=1)    # For the language label
        self.main_frame.rowconfigure(1, weight=0)    # For the buttons
        self.main_frame.rowconfigure(2, weight=0)    # For the footer
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=1)


        self.languages = []
        self.current_language_display = tk.StringVar()
        self.current_language_display.set("Click 'Spin' to get a language!")

        self.load_languages() # Load languages on startup

        # --- GUI Elements ---

        # Label to display the selected language
        # Parented to self.main_frame
        self.language_label = tk.Label(
            self.main_frame, # Parented to main_frame
            textvariable=self.current_language_display,
            font=("Inter", 18, "bold"),
            wraplength=500, # Wrap text if it's too long
            justify="center",
            bg="#f0f0f0", # Light grey background
            fg="#333333", # Dark grey text
            relief="groove", # Give it a slight border
            bd=2,
            padx=10,
            pady=20
        )
        self.language_label.grid(row=0, column=0, columnspan=2, pady=20, padx=20, sticky="nsew")

        # Spin Button
        # Parented to self.main_frame
        self.spin_button = tk.Button(
            self.main_frame, # Parented to main_frame
            text="Spin the Wheel!",
            command=self.spin_language,
            font=("Inter", 14),
            bg="#4CAF50", # Green background
            fg="white", # White text
            activebackground="#45a049", # Darker green on click
            activeforeground="white",
            relief="raised",
            bd=3,
            padx=15,
            pady=10,
            cursor="hand2" # Change cursor on hover
        )
        self.spin_button.grid(row=1, column=0, pady=10, padx=20, sticky="ew")

        # Reset Button
        # Parented to self.main_frame
        self.reset_button = tk.Button(
            self.main_frame, # Parented to main_frame
            text="Reset Languages",
            command=self.reset_languages,
            font=("Inter", 14),
            bg="#008CBA", # Blue background
            fg="white",
            activebackground="#007bb5",
            activeforeground="white",
            relief="raised",
            bd=3,
            padx=15,
            pady=10,
            cursor="hand2"
        )
        self.reset_button.grid(row=1, column=1, pady=10, padx=20, sticky="ew")

        # Footer Label (optional, for aesthetics)
        # Parented to self.main_frame
        self.footer_label = tk.Label(
            self.main_frame, # Parented to main_frame
            text="Developed with Python Tkinter",
            font=("Inter", 10, "italic"),
            fg="#777777",
            bg="#e0e0e0" # Match main_frame background
        )
        self.footer_label.grid(row=2, column=0, columnspan=2, pady=10)

    def load_languages(self):
        """
        Loads programming languages from dict.txt into the application's memory.
        Handles cases where dict.txt might be missing or empty.
        """
        self.languages = []
        try:
            with open(DICT_FILE, "r") as file:
                for line in file:
                    self.languages.append(line.strip()) # Remove newline characters
            if not self.languages:
                self.current_language_display.set("No languages left. Click 'Reset'!")
        except FileNotFoundError:
            messagebox.showwarning(
                "File Not Found",
                f"'{DICT_FILE}' not found. Please click 'Reset Languages' to create it."
            )
            self.current_language_display.set("File missing. Click 'Reset'!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred loading languages: {e}")
            self.current_language_display.set("Error loading languages.")

    def save_languages(self):
        """
        Saves the current list of languages back to dict.txt.
        """
        try:
            with open(DICT_FILE, "w") as file:
                for lang in self.languages:
                    file.write(f"{lang}\n")
        except Exception as e:
            messagebox.showerror("Save Error", f"Could not save languages to '{DICT_FILE}': {e}")

    def spin_language(self):
        """
        Randomly selects a programming language, displays it, and removes it from the list.
        Updates the dict.txt file.
        """
        if not self.languages:
            self.current_language_display.set("No languages left! Click 'Reset' to start over.")
            messagebox.showinfo("No Languages", "All languages have been used! Please reset the list.")
            return

        # Select a random language
        selected_language = random.choice(self.languages)

        # Display the selected language
        # We want to show only the language name and description, not the number and category.
        # Assuming the format is "NUMBER CATEGORY,LANGUAGE_NAME,DESCRIPTION"
        parts = selected_language.split(',', 2) # Split by comma, max 2 splits
        if len(parts) == 3:
            # Remove the leading number and category, just show language and description
            display_text = f"{parts[1].strip()}: {parts[2].strip().strip('\"')}"
        else:
            display_text = selected_language # Fallback if format is unexpected

        self.current_language_display.set(display_text)

        # Remove the selected language from the list
        self.languages.remove(selected_language)

        # Save the updated list back to the file
        self.save_languages()

    def reset_languages(self):
        """
        Resets the dict.txt file by copying content from programming_languages_cleaned.csv.
        This effectively restores all languages.
        """
        try:
            # Ensure the source file exists
            if not os.path.exists(CLEANED_CSV_FILE):
                messagebox.showerror(
                    "Error",
                    f"Source file '{CLEANED_CSV_FILE}' not found. Cannot reset."
                )
                return

            with open(CLEANED_CSV_FILE, "r") as source_file:
                programming_languages = [line.strip() for line in source_file]

            # Remove the header row if it exists (assuming first line is header)
            if programming_languages and "Category,Language,Description" in programming_languages[0]:
                programming_languages.pop(0)

            # Write to dict.txt with numbering
            with open(DICT_FILE, "w") as dest_file:
                for i, language_info in enumerate(programming_languages):
                    # Add numbering back as per original dict.txt format
                    dest_file.write(f"{i + 1} {language_info}\n")

            self.load_languages() # Reload languages after reset
            self.current_language_display.set("Languages reset! Click 'Spin' to begin.")
            messagebox.showinfo("Reset Complete", "The list of programming languages has been reset.")
        except Exception as e:
            messagebox.showerror("Reset Error", f"An error occurred during reset: {e}")

# Main execution block
if __name__ == "__main__":
    root = tk.Tk()
    app = LanguageRouletteApp(root)
    root.mainloop()



