class StoreDatabaseRouter:
    def db_for_read(self, model, **hints):
        """
        Directs read operations to the appropriate store database.
        """
        store = hints.get("store")
        if store in ["store1", "store2", "store3"]:
            return store
        return "default"

    def db_for_write(self, model, **hints):
        """
        Directs write operations to the appropriate store database.
        """
        store = hints.get("store")
        if store in ["store1", "store2", "store3"]:
            return store
        return "default"

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations between objects in the same database.
        """
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Control where migrations are applied:
        - 'auth' and 'contenttypes' go to 'default' (main database).
        - Store-specific models go to their respective databases.
        """
        if app_label in ["auth", "contenttypes", "admin", "sessions","users"]:
            return db == "default"  # Keep users in the main database
        elif db in ["store1", "store2", "store3"]:
            return True  # Allow store models in store databases
        return None  # Default behavior
