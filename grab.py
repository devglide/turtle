# print("\tdog \tbun \tketchup\tmustard\tonions")
# count = 1
# for dog in [0,1, 2]:
#     for bun in [0, 1, 2]:
#         for ketchup in [0, 1]:
#             for mustard in [0, 1]:
#                 for onion in [0, 1]:
#                     print("#", count, "\t", end='')
#                     print(dog, "\t", bun, "\t", ketchup, "\t", end='')
#                     print(mustard, "\t", onion)
#                     count = count + 1

# hugehairypants = ['huge', 'hairy', 'pants', 'blah'] 
# for i in hugehairypants:
#     print(i)
#     for j in hugehairypants:
#         print(j)
#         for k in hugehairypants:
#             print(k) 

# def mult_table(inputA, inputB):
#     for i in range(inputA, inputB + 1):
#         for j in range(inputA, inputB + 1):
#             if len(str(i)) <= 1:
#                 print(" " + str(i*j), end = " ")
#             else:
#                 print(str(i*j), end=" ")
#         print()

# mult_table(1, 4)

# draw square in Python Turtle
# draw Squre in Python Turtle
import turtle
  
t = turtle.Turtle()
t.pencolor('red')
 
s = int(120)
 
for i in range(91):
  t.forward(s) # Forward turtle by s units
  t.left(91) # Turn turtle by 90 degree

turtle.done()