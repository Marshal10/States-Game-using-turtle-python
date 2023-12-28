import turtle
import pandas
#read the csv file
data=pandas.read_csv("states_data.csv")

#store all the states inside a list
states=data.state.to_list()
num_of_states=len(states)
screen=turtle.Screen()
screen.title("States Game")


img="states.gif"
screen.addshape(img)
turtle.shape(img)

game_on=True
guessed_states=[]
while game_on:
    guess=screen.textinput(f"{len(guessed_states)}/{num_of_states} States Correct","What's another state name?").title()
    
    #When player exits
    if guess=="Exit":
        missing_states=[state for state in states if state not in guessed_states]
        data_dict={
            "Missing States":missing_states
        }
        new_csv=pandas.DataFrame(data_dict)   
        new_csv.to_csv("missing_states.csv")     
        game_on=False
        
    #When the player guesses it correct
    if guess in states:
        guessed_states.append(guess)
        x_cor=data[data["state"]==guess]["x"].to_list()[0]
        y_cor=data[data["state"]==guess]["y"].to_list()[0]
        new_turtle=turtle.Turtle()
        new_turtle.penup()
        new_turtle.hideturtle()
        new_turtle.goto(x_cor,y_cor)
        new_turtle.write(f"{guess}",align="center",font=("Arial",8,"normal"))
    else:
        print("There is no such state")  
    
    #When the user guesses all the states    
    if len(guessed_states)==num_of_states:
        new_turtle=turtle.Turtle()
        new_turtle.penup()
        new_turtle.hideturtle()
        new_turtle.color("green")
        new_turtle.write("You Guessed it all right!",align="center",font=("Arial",24,"normal"))
        game_on=False