## Getting Started

This is a simple project for the telegram-bot-api that can be run even on qpython or pydroid

Below, I am providing instructions for you to have a copy of the project, these instructions will show you how to start using it for learning, development and testing purposes.

* 1° step - Downloading Project

## ANDROID
download the qpython or pydroid app from your smartphone's app store and install the telepot library.
Note: check the documentation or website of the application used to install via pip.
With the library installed, download this project in zip and save it in the desired folder, if you use qpython oriento to save inside the `projects` folder

## PC
open the terminal and simply clone the repository as follows:
```
$ git clone https://github.com/VycktorStark/DbBot.git
```
Still with the repository open, install the following library: telepot, if you don't have it

```bash
# Tested on Ubuntu 14.04, 15.04 and 16.04, Debian 7, Linux Mint 17.2
$ sudo apt-get update && sudo apt-get upgrade   
$ sudo apt install python3 && python3-pip
$ sudo pip3 install telepot
```


* 2° step - Adding BOT Token

Open the `config.py` file and configure it with the following information:

os.environ ['TOKEN'] ## exchange for your token
Chatsuporte = "id_chat" ## put the id in the log chat


* 4° step - Turning the project on

## ANDROID
If you use qpython, you must open the application, click on the button that will be highlighted (in the middle), select the project and it will be executed.

If you choose pydroid, open the application, select the option to search for the main.py file among other files, with the main.py file open, just run.


## PC
To start the bot, run: sudo ./main.py
To stop the bot, press Ctrl + C. You can also start the bot with python3 main.py, to stop the bot, press Ctrl + C.
