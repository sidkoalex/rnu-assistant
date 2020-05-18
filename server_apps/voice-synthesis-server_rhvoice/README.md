# Docker example of RHVoice speech server

## Build a container

Open console in project folder, and run: `docker build . -t my_rhvoice`

## Run the voice synthesis server

Run your build by following command `docker run -d -p 8080:8080 my_rhvoice`

## Test the voice synthesis server

Open your browser and check localhost on 8080 port

### Some examples

- (use anatol voice by default) <http://localhost:8080?text=Садок+вишневий+коло+хати,+хрущі+над+вишнями+гудуть>

- <http://localhost:8080?voice=natalia&text=Щедрик,+щедрик,+щедрівочка.+Прилетіла+ластівочка>

- <http://localhost:8080?voice=aleksandr&text=У+лукоморья+дуб+зелёный.+Златая+цепь+на+дубе+том>

- <http://localhost:8080?voice=alan&text=The+slings+and+arrows+of+outrageous+fortune,+Or+to+take+arms+against+a+sea+of+troubles>

## Acknowledgment

And many thanks to the following projects:

[Olga-Yakovleva/RHVoice](https://github.com/Olga-Yakovleva/RHVoice)

RHVoice docker examples from [NaharD/tts](https://github.com/NaharD/tts)
and [mgarmash/rhvoice-rest](https://github.com/mgarmash/rhvoice-rest)
