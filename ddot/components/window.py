from gi.repository import Gtk, PangoCairo, Pango
from . import toolbar, drawingarea
from .. import graph

class Window(Gtk.Window):
    def __init__(self):
        super().__init__(title="ddot")

        self.set_default_size(640, -1)

        box = Gtk.Box()
        box.set_orientation(Gtk.Orientation.VERTICAL)
        self.add(box)

        self.toolbar = toolbar.Toolbar()
        box.add(self.toolbar)

        self.drawingarea = Gtk.DrawingArea()
        self.drawingarea.connect("draw", self.on_draw)
        self.drawingarea.set_size_request(640, 480)
        box.add(self.drawingarea)


    def on_draw(self, area, context):
        nodes = [
            graph.Node(x=135, y=300-86.3, label="a1"),
            graph.Node(x=315, y=300-86.3, label="a2"),
            graph.Node(x=495, y=300-86.3, label="a3"),
            graph.Node(x=27, y=300-14.3, label="a11"),
            graph.Node(x=99, y=300-14.3, label="a12"),
            graph.Node(x=171, y=300-14.3, label="a13"),
            graph.Node(x=243, y=300-14.3, label="a21"),
            graph.Node(x=315, y=300-14.3, label="a22"),
            graph.Node(x=387, y=300-14.3, label="a23"),
            graph.Node(x=459, y=300-14.3, label="a31"),
            graph.Node(x=531, y=300-14.3, label="a32"),
            graph.Node(x=603, y=300-14.3, label="a33"),
            graph.Node(x=315, y=300-158.3, label="a0"),
        ]
        drawingarea.draw(area, context, nodes)
