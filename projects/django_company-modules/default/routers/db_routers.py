# db_core
class CoreRouter:
    router_app_labels = {"admin", "auth", "contenttypes", "sessions", "admindocs", }
    def __init__(self) -> None:
        pass

    def db_for_read(self, model, **hints) -> str:
        if model._meta.app_label in self.router_app_labels:
            return "db_core"
        return None # type: ignore
    
    def db_for_write(self, model, **hints) -> str:
        if model._meta.app_label in self.router_app_labels:
            return "db_core"
        return None # type: ignore
    
    def allow_relation(self, obj1, obj2, **hints) -> bool:
        """ Allow relations if a model in the auth app is involved. For FK relations:\
            - If both models are in the auth app, allow the relation
            - If neither model is in the auth app, allow the relation
            - If one model is in the auth app, allow the relation
        """
        if (
            obj1._meta.app_label in self.router_app_labels or
            obj2._meta.app_label in self.router_app_labels
        ):
            return True
        return False
    
    def allow_migrate(self, db, app_label, model_name=None, **hints) -> bool:
        if app_label in self.router_app_labels:
            return db == "db_core"
        return False


# db_users
class UsersRouter:
    router_app_labels = {"register_login", }

    def __init__(self) -> None:
        pass
    
    def db_for_read(self, model, **hints) -> str:
        if model._meta.app_label in self.router_app_labels:
            return "db_users"
        return None # type: ignore
    
    def db_for_write(self, model, **hints) -> str:
        if model._meta.app_label in self.router_app_labels:
            return "db_users"
        return None # type: ignore

    def allow_relation(self, obj1, obj2, **hints) -> bool:
        if (
            obj1._meta.app_label in self.router_app_labels or
            obj2._meta.app_label in self.router_app_labels
        ):
            return True
        return False
    
    def allow_migrate(self, db, app_label, model_name=None, **hints) -> bool:
        if app_label in self.router_app_labels:
            return db == "db_users"
        return False


# db_warehouse
class WarehouseRouter:
    router_app_labels = {"warehouse", }

    def __init__(self) -> None:
        pass

    def db_for_read(self, model, **hints) -> str:
        if model._meta.app_label in self.router_app_labels:
            return "db_warehouse"
        return None # type: ignore
    
    def db_for_write(self, model, **hints) -> str:
        if model._meta.app_label in self.router_app_labels:
            return "db_warehouse"
        return None  # type: ignore
    
    def allow_relation(self, obj1, obj2, **hints) -> bool:
        if (
            obj1._meta.app_label in self.router_app_labels or
            obj2._meta.app_label in self.router_app_labels
        ):
            return True
        return False
    
    def allow_migrate(self, db, app_label, model_name=None, **hints) -> bool:
        if app_label in self.router_app_labels:
            return db == "db_warehouse"
        return False
