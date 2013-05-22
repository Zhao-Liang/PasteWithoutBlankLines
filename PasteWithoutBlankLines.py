# Delete blank lines of clipboard and then paste

import sublime, sublime_plugin, re

class ClipboardDeleteBlankLinesPasteCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		s = sublime.get_clipboard()
		line_ending = self.view.settings().get('default_line_ending')
		if line_ending == 'windows':
			s = re.compile('\n\r').sub('',s)
			s = re.compile('\r\n\s*\r\n').sub('\r\n',s)
		elif line_ending == 'mac':
			s = re.compile('\r\r').sub('\r',s)
			s = re.compile('\r\s*\r').sub('\r',s)
		else: # unix / system
			s = re.compile('\n\n').sub('\n',s)
			s = re.compile('\n\s*\n').sub('\n',s)
		sublime.set_clipboard(s)
		self.view.run_command('paste')
