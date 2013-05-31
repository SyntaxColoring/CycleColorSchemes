import sublime, sublime_plugin

# The color scheme cycle works as a sort of double-ended queue.  The current
# scheme in the cycle (not necessarily the scheme actually being rendered) is the
# first element in the cycled_color_schemes setting.  When the user cycles to the
# next color scheme, the entire list is rotated to the left so that the old
# scheme resides at the end of the list.  (When cycling backwards, the list is
# rotated to the right.)  

class CycleColorSchemeCommand(sublime_plugin.ApplicationCommand):
	def run(args, reverse = False):
		settings = sublime.load_settings("Preferences.sublime-settings")
		scheme_cycle = settings.get("cycled_color_schemes", [])
		if scheme_cycle: # Only attempt cycling if there is something to cycle to.
			if reverse: scheme_cycle.insert(0, scheme_cycle.pop()); # Rotate right.
			else: scheme_cycle.append(scheme_cycle.pop(0)) # Rotate left.
			settings.set("color_scheme", scheme_cycle[0])
			settings.set("cycled_color_schemes", scheme_cycle)
			sublime.save_settings("Preferences.sublime-settings")
	def is_enabled(args):
		settings = sublime.load_settings("Preferences.sublime-settings")
		scheme_cycle = settings.get("cycled_color_schemes", [])
		# Cycling only makes sense when there are at least two items in the cycle,
		# or when there is only one item but it's different from what's actually
		# being rendered.  In other words, cycling is only enabled when it could
		# change what's being displayed.
		return len(scheme_cycle) >= 2 or (scheme_cycle and settings.get("color_scheme") != scheme_cycle[0])
class AddColorSchemeCommand(sublime_plugin.ApplicationCommand):
	def run(args):
		settings = sublime.load_settings("Preferences.sublime-settings")
		scheme_cycle = settings.get("cycled_color_schemes", [])
		
		# Insert the new color scheme after the current one, if it exists.
		if (scheme_cycle): scheme_cycle.append(scheme_cycle.pop(0))
		scheme_cycle.insert(0, settings.get("color_scheme"))
		
		settings.set("cycled_color_schemes", scheme_cycle)
		sublime.save_settings("Preferences.sublime-settings")
		
class RemoveColorSchemeCommand(sublime_plugin.ApplicationCommand):
	def run(args):
		# To provide visual feedback for the command, move on to the next scheme
		# as the current one is removed from the cycle.
		sublime.run_command("cycle_color_scheme")
		
		settings = sublime.load_settings("Preferences.sublime-settings")
		scheme_cycle = settings.get("cycled_color_schemes", [])
		scheme_cycle.pop(); # Remove the scheme (now at the end of the list from the previous line) so it's not shown in the next cycle.
		
		settings.set("cycled_color_schemes", scheme_cycle)
		sublime.save_settings("Preferences.sublime-settings")
	def is_enabled(args):
		# Only show the command to remove the scheme from the cycle when it exists in the cycle in the first place.
		settings = sublime.load_settings("Preferences.sublime-settings")
		return settings.get("color_scheme") in settings.get("cycled_color_schemes", [])
