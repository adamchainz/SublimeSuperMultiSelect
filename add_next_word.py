import sublime
import sublime_plugin


def add_next_word(view, skip=False):
    sels = view.sel()
    last_sel = view.sel()[-1]

    edit = view.begin_edit()

    found = view.find('\\b\\w+\\b', last_sel.end(), sublime.IGNORECASE)
    if last_sel.empty() or skip:
        sels.subtract(last_sel)
    sels.add(found)

    view.end_edit(edit)


class AddNextWordCommand(sublime_plugin.WindowCommand):
    def run(self):
        add_next_word(self.window.active_view())


class AddNextWordSkipCommand(sublime_plugin.WindowCommand):
    def run(self):
        add_next_word(self.window.active_view(), skip=True)
