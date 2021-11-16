#!/usr/bin/env bash

cd rest-server && make && cd ../
cd grpc_server && make
