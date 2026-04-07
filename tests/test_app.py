"""Tests for the FastAPI backend application"""

def test_root_redirect(client):
    """Test that GET / redirects to static index.html"""
    # Arrange
    # (client fixture provides TestClient with reset data)

    # Act
    response = client.get("/")

    # Assert
    assert response.status_code == 307  # Temporary redirect
    assert response.headers["location"] == "/static/index.html"


def test_get_activities(client):
    """Test that GET /activities returns all activities"""
    # Arrange
    # (client fixture provides TestClient with reset data)

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "Chess Club" in data
    assert "Programming Class" in data
    # Check structure of one activity
    chess_club = data["Chess Club"]
    assert "description" in chess_club
    assert "schedule" in chess_club
    assert "max_participants" in chess_club
    assert "participants" in chess_club
    assert isinstance(chess_club["participants"], list)


def test_signup_success(client):
    """Test successful signup for an activity"""
    # Arrange
    new_email = "newstudent@mergington.edu"
    activity_name = "Chess Club"

    # Act
    response = client.post(f"/activities/{activity_name}/signup",
                          params={"email": new_email})

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert new_email in data["message"]
    assert activity_name in data["message"]

    # Verify the email was added to participants
    activities_response = client.get("/activities")
    activities_data = activities_response.json()
    assert new_email in activities_data[activity_name]["participants"]


def test_signup_activity_not_found(client):
    """Test signup for non-existent activity returns 404"""
    # Arrange
    email = "test@mergington.edu"
    nonexistent_activity = "Nonexistent Club"

    # Act
    response = client.post(f"/activities/{nonexistent_activity}/signup",
                          params={"email": email})

    # Assert
    assert response.status_code == 404
    data = response.json()
    assert "detail" in data
    assert "Activity not found" in data["detail"]


def test_signup_duplicate_email(client):
    """Test signup with email already signed up returns 400"""
    # Arrange
    existing_email = "michael@mergington.edu"  # Already in Chess Club
    activity_name = "Chess Club"

    # Act
    response = client.post(f"/activities/{activity_name}/signup",
                          params={"email": existing_email})

    # Assert
    assert response.status_code == 400
    data = response.json()
    assert "detail" in data
    assert "Student already signed up" in data["detail"]