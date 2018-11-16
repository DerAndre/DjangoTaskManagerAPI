Django Showcase Project to show programming techniques with Python (3.6.6) and Django (2.1.3).

To run this project you have to create a virtual environment and have a mySQL server installed. To set up the virtual
environment correctly just run:

sudo easy_install virtualenv
mkdir ~/.virtualenv
virtualenv ~/.virtualenv/task_manager --python=<Path to Python 3.6>

Since it's a good practice not to store credentials in your source code, the database credentials are stored in
environment variables. For testing purpose you can put them back into the code or export the database user and password
as follows:

export DATABASE_USER="<Your DB User>"
DATABASE_PASSWORD="<Your super secret password>"

This project uses the Django Rest Framework (3.9) to provide a backend with similar functionality and model structure
like Trello (https://trello.com). In addition to the standard manage.py commands, django extensions are installed which
add several useful commands and are highly recommendable.

The application structure is pretty much oriented after the models needed for the tasks to accomplish, except lists and
labels which are summarized in the boards app. This is because these to models have a close relation to a single board
and beside this, they have just a structuring and describing character with no further functionality.

Members, cards and boards are logical units with a specific purpose each. Having them in own apps makes it easier to
extend their range of functions if needed.

Urls for each app are build with DRF routers which provide a easy way to build a CRUD structure. In combination with
DRF ViewSets, one need just a view lines of code to build a fully functional CRUD API.
Features like authentication and permissions are not covered in this example, but they would just need a few lines more
and are easy to integrate.

Every app contains testcases to check if the API, defined for the app works as expected (25 tests in total). Just run
python manage.py test to run them all (the database user needs the privileges to create new databases in order to create
and delete the test database)

The API exposes the following routes and views. List views to get lists of entities and create new ones and detail views
to view single entities, update or delete them.

/api/boards/ -> rest_framework.routers.APIRootView -> api-root
/api/boards/ -> boards.views.BoardViewSet -> board-list
/api/boards/<format>/ -> boards.views.BoardViewSet -> board-list
/api/boards/<pk>/ -> boards.views.BoardViewSet -> board-detail
/api/boards/<pk><format>/ ->  boards.views.BoardViewSet -> board-detail

/api/cards/ -> rest_framework.routers.APIRootView -> api-root
/api/cards/ -> cards.views.CardViewSet -> card-list
/api/cards/<format>/ -> cards.views.CardViewSet -> card-list
/api/cards/<pk>/ -> cards.views.CardViewSet -> card-detail
/api/cards/<pk><format>/ -> cards.views.CardViewSet -> card-detail

/api/labels/ -> rest_framework.routers.APIRootView -> api-root
/api/labels/ -> boards.views.LabelViewSet -> label-list
/api/labels/<format>/ -> boards.views.LabelViewSet -> label-list
/api/labels/<pk>/ -> boards.views.LabelViewSet -> label-detail
/api/labels/<pk><format>/ -> boards.views.LabelViewSet -> label-detail

/api/lists/ -> rest_framework.routers.APIRootView -> api-root
/api/lists/ -> boards.views.ListViewSet ->  -> list-list
/api/lists/<format>/ -> boards.views.ListViewSet -> list-list
/api/lists/<pk>/ -> boards.views.ListViewSet -> list-detail
/api/lists/<pk><format>/ -> boards.views.ListViewSet -> list-detail

/api/members/ -> rest_framework.routers.APIRootView -> api-root
/api/members/ -> members.views.MemberViewSet -> member-list
/api/members/<format>/ -> members.views.MemberViewSet -> member-list
/api/members/<pk>/ -> members.views.MemberViewSet ->  member-detail
/api/members/<pk><format>/ -> members.views.MemberViewSet -> member-detail