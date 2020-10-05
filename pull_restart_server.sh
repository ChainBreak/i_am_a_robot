#!/usr/bin/env bash

ssh -t thomas@172.105.178.196 "cd co/i_am_a_robot && git pull && sudo systemctl restart i-am-a-robot.service"
