import wx
from dict_functions import translate_en_to_fa
from dict_functions import translate_fa_to_en
import os


class MenuBar(wx.MenuBar):

    """
    This class represents the menu bar for the application. 

    It provides functionalities for opening documents and exiting the application.
    """

    def __init__(self, parent):
        """
        Initialize the MenuBar object.

        Args:
            parent (wx.Frame): The parent frame of the menu bar.
        """
        super().__init__()

        self.parent = parent

        file_menu = wx.Menu()
        file_menu.Append(wx.ID_OPEN, "&Open Document\tCtrl+O", "Open a Document to translate")
        file_menu.Append(wx.ID_EXIT, "Exit")

        self.Append(file_menu, "File")

        self.Bind(wx.EVT_MENU, self.on_exit, id=wx.ID_EXIT)
        self.Bind(wx.EVT_MENU, self.OnOpenDocument, id=wx.ID_OPEN)

    def on_exit(self, event):
        """
        Handle the 'Exit' menu option event.

        Closes the application window.
        """
        self.Close()

    def OnOpenDocument(self, event):
        """
        Handle the 'Open Document' menu option event.

        Opens a file dialog for selecting a document to translate.
        If a document is selected, translates its content and saves the translated version.
        """
        with wx.FileDialog(self, "Select Document", wildcard="*.txt;*.docx;*.pdf",
                                 style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as dlg:
            if dlg.ShowModal() == wx.ID_OK:
                filepath = dlg.GetPath()
                self.TranslateAndSaveFile(filepath, self.parent)

    def TranslateAndSaveFile(self, filepath, parent):
        """
        Translates the content of a specified file and saves the translated version.

        Args:
            filepath (str): The path to the document file.
            parent (wx.Frame): The parent frame of the application.
        """
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                file_content = f.read()

                if parent.rb1.GetValue():  # Assuming rb1 refers to a radio button for English to Persian translation
                    translated_text = translate_en_to_fa(file_content)
                else:
                    translated_text = translate_fa_to_en(file_content)

            documents_dir = os.path.join(os.path.dirname(__file__), "Documents")
            if not os.path.exists(documents_dir):
                os.makedirs(documents_dir)

            filename, ext = os.path.splitext(os.path.basename(filepath))
            translated_filepath = os.path.join(documents_dir, filename + "_fa" + ext)

            with open(translated_filepath, 'w', encoding='utf-8') as f:
                f.write(translated_text)

            wx.MessageBox("Translation Successful!", "Message", wx.OK | wx.ICON_INFORMATION)

        except Exception as e:
            print(e)
            wx.MessageBox("Error occurred during translation!", "Error", wx.OK | wx.ICON_ERROR)
