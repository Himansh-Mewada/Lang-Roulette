# Programming Language Roulette 🎲

A fun and educational desktop application that randomly selects programming languages to help you discover new technologies and expand your programming horizons!

## 🎯 What is Programming Language Roulette?

Programming Language Roulette is a Python GUI application built with Tkinter that randomly selects programming languages from a curated list of 55+ languages across different categories. It's perfect for:

- **Learning new technologies**: Discover languages you've never heard of
- **Breaking out of comfort zones**: Challenge yourself with unfamiliar paradigms
- **Educational purposes**: Great for coding bootcamps, workshops, or personal learning
- **Decision making**: Can't decide what to learn next? Let the roulette decide!

## 🎮 Features

- **Random Selection**: Spin the wheel to get a random programming language
- **Detailed Descriptions**: Each language comes with its use cases and strengths
- **No Repeats**: Languages are removed after selection to avoid duplicates
- **Easy Reset**: Restore all languages with a single click
- **Responsive Design**: Clean, modern GUI that adapts to window resizing
- **55+ Languages**: Comprehensive collection across multiple categories
- **Standalone Executable**: No need to install Python - runs directly on Windows!

## 🗂️ Language Categories

The application includes languages from these categories:

- **General-purpose & Widely Used**: Python, JavaScript, Java, C#, C++, Go, Rust, etc.
- **Data Science & AI & Math**: Python, R, Julia, MATLAB, Octave
- **Web Development**: JavaScript, TypeScript, HTML/CSS, PHP, Ruby, Elixir
- **Functional & Academic**: Haskell, OCaml, F#, Erlang, Clojure, Coq
- **Mobile & Cross-platform**: Swift, Kotlin, Dart, React Native, Xamarin
- **Scripting & Automation**: Bash, PowerShell, Python, Go, Perl
- **Domain-Specific**: SQL, VHDL/Verilog, OpenCL/GLSL, Q#, Assembly

## 🚀 Getting Started

### 📦 Option 1: Download the Executable (Recommended)

**For Windows Users:**
1. Download the latest release from the `dist/` folder
2. Extract the files to your desired location
3. Run `main.exe` - no installation required!

**What's included in the executable:**
- Standalone application (no Python installation needed)
- All language data files bundled
- Complete GUI interface
- Automatic file handling

### 🐍 Option 2: Run from Source Code

**Prerequisites:**
- Python 3.6 or higher
- Tkinter (usually comes with Python)

**Installation:**
1. **Clone or download** the repository
2. **Ensure all files are in the same directory**
3. **Run the application**:
   ```bash
   python main.py
   ```

## 🎲 How to Use

1. **Launch the application**:
   - **Executable**: Double-click `main.exe`
   - **Source**: Run `python main.py`
2. **Click "Spin the Wheel!"** to randomly select a programming language
3. **Read the description** to learn about the selected language
4. **Continue spinning** to discover more languages
5. **Click "Reset Languages"** when you've gone through all languages

## 📁 Project Structure

```
Programming-Language-Roulette/
├── main.py                           # Main application source code
├── dict.txt                          # Current list of available languages
├── programming_languages_cleaned.csv # Master list for reset functionality
├── main.spec                         # PyInstaller specification file
├── build/                           # Build artifacts (PyInstaller)
│   └── main/                        # Temporary build files
├── dist/                            # Distribution folder
│   └── main/                        # Executable and dependencies
│       ├── main.exe                 # Standalone executable
│       ├── dict.txt                 # Language data
│       ├── programming_languages_cleaned.csv
│       └── [other dependencies]     # Required libraries
└── README.md                        # This file
```

### File & Folder Descriptions

- **`main.py`**: The main Python application with GUI and game logic
- **`dict.txt`**: Working file that tracks remaining languages (gets modified during gameplay)
- **`programming_languages_cleaned.csv`**: Master reference file used to reset the language list
- **`main.spec`**: PyInstaller configuration file for building the executable
- **`build/`**: Temporary build artifacts created by PyInstaller (can be deleted)
- **`dist/`**: Contains the final executable and all required files
- **`dist/main/main.exe`**: The standalone Windows executable
- **`README.md`**: Documentation and usage instructions

