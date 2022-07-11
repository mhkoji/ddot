from gi.repository import Gtk, PangoCairo, Pango

import contextlib

@contextlib.contextmanager
def save_context(context):
    try:
        context.save()
        yield
    finally:
        context.restore()

def draw_node(context, node):
    context.set_source_rgb(0, 0, 0)
    context.set_font_size(node.font_size)
    context.move_to(node.x, node.y)
    context.show_text(node.label)

def draw_graph(context, nodes):
    with save_context(context):
        for node in nodes:
            draw_node(context, node)


def draw(area, context, nodes):
    width = area.get_allocated_width()
    height = area.get_allocated_height()

    context.set_source_rgb(255, 255, 255)
    context.fill()
    context.paint()

    draw_graph(context, nodes)
