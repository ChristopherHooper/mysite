=====
Favorite_Things
=====

Favorite_Things is a simple Django app to retrieve Eventbrite Events based on User's Categorical Interests. A User selects
interests from catagories gleaned from the Eventbrite API and is transfered to a paginated page containing related events.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "Favorite_Things" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'Favorite_Things',
    )

2. Include the Favorite_Things URLconf in your project urls.py like this::

    url(r'^Favorite_Things/', include('Favorite_Things.urls')),

3. Run `python manage.py migrate` to create the Favorite_Things models.

4. Start the development server and visit http://127.0.0.1:8000/admin/ (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/Favorite_Things/ to participate.
