import sublime
import sublime_plugin
import functools
import os
import sys
pywin_dir = "pywin 64bit" if sys.maxsize > 2**32 else "pywin 32bit"
sys.path.append(os.getcwd() + "/lib")
sys.path.append(os.getcwd() + "/lib/%s" % pywin_dir)
sys.path.append(os.getcwd() + "/lib/%s/win32" % pywin_dir)
sys.path.append(os.getcwd() + "/lib/%s/win32/lib" % pywin_dir)
sys.path.append(os.getcwd() + "/lib/%s/Pythonwin" % pywin_dir)
from dragonfly import *


# -----------------------------------------------------------------------------
# Sublime commands
# -----------------------------------------------------------------------------
class SublimeCommand(ActionBase):

    def __init__(self, command, repeatable=False, **args):
        super(SublimeCommand, self).__init__()
        self.command = command
        self.repeatable = repeatable
        self.args = dict(args)

    def _execute(self, data=None):
        repeat = 1
        args = self.args
        if data:
            if self.repeatable:
                repeat = data.pop("n", 1)
            for k, v in self.args.items():
                try:
                    args[k] = v % data
                except:
                    pass
        for _ in range(repeat):
            self.run_command(self.args)


class SublimeApplicationCommand(SublimeCommand):

    def run_command(self, data):
        sublime.run_command(self.command, data)


class SublimeWindowCommand(SublimeCommand):

    def run_command(self, data):
        sublime.active_window().run_command(self.command, data)


class SublimeTextCommand(SublimeCommand):

    def run_command(self, data):
        sublime.active_window().active_view().run_command(self.command, data)


# -----------------------------------------------------------------------------
# Action functions
# -----------------------------------------------------------------------------
def status_message(phrase):
    sublime.set_timeout(functools.partial(sublime.status_message, str(phrase)), 0)


def unknown_command():
    recognizer.grammar.echo_command = False
    status_message("What was that?")


def sleep_recognizer():
    recognizer.sleep(True)
    recognizer.announce_status()


def wake_up_recognizer():
    recognizer.sleep(False)
    sublime.status_message("")


def turn_off_recognizer():
    recognizer.enable(False)
    recognizer.announce_status()


# -----------------------------------------------------------------------------
# Rules
# -----------------------------------------------------------------------------
release = Key("shift:up, ctrl:up")


class SleepRule(MappingRule):

    mapping = {
        "wake up":                              Function(wake_up_recognizer),
        "turn off":                             Function(turn_off_recognizer),
    }


