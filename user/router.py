class AuthRouter:
    """
    A router to control all database operations on models in the
    auth application.
    """
    route_app_labels = {'user', 'auth', 'contenttypes', 'sessions', 'admin'}

    def db_for_read(self, model, **hints):
        """
        Attempts to read auth models go to users_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'users'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth models go to users_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'users'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth app is involved.
        """
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth app only appears in the 'users_db'
        database.
        """
        if app_label in self.route_app_labels:
            return db == 'users'
        if db == 'users':
            return False
        return None
    
##     python manage.py makemigrations --database=users
##     python manage.py migrate --database=users
##     python manage.py create_superuser --database=users