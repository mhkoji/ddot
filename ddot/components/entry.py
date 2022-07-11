from gi.repository import Gtk, PangoCairo, Pango

from .window import Window

def main():
    win = Window()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