class NonRepeatableRule(MappingRule):

    mapping = {
        "sleep":                                Function(sleep_recognizer),
        "turn off":                             Function(turn_off_recognizer),

        "new file":                             SublimeWindowCommand("new_file"),
        "close file":                           SublimeWindowCommand("close"),
        "new window":                           SublimeWindowCommand("new_window"),
        "close window":                         SublimeWindowCommand("close_window"),

        "default settings":                     SublimeWindowCommand("open_file", file="${packages}/Default/Preferences.sublime-settings"),
        "user settings":                        SublimeWindowCommand("open_file", file="${packages}/User/Preferences.sublime-settings"),
        "syntax settings":                      SublimeWindowCommand("open_file_settings"),
        "distraction free settings":            SublimeWindowCommand("open_file", file="${packages}/User/Distraction Free.sublime-settings"),
        "default keys":                         SublimeWindowCommand("open_file", file="${packages}/Default/Default ($platform).sublime-keymap"),
        "user keys":                            SublimeWindowCommand("open_file", file="${packages}/User/Default ($platform).sublime-keymap"),

        "switch project":                       SublimeWindowCommand("prompt_select_project"),
        "find <text>":                          SublimeWindowCommand("show_panel", panel="find") + Text("%(text)s"),
        "next":                                 SublimeWindowCommand("find_next"),
        "previous":                             SublimeWindowCommand("find_prev"),
        "all":                                  SublimeWindowCommand("find_all_under"),

        "upper case":                           SublimeTextCommand("upper_case"),
        "lower case":                           SublimeTextCommand("lower_case"),

        "console":                              SublimeWindowCommand("show_panel", panel="console", toggle=True),
        "[command] palette":                    SublimeWindowCommand("show_overlay", overlay="command_palette"),
        "goto panel":                           SublimeWindowCommand("show_overlay", overlay="goto", show_files=True),
        "goto symbols":                         SublimeWindowCommand("show_overlay", overlay="goto", text="@"),
        "minimap":                              SublimeWindowCommand("toggle_minimap"),
        "side bar":                             SublimeWindowCommand("toggle_side_bar"),
        "fullscreen":                           SublimeWindowCommand("toggle_full_screen"),
        "distraction free":                     SublimeWindowCommand("toggle_distraction_free"),

        "spell check":                          SublimeWindowCommand("toggle_setting", setting="spell_check"),
        "next misspelling":                     SublimeWindowCommand("next_misspelling"),
        "previous misspelling":                 SublimeWindowCommand("prev_misspelling"),

        "word wrap":                            SublimeWindowCommand("toggle_setting", setting="word_wrap"),
        "sort lines":                           SublimeTextCommand("sort_lines", case_sensitive=False),

        "build":                                SublimeWindowCommand("build"),
        "build [and] run":                      SublimeWindowCommand("build", variant="Run"),
        "kill":                                 SublimeWindowCommand("exec", kill=True),

        "set syntax":                           SublimeWindowCommand("show_overlay", overlay="command_palette", text="Set Syntax: "),
        "set syntax <phrase>":                  SublimeWindowCommand("show_overlay", overlay="command_palette", text="Set Syntax: %(phrase)s") + Key("enter"),

        "snippet":                              SublimeWindowCommand("show_overlay", overlay="command_palette", text="Snippet: "),
        "snippet <phrase>":                     SublimeWindowCommand("show_overlay", overlay="command_palette", text="Snippet: %(phrase)s") + Key("enter"),

        "reset font [size]":                    SublimeApplicationCommand("reset_font_size"),
        "[go to] line <n>":                     SublimeTextCommand("goto_line", line="%(n)d"),
        "comment":                              SublimeTextCommand("toggle_comment"),
        "select all":                           SublimeTextCommand("select_all"),
        "indent":                               SublimeTextCommand("reindent"),
        "(convert | translate) [to] tabs":      SublimeTextCommand("unexpand_tabs", set_translate_tabs=True),
        "(convert | translate) [to] spaces":    SublimeTextCommand("expand_tabs", set_translate_tabs=True),

        "save":                                 SublimeTextCommand("save"),
        "save as":                              SublimeTextCommand("prompt_save_as"),

        "<text>":                               Function(unknown_command)
    }

    extras = [
        Dictation("text"),
        Dictation("phrase"),
        Integer("n", 1, 9999999999),
    ]


