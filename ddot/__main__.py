import gi
gi.require_version("Gtk", "3.0")
gi.require_version('PangoCairo', '1.0')

from .components.entry import main

if __name__ == '__main__':
    main()
