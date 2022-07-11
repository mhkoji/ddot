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

def draw_text(context):
    ops = [
        { "x": 135, "y": 86.3, "str": "a1" },
        { "x": 315, "y": 86.3, "str": "a2" },
        { "x": 495, "y": 86.3, "str": "a3" },
        { "x":  27, "y": 14.3, "str": "a11" },
        { "x":  99, "y": 14.3, "str": "a12" },
        { "x": 171, "y": 14.3, "str": "a13" },
        { "x": 243, "y": 14.3, "str": "a21" },
        { "x": 315, "y": 14.3, "str": "a22" },
        { "x": 387, "y": 14.3, "str": "a23" },
        { "x": 459, "y": 14.3, "str": "a31" },
        { "x": 531, "y": 14.3, "str": "a32" },
        { "x": 603, "y": 14.3, "str": "a33" },
        { "x": 315, "y": 158.3, "str": "a0" },
    ]
    for op in ops:
        with save_context(context):
            context.set_source_rgb(0, 0, 0)
            context.set_font_size(14.0)
            context.move_to(op["x"], 300 - op["y"])
            context.show_text(op["str"])

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
