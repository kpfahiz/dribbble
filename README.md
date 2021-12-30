# dribbble

#Urls

- create a new user

`http://127.0.0.1:8000/api/users/register/`

- login

`http://127.0.0.1:8000/api/users/login/`

- logout

`http://127.0.0.1:8000/api/users/logout/`

- Create a new post

    authentication required for this APi.

`http://127.0.0.1:8000/api/posts/create/`

- List all posts

`http://127.0.0.1:8000/api/posts/listall/`

- Get a Detail of a post

`http://127.0.0.1:8000/api/posts/<int:pk>/`


- Search a post by title, content, author, etc

`http://127.0.0.1:8000/api/posts/listall/?q=<str:query>`

or filter by django rest framework filters.

- Update a post

    authentication required for this APi.

`http://127.0.0.1:8000/api/posts/<int:pk>/edit/`

- Delete a post

    authentication required for this APi.

`http://127.0.0.1:8000/api/posts/<int:pk>/delete/`

- Create a new comment

    authentication required for this APi.
    
`http://127.0.0.1:8000/api/comments/create/`

- Get details of a comment

`http://127.0.0.1:8000/api/comments/<int:id>/`

- Gets likes of a post

`http://127.0.0.1:8000/api/posts/like/`
