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
