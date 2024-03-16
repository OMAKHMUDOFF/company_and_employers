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

    def her_employees(self):
        employees = self.employees.all()
        for employee in employees:
            return employee

    def received_salary(self):
        if self.salary < 1000:
            return self.salary
        else:
            salary_count = 0
            new_salary = ""
            str_salary = str(self.salary)
            while 10**salary_count < self.salary:
                salary_count += 1
            else:
                for i in range(salary_count):
                    new_salary += str(self.salary % 10**i)

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
