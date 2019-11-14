# Echo Rest

This image is used for debugging. Sending a request to this service will echo the same request and print the headers, url-query and body in the log. <br/>
It accepts GET-, POST-, PUT-, DELETE-, PATCH- and OPTIONS-requests.

# Run
You can run the image on docker-hub by calling <br>
```
    docker run -p 80:80 mollee/echo-rest
```
You can also build and run the application you self with these commands <br>
```
    git clone git@github.com:molleer/echo-rest.git
    cd echo-rest
    docker-compose -f prod.docker-compose.yml up --build
```

## Config
Configure the environment variables via the ```prod.docker-compose.yml``` file or add the ```-e``` flag when running the ```docker run ```command. <br>

```LISTEN_PORT``` - The default port is 80 but can be changes with the environment variable ```LISTEN_PORT```.