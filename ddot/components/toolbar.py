from gi.repository import Gtk

class Toolbar(Gtk.Toolbar):
    def __init__(self):
        super().__init__()
        self.search = Gtk.ToolButton()
        self.search.set_label("Search")
        self.search.set_icon_name("gtk-search")
        self.insert(self.search, 0)
