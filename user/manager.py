from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin      


class UserAccountManager(BaseUserManager):
    # Create a user
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError("User must have an email address")
        if not name:
            raise ValueError("User must have a name")

        email = self.normalize_email(email)
        email = email.lower()
        user = self.model(
            email=email,
            name=name,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user
    #--------------Create Realtor---------------------------
    def create_realtor(self, email, name, password=None):
        user = self.create_user(email, name, password)
        user.is_realtor = True
        user.save(using=self._db)

        return user
    #----------------Create Superuser---------------------------
    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)

        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user
