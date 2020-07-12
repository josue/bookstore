## Development Setup

Requires: [docker-compose](https://docs.docker.com/compose/install/)

Makefile targets:

- `make stack_up` - Runs the startup command --> `docker-compose up --build -d`
- `make stack_down` - Runs the stop command --> `docker-compose down`
- `make stack_logs` - Runs the command to display logs --> `docker-compose logs -f`

*You can use the alternative docker-compose commands if you wish.*

----

## Bookstore API

API URL: `http://localhost:8000`

A bookstore API service with endpoints:

```json
{
    "users": "http://localhost:8000/users/",
    "books": "http://localhost:8000/books/",
    "transactions": "http://localhost:8000/transactions/",
    "library": "http://localhost:8000/library/"
}
```

**API Endpoints:**

List of Users:
```bash
curl -X GET 'http://127.0.0.1:8000/users/
```

User Details:
```bash
curl -X GET 'http://127.0.0.1:8000/users/14'
```

List of transaction *(Primary Ordering by Due date)*:
```bash
curl -X GET 'http://127.0.0.1:8000/transactions/'
```

Transaction Details:
```bash
curl -X GET 'http://127.0.0.1:8000/transactions/20'
```

List of books title, author, and isbn:
```bash
curl -X GET 'http://127.0.0.1:8000/books/
```

Book Details title, author, and isbn:
```bash
curl -X GET 'http://127.0.0.1:8000/books/11'
```

Users rented books past and current *(Order by due date)*:
```bash
curl -X GET 'http://127.0.0.1:8000/users/12/books/'
```

List of books in a library and their start:
```bash
curl -X GET 'http://127.0.0.1:8000/library/4/books/'
```

----

#### Django Admin Panel:
- URL: `http://localhost:8000/admin`
- Username: `admin`
- Password: `testpass`