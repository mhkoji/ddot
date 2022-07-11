from gi.repository import Gtk, PangoCairo, Pango

import contextlib

from .toolbar import Toolbar

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

        self.toolbar = Toolbar()
        box.add(self.toolbar)

        self.drawingarea = Gtk.DrawingArea()
        self.drawingarea.connect("draw", self.on_draw)
        self.drawingarea.set_size_request(640, 480)
        box.add(self.drawingarea)


    def on_draw(self, area, context):
        draw_graph(area, context)
