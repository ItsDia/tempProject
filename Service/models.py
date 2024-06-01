from django.db import models
class Service(models.Model):
    name = models.CharField(max_length=320)
    type = models.CharField(max_length=320)
    cost = models.IntegerField()
    input_concepts = models.JSONField()
    output_concepts = models.JSONField()

    def __str__(self):
        return f"Service(name={self.name}, cost={self.cost}, input_concepts={self.input_concepts}, output_concepts={self.output_concepts}, x={self.x}, y={self.y})"
