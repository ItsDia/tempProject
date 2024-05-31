import django.db as models


class Parameter_Concept(models.Model):
    name = models.CharField(max_length=500)
    is_input = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} ({'Input' if self.is_input else 'Output'})"


class ServiceType(models.Model):
    name = models.CharField(max_length=500)
    concepts = models.ManyToManyField(Parameter_Concept, related_name='input_concepts_set')

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=500)
    cost = models.FloatField()
    input_concepts = models.ManyToManyField(Parameter_Concept, related_name='input_services')
    output_concepts = models.ManyToManyField(Parameter_Concept, related_name='output_services')
    x = models.FloatField(default=300)
    y = models.FloatField(default=0)
    type = models.ManyToManyField(ServiceType, related_name='services')

    def __str__(self):
        return f"Service(name={self.name}, cost={self.cost}, input_concepts={self.input_concepts}, output_concepts={self.output_concepts}, x={self.x}, y={self.y})"
