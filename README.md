# MicroBat

Startup Guide:

So. You want to start a MicroBat server. I was once like you. Young and full of hope. I'll help you know, but just know. There's no help on the other side.

First, you want to install the dependencies. Make sure you have python3_flask installed (using your appropriate package manager).

Next, run the following command:
```
pip3 install -r dependencies.txt
```

This will install all of the python libraries required to run MicroBat.

If you want to make this a public server (unsecure! but lots of fun :-))

Allow the port to be opened
```
sudo ufw allow 5000/tcp
```

Make sure your port is forwarded

HALL OF QUOTES:

I've added a tenative file structure to be discussed at a later date.<br><br>
"I think Flask is going to make this nearly trivial."<br>
 \- John Alan Carmack, 2020  

"I was totally right about Flask and trivality"<br>
 \- John Alan Carmack, Slightly Later.

"Okay the poll isn't going to be trival."<br>
 \- John Alan Carmack, Slightly Laterer.
