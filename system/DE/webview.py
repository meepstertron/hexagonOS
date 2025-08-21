import gi
gi.require_version("Gtk", "3.0")
gi.require_version("WebKit2", "4.0")
from gi.repository import Gtk, WebKit2

win = Gtk.Window()
win.fullscreen()
win.connect("destroy", Gtk.main_quit)

webview = WebKit2.WebView()
win.add(webview)

# load HTML
webview.load_uri("file:///opt/hexagon/system/DE/html/main.html")

# disable context menu
webview.connect("context-menu", lambda w, *args: True)

# disable all keys
webview.connect("key-press-event", lambda w, e: True)
webview.connect("key-release-event", lambda w, e: True)

win.show_all()
Gtk.main()
