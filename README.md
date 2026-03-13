how to set up the environment and run the FastAPI app:

markdown
# EMT-FastAPI-REACT

## 🚀 Setup Instructions

Follow these steps every time you clone this project to a new machine:

### 1. Create and activate virtual environment
```python -m venv .venv```
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
2. Install dependencies

```pip install uvicorn```

```pip install fastapi[all]```
3. Run the FastAPI server

4. ```uvicorn main:app --reload```

5. Run the React frontend
Navigate to the React project folder and install dependencies:
```npm install```
```npm start```