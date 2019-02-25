import numpy as np
import cv2
import os

class Animal:

	def __init__(self, name, color, age, image):
		self.name = name
		self.color = color
		self.age = age
		self.image = image
	
	def sound():
		pass


class Cat(Animal):

	def __init__(self, name, color, age, image):
		super().__init__(name, color, age, image)

	def sound(self):
		print('MIAU!')
		

class Dog(Animal):

	def __init__(self, name, color, age, image):
		super().__init__(name, color, age, image)

	def sound(self):
		print('GUAU!')
		

class Spider(Animal):

	def __init__(self, name, color, age, image):
		super().__init__(name, color, age, image)
		
	def sound(self):
		print('...')

def main():

	animals = []

	cat_1 = Cat('Nitrito', 'white', '7', os.path.dirname(os.path.abspath(__file__))+'/images/nitrito.jpeg')
	animals.append(cat_1)
	cat_2 = Cat('Sifu', 'brown', '15', os.path.dirname(os.path.abspath(__file__))+'/images/sifu.jpg')
	animals.append(cat_2)
	dog_1 = Dog('Gohan', 'black', '5', os.path.dirname(os.path.abspath(__file__))+'/images/gohan.jpeg')
	animals.append(dog_1)
	spider_1 = Spider('Tarantina', 'black', 'unknown', os.path.dirname(os.path.abspath(__file__))+'/images/tarantina.jpeg')
	animals.append(spider_1)


	print('****** ANIMALS INFORMATION ******\n')
	print('LIST:')
	for x in animals:
		print(x.name)

	selec = str(input('Please choose an animal\n'))

	for x in animals:
		if selec == x.name:
			print('\nINFORMATION')
			print('Name:', x.name)
			print('Color:', x.color)
			print('Age:', x.age)
			print()
			sound = str(input('Do you want to see {}s sound? (y/n)'.format(x.name)))
			if sound == 'y':
				x.sound()

			image = str(input('Do you want to see {}s image? (y/n)'.format(x.name)))
			if image == 'y':
				img = cv2.imread(x.image,1)
				cv2.namedWindow(x.name,cv2.WINDOW_NORMAL)
				cv2.imshow(x.name,img)
				cv2.waitKey(0)
				cv2.destroyAllWindows()
	
main()
