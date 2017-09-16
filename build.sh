#!/usr/bin/env bash

(
    cd app
    docker build . -t xbird_app
)

