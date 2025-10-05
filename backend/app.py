import os
import logging
from flask import Flask, jsonify
from flask_cors import CORS

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

# Sample movie data
MOVIES = [
    {
        "id": 1,
        "title": "The Shawshank Redemption",
        "year": 1994,
        "director": "Frank Darabont",
        "genre": "Drama",
        "rating": 9.3,
        "description": "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency."
    },
    {
        "id": 2,
        "title": "The Godfather",
        "year": 1972,
        "director": "Francis Ford Coppola",
        "genre": "Crime",
        "rating": 9.2,
        "description": "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son."
    },
    {
        "id": 3,
        "title": "The Dark Knight",
        "year": 2008,
        "director": "Christopher Nolan",
        "genre": "Action",
        "rating": 9.0,
        "description": "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice."
    },
    {
        "id": 4,
        "title": "Pulp Fiction",
        "year": 1994,
        "director": "Quentin Tarantino",
        "genre": "Crime",
        "rating": 8.9,
        "description": "The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption."
    },
    {
        "id": 5,
        "title": "Forrest Gump",
        "year": 1994,
        "director": "Robert Zemeckis",
        "genre": "Drama",
        "rating": 8.8,
        "description": "The presidencies of Kennedy and Johnson, the Vietnam War, the Watergate scandal and other historical events unfold from the perspective of an Alabama man with an IQ of 75."
    },
    {
        "id": 6,
        "title": "Inception",
        "year": 2010,
        "director": "Christopher Nolan",
        "genre": "Sci-Fi",
        "rating": 8.8,
        "description": "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O."
    },
    {
        "id": 7,
        "title": "The Matrix",
        "year": 1999,
        "director": "The Wachowskis",
        "genre": "Sci-Fi",
        "rating": 8.7,
        "description": "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers."
    },
    {
        "id": 8,
        "title": "Goodfellas",
        "year": 1990,
        "director": "Martin Scorsese",
        "genre": "Crime",
        "rating": 8.7,
        "description": "The story of Henry Hill and his life in the mob, covering his relationship with his wife Karen Hill and his mob partners Jimmy Conway and Tommy DeVito."
    }
]

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "healthy", "message": "Backend service is running"}), 200

@app.route('/api/movies', methods=['GET'])
def get_movies():
    """Get all movies"""
    try:
        logger.info("Fetching movies data")
        return jsonify({
            "movies": MOVIES,
            "count": len(MOVIES),
            "message": "Movies retrieved successfully"
        }), 200
    except Exception as e:
        logger.error(f"Error fetching movies: {str(e)}")
        return jsonify({"error": "Failed to fetch movies"}), 500

@app.route('/api/movies/<int:movie_id>', methods=['GET'])
def get_movie(movie_id):
    """Get a specific movie by ID"""
    try:
        movie = next((m for m in MOVIES if m['id'] == movie_id), None)
        if movie:
            return jsonify({"movie": movie}), 200
        else:
            return jsonify({"error": "Movie not found"}), 404
    except Exception as e:
        logger.error(f"Error fetching movie {movie_id}: {str(e)}")
        return jsonify({"error": "Failed to fetch movie"}), 500

@app.route('/', methods=['GET'])
def root():
    """Root endpoint"""
    return jsonify({
        "message": "Movie Picture Pipeline Backend API",
        "version": "1.0.0",
        "endpoints": {
            "movies": "/api/movies",
            "health": "/health"
        }
    }), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') == 'development'
    app.run(host='0.0.0.0', port=port, debug=debug)
