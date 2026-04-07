import pytest
from fastapi.testclient import TestClient
from src.app import app as fastapi_app, activities

# Initial activities data for resetting between tests
INITIAL_ACTIVITIES = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    },
    "Basketball Team": {
        "description": "Join the school basketball team and compete in leagues",
        "schedule": "Mondays and Wednesdays, 4:00 PM - 5:30 PM",
        "max_participants": 15,
        "participants": ["alex@mergington.edu"]
    },
    "Soccer Club": {
        "description": "Practice soccer skills and play friendly matches",
        "schedule": "Tuesdays and Thursdays, 4:00 PM - 5:30 PM",
        "max_participants": 20,
        "participants": ["sarah@mergington.edu", "james@mergington.edu"]
    },
    "Art Studio": {
        "description": "Explore painting, drawing, and sculpture techniques",
        "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
        "max_participants": 16,
        "participants": ["lucy@mergington.edu"]
    },
    "Music Band": {
        "description": "Learn to play instruments and perform in concerts",
        "schedule": "Mondays and Fridays, 3:30 PM - 4:30 PM",
        "max_participants": 25,
        "participants": ["nicholas@mergington.edu", "grace@mergington.edu"]
    },
    "Debate Club": {
        "description": "Develop public speaking and critical thinking skills",
        "schedule": "Thursdays, 4:00 PM - 5:30 PM",
        "max_participants": 18,
        "participants": ["thomas@mergington.edu"]
    },
    "Science Club": {
        "description": "Conduct experiments and explore scientific concepts",
        "schedule": "Tuesdays, 3:30 PM - 5:00 PM",
        "max_participants": 22,
        "participants": ["jessica@mergington.edu", "ryan@mergington.edu"]
    }
}


@pytest.fixture
def client():
    """Fixture to provide a TestClient for the FastAPI app"""
    # Reset activities to initial state before each test
    activities.clear()
    activities.update(INITIAL_ACTIVITIES)
    return TestClient(fastapi_app, follow_redirects=False)