class KeystrokeRule(MappingRule):

    exported = False

    mapping  = {
        "up [<n>]":                                 SublimeTextCommand("move", repeatable=True, by="lines", forward=False),
        "down [<n>]":                               SublimeTextCommand("move", repeatable=True, by="lines", forward=True),
        "left [<n>]":                               SublimeTextCommand("move", repeatable=True, by="characters", forward=False),
        "right [<n>]":                              SublimeTextCommand("move", repeatable=True, by="characters", forward=True),
        "page up [<n>]":                            SublimeTextCommand("move", repeatable=True, by="pages", forward=False),
        "page down [<n>]":                          SublimeTextCommand("move", repeatable=True, by="pages", forward=True),
        "up <n> (page | pages)":                    SublimeTextCommand("move", repeatable=True, by="pages", forward=False),
        "down <n> (page | pages)":                  SublimeTextCommand("move", repeatable=True, by="pages", forward=True),
        "left <n> (word | words)":                  SublimeTextCommand("move", repeatable=True, by="words", forward=False),
        "right <n> (word | words)":                 SublimeTextCommand("move", repeatable=True, by="word_ends", forward=True),
        "home":                                     SublimeTextCommand("move_to", to="bol", extend=False),
        "end":                                      SublimeTextCommand("move_to", to="eol", extend=False),
        "doc home":                                 SublimeTextCommand("move_to", to="bof", extend=False),
        "doc end":                                  SublimeTextCommand("move_to", to="eof", extend=False),

        "select <n> lines down":                    SublimeTextCommand("select_lines", repeatable=True, forward=True),
        "select <n> lines up":                      SublimeTextCommand("select_lines", repeatable=True, forward=False),
        "scroll down [<n>]":                        SublimeTextCommand("scroll_lines", repeatable=True, amount=-1),
        "scroll up [<n>]":                          SublimeTextCommand("scroll_lines", repeatable=True, amount=1),

        "find next [<n>]":                          SublimeWindowCommand("find_under_expand", repeatable=True),

        "space [<n>]":                              release + Key("space:%(n)d"),
        "enter [<n>]":                              release + Key("enter:%(n)d"),
        "tab [<n>]":                                Key("tab:%(n)d"),
        "delete [<n>]":                             release + Key("del:%(n)d"),
        "delete [<n> | this] (line|lines)":         release + Key("home, s-down:%(n)d, del"),
        "backspace [<n>]":                          release + Key("backspace:%(n)d"),
        "escape":                                   release + Key("escape"),

        "paste":                                    release + Key("c-v"),
        "duplicate <n>":                            release + Key("c-c, c-v:%(n)d"),
        "copy":                                     release + Key("c-c"),
        "cut":                                      release + Key("c-x"),
        "[hold] shift":                             Key("shift:down"),
        "release shift":                            Key("shift:up"),
        "[hold] control":                           Key("ctrl:down"),
        "release control":                          Key("ctrl:up"),
        "release [all]":                            release,

        "(say | dictate | echo) <text>":            SublimeTextCommand("insert", characters="%(text)s"),

        "(decrease | smaller) font [size]":         SublimeApplicationCommand("decrease_font_size"),
        "(increase | bigger | larger) font [size]": SublimeApplicationCommand("increase_font_size"),

        "undo":                                     SublimeTextCommand("undo"),
        "redo":                                     SublimeTextCommand("redo"),

        "next view":                                SublimeWindowCommand("next_view"),
        "previous view":                            SublimeWindowCommand("prev_view"),

        "next field":                               SublimeTextCommand("next_field"),
        "previous field":                           SublimeTextCommand("previous_field"),

        "new line":                                 SublimeTextCommand("insert", characters="\n"),
        "exclamation mark":                         SublimeTextCommand("insert", characters="!"),
        "question mark":                            SublimeTextCommand("insert", characters="?"),
        "left parenthesis":                         SublimeTextCommand("insert", characters="("),
        "right parenthesis":                        SublimeTextCommand("insert", characters=")"),
        "parentheses":                              SublimeTextCommand("insert", characters="()"),
        "left square bracket":                      SublimeTextCommand("insert", characters="["),
        "right square bracket":                     SublimeTextCommand("insert", characters="]"),
        "square brackets":                          SublimeTextCommand("insert", characters="[]"),
        "left (brace | curly bracket)":             SublimeTextCommand("insert", characters="{"),
        "right (brace | curly bracket)":            SublimeTextCommand("insert", characters="}"),
        "(braces | curly brackets)":                SublimeTextCommand("insert", characters="{}"),
        "forward slash":                            SublimeTextCommand("insert", characters="/"),
        "backward slash":                           SublimeTextCommand("insert", characters="\\"),
        "dot | period":                             SublimeTextCommand("insert", characters="."),
        "comma":                                    SublimeTextCommand("insert", characters=","),
        "ampersand":                                SublimeTextCommand("insert", characters="&"),
        "colon":                                    SublimeTextCommand("insert", characters=":"),
        "semicolon":                                SublimeTextCommand("insert", characters=";"),
        "asterisk":                                 SublimeTextCommand("insert", characters="*"),
    }

    extras   = [
                IntegerRef("n", 1, 1000),
                Dictation("text"),
               ]

    defaults = {
                "n": 1,
               }


