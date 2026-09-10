def test_create_user_success(client):
    """Test successful creation/registration of a user."""
    payload = {
        "name": "John Doe",
        "email": "john@example.com",
        "password": "securepassword123"
    }

    response = client.post("/users", json=payload)
    assert response.status_code == 201

    data = response.get_json()
    assert "id" in data
    assert data["name"] == "John Doe"
    assert data["email"] == "john@example.com"
    assert "password" not in data  # Ensure password is not returned in responses
    assert "created_at" in data


def test_create_user_non_standard_email_accepted(client):
    """
    Test user creation accepts normal strings as email addresses.
    (Baseline behavior: email format validation is not yet implemented).
    """
    payload = {
        "name": "Plain User",
        "email": "invalid-email-format-without-at-symbol",
        "password": "password123"
    }

    response = client.post("/users", json=payload)
    assert response.status_code == 201

    data = response.get_json()
    assert data["email"] == "invalid-email-format-without-at-symbol"


def test_create_user_missing_required_fields(client):
    """Test user creation with missing required fields returns 400 Bad Request."""
    # Missing name
    response = client.post("/users", json={"email": "test@example.com", "password": "pass"})
    assert response.status_code == 400
    assert "Field 'name' is required" in response.get_json()["error"]

    # Missing email
    response = client.post("/users", json={"name": "Test", "password": "pass"})
    assert response.status_code == 400
    assert "Field 'email' is required" in response.get_json()["error"]

    # Missing password
    response = client.post("/users", json={"name": "Test", "email": "test@example.com"})
    assert response.status_code == 400
    assert "Field 'password' is required" in response.get_json()["error"]


def test_create_user_duplicate_email(client):
    """Test user creation with an existing email returns 409 Conflict."""
    payload = {
        "name": "Original User",
        "email": "duplicate@example.com",
        "password": "password123"
    }

    res1 = client.post("/users", json=payload)
    assert res1.status_code == 201

    res2 = client.post("/users", json=payload)
    assert res2.status_code == 409
    assert "already exists" in res2.get_json()["error"]


def test_get_all_users(client):
    """Test retrieving list of all users."""
    # Initially empty
    res = client.get("/users")
    assert res.status_code == 200
    assert res.get_json() == []

    # Add two users
    client.post("/users", json={"name": "User 1", "email": "user1@example.com", "password": "p1"})
    client.post("/users", json={"name": "User 2", "email": "user2@example.com", "password": "p2"})

    res = client.get("/users")
    assert res.status_code == 200
    data = res.get_json()
    assert len(data) == 2
    assert data[0]["name"] == "User 1"
    assert data[1]["name"] == "User 2"


def test_get_user_by_id(client):
    """Test retrieving a single user by ID."""
    create_res = client.post(
        "/users",
        json={"name": "Alice", "email": "alice@example.com", "password": "pass"}
    )
    user_id = create_res.get_json()["id"]

    # Get existing user
    res = client.get(f"/users/{user_id}")
    assert res.status_code == 200
    data = res.get_json()
    assert data["id"] == user_id
    assert data["name"] == "Alice"
    assert data["email"] == "alice@example.com"

    # Get non-existing user
    res_404 = client.get("/users/99999")
    assert res_404.status_code == 404
    assert "not found" in res_404.get_json()["error"]


def test_delete_user(client):
    """Test deleting a user by ID."""
    create_res = client.post(
        "/users",
        json={"name": "Bob", "email": "bob@example.com", "password": "pass"}
    )
    user_id = create_res.get_json()["id"]

    # Delete user
    del_res = client.delete(f"/users/{user_id}")
    assert del_res.status_code == 200
    assert "deleted successfully" in del_res.get_json()["message"]

    # Verify user is deleted
    get_res = client.get(f"/users/{user_id}")
    assert get_res.status_code == 404

    # Delete non-existing user
    del_404 = client.delete(f"/users/{user_id}")
    assert del_404.status_code == 404
    assert "not found" in del_404.get_json()["error"]
