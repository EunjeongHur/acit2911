# acit2911

## Set up & Installation

### 1. Create a virtual environment
```bash
cd [folder]
py -3 -m venv [venv_name]
```

```
ex)
cd acit2911
py -3 -m venv my_env
```

### 2. Activate the virtual environment
```
[venv_name]\Scripts\activate.ps1
```
In VSCode, go to **select interpreter** and change default path to venv interpreter path.
### 3. Install the requirements
```
cd [folder]
pip install -r requirements.txt
```

```
ex)
cd acit2911
pip install -r requirements.txt
```

### 4. Migrate/Create a datbase

Run manage.py file
```
python manage.py
```

### 5. Run app

Before running the app, make sure your virtual environment is on!!
```
python routes.py
```
