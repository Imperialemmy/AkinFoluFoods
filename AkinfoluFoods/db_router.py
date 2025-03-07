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
    """Control migrations for multiple databases."""
    if app_label == "users":
        return db == "default" or db.startswith("store")  # Allow user migrations in all DBs
    return db.startswith("store")  # Other apps go to store databases
