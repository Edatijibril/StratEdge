# StratEdge Innovation Consulting - Flask website

    python -m venv venv && source venv/bin/activate   # Windows: venv\Scripts\activate
    pip install -r requirements.txt
    python app.py                                      # http://127.0.0.1:5000

Production: `SECRET_KEY=your-secret gunicorn app:app`

- Edit contact details, services and copy at the top of `app.py`.
- Contact form submissions are saved to `messages.jsonl`.
- Brand colours are CSS variables at the top of `static/css/style.css`.
