# SyncFileYouWant

A Sublime Text plugin that enables syncing files between two folders. This is initially designed to help copying files between local work folder and github folder for FTR lab. 

Although we already have tools like FileSync which automatically sync two folders, I do find there are situations where though two directories are quite the same, we still want to keep some files identical due to version/experiment considerations. So I introduced this relatively manual way to sync files between two folders where you can decide which files you want to sync. 

I don't see any reason it can't be used in ST2 or other OSes. But I have only tested it on ST3 and Windows. 

To enable using Sync file, you need to first config your source and dest locations at:
Preferences > Package Settings > SyncFileYouWant > Settings - User. 

I recommend you copy the settings file template from:
Preferences > Package Settings > SyncFileYouWant > Settings - Default

And add your source and dest locations based on that template. 

Source and dest locations will automatically include all their sub-folders. 

To sync a file, simply press ctrl + alt + s at the file you want to sync.

Alternatively, you can click Tools >  SyncFileYouWant > Sync File

To sync multiple files, at side bar, choose multiple files, right click > Sync File

Works with Sublime Text 3 (Stable version)


## How to install ##

### Package Control ###

Install Will Bond's [Package Control](https://sublime.wbond.net/installation), and then:

* In the Command Palette, choose `Package Control: Install Package`
* Search for `SyncFileYouWant` and install it

### Github ###

Go to your Sublime Text "Packages" directory (`Preferences` / `Browse Packages...`).

Then clone this GitHub repository:

    $ git clone https://github.com/Lanceshi2/SyncFileYouWant.git "Sync File"