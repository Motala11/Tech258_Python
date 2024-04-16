# APIs

## What are APIs?
API stands for Application Programming Interface. An API, quite simply, is a way for 2 or more programs or components to communicate with each other.

## The data transfer process in API communication
![img.png](img.png)

## How are they used and why are they so popular?
APIs have a plethora of uses, such as integration, modularity, scalability and standardisation. <br>
APIs are popular due to the flexibility it allows developers, as well as increasing the speed of development. This is achieved through reusing existing functionalities and services, thus reducing development time.

## What is a REST API? What makes an API RESTful?
REST means Representational State Transfer. It is an architectural style for providing standards between computer systems on the web, allowing easier system-to-system communication. <br>
An API becomes RESTful when it follows the REST architectural style known as RESTful web services.

## What are the REST API guidelines?
Some common REST API guidelines are as follows:
- Use nouns for resources e.g. `/users` as opposed to `/getUsers`.
- Use plural nouns for resources.
- Use HTTP methods correctly.
- Use proper HTTP status codes.
- Versioning - Include versioning in the API endpoint to ensure backwards compatibility as the API evolves.
## What is HTTP?
HTTP stands for Hypertext Transfer Protocol. It is an application-layer protocol used for transmitting hypermedia documents, such as HTML.
## Explaining HTTP request structures:
The HTTP request used here is the `GET` method. <br>
The URL requested is `index.html` <br>
The text labelled 'Headers' show the specific request or describe the content of the message body/
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*oy4-WDRk2mYmbNv7.jpg)
## Explaining HTTP response structures:
The first line is the status line, the code `200` means the request was OK. <br>
The response headers are in `name:value` pairs. <br>
![](https://www3.ntu.edu.sg/home/ehchua/programming/webprogramming/images/HTTP_ResponseMessageExample.png)
## What are the 5 HTTP verbs? What does each do?
The 5 HTTP verbs are:
- `GET` = The GET request is used to retrieve data.
- `POST` = The POST method is used to submit data, commonly used to create new resources on the server.
- `PUT` = The PUT method is used to update or replace the representation of a resource.
- `DELETE` = The DELETE method is used to delete the specified resource from the server.
- `PATCH` = The PATCH method is used to apply partial modifications to a resource.
## What is 'statelessness'?
Statelessness is when each transaction or request is independent and does not rely on previous interactions. Essentially, the system or protocol does not retain any information about the previous history of the client between requests. <br>
The following image showcases how a stateless http request works, as the server does not remember the client.
![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*7BA8zaVExmMRpTlvtGaT5g.png)

To counteract HTTP being 'stateless', cookies are used to ensure details are remembered. Cookies are a form of caching, that will be explained in the following section.
![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*lpVQgD8uzEwofKlyIGZZ7Q.png)
## What is caching?
Caching is the process of storing copies of frequently accessed data in a temporary storage location, known as cache. This is used for faster retrieval when the same data is requested. Caching improves the performance and the efficiency of systems.