## 🔧 Building the Executable

If you want to build the executable yourself:

### Prerequisites
```bash
pip install pyinstaller
```

### Build Commands
```bash
# Create the executable
pyinstaller main.spec

# Or build from scratch
pyinstaller --onedir --windowed --add-data "dict.txt;." --add-data "programming_languages_cleaned.csv;." main.py
```

### Build Process
1. **PyInstaller** analyzes the Python script and its dependencies
2. **Creates** a standalone executable in the `dist/` folder
3. **Bundles** all required files and libraries
4. **Includes** data files (dict.txt and CSV) automatically

## 🎨 Application Interface

The application features a clean, modern interface with:
- **Large display area** for selected programming languages
- **Prominent "Spin the Wheel!" button** for easy interaction
- **"Reset Languages" button** for starting over
- **Responsive design** that adapts to window resizing
- **Professional styling** with modern colors and fonts

## 🛠️ Technical Details

- **Built with**: Python 3.x and Tkinter
- **Packaged with**: PyInstaller for standalone distribution
- **Architecture**: Object-oriented design with clean separation of concerns
- **File I/O**: Automatic saving/loading of language state
- **Error Handling**: Graceful handling of missing files and edge cases
- **Cross-platform**: Source code runs on Windows, macOS, and Linux
- **Distribution**: Windows executable available in `dist/` folder

## 🎯 Use Cases

### For Educators
- **Programming Workshops**: Assign random languages for exploration exercises
- **Coding Bootcamps**: Help students discover diverse programming paradigms
- **Computer Science Classes**: Introduce students to the breadth of programming languages

### For Self-Learning
- **Skill Diversification**: Push yourself to learn unfamiliar technologies
- **Career Development**: Explore languages relevant to different career paths
- **Hobby Projects**: Get inspiration for your next side project

### For Teams
- **Team Building**: Group challenges with randomly assigned languages
- **Hackathons**: Add an element of surprise to coding competitions
- **Learning Sessions**: Structured exploration of new technologies

## 📋 System Requirements

### For Executable Version
- **Operating System**: Windows 10 or later
- **Memory**: 50MB free space
- **No additional software required**

### For Source Code Version
- **Python**: 3.6 or higher
- **Tkinter**: Usually included with Python
- **Operating System**: Windows, macOS, or Linux

## 🤝 Contributing

Want to improve the application? Here are some ways to contribute:

1. **Add more languages**: Update the CSV file with additional programming languages
2. **Improve descriptions**: Enhance the language descriptions for clarity
3. **UI/UX improvements**: Suggest or implement interface enhancements
4. **Cross-platform builds**: Help create macOS and Linux executables
5. **Feature requests**: Propose new features like filtering by category
6. **Bug reports**: Report any issues you encounter

## 🚀 Distribution

### For End Users
- Download the executable from `dist/main/`
- No Python installation required
- Run directly on Windows

### For Developers
- Access source code in the root directory
- Modify and rebuild using PyInstaller
- Contribute improvements via pull requests

## 📝 License

This project is open source and available under the MIT License.

## 🔮 Future Enhancements

Potential improvements for future versions:
- **Cross-platform executables** (macOS, Linux)
- **Category filtering** (e.g., show only web development languages)
- **Difficulty levels** (beginner, intermediate, advanced)
- **Language popularity indicators**
- **Links to learning resources**
- **Export functionality** for selected languages
- **Dark mode theme** option
- **Auto-updater** for the executable version

## 🎉 Have Fun!

Programming Language Roulette is designed to make discovering new programming languages fun and engaging. Whether you're a beginner looking to expand your horizons or an experienced developer wanting to explore new territories, spin the wheel and see where your coding journey takes you!

### Quick Start
1. **Download**: Get `main.exe` from the `dist/main/` folder
2. **Run**: Double-click to launch (no installation needed!)
3. **Spin**: Click "Spin the Wheel!" to discover a new language
4. **Learn**: Read about the language and consider exploring it further

---

*Happy coding! 🚀*