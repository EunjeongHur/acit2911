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

## Git commands

Don't forget **git pull** in the main branch before make changes

To create branch,
``` git branch [branch_name] ```

To change branch,
``` git checkout [branch_name] ```


To check status,
``` git status ```

To add change,
``` git add [filename]```

To commit change,
``` git commit -m '[commit_msg]'```

To push changes to repository,
``` git push origin [branch_name]```

To delete branch,
```git branch -d [branch_name]```

```
ex)
git pull (in the main)
git branch example
git checkout example
**Make changes, Edit file**
git commit -m 'Edited ReadMe'
git push origin example
**In github repository page, click 'pull request'**
git checkout main
git pull
git branch -d example
```
