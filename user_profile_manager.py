import datetime
import weakref


class ValidatedProperty:
    def __init__(self,property_name):
        pass

    def __set_name__(self, owner_class, property_name):
        self.property_name = property_name
        print(f'New {self.property_name}')

    def __set__(self, instance, value):
        if self.property_name == 'username':
            print(f' {self.property_name} block')
            if not isinstance(value, str) or len(value)<1:
                raise ValueError("username must be as non-empty string")
            instance.__dict__[self.property_name] = value

        if self.property_name == 'email':
            print(f' {self.property_name} block')

            if not isinstance(value, str) or '@' not in value or '.' not in value:
                raise ValueError("email must contain '@' and '.' characters")
            
            instance.__dict__[self.property_name] = value

        if self.property_name == 'last_login':
            print(f' {self.property_name} block')

            if value is not None and not isinstance(value, datetime):
                raise ValueError("last_login must be a datetime object or None")
            instance.__dict__[self.property_name] = value


    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            print (f'calling __get__ for {self.property_name}')
            return instance.__dict__.get(self.property_name, None)
        
class UserProfileManager:
        username = ValidatedProperty('username')
        email = ValidatedProperty('email')
        last_login = ValidatedProperty('last_login')

        _cache = {}

        @classmethod
        def add_to_cache(cls, instance):
            cls._cache[id(instance)] = weakref.ref(instance)

        @classmethod 
        def get_from_cache(cls, uid):
            if uid in cls._cache:
                return cls._cache[uid]()
            return None
