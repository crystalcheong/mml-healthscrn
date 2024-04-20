APP_NAME := healthscreen
COMPOSE_FILE := compose.yml --env-file .env

compose-build:
	@echo ${APP_NAME}: building w/ ${COMPOSE_FILE}
	@docker compose -f ${COMPOSE_FILE} build --no-cache
compose-up:
	@echo ${APP_NAME}: starting w/ ${COMPOSE_FILE}
	@docker compose -f ${COMPOSE_FILE} up --quiet-pull --remove-orphans
compose-down:
	@echo ${APP_NAME}: ending w/ ${COMPOSE_FILE}
	@docker compose -f ${COMPOSE_FILE} down --remove-orphans

## 🚨 Use with caution
docker-prune:
	@echo ${APP_NAME}: pruning docker images, volumes
	@docker compose down --volumes
	@docker image prune -f
	@docker system prune --volumes -f
	@docker volume prune -f -a

start: compose-build
stop: docker-prune