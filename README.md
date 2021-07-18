**Welcome to Tamminga Coin** --
**A Proof of Work Blockchain**

----
First
----
**Activate the virtual environment**
----
Create one

>python -m venv env

----
- Windows
> env/Script/activate

- Mac
> source env/bin/activate

----
Then
----
**Install requirements.txt**
----
> pip install -r requirements.txt

Packages in the file are
- Pip
- Pytest
- Flask
- Pubnub

----
**To Run the tests**
----

- Make sure to activate the virtual environment

>python -m pytest backend/tests

----
**To Run the Application and API**
----

- Make sure to activate the virtual environment

>python -m backend.app

----
**Run a peer instance**
----
- Make sure to activate the virtual environment

MAC
>export PEER=True && python3 -m backend.app

WINDOWS -CMD
>set PEER PEER=True && python -m backend.app

WINDOWS - Powershell
>$env:PEER = 'True'; python -m backend.app


