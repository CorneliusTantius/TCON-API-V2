# TCON-API
4th Semester Software Engineering Project Backend API (Cont.)

This is basically the continued development of first version of [TCON](https://github.com/CorneliusTantius/TCON-API). When previously we use [Flask](https://flask.palletsprojects.com/) as our API framework and [SQlite](https://www.sqlite.org/index.html) as our database, At this version we've done some improvement such as design pattern optimization, code optimization and also migrating our API framework to [FastAPI](https://fastapi.tiangolo.com/) and our database to [MongoDB](https://www.mongodb.com/cloud/atlas/).


## How to run
- Make sure to clone the project first.
- After cloning, make sure to satisfy packages in requirements.txt. You can do that by running ```pip install -r requirements.txt"```.
- You can now run the project using ```python start.py```.


## Database and Configuration
- The config is located on root Server/ folder (```Server/configuration.json```).
- The configuration example can be found inside Templates.
- Make sure to set up your [MongoDB Atlas](https://www.mongodb.com/cloud/atlas/) account and obtain your own key.


## Deployment
The development target is simply heroku server, and the Procfile is already being set up. As for other development platform, you can use the same [Uvicorn](https://www.uvicorn.org/) command.


## Sample request
- The API Documentation can be accessed from swagger(FastAPI built in feature) using ```http://localhost:5000/docs```
- Make sure you have postman in your local machine.
- Open postman and import a collection.
- The collection can be obtained from [Templates] folder. (To be updated)
- The base URL deployed in heroku: https://tcon-api.herokuapp.com/ (Old TCon V1 API, To be updated)


## Design Pattern
![Design Pattern](https://github.com/CorneliusTantius/TCON-API-V2/blob/master/Templates/Code%20Flow.png?raw=true)


Copyright (C) 2021 Cornelius Tantius

All Rights Reserved
