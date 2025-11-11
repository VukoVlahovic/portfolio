# Jupyter Notebook Integration

This portfolio includes a system for showcasing Jupyter notebooks from my data science projects.

## Directory Structure

```
portfolio/
├── notebooks/              # Store original .ipynb files here
├── templates/
│   └── notebooks/         # Converted HTML files stored here
├── convert_notebook.sh    # Conversion script
└── server.py             # Flask app with /notebooks/ route
```

## Workflow

### 1. Add My Notebook
Copy your `.ipynb` file from any project into the `notebooks/` folder:
```bash
cp /path/to/my/project/analysis.ipynb notebooks/
```

### 2. Convert to HTML
Run the conversion script:
```bash
./convert_notebook.sh my_notebook.ipynb
```

Or use the jupyter command directly:
```bash
jupyter nbconvert --to html notebooks/my_notebook.ipynb --output-dir=templates/notebooks
```

### 3. Access on Website
The notebook will be available at:
```
http://localhost:5000/notebooks/your_notebook.html
```

### 4. Link from My Portfolio
Add links in `templates/works.html` or create a dedicated projects page:
```html
<a href="/notebooks/my_notebook.html">View My Data Analysis Project</a>
```

## Requirements

Make sure `jupyter` is installed:
```bash
pip install jupyter nbconvert
```

## Tips

- Keep original `.ipynb` files in `notebooks/` so you can re-convert after updates
- Clear notebook outputs before converting for cleaner HTML (Cell > All Output > Clear)
- You can customize the HTML template used by nbconvert for better integration with your site's styling
- Consider adding a `.gitignore` entry for large notebook outputs if needed

## Sample Notebook

A sample notebook (`sample_data_analysis.ipynb`) is included in the `notebooks/` folder to demonstrate the workflow.