alternatives = []
alternatives.append(RuleRef(rule=KeystrokeRule()))
single_action = Alternative(alternatives)
sequence = Repetition(single_action, min=1, max=16, name="sequence")


class RepeatRule(CompoundRule):

    spec     = "<sequence> [[[and] repeat [that]] <n> times]"
    extras   = [
                sequence,
                IntegerRef("n", 1, 100),
               ]
    defaults = {
                "n": 1,
               }

    def _process_recognition(self, node, extras):
        sequence = extras["sequence"]
        count = extras["n"]
        for i in range(count):
            for action in sequence:
                action.execute()
        release.execute()


# -----------------------------------------------------------------------------
# Grammar
# -----------------------------------------------------------------------------
class SublimeGrammar(Grammar):

    def __init__(self, name, description=None, context=None):
        super(SublimeGrammar, self).__init__(name, description, context)
        self.echo_command = True

    def on_rule_matched(self, node):
        if self.echo_command:
            status_message("Command: " + " ".join(node.words()))
        self.echo_command = True


# -----------------------------------------------------------------------------
# Recognizer
# -----------------------------------------------------------------------------
class SpeechRecognizer:

    def __init__(self):
        try:
            self.error = False
            self.context = AppContext(executable="sublime_text")
            self.grammar = SublimeGrammar("Sublime Text 2", context=self.context)
            self.main_rules = (NonRepeatableRule(), RepeatRule())
            self.sleep_rule = SleepRule()
            [self.grammar.add_rule(rule) for rule in self.main_rules]
            self.grammar.add_rule(self.sleep_rule)
            self.grammar.load()

            settings = sublime.load_settings("Speech.sublime-settings")
            state = settings.get("startup", True)
            if state == False:
                self.enable(False)
                self.sleep(False)
            elif state == "sleep":
                self.enable(True)
                self.sleep(True)
            else:
                self.enable(True)
                self.sleep(False)
        except Exception as ex:
            import traceback
            print "Exception initializing speech recognizer: ", ex
            traceback.print_exc()
            self.error = True

    def __del__(self):
        self.grammar.unload()

    def sleep(self, do_sleep):
        if self.is_enabled:
            if do_sleep:
                [rule.disable() for rule in self.main_rules]
                self.sleep_rule.enable()
            else:
                [rule.enable() for rule in self.main_rules]
                self.sleep_rule.disable()

    def is_sleeping(self):
        return self.sleep_rule.enabled

    def enable(self, do_enable):
        if do_enable:
            get_engine()._recognizer.State = 1
            self.sleep(False)
        else:
            get_engine()._recognizer.State = 0

    def is_enabled(self):
        return get_engine()._recognizer.State == 1

    def announce_status(self):
        sublime.set_timeout(self.announce_status, 1)
        if self.error:
            sublime.status_message("Speech plugin error")
        elif not self.is_enabled():
            sublime.status_message("Speech recognition off")
        elif self.is_sleeping():
            sublime.status_message("Speech recognition sleeping")
        else:
            return False
        return True


recognizer = SpeechRecognizer()
recognizer.announce_status()


class SetSpeechRecognitionModeCommand(sublime_plugin.ApplicationCommand):

    def run(self, toggle=False, enable=None, sleep=None):

        if enable is not None:
            recognizer.enable(enable)
        elif sleep is not None:
            recognizer.sleep(sleep)
        elif toggle:
            if recognizer.is_enabled() and recognizer.is_sleeping():
                recognizer.sleep(False)
            else:
                recognizer.enable(not recognizer.is_enabled())

        if not recognizer.announce_status():
            sublime.status_message("")
