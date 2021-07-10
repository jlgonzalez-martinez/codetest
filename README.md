# Fever Pets - Back

## 1.- Structure

For the structure I try to clearly separate the application from the infrastructure and the presentation for this reason I include the following top level dirs:

- Application: This directory includes the domain pet objects (cats and dogs) and the mappers and converters to generate 
  or transform the domain,
- Infrastructure: This directory includes the information providers for the pets, I'm not totally sure that this 
  providers go to the infrastructure directory, but I thought this providers as external databases. 
  In the future we will have providers that get info from a database or from a queue
- Presentation: The presentation layer, that includes the Flask application and endpoints.
- Utils: Utils module, I don't like the utils module because is a bag to put code that has no explicit location.
- Tests: Tests for the application.

Also, to this structure I added a Dockerfile, configuration and a health endpoint.

## 2.- Solution to Fever pets

Like I want a very extensible solution, I try to make a solution high configurable, using the three following classes:

- Providers: Get information from a provider, in this case we have only a type of provider, that is the HTTP provider, 
  that works with fever_pets_data and fever_pets_data_2.
  
  This http provider can be configured with a list of urls to 
  solve the problem that one provider have only one endpoint and other have two endpoints. Also, if another provider who
  uses http have three endpoints it would fit with the solution.

- Mappers: Solve the problem of how the information it's mapped to the domain, this mappers allow us by configuration 
  map fields like the picture field into the photo_url attribute and also handle how to determine if the pet is a 
  cat and a dog. In this first version it's provided a route_mapper and a field_mapper. The route mapper looks in the
  url if 'cats' or 'dogs' if present to determine this category, and the field mapper looks up in a configurable field
  this values to allow us to include a third provider that have this field in the 'type' field instead of the 'kind' 
  field.
  
  This solution has a little problem, because the literal to define cats and dogs must be configurable, and probably 
  a list. To allow, for example a third api that have a field 'tipo' with values 'gato' and 'perro'.
  
- Converters: Are used to convert the domain pet with some logic, like change from grams to kilograms.


Taking into account the previous classed we can define this two providers in the config.yml adding this in the providers
section:

```yaml
providers:
  - http_provider:
      name: all_together
      protocol: https
      host: my-json-server.typicode.com
      port: 443
      routes:
        - /Feverup/fever_pets_data/pets/
      mapper:
        name: field_mapper
        field_name: kind
      converters:
        - weight_converter
  - http_provider:
      name: cats_vs_dogs
      protocol: https
      host: my-json-server.typicode.com
      port: 443
      routes:
        - /Feverup/fever_pets_data_2/cats/
        - /Feverup/fever_pets_data_2/dogs/
      mapper:
        name: route_mapper
        rename_fields:
          picture: photo_url
```

Also, we expose an API with two that can be executed in swagger:

- /pet/: List all pets
- /pet/<provider_name>/<pet_id>: Get a pet by provider and id. It needs to specify the provider, because the ids
  are not unique between the providers.
  
Note: To speed up the application the http requests to the providers have been cached with a TTL of 600s.


## 3.- Possible improvements and leftovers of the solution:

- Error handling: The error handling could be improved, there are no custom exceptions for this application, 
  when the http requests fails it's not controlled...
  
- Logging: The logging config is with the basic config. In addition, there are not practically logs in the application
- Service binding: The application context of Flask is not used, to solve this problem the Pet service is converted to
  a Singleton.
  
- Performance: Like the pagination is made in the presentation module, if we request only five pets we are calling all 
the providers and then filter in the controller.
  
- Api documentation: he api is not totally documented.
- Api tests: There are no tests for the api.
- String to decide if a pet is a dog, or a cat is not configurable, it's always 'dog' or 'cat'

## Start the application
```bash
python main.py -c config.yml
```
## Run tests
```bash
python -m unittest
```