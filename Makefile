NAME = marvin

all: prune reload

reload:
	@ docker-compose -f docker-compose.yml up --build

prune: stop
	@ docker system prune -f

stop:
	@ docker-compose -f docker-compose.yml down

.PHONY: stop prune reload all
