# News API Project

This project is a Django-based REST API for managing news articles and their associated journalists. It allows users to perform CRUD operations on articles and view details about journalists. The project is built using the Django REST Framework (DRF).

---

## Features

- **CRUD Operations on Articles:**
  - Create, read, update, and delete news articles through API endpoints.
  - Filter active articles.

- **Journalist Management:**
  - View details of journalists and their associated articles.

- **REST API Design:**
  - Class-based API views for structured and maintainable code.
  - Serialization for input validation and structured output.

- **Field Validations:**
  - Custom field validations for `title` and `description`. Example: Titles cannot be "test" or identical to descriptions.

---

## Technologies Used

- **Backend:**
  - Django 5.1
  - Django REST Framework
- **Database:**
  - SQLite (default setup; can easily be changed to PostgreSQL or others)
- **Utilities:**
  - `timesince` utility from Django for displaying time since article publication.

---

## Installation and Setup

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Create and Activate a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Database Migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

6. Access the API at `http://127.0.0.1:8000/api/`.

---

## API Endpoints

### Articles

| Method | Endpoint                          | Description                                |
|--------|-----------------------------------|--------------------------------------------|
| `GET`  | `/api/articles/`                  | Fetch a list of all active articles.       |
| `POST` | `/api/articles/`                  | Create a new article.                      |
| `GET`  | `/api/articles/<int:pk>/`         | Fetch details of a specific article.       |
| `PUT`  | `/api/articles/<int:pk>/`         | Update an existing article.                |
| `DELETE` | `/api/articles/<int:pk>/`       | Delete an article.                         |

### Journalists

Currently, journalist CRUD operations are managed via the Django Admin interface.

---

## Project Structure

- **models.py**:
  Defines the `Article` and `Journalist` models.

- **serializers.py**:
  Responsible for input validation and formatting API data for the `Article` and `Journalist` models.

- **views.py**:
  Contains class-based views (`APIView`) for handling business logic.

- **urls.py**:
  Defines endpoints for accessing API views.

- **admin.py**:
  Registers the `Article` and `Journalist` models in the Django Admin.

---

## Validations and Business Rules

- Articles must have unique `title` and `description`.
- `title` cannot have the value `"test"`.
- A `time_since_publication` field is calculated dynamically for each article.

---

## Development Notes

1. **Admin Setup**:
   - Use the Django admin interface at `/admin/` to manage journalists and articles.
   - Run `python manage.py createsuperuser` to create an admin user.

2. **Custom Field Validation**:
   - Errors are raised for invalid input in `serializers.py`.

3. **Extensibility**:
   - The project can be extended to include features like authentication, permissions, and pagination.

---

## Known Limitations

- Currently uses SQLite for development; not recommended for production.
- Basic validation rules are set; stricter checks can be added as needed.
- No authentication or authorization implemented yet.

---

## Future Enhancements

- Add user authentication and permissions.
- Implement pagination in the API.
- Extend journalist functionality with endpoints.
- Unit tests for all API endpoints.

---

## Contributing

1. Fork the project.
2. Create a new branch (`feature/some-feature`).
3. Commit changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/some-feature`).
5. Create a Pull Request.

---

## Acknowledgements

- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
