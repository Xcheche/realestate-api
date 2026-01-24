#Docker compose build
build:
	docker compose build --no-cache

#Docker compose up
up:
	docker compose up -d

#Docker compose down
down:
	docker compose down
#Check configuration
config:
	docker compose config

#Check logs
logs:
	docker compose logs -f


#Remove all stopped containers
clean:
	docker container prune -f

#Remove all unused images
rmi:
	docker image prune -a -f

#Delete volumes
volumes:
	docker volume prune -f

#Down volumes
v:
	docker compose down -v

#Psql terminal
psql:
	docker exec -it postgres_container psql -U postgres_user -d postgres_db

#Redis terminal	
redis:
	docker exec -it redis_container redis-cli			




