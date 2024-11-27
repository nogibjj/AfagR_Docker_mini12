# import pytest
# from app import app


# @pytest.fixture
# def client():
#     """
#     Set up a test client for the Flask app.
#     """
#     app.config["TESTING"] = True
#     with app.test_client() as client:
#         yield client


# def test_home_page(client):
#     """
#     Test if the home page loads successfully.
#     """
#     rv = client.get("/")
#     assert rv.status_code == 200
#     assert b"Welcome to the Sports Workout Planner App!" in rv.data


# def test_workout_endpoint_valid(client):
#     """
#     Test the workout endpoint with a valid body part.
#     """
#     rv = client.get("/workout?part=arms")
#     assert rv.status_code == 200
#     assert b"Bicep Curls" in rv.data  # Check if a valid exercise is returned


# def test_workout_endpoint_invalid(client):
#     """
#     Test the workout endpoint with an invalid body part.
#     """
#     rv = client.get("/workout?part=unknown")
#     assert rv.status_code == 404
#     assert b"Sorry, we don't have a workout plan for 'unknown'." in rv.data


# def test_workout_endpoint_missing(client):
#     """
#     Test the workout endpoint without specifying a body part.
#     """
#     rv = client.get("/workout")
#     assert rv.status_code == 400
#     assert b"Please specify a body part" in rv.data

import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home(client):
    rv = client.get("/")
    assert rv.status_code == 200
    assert b"Welcome to the Sports Workout Planner App!" in rv.data


def test_workout_valid(client):
    rv = client.get("/workout?part=arms")
    assert rv.status_code == 200
    assert b"Bicep Curls" in rv.data


def test_workout_invalid(client):
    rv = client.get("/workout?part=unknown")
    assert rv.status_code == 404
    assert b"Sorry, we don't have a workout plan" in rv.data


def test_workout_missing(client):
    rv = client.get("/workout")
    assert rv.status_code == 400
    assert b"Please specify a body part" in rv.data
