NOTE ::-
        THIS IS A COMMAND LINE APPLICATION TO FETCH THE DATA FROM SWAPI.DEV

This is a project that pulls the data of `swapi.dev`

`Virtualenv` : Virtual Environment
    - We created one virtual environment to keep our project dependencies 

* In star_warsAPI there are some resources
  1) People
  2) Vehicles
  3) Starships
  4) Planets 
  5) Species
  6) Films

```
TASK - 1
    - The Star Wars API lists 82 main characters in the Star Wars saga. For the first task, we would like you to use a 
       random number generator that picks a number between 1-82. Using these random numbers you will be pulling 15 
       characters from the API using Python.
```

```
TASK - 2
    - We have to fetch the data of first film from swapi.dev
    - After pulling out the data write json data in `output.txt`
        - Then we have to list down only first name and last name of the character who worked in 1st film [ LIST FORMAT]
        - Also we have to list down the names of planets and vehicles which are in 1st film in [ LIST FORMAT]
```

```
TASK - 3
1. TODO - import all resource classes here
2. TODO - get count of each resource      
3. TODO - get singular resource URL from each resource
    - for example,
    - hit plural URL of starships and that will list all starships data
    - iterate on each starship data and capture singular URLs
    - all_starship_data = data.get("results")
    - you will iterate on `all_starship_data`,
4. TODO - pull data from random 3 "singular" resource URLs
    - utilize`utils` package to produce random 3 numbers from resource ids
    - and pull data for them
5. TODO - convert the script into CLI application
6. TODO - pretty print output (from pprint import pprint)

```