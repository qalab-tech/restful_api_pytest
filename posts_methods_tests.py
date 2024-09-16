import pytest
import requests
from typing import Final
import yaml

config = yaml.safe_load(open("config.yaml"))
BASE_URL:  Final = config['API base URL']

@pytest.fixture
def new_post():
    """Post Creation Fixture"""
    return {
        "title": "Test Post",
        "body": "This is a test post body",
        "userId": 1
    }

def test_get_all_posts():
    """GET All Posts Test"""
    response = requests.get(BASE_URL)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0

def test_get_single_post():
    """GET One Post Test"""
    post_id = 1
    response = requests.get(f"{BASE_URL}/{post_id}")
    assert response.status_code == 200
    post = response.json()
    assert post['id'] == post_id
    assert 'title' in post
    assert 'body' in post

def test_create_post(new_post):
    """New Post Creation Test"""
    response = requests.post(BASE_URL, json=new_post)
    assert response.status_code == 201
    created_post = response.json()
    assert created_post['title'] == new_post['title']
    assert created_post['body'] == new_post['body']
    assert created_post['userId'] == new_post['userId']

def test_update_post(new_post):
    """Existed Post UPDATE Test"""
    post_id = 1
    updated_post = new_post.copy()
    updated_post['title'] = "Updated Title"
    response = requests.put(f"{BASE_URL}/{post_id}", json=updated_post)
    assert response.status_code == 200
    updated = response.json()
    assert updated['title'] == "Updated Title"

@pytest.mark.parametrize("post_id, partial_update, expected_status, expected_title", [
    (1, {"title": "Partially Updated Title"}, 200, "Partially Updated Title"),  # Standard title field update
    (2, {"body": "Updated Body Content"}, 200, None),  # Body field update
    (3, {"title": "New Title", "body": "New Body"}, 200, "New Title"),  # Two fields update
    (4, {}, 200, None),  # Empty JSON data example
    (5, {"title": None}, 200, None),  # Title field is None
    (6, {"non_existing_field": "New Value"}, 200, None),  # Non-existing field update attempt
])

def test_partial_update_post(post_id, partial_update, expected_status, expected_title):
    """Partial Update Test (PATCH) with different data"""
    response = requests.patch(f"{BASE_URL}/{post_id}", json=partial_update)
    assert response.status_code == expected_status
    updated_post = response.json()
    # Title update validation if it was in partial_update
    if "title" in partial_update:
        assert updated_post['title'] == expected_title
    else:
        assert 'title' in updated_post


def test_delete_post():
    """DELETE Post Test"""
    post_id = 1
    response = requests.delete(f"{BASE_URL}/{post_id}")
    assert response.status_code == 200
