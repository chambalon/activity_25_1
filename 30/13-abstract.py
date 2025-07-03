from abc import ABC, abstractmethod

class Book(ABC,object):
  def __init__(self,author):
    self.author = author

  @abstractmethod
  def display(self):
    pass

class Mybook(Book):
  def __init__(self,author, title,price):
    Book.__init__(self,author)
    self.title = title
    self.price = price

  def display(self):
    print(f'Author: {author}')
    print(f'Title: {title}')
    print(f'Price: {price}')


author = input()
title = input()
price = int(input())

mybook = Mybook(author,title,price)
mybook.display()