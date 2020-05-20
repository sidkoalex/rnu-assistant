## Deployment

Requirements: 

- Installed, running and ready __Docker__ (with docker-compose) 

- Installed __Python__, latest or at least 3.6+ version

- Installed __ffmpeg__ (and added to PATH variable)  
Detailed ffmpeg installation instructions can be found [here](http://blog.gregzaal.com/how-to-install-ffmpeg-on-windows/). 

### Run server-side parts

1) Open `run_all/docker-compose` folder in terminal

2) Execute `docker-compose up -d` to build and run all services automatically

### Running client applications and test the Assistant

Now, when server-side part is running, you can create your applications that can connect to Kafka topic and listen for activated jobs.

There is a simple Job already build in named __HELLO__

Here is how it is stored in MongoDB:
```
{
    'name': 'HELLO',
    'search_type': 'EXACT_MATCH',
    'search_data': 'hello'
}
```

`search_data` field tells us that this command can be activated by _hello_ word

For now, to activate this command just open your browser on url: <http://localhost:8080/text/hello> to send _hello_ text to Assistant.

You will see something like this in response: `{"user_request_id": "0154-5736", "user_request_text": "hello"}`,
that means your request is accepted.

Assistant will found this __HELLO__ Job by `hello` text that you've sent and fire an event to Kafka.

But nothing will happen until you run some application that can listen to jobs and react to them.

So, go to `client_apps` folder. There you will see a `hello` application and if you run it, it will listen for a Job named __HELLO__ from Kafka topic and print a greeting to you. Also, it will redirect this greeting messages to special Kafka topic named `say`.

In addition, if you run a `client_apps/voice-listener` application, it will listen the `say` topic and
speak aloud all the messages that get there. It means that now you can hear all greeting messages sent by `client_apps/hello` app to you.  

### Additional tools

If you want to see what is going on in Kafka topics, I would recommend you to install [Kafka Tool 2](https://www.kafkatool.com/download.html)  
By default the settings are:
- Zookeeper host: _localhost_
- Zookeeper port: _2181_
- Bootstrap servers: _localhost:29092_ (because port 9092 is used for internal connections between docker services)

To explore MongoDB, you can install their MongoDBCompass application.  
By default the connection url is: `mongodb://root:root@localhost:27017/`
