#!/usr/bin/env bash

(
    cd app
    orator migrate -c db/orator_local.yml
)
