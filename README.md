TaskVerse is a simple yet powerful Django-based To-Do manager that helps you stay organized. It allows you to add, edit, and delete tasks while automatically tracking history for every change—so you always know what’s been done. Designed with a clean, responsive UI and easy setup, TaskVerse boosts your productivity right away.

Setup & Run Instructions
python -m venv myenv

source myenv/bin/activate

Copy the downloaded project files and paste them next to the myenv folder

pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

python manage.py runserver 4467

Important Note:
Always run the server on port 4456 (or the port specified in your settings). Running on the default port 8000 may cause CSS and static files to not load properly.
