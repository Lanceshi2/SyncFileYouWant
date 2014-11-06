# Sync File

A Sublime Text plugin that syncs file between two folders. This is initially designed to help copying files between local work folder and github folder for FTR lab. 

Although we already have tools like FileSync which automatically sync two folders, I do find there are situations where though two directories are quite the same, we still want to keep some files identical due to version/experiment considerations. So I introduced this relatively manual way to sync files between two folders where you can decide which files you want to sync. 

To sync a file, simply press ctrl + alt + s at the file you want to sync.

Alternatively, you can click Tools >  Sync File > Sync File

To sync multiple files, at side bar, choose multiple files, right click > Sync File

Works with Sublime Text 3 (Stable version)


## How to install ##

### Package Control ###

Install Will Bond's [Package Control](https://sublime.wbond.net/installation), and then:

* In the Command Palette, choose `Package Control: Install Package`
* Search for `Sync File` and install it

### Github ###

Go to your Sublime Text "Packages" directory (`Preferences` / `Browse Packages...`).

Then clone this GitHub repository:

    $ git clone https://github.com/Lanceshi2/SyncFile.git "Sync File"