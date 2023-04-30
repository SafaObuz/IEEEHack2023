# IEEEHack2023
Drexel IEEE 2023 Hackathon

# (1) INSTALL PIP

Mostly from: https://www.geeksforgeeks.org/how-to-install-pip-on-windows/#

## Method 1: Using cURL in Python

### Step 1: Open the cmd terminal 

### Step 2: In python, a curl is a tool for transferring data requests to and from a server. Use the following commands to request:

curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py

## Method 2: Manually install PIP on Windows

### Step 1: Download the get-pip.py (https://bootstrap.pypa.io/get-pip.py) file and store it in the same directory as python is installed.

### Step 2: Change the current path of the directory in the command line to the path of the directory where the above file exists. 

### Step 3: get-pip.py is a bootstrapping script that enables users to install pip in Python environments. Run the command given below:

python get-pip.py

### Step 4: Now wait through the installation process. Voila! pip is now installed on your system.

Do this command to verify the version.

pip --version

Adding PIP To Windows Environment Variables
If you are facing any path error then you can follow the following steps to add the pip to your PATH. You can follow the following steps to set the Path:

Go to System and Security > System in the Control Panel once it has been opened.
On the left side, click the Advanced system settings link.
Then select Environment Variables.
Double-click the PATH variable under System Variables.
Click New, and add the directory where pip is installed, e.g. C:Python33Scripts, and select OK.

pip can be upgraded using the following command.

python -m pip install -U pip

# 2 INSTALLING PACKAGES

Partially from: https://github.com/openai/openai-quickstart-python

## 1. Run this command

git clone https://github.com/SafaObuz/IEEEHack2023.git

## 2. Create a new virtual environment:

python -m venv venv
. venv/bin/activate

Note that this didnt work for me... I did this command.

python -m venv venv/bin/activate

## 3. pip the requirements

pip install -r requirements.txt

For me this also didn't work when it was trying to install numpy. If this doens't work, just manually do this command.

pip install <name_of_library>

where <name_of_library> is just the package that failed, like numpy for me.

## . Get your own OpenAI key

https://platform.openai.com/account/api-keys

I am revoking my API key a couple days after the event because I don't want someone to use use and abuse my key. Replace with yours.

## 5. Install flask

pip install flask

# FINISH

## 1. Almost done!

Do this command in the folder. It will run a local host server which you can use the website from.

flask run








