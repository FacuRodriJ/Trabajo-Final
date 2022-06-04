#!/bin/bash
sudo systemctl restart postgresql && psql -U postgres -c "drop database IF EXISTS reserva_db" -c "create database reserva_db"