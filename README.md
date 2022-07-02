# Leaky URLs
An imperfect implementation of the TinyURL project that focuses more on demonstrating system design and specific technologies.

## Architecture
Django will be used for the backend, and will be the primary component for the whole Web Application (WebApp). Its Object Relational Mapper (ORM) will be used to interface with SQLite and Postgres databases, while its templating engine with url schemas will be used to server-side render the WebApp. React will be the primary javascript library used to create interactive interfaces, while the choice of bundler will be up for discussion.

Further improvements and discussions will be made on how to improve the user experience of the WebApp, specifically focusing on how the WebApp should be rendered: (1) client-side rendering; (2) pre-rendering; or (3) server-side rendering.

## User Interface
__Users__ will navigate to the _Leaky URLs_ website and be shown a simple ```Input``` box for them to enter their URL to shorten. After hitting enter, a simple ```Loading``` screen will appear while the request finishes, following which showing the shorten URL in a ```Textbox```. Users can then share this URLs to guide people to the specific website that they have chosen.

__Admins__ will have an authenticated website that they can view, which shows all the registered URLs and their corresponding shorten URLs. They have the permission to manually add or remove certain URLs as they deemed fit.

Every shorten URL also has an additional ```/details``` route that directs the __User__ to a static website showing a preview of the actual URL, along with other statistics about the shorten URL.

## Algorithm
We will set the following constraints:
- The shorten route can only contain characters from the set __[A-Z][a-z][0-9]__.
- The shorten route can only contain __3 characters__.
- There can only be a total of __238,328__ shorten URLs. ((26 + 26 + 10) permuations of (3)).
- Once the database is full, the __oldest__ shorten URL will be deleted.

Upon a new shorten URL request, the flow will be as follows:
1. If the maximum number of shorten URLs is already reached:
    1. Find the oldest shorten URL, and replace its redirected link to the current one.
    2. Return the shorten URL to the user.
2. Else, generate a random route using the constraints listed in the previous section.
3. If the route is already taken, increment the generated route by 1 character till an empty route is found.
4. Return the shorten URL to the user

The best-case _Time Complexity_ for creation of a shorten URL is _O(1)_, while the worst-case is _O(N)_, where _N_ is the number of permutations.
