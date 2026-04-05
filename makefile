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
#logs for web service
logs-web:
	docker compose logs -f web
#logs for postgres service
logs-listing-db:
	
	docker compose logs -f listings_db
#logs for postgres2 service
logs-users-db:
	docker compose logs -f users_db	




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

#Remove network for project
network-v:
	docker network prune -f


#make migrations for users app
make-migrations-users:
	docker compose exec web python manage.py makemigrations user
#make migrations for listings app
make-migrations-listings:
	docker compose exec web python manage.py makemigrations listing



#migrate-users
migrate-users:
	docker compose exec web python manage.py migrate --database=users
#make migrations for listings app
migrate-listings:
	docker compose exec web python manage.py migrate --database=listings





