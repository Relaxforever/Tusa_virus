from django.db import models


class States(models.Model):
    """Creating the ORM for the text"""
    state = models.CharField(max_length=80)
    victims = models.IntegerField()

    def __str__(self):
        """Generate  a more clear representation """
        return self.state



