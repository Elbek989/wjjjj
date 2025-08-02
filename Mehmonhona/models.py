from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class RoomSize(models.Model):
    title = models.CharField(max_length=100)
    context = models.TextField()

    def __str__(self):
        return self.title


class User(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    seria_id = models.IntegerField()
    phone = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Employee(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=100)
    seria_id = models.IntegerField()
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Room(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    id_room_type = models.ForeignKey(Category, on_delete=models.CASCADE)
    id_room_size = models.ForeignKey(RoomSize, on_delete=models.CASCADE)
    id_employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title, self.id_room_type}"


class Deal(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField()

    def __str__(self):
        return f"{self.id_user} - {self.id_room}"
