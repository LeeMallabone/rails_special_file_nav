Rails Special File Nav
======================

A Sublime Text 2 plugin to quickly navigate to special files in a project.

The plugin searches upward from the active view's file path until it finds a specific named file. There are two commands by default, one to find a rails project's Gemfile, and another to find its Rakefile.

Installation
------------

Copy rails_special_file_nav.py to your Sublime packages/User directory (on OS X: `~/Library/Application Support/Sublime Text 2/Packages/User`), and then add keyboard shortcuts to your Sublime keyboard config:

{ "keys": ["super+ctrl+g"],  "command": "gemfile_navigation"},
{ "keys": ["super+ctrl+r"],  "command": "rakefile_navigation"}

Customizing
-----------

Edit the rails_special_file_nav.py to create your own commands, then add the keybinding above. (Or wait a while and I'll probably extend the command to be a proper suite for all the rails special files.)

License
-------

Copyright 2013 Lee Mallabone.
MIT License, see MIT-LICENSE for more.
