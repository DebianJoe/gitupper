gitupper
========

automate git updates

Installing
========
```
clone this repo  
cd to the newly created directory  
chmod 755 gitupper
```
with root permissions:
```
cp gitupper /usr/bin/gitupper
```

Configure
=======
gitupper parses a file located in the user's ~/gitupper/ directory, named "repos"  make changes to this file, following the provided example syntax to add git repos to gitupper's check and update functions. 

Using
=======
use:

* gitupper -ls  
to list files included in the ~/gitupper/repos config file.

* gitupper -up
to automatically update all directories in ~/gitupper/repos
