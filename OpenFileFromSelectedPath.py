import os
import sublime
import sublime_plugin


class OpenFileFromSelectedPathCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sels = self.view.sel()

		for sel in sels:
			s = self.view.substr(sel) # get the selected text as str
			
			# Get current directory, to check if file exists locally 
			current_dir = self.view.window().extract_variables()['file_path']
			local_path = current_dir + os.path.sep + s 
			
			# If file exists, open it
			if os.path.exists(local_path):
				self.view.window().open_file(local_path)
			elif os.path.exists(s):
				self.view.window().open_file(s)

			break
