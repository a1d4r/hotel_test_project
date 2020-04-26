# Backend test task
### Run server
`python manage.py runserver`
### Enter admin menu
`http://127.0.0.1:8000/admin/`
with
- login: `admin`
- password: `admin`
### Login as user
`http://127.0.0.1:8000/login/`
with
- login: `userX`
- password `userX`

where X - number from 1 to 4. Users 1, 2, 3 are assigned hotels with corresponding ids.
### Index page
`http://127.0.0.1:8000/` (authentication is needed)
#### Logout
`http://127.0.0.1:8000/logout/`
#### Change password
`http://127.0.0.1:8000/change-password/`
## API
### List APIs
`http://127.0.0.1:8000/api/` (authentication is needed)
```
{
    "User list": "/users/",
    "User detail": "/users/<user_id>/",
    "Hotel list": "/hotels/",
    "Hotel detail": "/hotels/<hotel_id>/",
    "Room detail": "/hotels/<hotel_id>/rooms/<room_id>/",
    "Room list": [
        "/hotels/<hotel_id>/room-categories/<room_category_id>/rooms/",
        "/hotels/<hotel_id>/rooms/"
    ],
    "Room category detail": "/hotels/<hotel_id>/room-categories/<room_category_id>/",
    "Room category list": "/hotels/<hotel_id>/room-categories/",
    "Booking detail": "/hotels/<hotel_id>/bookings/<booking_id>",
    "Booking list": [
        "/hotels/<hotel_id>/bookings/",
        "/hotels/<hotel_id>/rooms/<room_id>/bookings/"
    ],
    "Create bookings': "/hotels/<hotel_id>/bookings/",
}
```
## Examples
`http://127.0.0.1:8000/api/hotels/`

`http://127.0.0.1:8000/api/hotels/3/room-categories/1/`

`http://127.0.0.1:8000/api/hotels/1/bookings/3`