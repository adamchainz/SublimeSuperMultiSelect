# coding=utf-8
import sublime
import sublime_plugin


class SelectColumnCommand(sublime_plugin.WindowCommand):
    def run(self, column_num):
        view = self.window.active_view()

        regex = "^([^\\t]+\\t){%i}([^\\t\\n]+){%i}" % \
                        (column_num - 1, column_num)

        found = view.find_all(regex, sublime.IGNORECASE)

        if len(found) > 0:
            edit = view.begin_edit()

            view.sel().clear()
            for f in found:
                substr = view.substr(f)
                if column_num > 1:
                    last_tab = substr.rfind("\t") + 1
                else:
                    last_tab = 0
                view.sel().add(sublime.Region(f.a + last_tab, f.b))

            view.end_edit(edit)


class SelectColumnPromptCommand(sublime_plugin.WindowCommand):

    def run(self):
        self.window.show_input_panel("Column Number:", "",
                                     self.on_done, None, None)
        pass

    def on_done(self, text):
        try:
            column_num = int(text)
        except ValueError:
            return

        if column_num < 1:
            return

        self.window.run_command("select_column", {"column_num": column_num})
