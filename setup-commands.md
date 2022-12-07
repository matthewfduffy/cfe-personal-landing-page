python -m pip install -r requirements.txt

%% Initial Django Project %%
django-admin startproject cfehome .
%% Additional 'apps' %%
python manage.py start _app <app_name>
(use plural name)
python manage.py runserver

Add views.py
Add urlsA
Add templates to settings.py -> 'DIRS': [BASE_DIR / "templates"],