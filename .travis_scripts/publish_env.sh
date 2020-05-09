#!/bin/sh

PAYLOAD='{"APP_VERSION": "'"$TRAVIS_TAG"'"}';
curl -n -X PATCH https://api.heroku.com/apps/backend-flaskrestx/config-vars \
     -d "${PAYLOAD}" \
     -H "Content-Type: application/json" \
     -H "Accept: application/vnd.heroku+json; version=3" \
     -H "Authorization: Bearer ${HEROKU_API_KEY}" > /dev/null;