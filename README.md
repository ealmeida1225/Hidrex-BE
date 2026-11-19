
# STEPS FOR CLONING 
```
cd existing_folder
git remote add origin https://github.com/ExtGroupJs/supermario_shop.git
git branch -M main
git push -uf origin main
```

# STEPS FOR DEVELOPING
1.  when the code is already cloned, install dependencies with [uv](https://docs.astral.sh/uv/) (uses `pyproject.toml`; Python **3.11.x** is recommended/required as specified):

```bash
uv sync
```

For deployment dependencies (Gunicorn, psycopg2-binary), run:

```bash
uv sync --extra deploy
```

For optional development tools (e.g., `runserver_plus` via Werkzeug), run:

```bash
uv sync --group dev
```

2. Make a copy of `REFERENCE.env` in the same directory and rename it to `.env`.

3. Run migrations (creates/syncs the database as configured):

```bash
uv run python manage.py migrate
```

<!-- 4. Create some dummy user objects (300):
uv run python manage.py create_test_users -->

4. Load initial data (promotes the default admin to SUPER_ADMIN, as applicable):

```bash
uv run python manage.py load_data
```

5. Run server:

```bash
uv run python manage.py runserver
```

6. API (Swagger): http://127.0.0.1:8000/api/swagger/

7. Optional HTTPS locally:

```bash
uv run python manage.py runserver_plus --cert-file localhost.crt --key-file localhost.key
```
