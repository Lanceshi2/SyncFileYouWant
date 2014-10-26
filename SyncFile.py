
import sublime
import sublime_plugin
import shutil 

class SyncFileCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        settings = sublime.load_settings('SyncFile.sublime-settings')
        source1  = settings.get('sf_source_1')
        dest1    = settings.get('sf_dest_1')
        source2  = settings.get('sf_source_2')
        dest2    = settings.get('sf_dest_2')

        source3  = settings.get('sf_source_3')
        dest3    = settings.get('sf_dest_3')

        source4  = settings.get('sf_source_4')
        dest4    = settings.get('sf_dest_4')

        source5  = settings.get('sf_source_5')
        dest5    = settings.get('sf_dest_5')

        sourceFileName = self.view.file_name()
        destFileName   = sourceFileName
        
        if source1 != None and source1 != "" and dest1 != None and dest1 != "" and source1 in sourceFileName:
            destFileName = sourceFileName.replace(source1, dest1)
        elif source2 != None and source2 != "" and dest2 != None and dest2 != "" and source2 in sourceFileName:
            destFileName = sourceFileName.replace(source2, dest2)
        elif source3 != None and source3 != "" and dest3 != None and dest3 != "" and source3 in sourceFileName:
            destFileName = sourceFileName.replace(source3, dest3)
        elif source4 != None and source4 != "" and dest4 != None and dest4 != "" and source4 in sourceFileName:
            destFileName = sourceFileName.replace(source4, dest4)
        elif source5 != None and source5 != "" and dest5 != None and dest5 != "" and source5 in sourceFileName:
            destFileName = sourceFileName.replace(source5, dest5)
        else:
            msg = 'Your current file location is not in one of your source locations '
            msg += 'or the relevant dest location is empty. '
            msg += 'Please set the settings file properly and retry.'
            sublime.error_message(msg)  
            raise BaseException

        #self.view.insert(edit, 0, sourceFileName + '\n')
        #self.view.insert(edit, 0, destFileName + '\n')

        shutil.copyfile(sourceFileName, destFileName)
