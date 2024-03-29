from django.db import models


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Companies"

    def __str__(self) -> str:
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Positiones"

    def __str__(self) -> str:
        return self.name


class Employer(models.Model):
    name = models.CharField(max_length=255)
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="employers"
    )
    position = models.ForeignKey(Position, on_delete=models.DO_NOTHING)
    salary = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    def him_employees(self):
        employees = self.employees.all()
        for employee in employees:
            return employee

    def received_salary(self):
        if self.salary < 1000:
            return self.salary
        else:
            new_salary = f"{self.salary:,}".replace(",", ".")
            return new_salary


class Employee(models.Model):
    name = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    employer = models.ForeignKey(
        Employer, on_delete=models.DO_NOTHING, related_name="employees"
    )
    position = models.ForeignKey(Position, on_delete=models.DO_NOTHING)
    salary = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
