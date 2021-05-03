# movies-collection-api-using-django-rest-framework
This is a movie collection Application Programming Interface, where users can store their favorite movies information in different collections (groups).

  ## Features of project:

  1. **Display movies to API user without storing data**. when user calls on ` http://127.0.0.1:8000/movies/ ` it will call another API internally to get movies from it and it to the user.

  2. **User can make collections of movies**. user can create his own collections also update , delete operations can performe.

  3. **User authentication**. Only authenticated user can make collection.

  4. **JWT Token authentication**. JWT Token authention is use for user authention. User can register or login to same url ` http://127.0.0.1:8000/register/ ` to get JWT Token.

  5. **Collection Privacy**. User can only read, create, update or delete his own collections

  ## Technology Used:

  * Python, 
  * Django
  * Django Rest FrameWork
  * SQLite3

### Run the following commands to get started your project:

  1. download project

  ```
  git clone https://github.com/dwipalshrirao/movies-collection-api-using-django-rest-framework

  cd movies-collection-api-using-django-rest-framework

  ```

  2. install requierd libraries

  ```python
  
  pip install requirements.txt

  ```

  3. run command below

  ```python
  python3 manage.py makemigrations

  python3 manage.py migrate

  python3 manage.py runserver
  ```

  if found this project helpful please give star to repo. 
  thank you.


