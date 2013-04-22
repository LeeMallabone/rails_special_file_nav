import sublime, sublime_plugin, os.path


def find_nearest_file(starting_filename, needle):
    potential_file = starting_filename

    while True:
        active_directory = os.path.split(os.path.dirname(potential_file))[0]
        potential_file = active_directory + "/" + needle

        if os.path.exists(potential_file):
            return potential_file
        if active_directory == '/':
            return None

# Starts at the current file and traverses the filesystems upwards until it hits the top.
# If it finds a file, (eg. 'Gemfile') on its way it opens that file in the editor.
def toggle_nearest_file(file_basename):
    view = sublime.active_window().active_view()
    if view.file_name().endswith(file_basename):
        sublime.active_window().run_command("close")
    else:
        discovered_file = find_nearest_file(view.file_name(), file_basename)
        if discovered_file != None:
            view.window().open_file(discovered_file, sublime.TRANSIENT)
        else:
            sublime.status_message('No ' + file_basename + ' found.')

##################################################################################
# Rails navigation commands. Add a line like this to your keyboard shortcuts file:
# { "keys": ["super+ctrl+g"],  "command": "gemfile_navigation"}
##################################################################################

class GemfileNavigationCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        toggle_nearest_file('Gemfile')

class RakefileNavigationCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        toggle_nearest_file('Rakefile')
