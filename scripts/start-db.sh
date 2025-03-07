#!/bin/bash

echo "Starting database server..."
docker compose --file ./scripts/compose.db.yaml up --watch
