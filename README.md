```bash
# Install protobuf compiler
$ sudo apt-get install protobuf-compiler

# Install buildtools
$ sudo apt-get install build-essential make

# Install grpc packages
$ pip3 install -r requirements.txt
```

## Compile protobuf schema to python wrapper

```bash
chmod +x ./install.sh
./install
```

## Run gRPC server and REST server

```bash
chmod +x ./run.sh
./run
```



## Commands to run

**Send to server**

`curl -X POST -H "Content-Type: application/json" http://127.0.0.1:8000/rest/fibonacci -d "{\"order\":\"{NUMBER}\"}"`



**To Get History**

`curl 127.0.0.1:8000/rest/logs`

