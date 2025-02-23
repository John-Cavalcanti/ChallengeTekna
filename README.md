# ChallengeTekna

## Challenge description

This challenge requires to create an access to a google sheets database, then make manipulations on the columns so we can calculate the average grades of the students.

## Guide to run the code 

This project was developed using python 3 and some of their libraries, alogside with some google libraries so that we can access the google sheet.
Then following there is a guide to help you run the code.

### 1 - Python installation

First we need to make sure that our engine is working. Check if python3 is installed in you computer, run this code on the terminal of your preference(i recommend git bash if you are on windows) :

``` bash
python3 --version
```

It should show something like :

```bash
Python 3.x.x
```

If it doesn't show anything like that, we need to install python. 

If you are on windows download python on the official Python website, click [here](https://www.python.org/downloads/) to access.

If you are on ubuntu you will be fine running these commands on you terminal :

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip -y
```

Verify if both are correctly installed with these two commands :

```bash
python3 --version
pip --version
```

### 2 - Preparing the enviroment

We are gonna use venv to keep an isolate enviroment so we can instaal dependencies without setting them globally and our application can run smoothly.

On ubuntu run the code below to install venv :

```bash
sudo apt install python3-venv
```

Note: On windows there is no need to install the venv package since it already comes along with the instalation of Python 3.3 and beyond.

Now to setup the enviroment on the command prompt of your preference, run the code:

Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

Ubuntu :
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see something like (venv) before the path on your terminal indicating that the enviroment is active.

Before we install the dependencies we need the credentials for the code to access the sheet we want to manipulate, so the link with the TeknaChallenge-chave.json file will be sent via email, you will need to download the file and place in the root of the directory so the code can access the credentials correctly. 

### 3 - Installing dependencies

Before we run the code we need to make sure all of the dependencies used in the projext are installed.

Luckily there is a requirement.txt in the root of the repository that you can run with the command :

```bash
pip install -r requirements.txt
```

### 4 - Runnig the code

Finally we can run the code after all of the setup, you can run the code with the command :

Windows:
```bash
python main.py
```

Ubuntu :
```bash
python3 main.py
```

It should show the menu for choosing the options of what you want to do with the project.
