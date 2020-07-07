mongo:
	docker-compose -f mongo.yaml up -d

kafka:
	docker-compose -f kafka.yaml up -d

voice:
	docker-compose -f voice.yaml up -d

handle:
	docker-compose -f handle.yaml up -d
rebuild:
	docker-compose -f handle.yaml up -d --build

db: mongo kafka
base: db handle
