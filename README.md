SamiDict v1.0.0
Copyright © 2024 SamiDict Developers. All rights reserved.
This software is licensed under the MIT License.

SamiDict: A Simple and User-Friendly English-Persian Dictionary Application
Introduction
SamiDict is a desktop application designed to provide a user-friendly interface for translating text between English and Persian. It utilizes the Google Translator API for efficient and accurate translations.
Features
• User-friendly Interface: SamiDict boasts a clear and intuitive design with well-organized elements for easy navigation.
 Language Selection: Choose between English and Persian for translation using radio buttons.
 Text Input and Translation: Enter text into the designated input field and click the "Translate" button to generate the translation in the designated output field.
 Clear Translation Notification: Upon successful translation, a message box appears to inform the user.
 Text Clearing: Clear both the input and output fields using the "Clear" button for a fresh start.
 Application Closing: Close the application gracefully with the "Close" button.
 Text Copying: Easily copy the translated text to your clipboard using the "Copy" button for further use.
 Text Reading (Optional): Read the translated text aloud using the Text-to-Speech functionality (requires enabling speaker settings and potentially installing libraries).
 File Translation (Optional): Translate the content of an opened document (supported formats: TXT, DOCX, PDF) and save the translated version as a separate file (requires enabling additional libraries).

Installation
1. 
Clone the Repository: Clone the SamiDict repository from [placeholder_github_link] to your local machine.
2. 
Install Requirements: Install the required Python packages using pip:
pip install -r requirements.txt

Running the Application
1. 
Navigate to Project Directory: Open a terminal window and navigate to the SamiDict project directory.
2. 
Run the Main Script: Execute the main script using the following command:
python main.py

Usage
1. Launch SamiDict: The application will launch with a graphical user interface.
2. Select Language: Choose the source and target languages using the radio buttons ("EN to FA" or "FA to EN").
3. Enter Text: Type the text you want to translate into the input field.
4. Click Translate: Click the "Translate" button to initiate the translation process.
5. View Translation: The translated text will appear in the output field.
6. Optional Actions:
 Clear: Clear both input and output fields using the "Clear" button.
 Close: Close the application using the "Close" button.
 Copy: Copy the translated text to your clipboard using the "Copy" button.
 Read (Optional): Enable speakers in your system settings (if applicable) and click the "Read" button (may require additional libraries) to hear the translated text aloud.
 Open Document (Optional): Use the "File" menu option to open a document (supported formats: TXT, DOCX, PDF) for translation and saving the translated version (may require additional libraries).

Requirements
 Python 3 (https://www.python.org/downloads/)
 wxPython (https://www.wxpython.org/)
 deep_translator (https://pypi.org/project/deep-translator/) (Optional: for text-to-speech and file translation)
Optional Libraries
 pyttsx3 (https://pyttsx3.readthedocs.io/en/latest/) (for text-to-speech functionality)
 Additional libraries might be required for document translation. Refer to the dict_functions.py file for details.

We welcome contributions to improve SamiDict! Feel free to fork the repository on [placeholder_github_link] and submit pull requests.

For any questions or feedback, please reach out to [samangive@gmail.com].