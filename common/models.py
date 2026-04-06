from django.db import models
from common.manager import GeneralManager, AllObjectsManager
from django.utils import timezone
from django.utils.timezone import now

# Utils/Timezone models


class TimeStampedModel(models.Model):
    # Utility fields
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    is_published = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=now)

    # Make abstract so that it doesn't create a table in the database
    class Meta:
        abstract = True


# -------------Abstract class for all models in the project-------------#
class SoftDeleteModel(models.Model):
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    objects = GeneralManager()
    all_objects = AllObjectsManager()

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False, hard=False):
        if hard:
            return super().delete(using=using, keep_parents=keep_parents)
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        self.is_deleted = False
        self.deleted_at = None
        self.save()


# -----------Join TimeStampedModel and BaseModel to create a common base model for all models in the project-----------#
class CommonModel(TimeStampedModel, SoftDeleteModel):
    class Meta:
        abstract = True