# periwinkle-api

## Getting started with Development
### Pre-requisites
Before running the application, make sure you have the following installed:

* Python v3.12^
* uv v0.5.23^

```sh
# On macOS and Linux.
curl -LsSf https://astral.sh/uv/install.sh | sh

# On Windows.
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/The-Periwinkle-Project/periwinkle-api.git
   ```
2. Navigate to the project directory:
   ```bash
   cd periwinkle-api
   ```
3. Install dependencies:
   ```bash
    # Create the virtual environment within the project directory for code editors to use.
    uv venv --python 3.12.0

    # Activate the virtual environment

    # On macOS/Linux
    source .venv/bin/activate

    # On Windows
    .venv\Scripts\activate

    # Install all the dependencies for the package in a virtual environment
    uv pip install -e .

    # Install pre-commit hooks
    uv run pre-commit install
   ```

### Running from a virtual environment

1. If you haven't already, copy the example `.env.example` file to `.env` and edit with the necessary values.

2. Ensure all dependencies are installed using `uv pip install -e .`.

3. Start the API with Uvicorn, This can be done manually or through your editor.

    * If running manually, start uvicorn in the virtual environment with:
    ```bash
    uv run uvicorn app.main:app --host 0.0.0.0 --port 8000
    ```

4. Access the API at http://localhost:8000/docs
