SublimeSuperMultiSelect
=======================

Adds a whole lot of multi-select goodness to [Sublime Text 2][1]: select previous occurence, select next word, select all blank lines, etc.


How to Use
==========

This Plugin features a lot of goodness:

* Line Commands such as "Select all blank lines"

* Select a Column (in a Tab-delimited file)

You can find most of these under the command palette.

There is also **Find Under Prev Expand**, which is like the classic find_under_expand (_Ctrl/Command - D_), but in reverse. I would have added a keybinding, but with shift it would intersect with the default **Duplicate Line**. Example OS X keybinding:

    // Find Under Previous Expand
    { "keys": ["super+shift+d"], "command": "find_under_prev_expand" },
    { "keys": ["super+k", "super+shift+d"], "command": "find_under_prev_expand_skip" },
    { "keys": ["super+shift+k", "super+shift+d"], "command": "find_under_prev_expand_skip" },

And also **Add Next Word**, e.g.:

    // Select words
    { "keys": ["super+alt+d"], "command": "add_next_word" },
    { "keys": ["super+k","super+alt+d"], "command": "add_next_word_skip" },
    { "keys": ["super+alt+k","super+alt+d"], "command": "add_next_word_skip" },

License
=======

SublimeSuperMultiSelect is released under the MIT license.

Copyright (c) 2012 Adam Johnson <me@adamj.eu>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.




[1]: http://www.sublimetext.com/2
