# Data Browser

A frontend-only web application for browsing HuggingFace datasets with model and prompt type selection. This application can be hosted on GitHub Pages as a static website.

## Features

- Dropdown selection for models and prompt types
- Direct loading of datasets from HuggingFace using their Dataset Viewer API
- Displays query, source path, and predictions
- Navigation controls (next/back/jump to index)
- Client-side dataset caching for faster subsequent loads
- Pure frontend - no backend server required

## Usage

1. Open `index.html` in a web browser or host it on GitHub Pages
2. Select a model from the dropdown (e.g., "gpt-4.1-mini")
3. Select a prompt type (e.g., "original prompting" or "creative prompting")
4. Click "Load Dataset" to load the dataset from HuggingFace
5. Use the navigation controls to browse through instances:
   - **Back**: Go to previous instance
   - **Next**: Go to next instance
   - **Jump**: Navigate to a specific index

## Adding More Datasets

To add more datasets, edit the `DATASET_CONFIG` object in `index.html`:

```javascript
const DATASET_CONFIG = {
    "model-name": {
        "prompt-type": "huggingface-dataset-repo-name"
    }
};
```

## GitHub Pages Deployment

1. Push this directory to your GitHub repository
2. Enable GitHub Pages in your repository settings
3. Set the source to the branch containing this directory
4. Access your site at `https://yourusername.github.io/repository/projects/create/`

## Technical Details

- Uses HuggingFace Dataset Viewer API (`datasets-server.huggingface.co`) to load datasets
- Loads datasets in batches of 100 rows for efficient loading
- All data processing happens client-side in the browser
- **Python Support**: Uses Pyodide to run Python functions in the browser for data transformation
- Falls back to JavaScript if Python runtime is unavailable

## Using Python Functions

The application includes Pyodide, which allows you to write Python functions and call them from JavaScript. Example:

```javascript
// Call a Python function
const result = await callPythonFunction('format_source_path', triple1, triple2, triple3);
```

To add your own Python functions:

1. Add your function to the `pyodide.runPython()` call in `index.html`
2. Or edit `python_functions.py` and copy the functions to the HTML file
3. Create a JavaScript wrapper function if needed

Example Python function:
```python
def my_transformation(data):
    # Your Python code here
    return processed_data
```

Then call it from JavaScript:
```javascript
const result = await callPythonFunction('my_transformation', data);
```
