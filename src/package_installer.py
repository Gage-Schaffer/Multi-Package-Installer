import sys
import subprocess


PACKAGES = ["pytest", "flask"]  # Edit this to contain the packages that are needing to be installed
PYTHON_INTERPRETER_PATH = sys.executable
failed_packages = []
successful_packages = []


print("-------- Installing Packages ---------")
if PACKAGES and PYTHON_INTERPRETER_PATH:
    if "venv" not in PYTHON_INTERPRETER_PATH:
        print("WARNING: INSTALLING PACKAGES GLOBALLY")
        print("         Packages will have to manually uninstalled with pip.\n")

    for package in PACKAGES:
        stdout = subprocess.run(
            PYTHON_INTERPRETER_PATH + " -m pip install " + package,
            shell=True,
            capture_output=True,
        )
        if stdout.returncode != 0:
            failed_packages.append(package)
            print(f"WARNING: {package} WAS NOT INSTALLED")
            print("          This can be manually installed via pip.\n")
            continue

        successful_packages.append(package)

if not PYTHON_INTERPRETER_PATH:
    print("Could not find Python interpreter. No packages were installed.")

if not PACKAGES:
    print("No packages were supplied. No packages were installed.")

print("-------- Install completed -----------")
if failed_packages:
    print("Some packages could not be installed:")
    for package in failed_packages:
        print(f"- {package}")
print("The following packages were installed or updated:")
for package in successful_packages:
    print(f"- {package}")


