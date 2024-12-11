import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home_get(client):
    """Test the home page with a GET request."""
    rv = client.get("/")
    assert rv.status_code == 200
    assert b"Welcome to the Sports Workout Planner App!" in rv.data


def test_workout_valid(client):
    """Test the /workout route with a valid query parameter."""
    rv = client.get("/workout?part=arms")
    assert rv.status_code == 200
    assert b"Bicep Curls" in rv.data  # Ensure your JSON file contains "Bicep Curls"


def test_workout_invalid(client):
    """Test the /workout route with an invalid query parameter."""
    rv = client.get("/workout?part=unknown")
    assert rv.status_code == 404
    assert b"Sorry, we don't have a workout plan for 'unknown'." in rv.data


def test_workout_missing(client):
    """Test the /workout route with a missing query parameter."""
    rv = client.get("/workout")
    assert rv.status_code == 400
    assert b"Please specify a body part using the 'part' query parameter." in rv.data
