# Python Text-to-Speech Tool

## HaiHaiHaiiii

This is a super simple Text-to-Speech (TTS) tool built using Python and Tkinter. It allows users to input text and convert it to speech using the `espeak` command-line tool. Maybe will make it a .EXE file later on. Maybe.

## Features

- Ultra basic and ugly GUI made with Tkinter
- Real-time text-to-speech conversion!!!!!11!! (The voice is ALSO ugly)


## Requirements

- Python 3+
- Tkinter (usually included with Python)
- `espeak` (Text-to-Speech engine)

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/python-tts-tool.git
    cd python-tts-tool
    ```

2. **Install the required packages:**

    Tkinter is usually included with Python, but if it's not, you can install it using:

    ```bash
    sudo apt-get install python3-tk
    ```

3. **Install `espeak`:**

    ```bash
    sudo apt-get install espeak
    ```

## Usage

1. **Run the application:**

    ```bash
    python TTS.py
    ```

2. **Enter your text in the input field and click the "Speak" button to hear the text spoken aloud.**

## Code Explanation

The main components of the code are:

- **GUI Setup:** The GUI is created using Tkinter, with a [LabelFrame](http://_vscodecontentref_/1) for the main container, [Label](http://_vscodecontentref_/2) for instructions, [Entry](http://_vscodecontentref_/3) for text input, and [Button](http://_vscodecontentref_/4) for triggering the speech.

- **Text-to-Speech Functionality:** The [speak_thread](http://_vscodecontentref_/5) function uses [subprocess.run](http://_vscodecontentref_/6) to call `espeak` with the input text. This function is run in a separate thread to keep the GUI responsive.

- **Multithreading:** The [speaknow](http://_vscodecontentref_/7) function starts a new thread for the [speak_thread](http://_vscodecontentref_/8) function, ensuring that the GUI remains responsive during speech synthesis.

## Example

Here's a quick example of how to use the tool:

1. **Open the application:**

    ![TTS Tool GUI](screenshot.png)

2. **Enter your text:**

    ```plaintext
    Hello, this is a test of the Text-to-Speech tool.
    ```

3. **Click the "Speak" button to hear the text spoken aloud.**

## Contributing

Dude, it's a hyperbasic TTS. I'll make another with more voices another day, it's 3 am.


## Contact

For any questions or suggestions, please contact:

- Instagram = polterwine_egoz

## Acknowledgments

- The Tkinter documentation and various online tutorials
- Whoever invented caffeine pills. Thanks man.

---
