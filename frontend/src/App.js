import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

const API_URL = process.env.REACT_APP_MOVIE_API_URL || 'http://localhost:5000';

function App() {
  const [movies, setMovies] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchMovies();
  }, []);

  const fetchMovies = async () => {
    try {
      setLoading(true);
      const response = await axios.get(`${API_URL}/api/movies`);
      setMovies(response.data.movies);
      setError(null);
    } catch (err) {
      setError('Failed to fetch movies. Please check if the backend is running.');
      console.error('Error fetching movies:', err);
    } finally {
      setLoading(false);
    }
  };

  const MovieCard = ({ movie }) => (
    <div className="movie-card">
      <div className="movie-header">
        <h3 className="movie-title">{movie.title}</h3>
        <span className="movie-year">({movie.year})</span>
      </div>
      <div className="movie-details">
        <p className="movie-director"><strong>Director:</strong> {movie.director}</p>
        <p className="movie-genre"><strong>Genre:</strong> {movie.genre}</p>
        <p className="movie-rating"><strong>Rating:</strong> ⭐ {movie.rating}/10</p>
      </div>
      <p className="movie-description">{movie.description}</p>
    </div>
  );

  if (loading) {
    return (
      <div className="app">
        <header className="app-header">
          <h1>Movie Picture Pipeline</h1>
          <p>Loading movies...</p>
        </header>
      </div>
    );
  }

  if (error) {
    return (
      <div className="app">
        <header className="app-header">
          <h1>Movie Picture Pipeline</h1>
          <div className="error-message">
            <p>{error}</p>
            <button onClick={fetchMovies} className="retry-button">
              Retry
            </button>
          </div>
        </header>
      </div>
    );
  }

  return (
    <div className="app">
      <header className="app-header">
        <h1>Movie Picture Pipeline</h1>
        <p>Discover amazing movies from our collection</p>
        <div className="api-info">
          <small>API URL: {API_URL}</small>
        </div>
      </header>
      
      <main className="movies-container">
        <div className="movies-grid">
          {movies.map((movie) => (
            <MovieCard key={movie.id} movie={movie} />
          ))}
        </div>
      </main>
      
      <footer className="app-footer">
        <p>Total Movies: {movies.length}</p>
      </footer>
    </div>
  );
}

export default App;
