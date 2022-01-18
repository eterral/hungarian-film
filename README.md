# Hungarian Film (1945-1989) API

This is an API for displaying films made in Hungary from 1945-1989. For now the data is fairly incomplete

# API Routes

The routes are listed below for accessing the database

#	Schema

`films`
```
{
  title_en VARCHAR(255),
  title_hu VARCHAR(255),
  year INTEGER,
  was_banned BOOLEAN,
  directed_by INTEGER,
  restored BOOLEAN,
  is_documentary BOOLEAN
}
```

`directors`
```
{
  director_id INTEGER,
  name VARCHAR(255),
  birth VARCHAR(255)
}
```

## Get list of films

### Request

`GET /films/`

 Returns all films in the databaase

### Response

```
{
	"directed_by": 1,
	"id": 3,
	"is_documentary": false,
	"restored": true,
	"title_en": "The Whistling Cobblestone",
	"title_hu": "A sípoló macskakő",
	"was_banned": true,
	"year": 1971
},
```

### Request
`GET /films/banned`

Return all films that were banned

### Response

```
{
	"directed_by": 1,
	"id": 4,
	"is_documentary": true,
	"restored": false,
	"title_en": "The Resolution",
	"title_hu": "A határozat",
	"was_banned": true,
	"year": 1972
}
```

### Request
`GET /films/documentary`

Return all films that are documentarys

### Response
```
{
	"directed_by": 1,
	"id": 2,
	"is_documentary": true,
	"restored": false,
	"title_en": "The Selection",
	"title_hu": "A válogatás",
	"was_banned": true,
	"year": 1970
},
```
## Create a new film

### Request

`POST /films/`

 Create a new film in the database

### Response

 ```
 {
	"directed_by": 2,
	"id": 20,
	"is_documentary": true,
	"restored": false,
	"title_en": "The Turin Horse",
	"title_hu": "A torinói ló ",
	"was_banned": false,
	"year": 2011
}
 
 ```

## Update a film

### Request

`PUT /films/<id>`


### Response
```
 {
	"directed_by": 2,
	"id": 20,
	"is_documentary": true,
	"restored": false,
	"title_en": "The Turin Horse",
	"title_hu": "A torinói ló ",
	"was_banned": false,
	"year": 2011
}
```
## Delete a film

### Request

`DELETE /films/<id>`


### Response
```
{
	"deleted": true
}
```
## Get all films from a director

### Request

`GET /directors/films/<id>`

    

### Response
```
[
  {
    "directed_by": 1,
    "id": 1,
    "is_documentary": true,
    "restored": false,
    "title_en": "The Long Distance Runner",
    "title_hu": "Hosszú futásodra mindig számíthatunk...",
    "was_banned": false,
    "year": 1969
  },
  {
    "directed_by": 1,
    "id": 2,
    "is_documentary": true,
    "restored": false,
    "title_en": "The Selection",
    "title_hu": "A válogatás",
    "was_banned": true,
    "year": 1970
  }
 ]
  ```
