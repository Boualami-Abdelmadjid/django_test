
# Django TEST 

#### A small django project




## Deployment

To deploy this project run

```bash
  docker-compose up -d #run docker containers in the background
  docker-compose restart #if containers are already running
  docker-compose run --rm web python manage.py migrate #To apply migrations to the database
```


## Environment Variables

To run this project, you will need to add the following environment variables to your docker-compose.yml file

`SECRET`

`DEBUG`


## Screenshots

![App Screenshot](https://i.imgur.com/sio7UH9.png)

