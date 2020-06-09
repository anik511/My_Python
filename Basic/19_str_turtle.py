import turtle
name = turtle.textinput('Name', 'What is your name?')
name = name.lower()
if name.startswith('mr'):
    print("Hellow Sir, How are you?")
elif name.startswith('mrs') or name.startswith('miss') or name.startswith('ms'):
    print("Hellow Mam, How are you?")
else:
    name = name.capitalize()
    strs = 'Hi '+name+'! How are you?'
    print(strs)
turtle.exitonclick()
