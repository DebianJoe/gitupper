gitupper
========

automate git updates

Installing
========
clone this repo  
cd to the newly created directory  
```
chmod 755 gitupper
```
with root permissions:
```
cp gitupper /usr/bin/gitupper
```
Configure
=======
gitupper parses a file located in the user's ~/gitupper/ directory, named "repos"  make changes to this file, following the provided example syntax to add git repos to gitupper's check and update functions.  

One of the primary focuses of this project is to simplify organization of multiple git repos across different installs.  The method 'git pull' may not be the best possible choice for updating a repo that you are currently working on, and as such I suggest this only for projects that you are a normal user of.  

Using
=======
use:

* gitupper -ls  
to list files included in the ~/gitupper/repos config file.

* gitupper -up  
to automatically update all directories in ~/gitupper/repos  

* gitupper -gc  
to clean/prune/fsck all directories in ~/gitupper/repos  

* gitupper -up {repo-name}  
will look for a repo tied to {repo-name} and ONLY update that one.  The {repo-name} parameter should be the name that the repo is referred to by "gitupper -ls", and is tied to values on the left side of the "repos" config file.

License
========
Copyright (c) <2013> <Joe Brock> (<DebianJoe@linuxbbq.org>)

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
