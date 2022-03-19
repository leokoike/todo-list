# TODO - LIST

## Building postgres database via docker

```sh
$ docker run --name name_tag -e POSTGRES_USER=user_name -e POSTGRES_DB=db_name -e POSTGRES_PASSWORD=password -p 5432:5432 -d postgres
```