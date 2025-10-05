import React from 'react';
import { render, screen, waitFor } from '@testing-library/react';
import axios from 'axios';
import App from './App';

// Mock axios
jest.mock('axios');
const mockedAxios = axios;

describe('App Component', () => {
  beforeEach(() => {
    mockedAxios.get.mockClear();
  });

  test('renders loading state initially', () => {
    mockedAxios.get.mockImplementation(() => new Promise(() => {})); // Never resolves
    
    render(<App />);
    expect(screen.getByText('Loading movies...')).toBeInTheDocument();
  });

  test('renders movies after successful API call', async () => {
    const mockMovies = [
      {
        id: 1,
        title: 'Test Movie',
        year: 2023,
        director: 'Test Director',
        genre: 'Action',
        rating: 8.5,
        description: 'A test movie description'
      }
    ];

    mockedAxios.get.mockResolvedValueOnce({
      data: { movies: mockMovies }
    });

    render(<App />);

    await waitFor(() => {
      expect(screen.getByText('Test Movie')).toBeInTheDocument();
    });

    expect(screen.getByText('Test Director')).toBeInTheDocument();
    expect(screen.getByText('Action')).toBeInTheDocument();
    expect(screen.getByText('⭐ 8.5/10')).toBeInTheDocument();
  });

  test('renders error message when API call fails', async () => {
    mockedAxios.get.mockRejectedValueOnce(new Error('API Error'));

    render(<App />);

    await waitFor(() => {
      expect(screen.getByText(/Failed to fetch movies/)).toBeInTheDocument();
    });

    expect(screen.getByText('Retry')).toBeInTheDocument();
  });

  test('displays API URL information', async () => {
    mockedAxios.get.mockResolvedValueOnce({
      data: { movies: [] }
    });

    render(<App />);

    await waitFor(() => {
      expect(screen.getByText(/API URL:/)).toBeInTheDocument();
    });
  });

  test('displays total movie count', async () => {
    const mockMovies = [
      { id: 1, title: 'Movie 1', year: 2023, director: 'Director 1', genre: 'Action', rating: 8.0, description: 'Description 1' },
      { id: 2, title: 'Movie 2', year: 2023, director: 'Director 2', genre: 'Comedy', rating: 7.5, description: 'Description 2' }
    ];

    mockedAxios.get.mockResolvedValueOnce({
      data: { movies: mockMovies }
    });

    render(<App />);

    await waitFor(() => {
      expect(screen.getByText('Total Movies: 2')).toBeInTheDocument();
    });
  });
});
