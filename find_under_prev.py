# coding=utf-8
from collections import deque
import sublime
import sublime_plugin


last_added = None


def find_under_prev(window, skip=False):
    view = window.active_view()
    sels = view.sel()

    if len(sels) == 1 and sels[0].size() == 0:
        # Just select word if we haven't got one already
        edit = view.begin_edit()
        window.run_command("find_under_expand")
        view.end_edit(edit)
    else:
        # Move to single sel, jump back one, then reselect what we had previously. A hack, for sure, but no easier way to do it.

        edit = view.begin_edit()
        try:
            wheres = deque([(i.a, i.b) for i in sels])
            window.run_command("single_selection")
            window.run_command("find_under_prev")

            if skip:
                wheres.popleft()

            for w in wheres:
                r = sublime.Region(w[0], w[1])
                view.sel().add(r)
        finally:
            view.end_edit(edit)


class FindUnderPrevExpandCommand(sublime_plugin.WindowCommand):
    def run(self):
        find_under_prev(self.window)


class FindUnderPrevExpandSkipCommand(sublime_plugin.WindowCommand):
    def run(self):
        find_under_prev(self.window, skip=True)
