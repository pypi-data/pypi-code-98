# Copyright 2014 OpenStack Foundation
# Copyright 2014 Hewlett-Packard Development Company, L.P.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import re

import urwid

# urwid command map:
REDRAW_SCREEN = urwid.REDRAW_SCREEN
CURSOR_UP = urwid.CURSOR_UP
CURSOR_DOWN = urwid.CURSOR_DOWN
CURSOR_LEFT = urwid.CURSOR_LEFT
CURSOR_RIGHT = urwid.CURSOR_RIGHT
CURSOR_PAGE_UP = urwid.CURSOR_PAGE_UP
CURSOR_PAGE_DOWN = urwid.CURSOR_PAGE_DOWN
CURSOR_MAX_LEFT = urwid.CURSOR_MAX_LEFT
CURSOR_MAX_RIGHT = urwid.CURSOR_MAX_RIGHT
ACTIVATE = urwid.ACTIVATE
# Global hubtty commands:
KILL = 'kill'
YANK = 'yank'
YANK_POP = 'yank pop'
PREV_SCREEN = 'previous screen'
TOP_SCREEN = 'top screen'
HELP = 'help'
QUIT = 'quit'
PR_SEARCH = 'pull request search'
REFINE_PR_SEARCH = 'refine pull request search'
LIST_HELD = 'list held pull requests'
# Pull requests screen:
TOGGLE_REVIEWED = 'toggle reviewed'
TOGGLE_HIDDEN = 'toggle hidden'
TOGGLE_STARRED = 'toggle starred'
TOGGLE_HELD = 'toggle held'
TOGGLE_MARK = 'toggle process mark'
REVIEW = 'review'
DIFF = 'diff'
LOCAL_CHECKOUT = 'local checkout'
LOCAL_CHERRY_PICK = 'local cherry pick'
SEARCH_RESULTS = 'search results'
NEXT_PR = 'next pull request'
PREV_PR = 'previous pull request'
TOGGLE_HIDDEN_COMMENTS = 'toggle hidden comments'
CLOSE_PR = 'close pull request'
REOPEN_PR = 'reopen pull request'
REBASE_PR = 'rebase pull request'
REFRESH = 'refresh'
EDIT_LABELS = 'edit labels'
EDIT_PULL_REQUEST = 'edit pull request'
MERGE_PR = 'merge pull request'
SORT_BY_NUMBER = 'sort by number'
SORT_BY_UPDATED = 'sort by updated'
SORT_BY_LAST_SEEN = 'sort by last seen'
SORT_BY_REVERSE = 'reverse the sort'
# Repository list screen:
TOGGLE_LIST_REVIEWED = 'toggle list reviewed'
TOGGLE_LIST_SUBSCRIBED = 'toggle list subscribed'
TOGGLE_SUBSCRIBED = 'toggle subscribed'
NEW_REPOSITORY_TOPIC = 'new repository topic'
DELETE_REPOSITORY_TOPIC = 'delete repository topic'
MOVE_REPOSITORY_TOPIC = 'move to repository topic'
COPY_REPOSITORY_TOPIC = 'copy to repository topic'
REMOVE_REPOSITORY_TOPIC = 'remove from repository topic'
RENAME_REPOSITORY_TOPIC = 'rename repository topic'
# Diff screens:
# SELECT_PATCHSETS = 'select patchsets'
NEXT_SELECTABLE = 'next selectable'
PREV_SELECTABLE = 'prev selectable'
NEXT_COMMIT = 'next commit'
PREV_COMMIT = 'prev commit'
INTERACTIVE_SEARCH = 'interactive search'
# Special:
FURTHER_INPUT = 'further input'

DEFAULT_KEYMAP = {
    REDRAW_SCREEN: 'ctrl l',
    CURSOR_UP: 'up',
    CURSOR_DOWN: 'down',
    CURSOR_LEFT: 'left',
    CURSOR_RIGHT: 'right',
    CURSOR_PAGE_UP: ['page up', 'meta v'],
    CURSOR_PAGE_DOWN: ['page down', 'ctrl v'],
    CURSOR_MAX_LEFT: ['home', 'ctrl a'],
    CURSOR_MAX_RIGHT: ['end', 'ctrl e'],
    ACTIVATE: 'enter',
    KILL: 'ctrl k',
    YANK: 'ctrl y',
    YANK_POP: 'meta y',

    PREV_SCREEN: 'esc',
    TOP_SCREEN: 'meta home',
    HELP: ['f1', '?'],
    QUIT: ['ctrl q'],
    PR_SEARCH: 'ctrl o',
    REFINE_PR_SEARCH: 'meta o',
    LIST_HELD: 'f12',

    TOGGLE_REVIEWED: 'v',
    TOGGLE_HIDDEN: 'k',
    TOGGLE_STARRED: '*',
    TOGGLE_HELD: '!',
    TOGGLE_MARK: '%',
    REVIEW: 'r',
    DIFF: 'd',
    LOCAL_CHECKOUT: 'c',
    LOCAL_CHERRY_PICK: 'x',
    SEARCH_RESULTS: 'u',
    NEXT_PR: 'n',
    PREV_PR: 'p',
    TOGGLE_HIDDEN_COMMENTS: 't',
    CLOSE_PR: 'meta c',
    REOPEN_PR: 'ctrl e',
    REBASE_PR: 'ctrl b',
    REFRESH: 'ctrl r',
    EDIT_LABELS: 'meta l',
    EDIT_PULL_REQUEST: 'ctrl d',
    MERGE_PR: 'meta m',
    SORT_BY_NUMBER: [['S', 'n']],
    SORT_BY_UPDATED: [['S', 'u']],
    SORT_BY_LAST_SEEN: [['S', 's']],
    SORT_BY_REVERSE: [['S', 'r']],

    TOGGLE_LIST_REVIEWED: 'l',
    TOGGLE_LIST_SUBSCRIBED: 'L',
    TOGGLE_SUBSCRIBED: 's',
    NEW_REPOSITORY_TOPIC: [['T', 'n']],
    DELETE_REPOSITORY_TOPIC: [['T', 'delete']],
    MOVE_REPOSITORY_TOPIC: [['T', 'm']],
    COPY_REPOSITORY_TOPIC: [['T', 'c']],
    REMOVE_REPOSITORY_TOPIC: [['T', 'D']],
    RENAME_REPOSITORY_TOPIC: [['T', 'r']],

    # SELECT_PATCHSETS: 'p',
    NEXT_SELECTABLE: 'tab',
    PREV_SELECTABLE: 'shift tab',
    NEXT_COMMIT: '>',
    PREV_COMMIT: '<',
    INTERACTIVE_SEARCH: 'ctrl s',
}

