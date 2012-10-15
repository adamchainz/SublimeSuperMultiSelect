# coding=utf-8
import sublime
import sublime_plugin


def select_all_lines_matching(view, regex):
    found = view.find_all(regex, sublime.IGNORECASE)

    if len(found) > 0:
        edit = view.begin_edit()

        view.sel().clear()
        for f in found:
            view.sel().add(f)

        view.end_edit(edit)


class SelectAllLinesCommand(sublime_plugin.WindowCommand):
    def run(self):
        view = self.window.active_view()
        select_all_lines_matching(view, '^.*$')


class SelectAllWordsCommand(sublime_plugin.WindowCommand):
    def run(self):
        view = self.window.active_view()
        select_all_lines_matching(view, '\\b\\w+\\b')


class SelectBlankLinesCommand(sublime_plugin.WindowCommand):
    def run(self):
        view = self.window.active_view()
        select_all_lines_matching(view, '^$')


class SelectNonBlankLinesCommand(sublime_plugin.WindowCommand):
    def run(self):
        view = self.window.active_view()
        select_all_lines_matching(view, '^.+$')


class SelectAllEmailsCommand(sublime_plugin.WindowCommand):
    # Source : http://www.regular-expressions.info/email.html
    email_re = "[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?"

    def run(self):
        view = self.window.active_view()
        select_all_lines_matching(view, self.email_re)


class SelectAllUrlsCommand(sublime_plugin.WindowCommand):
    # Source : http://mathiasbynens.be/demo/url-regex
    url_re = "(?:(?:https?|ftp)://)(?:\S+(?::\S*)?@)?(?:(?!10(?:\.\d{1,3}){3})(?!127(?:\.\d{1,3}){3})(?!169\.254(?:\.\d{1,3}){2})(?!192\.168(?:\.\d{1,3}){2})(?!172\.(?:1[6-9]|2\d|3[0-1])(?:\.\d{1,3}){2})(?:[1-9]\d?|1\d\d|2[01]\d|22[0-3])(?:\.(?:1?\d{1,2}|2[0-4]\d|25[0-5])){2}(?:\.(?:[1-9]\d?|1\d\d|2[0-4]\d|25[0-4]))|(?:(?:[a-z\\x{00a1}-\\x{ffff}0-9]+-?)*[a-z\\x{00a1}-\\x{ffff}0-9]+)(?:\.(?:[a-z\\x{00a1}-\\x{ffff}0-9]+-?)*[a-z\\x{00a1}-\\x{ffff}0-9]+)*(?:\.(?:[a-z\\x{00a1}-\\x{ffff}]{2,})))(?::\d{2,5})?(?:/[^\s]*)?"

    def run(self):
        view = self.window.active_view()
        select_all_lines_matching(view, self.url_re)
