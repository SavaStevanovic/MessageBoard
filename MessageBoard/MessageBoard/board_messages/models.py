from django.db import models

class Board(models.Model):
    name = models.CharField(max_length=200)
    order = models.IntegerField(default=0)
    pub_date = models.DateTimeField()
    def __str__(self):
        return self.name + ", " + str(self.order) + ", " + str(self.pub_date)


class List_board(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    order = models.IntegerField(default=0)
    pub_date = models.DateTimeField()
    def __str__(self):
        return str(self.board) + ", " + self.name + ", " + str(self.order) + ", " + str(self.pub_date)
    
class Card(models.Model):
    list = models.ForeignKey(List_board, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    card_text = models.TextField()
    order = models.IntegerField(default=0)
    pub_date = models.DateTimeField()    
    def __str__(self):
        return str(self.list) + ", " + self.name + ", " + self.card_text + ", " + str(self.order) + ", " + str(self.pub_date)
    
class Category(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
class User(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
class Comment(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    content = models.TextField()
    def __str__(self):
        return self.card + ", " + self.content
