auth/users/
GET: Depending on the user status this will return the current user that is logged in. 
POST: This is how you register a new user. 

auth/users/men
GET: Return current user
PUT: Edit details of current user as in email.
DELETE: Removes the current user

get-token
POST: Posting username and password of a existing account will return the existing token or create a new one for the user. 

api/menu
GET: This endpoint will return a list of menu-items
POST: This should create a new item on the menu, you will get a success message. 

restaurant/booking
GET: Gets the current list of bookings.
POST: Creates new booking. 

index/
GET: Return the homepage of the LittleLemon Web Application
