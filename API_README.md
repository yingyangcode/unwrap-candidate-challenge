# Library Management System API

A REST API for managing books, customers, and borrowing operations in a library.

## Quick Start

### Prerequisites
- Python 3.12+

### Installation & Setup

1. **Install uv** (if not already installed):
   ```bash

   # Homebrew
   brew install uv

   # On macOS/Linux
   curl -LsSf https://astral.sh/uv/install.sh | sh
   
   # On Windows
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
   
   # Or with pip
   pip install uv
   ```

2. **Run the API** (dependencies will be automatically installed):
   ```bash
   uv run fastapi dev main.py --port 3000
   ```

3. **API will be available at:**
   - API: `http://localhost:3000`
   - Interactive docs: `http://localhost:3000/docs`

### Running Tests

```bash
uv run python test_library_api.py
```