# Multi-Package Installer
This program is a simple way to install multiple packages, generally geared towards
teachers/mentors trying to push out packages en masse to students.

During classes or boot camps, it may be beneficial for Python packages to be pre-configured
for students instead of having them spend time on environmental setup.
This script intends to address this issue by allowing staff to provide a list
of package names in the script, run the script, and have them all installed without
worrying about explaining pip commands or package management.

This does NOT replace the functionality of requirements.txt files, but more intended
as an alternative way to say "Here's a script that will install the packages you need 
for this project".

## How To Use
- Git clone the repo
- Modify the PACKAGES list variable in package_installer.py to contain
  the packages necessary
- Run package_installer.py in the environment that needs the packages

### Notes
- This script will install the packages in whatever environment it's run in. This
  means that if ran with the global Python interpreter, it will install the packages
  globally.
- This *should* be portable to *nix systems, but I have not tested it.

## Future Plans?
- [ ] Add venv detection, and add ability to create a venv if not needed
- [ ] Add a few more functionalities, such as package deletion or reading from a file
- [ ] Add a verbose mode
- [ ] Prettify the text during runtime