# Hi vi users!  Add more things here!  This overrides the default
# keymap, so anything not defined here will just use what's defined
# above.
VI_KEYMAP = {
    QUIT: [[':', 'q'], 'ctrl q'],
    CURSOR_LEFT: ['h', 'left'],
    CURSOR_DOWN: ['j', 'down'],
    CURSOR_UP: ['k', 'up'],
    CURSOR_RIGHT: ['l', 'right'],
    CURSOR_PAGE_UP: ['ctrl u', 'page up'],
    # 'ctrl d' mapping conflicts with EDIT_PULL_REQUEST
    CURSOR_PAGE_DOWN: ['ctrl d', 'page down'],
    # The `gg` repetition doesn't seem to work, we bind `g` instead
    CURSOR_MAX_LEFT: ['g', '^', 'home', 'ctrl a'],
    CURSOR_MAX_RIGHT: ['G', '$', 'end'],
    INTERACTIVE_SEARCH: '/',
    TOGGLE_REVIEWED: [['t', 'r']],
    TOGGLE_HIDDEN: [['t', 'h']],
    TOGGLE_LIST_REVIEWED: [['t', 'R']],
    TOGGLE_LIST_SUBSCRIBED: 'L',

    EDIT_PULL_REQUEST: 'ctrl e',
}

URWID_COMMANDS = frozenset((
    urwid.REDRAW_SCREEN,
    urwid.CURSOR_UP,
    urwid.CURSOR_DOWN,
    urwid.CURSOR_LEFT,
    urwid.CURSOR_RIGHT,
    urwid.CURSOR_PAGE_UP,
    urwid.CURSOR_PAGE_DOWN,
    urwid.CURSOR_MAX_LEFT,
    urwid.CURSOR_MAX_RIGHT,
    urwid.ACTIVATE,
    KILL,
    YANK,
    YANK_POP,
))

FORMAT_SUBS = (
    (re.compile('ctrl '), 'CTRL-'),
    (re.compile('meta '), 'META-'),
    (re.compile('f(\d+)'), 'F\\1'),
    (re.compile('([a-z][a-z]+)'), lambda x: x.group(1).upper()),
    )

def formatKey(key):
    if type(key) == type([]):
        return  ''.join([formatKey(k) for k in key])
    for subre, repl in FORMAT_SUBS:
        key = subre.sub(repl, key)
    return key

class Key(object):
    def __init__(self, key):
        self.key = key
        self.keys = {}
        self.commands = []

    def addKey(self, key):
        if key not in self.keys:
            self.keys[key] = Key(key)
        return self.keys[key]

    def __repr__(self):
        return '%s %s %s' % (self.__class__.__name__, self.key, self.keys.keys())

class KeyMap(object):
    def __init__(self, config):
        # key -> [commands]
        self.keytree = Key(None)
        self.commandmap = {}
        self.multikeys = ''
        self.update(DEFAULT_KEYMAP)
        self.update(config)

    def update(self, config):
        # command -> [keys]
        for command, keys in config.items():
            if command == 'name':
                continue
            command = command.replace('-', ' ')
            if type(keys) != type([]):
                keys = [keys]
            self.commandmap[command] = keys
        self.keytree = Key(None)
        for command, keys in self.commandmap.items():
            for key in keys:
                if isinstance(key, list):
                    # This is a command series
                    tree = self.keytree
                    for i, innerkey in enumerate(key):
                        tree = tree.addKey(innerkey)
                        if i+1 == len(key):
                            tree.commands.append(command)
                else:
                    tree = self.keytree.addKey(key)
                    tree.commands.append(command)

    def getCommands(self, keys):
        if not keys:
            return []
        tree = self.keytree
        for key in keys:
            tree = tree.keys.get(key)
            if not tree:
                return []
        ret = tree.commands[:]
        if tree.keys:
            ret.append(FURTHER_INPUT)
        return ret

    def getFurtherCommands(self, keys):
        if not keys:
            return []
        tree = self.keytree
        for key in keys:
            tree = tree.keys.get(key)
            if not tree:
                return []
        return self._getFurtherCommands('', tree)

    def _getFurtherCommands(self, keys, tree):
        if keys:
            ret = [(formatKey(keys), tree.commands[:])]
        else:
            ret = []
        for subtree in tree.keys.values():
            ret.extend(self._getFurtherCommands(keys + subtree.key, subtree))
        return ret

    def getKeys(self, command):
        return self.commandmap.get(command, [])

    def updateCommandMap(self):
        "Update the urwid command map with this keymap"
        for key in self.keytree.keys.values():
            for command in key.commands:
                if command in URWID_COMMANDS:
                    urwid.command_map[key.key]=command

    def formatKeys(self, command):
        keys = self.getKeys(command)
        keys = [formatKey(k) for k in keys]
        return ' or '.join(keys)
