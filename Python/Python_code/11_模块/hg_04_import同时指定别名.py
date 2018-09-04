import hg_01_测试模块1 as DogModule
import hg_02_测试模块2 as CatModule

DogModule.say_hello()
CatModule.say_hello()

dog = DogModule.Dog()
print(dog)

cat = CatModule.cat()
print(cat)