import gi
gi.require_version("Gtk", "3.0")
gi.require_version('PangoCairo', '1.0')

import gi.repository.Gtk
import gi.repository.PangoCairo

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
        font = gi.repository.Pango.FontDescription()
        font.set_family("Monospace")
        layout = gi.repository.PangoCairo.create_layout(context)
        layout.set_text("aaa", -1)
        layout.set_font_description(font)

    with save_context(context):
        context.set_source_rgb(0, 0, 0)
        gi.repository.PangoCairo.show_layout(context, layout)

def draw_graph(area, context):
    width = area.get_allocated_width()
    height = area.get_allocated_height()

    context.set_source_rgb(255, 255, 255)
    context.fill()
    context.paint()

    draw_text(context)


class Window(gi.repository.Gtk.Window):
    def __init__(self):
        super().__init__(title="Hello, Wolrd")
        # self.btn = gi.repository.Gtk.Button(label="Hello, World")
        # self.btn.connect("clicked", self.on_button_clicked)
        # self.add(self.btn)

        self.drawingarea = gi.repository.Gtk.DrawingArea()
        self.drawingarea.connect("draw", self.on_draw)
        self.add(self.drawingarea)

    def on_button_clicked(self, widget):
        print("Hello!!")

    def on_draw(self, area, context):
        draw_graph(area, context)

win = Window()
win.connect("destroy", gi.repository.Gtk.main_quit)
win.show_all()
gi.repository.Gtk.main()
