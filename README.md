# Rabbit Dump

Dump rabbit mq messages to a csv file

## Usage

You need to install the dependencies of the project which is just `pika`. I
advise you to use a virtual environment like this.

```
$ virtualenv dev.venv
$ source dev.venv/bin/activate
$ python dump_queue.py localhost guest guest_pass my-host my-test-queue
```

Executing this will create a file the file `/output/message.csv` with the
messages from rabbit.

Disclaimer: This project will work only if the contents of your messages are in
JSON format, don't try this with binary data, because it won't work.

