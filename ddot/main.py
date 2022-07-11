import gi
gi.require_version("Gtk", "3.0")
gi.require_version('PangoCairo', '1.0')
from gi.repository import Gtk, PangoCairo, Pango

import contextlib

@contextlib.contextmanager
def save_context(context):
    try:
        context.save()
        yield
    finally:
        context.restore()

layout = None

def draw_text(context):
    global layout
    if not layout:
        font = Pango.FontDescription()
        font.set_family("Monospace")
        layout = PangoCairo.create_layout(context)
        layout.set_text("aaa", -1)
        layout.set_font_description(font)

    with save_context(context):
        context.set_source_rgb(0, 0, 0)
        PangoCairo.show_layout(context, layout)

def draw_graph(area, context):
    width = area.get_allocated_width()
    height = area.get_allocated_height()

    context.set_source_rgb(255, 255, 255)
    context.fill()
    context.paint()

    draw_text(context)


class Window(Gtk.Window):
    def __init__(self):
        super().__init__(title="ddot")

        self.set_default_size(640, -1)

        box = Gtk.Box()
        box.set_orientation(Gtk.Orientation.VERTICAL)
        self.add(box)

        self.toolbar = Gtk.Toolbar()
        self.toolbutton_search = Gtk.ToolButton()
        self.toolbutton_search.set_label("Search")
        self.toolbutton_search.set_icon_name("gtk-search")
        self.toolbar.insert(self.toolbutton_search, 0)
        box.add(self.toolbar)

        self.drawingarea = Gtk.DrawingArea()
        self.drawingarea.connect("draw", self.on_draw)
        self.drawingarea.set_size_request(640, 480)
        box.add(self.drawingarea)


    def on_draw(self, area, context):
        draw_graph(area, context)

win = Window()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
