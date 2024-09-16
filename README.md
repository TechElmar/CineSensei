# CineSensei Movie Recommendation System

CineSensei is a Python-based movie recommendation system that helps users find popular movies based on their genre preferences. The system fetches movie data from The Movie Database (TMDb) API and provides recommendations with user ratings.

## Features

- Fetches and displays popular movies based on selected genres.
- Provides movie recommendations with user rating percentages.
- Allows users to get a random movie recommendation if they can't decide.

## Installation

To set up the CineSensei project on your local machine, follow these steps:

1. **Clone the repository**

    ```bash
    git clone https://github.com/yourusername/cinesensei.git
    ```

2. **Navigate into the project directory**

    ```bash
    cd cinesensei
    ```

3. **Create a virtual environment (optional but recommended)**

    ```bash
    python -m venv venv
    ```

4. **Activate the virtual environment**

    - On Windows

        ```bash
        venv\Scripts\activate
        ```

    - On MacOS/Linux

        ```bash
        source venv/bin/activate
        ```

5. **Install dependencies**

    The project requires the `requests` library. Install it using:

    ```bash
    pip install requests
    ```

6. **Set up your TMDb API key**

    Replace `'your_api_key_here'` in the `main.py` file with your actual TMDb API key. You can obtain an API key by signing up on the [TMDb website](https://www.themoviedb.org/).

## Usage

To run the CineSensei movie recommendation system, use the following command:

```bash
python main.py
