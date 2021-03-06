# Effervescence18-Website

## To run locally

1. cd into the repository root folder.
2. Run virtualenv
3. Type 'sudo pip3 install -r requirements.txt'
4. Type 'python3 manage.py runserver'


## Url structures

### Authentication is done using the django-rest-auth library. Following are the end-points:

1. Login - /api/login/
2. Logout - /api/logout/
3. Password Change - /api/password/change/
4. User details - /api/user/
5. Register new user - /api/registration/

For api key and value pairs, refer this - http://django-rest-auth.readthedocs.io/en/latest/

### For user credentials, following are the end-points:

1. api/regular_user/

#### This end-point contains get, post and put methods for respectively accessing, creating and updating.


### Other end-point:

1. api/events/          for viewing the list of events with details
2. api/regular_user_payment_amount/     for updating the total subscibed amount of the user(default = 0)
3. api/regular_user_payment_id/     for the user to input his/her payment id
4. api/regular_user_event/  to add a particular event under the user's subscription

### For social authentication, the login access token has to be provided(PUSH) to the following end-point:

/auth/convert-token/

### which would return a local access token that needs to be provided in header for every request.
