import wx
from dict_functions import translate_en_to_fa
from dict_functions import translate_fa_to_en
import pyttsx3
from menubar import MenuBar


languages = ["English", "Persian"]  # Only English and Persian supported for now


class SamiDictApp(wx.Frame):
    """
    This class represents the main application window of SamiDict.

    It provides a user interface for translating text between English and Persian.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the SamiDictApp frame.

        Sets the title, size, and center position of the window.
        Creates the menu bar, panels, and UI elements for user interaction.
        Binds event handlers for button clicks.
        """
        super().__init__(*args, **kwargs)
        self.SetTitle("SamiDict")
        self.Center()
        self.SetSize((600, 500))

        panel = wx.Panel(self)
        panel.SetBackgroundColour("white")

        font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(11)

        self.menubar = MenuBar(self)
        self.SetMenuBar(self.menubar)

        my_box = wx.BoxSizer(wx.VERTICAL)

        box1 = wx.BoxSizer(wx.HORIZONTAL)
        self.rb1 = wx.RadioButton(panel, label="EN to FA", style=wx.RB_GROUP)
        self.rb1.SetName(self.rb1.GetLabel())
        self.rb1.SetFont(font)
        self.rb1.SetValue(True)
        self.rb2 = wx.RadioButton(panel, label="FA to EN")
        self.rb2.SetName(self.rb2.GetLabel())
        self.rb2.SetFont(font)
        box1.Add(self.rb1, flag=wx.EXPAND | wx.RIGHT, border=20)
        box1.Add(self.rb2, flag=wx.EXPAND | wx.LEFT, border=20)

        box2 = wx.BoxSizer(wx.HORIZONTAL)
        self.input_static = wx.StaticText(panel, label="Input")
        self.input_static.SetFont(font)

        box2.Add(self.input_static, proportion=1, flag=wx.ALL | wx.EXPAND, border=15)

        box3 = wx.BoxSizer(wx.HORIZONTAL)
        self.input_box = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
        self.input_box.SetName(self.input_static.GetLabel())
        box3.Add(self.input_box, proportion=1, flag=wx.EXPAND | wx.ALL, border=15)

        box4 = wx.BoxSizer(wx.HORIZONTAL)
        self.btn_translation = wx.Button(panel, label="Translate", size=(80, 40),
                                          style=wx.BORDER_NONE | wx.BORDER_SUNKEN)
        self.btn_translation.SetBackgroundColour(wx.Colour(0, 191, 255))
        box4.Add(self.btn_translation, flag=wx.EXPAND, proportion=1)

        box5 = wx.BoxSizer(wx.HORIZONTAL)
        self.translation_static = wx.StaticText(panel, label="Translation")
        self.translation_static.SetFont(font)
        box5.Add(self.translation_static, proportion=1, flag=wx.ALL | wx.EXPAND, border=15)

        box6 = wx.BoxSizer(wx.HORIZONTAL)
        self.translation_box = wx.TextCtrl(panel, style=wx.TE_READONLY | wx.TE_MULTILINE)
        self.translation_box.SetName(self.translation_static.GetLabel())
        box6.Add(self.translation_box, proportion=1, flag=wx.EXPAND | wx.ALL, border=15)

        box7 = wx.BoxSizer(wx.HORIZONTAL)
        self.btn_cls = wx.Button(panel, label="Clear", size=(80, 40), style=wx.BORDER_NONE | wx.BORDER_SUNKEN)
        self.btn_cls.SetForegroundColour(wx.Colour(255, 0, 0))
        self.btn_close = wx.Button(panel, label="Close", size=(80, 40), style=wx.BORDER_NONE | wx.BORDER_SUNKEN)
        self.btn_close.SetBackgroundColour(wx.Colour(255, 0, 0))
        self.btn_copy = wx.Button(panel, label="Copy", size=(80, 40), style=wx.BORDER_NONE | wx.BORDER_SUNKEN)
        self.btn_copy.SetBackgroundColour(wx.Colour(29, 29, 112))
        self.btn_read = wx.Button(panel, label="Read", size=(80, 40), style=wx.BORDER_NONE | wx.BORDER_SUNKEN)
        self.btn_read.SetBackgroundColour(wx.Colour(255, 165, 0))

        box7.Add(self.btn_read, flag=wx.EXPAND | wx.RIGHT, border=20)
        box7.Add(self.btn_copy, flag=wx.EXPAND | wx.RIGHT, border=20)
        box7.Add(self.btn_cls, flag=wx.EXPAND | wx.RIGHT, border=20)
        box7.Add(self.btn_close, flag=wx.EXPAND)

        my_box.Add(box1, flag=wx.EXPAND | wx.ALL, border=15)
        my_box.Add(box2, flag=wx.EXPAND | wx.ALL, border=15)
        my_box.Add(box3, proportion =1, flag=wx.EXPAND | wx.ALL, border=15)
        my_box.Add(box4, proportion=1, flag=wx.EXPAND | wx.ALL, border=15)
        my_box.Add(box5, flag=wx.EXPAND | wx.ALL, border=15)
        my_box.Add(box6, proportion=1, flag=wx.EXPAND | wx.ALL, border=15)
        my_box.Add(box7, proportion=1, flag=wx.EXPAND | wx.TOP, border=15)

        self.btn_cls.Bind(wx.EVT_BUTTON, self.on_clear_click)
        self.btn_close.Bind(wx.EVT_BUTTON, self.on_close_click)
        self.btn_copy.Bind(wx.EVT_BUTTON, self.on_copy_click)
        self.btn_translation.Bind(wx.EVT_BUTTON, self.on_translation_click)
        self.btn_read.Bind(wx.EVT_BUTTON, self.on_read_click)
        panel.SetSizer(my_box)

    def on_clear_click(self, event):
        """
        Clears the input and translation text boxes.
        """
        self.input_box.Clear()
        self.translation_box.Clear()

    def on_close_click(self, event):
        """
        Closes the SamiDict application window.
        """
        self.Close()

    def on_copy_click(self, event):
        """
        Copies the translated text from the translation box to the clipboard.
        """
        translation_text = self.translation_box.GetValue()
        if translation_text:
            clipboard = wx.TextDataObject()
            clipboard.SetText(translation_text)
            if wx.TheClipboard.Open():
                wx.TheClipboard.SetData(clipboard)
            wx.TheClipboard.Close()

    def on_translation_click(self, event):
        """
        Translates the input text from the input box to the translation box.
        """
        input_text = self.input_box.GetValue()
        if input_text:
            if self.rb1.GetValue():
                translated_text = translate_en_to_fa(input_text)
            else:
                translated_text = translate_fa_to_en(input_text)

            self.translation_box.Clear()
            self.translation_box.WriteText(translated_text)
            wx.MessageBox("Translation Successful!", "Message", wx.OK | wx.ICON_INFORMATION)

    def on_read_click(self, event):
        """
        Reads the translated text from the translation box aloud.
        """
        translated_text = self.translation_box.GetValue()
        if translated_text:
            engine = pyttsx3.init()
            # Optional: Set speech properties (e.g., speed, volume)
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[1].id)
            engine.setProperty('rate', 150)
            engine.say(translated_text)
            engine.runAndWait()

def main():
    """
    The main function that starts the SamiDict application.
    """
    app = wx.App()
    frame = SamiDictApp(None)
    frame.Show()
    app.MainLoop()

if __name__ == "__main__":
    main()
