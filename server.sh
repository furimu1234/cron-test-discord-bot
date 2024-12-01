cd /home/furimu/cron-test-discord-bot
git pull
docker compose stop
docker compose rm -f
docker compose up -d --build
docker compose logs -ft