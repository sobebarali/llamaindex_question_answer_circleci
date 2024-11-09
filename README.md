# Q&A Service

This project is a Q&A service built using Flask, which allows users to query a set of documents and receive answers. The service uses a vector store index to efficiently handle queries.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Testing](#testing)
- [Continuous Integration](#continuous-integration)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/sobebarali/llamaindex_question_answer_circleci.git
   cd llamaindex_question_answer_circleci
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**

   Create a `.env` file in the root directory and add any necessary environment variables.

## Usage

1. **Run the Flask application:**

   ```bash
   python src/main.py
   ```

2. **Access the service:**

   Open your browser and go to `http://127.0.0.1:5000/` to access the Q&A service.

3. **Query the service:**

   Use the `/answer` endpoint to post JSON queries and receive answers.

## Project Structure

- `src/`: Contains the main application code.
  - `__init__.py`: Initializes the Flask app.
  - `main.py`: Entry point for running the app.
  - `query.py`: Handles loading and querying the index.
  - `routes.py`: Defines the API routes.

- `tests/`: Contains unit tests for the application.
  - `test_app.py`: Tests for the Flask application.
  - `test_query.py`: Tests for the query functionality.

- `data/`: Contains sample data files.

- `storage/`: Contains storage files for the vector store index.

- `.circleci/`: Contains CI/CD configuration files.

## Testing

 ```bash
  pytest
   ```

## Continuous Integration

This project uses CircleCI for continuous integration. The configuration is located in `.circleci/config.yml`.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
