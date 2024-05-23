-- This script lists all the cities of California that can be found in the database hbtn_0d_usa.

SELECT cities.id, cities.name
FROM states JOIN cities
ON states.id = cities.state_id
WHERE states.name = 'California';
