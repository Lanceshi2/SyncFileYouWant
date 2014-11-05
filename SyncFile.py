import shutil
import sublime
import sublime_plugin

class SyncFileCommand(sublime_plugin.TextCommand):
    def run(self, edit, inputFile=None):
        settings = sublime.load_settings('SyncFile.sublime-settings')
        src_mappings = settings.get("mappings", [])
        mappings = []

        # Check if we have the correct value type
        if not isinstance(src_mappings, list):
            print("invalid value type, should be a list: %r" % src_mappings)
            return
        for mapping in src_mappings:
            
            # Check if we have the correct value types for the mappings
            if not isinstance(mapping, dict):
                print("invalid mapping type, should be a dict: %r" % mapping)
                continue
            # Check if required keys exist
            elif not all(name in mapping for name in ('source', 'dest')):
                print("required key(s) missing: %r" % mapping)
                continue
            # Check if required keys have correct value type
            elif not isinstance(mapping['source'], str) or not isinstance(mapping['dest'], str):
                print("invalid type for required key(s), should be str: %r" % mapping)
                continue
            # Check if required keys are not empty
            elif not mapping['source'] or not mapping['dest']:
                print("required key(s) empty: %r" % mapping)
                continue
            else:
                mappings.append(mapping)

        # Check if there are valid mappings
        if not mappings:
            print("No valid mappings found")
            return
        
        if inputFile == None:
            source_name = self.view.file_name()
        else:
            source_name = inputFile

        for mapping in mappings:
            if mapping['source'] in source_name and mapping['dest'] != None and mapping['dest'] != "":
                shutil.copyfile(source_name, source_name.replace(mapping['source'], mapping['dest']))
                return
        else:
            msg = 'Your current file location is not in one of your source locations '
            msg += 'or the relevant dest location is empty. '
            msg += 'Please set the settings file properly and retry.'
            sublime.error_message(msg)

class SyncWindowFileCommand(sublime_plugin.WindowCommand):
    def run(self, files):
        if files != None and type(files) is list and len(files) > 0:
            for f in files:
                self.window.active_view().run_command('sync_file', {'inputFile': f })
