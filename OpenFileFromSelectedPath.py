import os
import sublime
import sublime_plugin


class OpenFileFromSelectedPathCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sels = self.view.sel()

        # Get current directory
        current_dir = self.view.window().extract_variables().get('file_path')
        
        for sel in sels:
            # Get the selected text as str
            s = self.view.substr(sel)

            if s:  # if str not empty
                # If we have a current dir (=the calling file is saved), try to open the path locally
                if current_dir is not None:
                    local_path = current_dir + os.path.sep + s 
                
                    # If file exists, open it
                    if os.path.isfile(local_path):
                        self.view.window().open_file(local_path)
                        continue

                # If str contains an absolute path, open the file
                if os.path.isfile(s):
                    self.view.window().open_file(s)

    def is_visible(self, *args):
        sel = self.view.sel()[0]
        return not sel.empty()


   

