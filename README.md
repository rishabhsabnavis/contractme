<<<<<<< HEAD
# ContractMe API

A FastAPI-based application for processing and analyzing contract documents using LangChain and LangGraph.

## Features

- **Document Processing**: Upload and process contract documents
- **Contract Analysis**: Extract and analyze contract content
- **API Endpoints**: RESTful API for document processing
- **LangGraph Integration**: State management for contract processing workflows

## Project Structure

```
Contractor/
├── agent/
│   └── agent.py          # LangGraph agent implementation
├── data_pipeline/
│   ├── injest.py         # Data ingestion utilities
│   └── retriever.py      # Data retrieval components
├── app.py                # Main application entry point
├── main.py               # FastAPI application
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd Contractor
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

## Usage

### Running the API

Start the FastAPI server:

```bash
python main.py
```

The API will be available at `http://localhost:8000`

### API Endpoints

- `GET /`: Health check endpoint
- `POST /upload`: Upload and process documents

### Example Usage

```python
import requests

# Upload a document
with open("contract.pdf", "rb") as f:
    files = {"file": ("contract.pdf", f, "application/pdf")}
    response = requests.post("http://localhost:8000/upload", files=files)
    print(response.json())
```

Or using curl:

```bash
curl -X POST "http://localhost:8000/upload" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@your_document.pdf"
```

## Development

### Running Tests

```bash
# Add test commands here when tests are implemented
```

### Code Style

This project follows PEP 8 style guidelines.

## Dependencies

Key dependencies include:
- FastAPI: Web framework
- LangChain: LLM framework
- LangGraph: State management for workflows
- Pydantic: Data validation
- Uvicorn: ASGI server

See `requirements.txt` for the complete list of dependencies.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

[Add your license information here]

## Contact

[Add your contact information here] 
=======
# contractme
>>>>>>> ca7f6243d04d1cc7f8bc4fc69fab08c1579d4cdf
