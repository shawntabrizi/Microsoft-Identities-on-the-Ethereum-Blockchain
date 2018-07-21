# Middle Tier Application

This is the middle tier for Microsoft Identities on the blockchain. Built as a docker container.


[Install docker for mac](https://docs.docker.com/docker-for-mac/install/)

[Install docker for windows](https://docs.docker.com/docker-for-windows/install/)

To start the app in a container run:

```
    docker build -t msidonethmiddle .
    docker run -d -p 5000:5000 msidonethmiddle
```

Now the app is running in your computer. Head to your browser and go to http://localhost:5000 to see the app running.

If you want to stop the container run (will stop all running containers):

```
    docker stop $(docker ps -q)
```

If you want to delete the container run (will delete all containers):

```
    docker rm $(docker ps -a -q)
```