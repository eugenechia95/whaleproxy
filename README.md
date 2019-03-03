# whaleproxy
Whaleproxy is a proxy service built using Django and Memcached that is connected to whalemarket.

## Installation Instructions
User should have docker and Python 3.6 set up on computer.
Git Clone from repository and run the following code
```
$ docker-compose up --build

```
Once server is running, user can use cURL to make HTTP Requests to the proxy service.
If unable to successfully build, check firewall settings and disable temporarily if required.

## Available API EndPoints

**1.  POST /whales**
```
~ curl -X POST https://whalemarket.saleswhale.io/whales -H "Authorization: Bearer TOKEN" -d '{"name": "orca", "country": "Atlantis" }'
```
**Expected Response:**
{"whale":{"id":69,"name":"pinkwhale","country":"India"}}

**2.  GET /whale/:id**
```
~ curl -X GET http://127.0.0.1:8000/whales/69 -H "Authorization: Bearer TOKEN"
```
**Expected Response:**
{"whale":{"id":69,"name":"pinkwhale","country":"India"}}

**3.  GET /whales**
```
~ curl -X GET http://127.0.0.1:8000/whales -H "Authorization: Bearer TOKEN"
```
**Expected Response:**
{"whales":[{"id":69,"name":"pinkwhale","country":"India"}]}

**4.  PUT /whales** 

  *Forces Sync of of every whale in whalemarket*
```
~ curl -X PUT http://127.0.0.1:8000/whales -H "Authorization: Bearer TOKEN"
```
**Expected Response:**
All Whales Synced!

**5.  DELETE /whales**
  
  *Purges cache of service*
```
~ curl -X DELETE http://127.0.0.1:8000/whales -H "Authorization: Bearer TOKEN"
```

**6.  GET /hitratio**
```
~ curl -X GET http://127.0.0.1:8000/hitratio -H "Authorization: Bearer TOKEN"
```
**Expected Response:**
Total Retrieval Request: 4 
Total Cache Hits: 3
Cache Hit Ratio: 75%

## Testing
Testing of views can be checked by running
```
docker-compose run web python /code/manage.py test
```