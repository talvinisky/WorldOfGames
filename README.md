# World Of Games

### Welcome to my project 
### The project is designed to work with m1/m2 apple chips as the environment the docker container is built on.

**Build**: 
- ```docker-compose build```

**Run**:
- ```docker-compose up -d```

**Play the g**ame**:
- ```Pull the repoestory and execute MainGame.py```
- ```keep in mind that the scores.txt file already has values in it so delete it and the file will create it```

**Run test**:
- ```docker exec -it wog python tests/e2e.py```
- Should return 0 if test pass and -1 if not

**Clean**:
- ```docker-compose down;docker rmi $(docker images -q)```

**Run Jenkins test**:
- Set the following environment variables:
    - DOCKER_ID
    - DOCKER_PASSWORD

- Build Pipeline script from SCM
- The jenkins test tests the flask server and the e2e.py file 




