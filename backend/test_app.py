import pytest
import json
from app import app

@pytest.fixture
def client():
    """Create test client"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_endpoint(client):
    """Test health check endpoint"""
    response = client.get('/health')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['status'] == 'healthy'

def test_root_endpoint(client):
    """Test root endpoint"""
    response = client.get('/')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'message' in data
    assert 'endpoints' in data

def test_get_movies(client):
    """Test getting all movies"""
    response = client.get('/api/movies')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'movies' in data
    assert 'count' in data
    assert data['count'] > 0
    assert len(data['movies']) > 0

def test_get_specific_movie(client):
    """Test getting a specific movie"""
    response = client.get('/api/movies/1')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'movie' in data
    assert data['movie']['id'] == 1

def test_get_nonexistent_movie(client):
    """Test getting a movie that doesn't exist"""
    response = client.get('/api/movies/999')
    assert response.status_code == 404
    data = json.loads(response.data)
    assert 'error' in data

def test_movie_structure(client):
    """Test that movies have required fields"""
    response = client.get('/api/movies')
    assert response.status_code == 200
    data = json.loads(response.data)
    movies = data['movies']
    
    for movie in movies:
        assert 'id' in movie
        assert 'title' in movie
        assert 'year' in movie
        assert 'director' in movie
        assert 'genre' in movie
        assert 'rating' in movie
        assert 'description' in movie
