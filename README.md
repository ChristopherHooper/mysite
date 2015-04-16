=====
polls
=====

polls is a simple Django app to retrieve Eventbrite Events based on User's Categorical Interests. A User selects
interests from catagories gleaned from the Eventbrite API and is transfered to a paginated page containing related events.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "polls" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'polls',
    )

2. Include the polls URLconf in your project urls.py like this::

    url(r'^polls/', include('polls.urls')),
    
3. Check to make sure that /polls/fixtures contains fixtures.json. If it doesn't, the, initialize data by running:
    
    python /polls/get_Events.py
    
    Make sure that fixtures.json is placed into the poll/fixtures dir.

3. Run `python manage.py migrate` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/ (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/polls/category/ to participate.
