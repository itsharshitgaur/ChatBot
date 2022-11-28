from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *

my_bot = ChatBot("My Bot")

conv = [
    'Hello',
    'Hi There !',
    'What is your name ?',
    'My name is Bot, I am created by Harshit Gaur.',
    'How are you ?',
    'I am Fine, what about you ?',
    'Glad to hear that.',
    'Thank You',
    'Where do you study ?',
    'I am a student of GEU.',
    'Which language do you speak ?',
    'I mostly speak English.',
    'Python Programming Language',
    'Bye',
    'It was nice talking to you. See you soon.',
    'Tell me a joke!',
    'Student:Teacher! Would you punish me for something I did not do\nTeacher:No\nStudent:I did not do my homework',
    'Which semester are you currently in?',
    'I am in 6th semester.',
    'What are you doing?',
    'Nothing just talking to you.'
]

bot_trainer = ListTrainer(my_bot)

# now training the bot with the help of trainer

bot_trainer.train(conv)

main = Tk()

main.geometry("500x650")

main.title("ChatBot Using Python By Harshit Gaur")
img = PhotoImage(file="bot.png")

photoL = Label(main, image=img)

photoL.pack(pady=5)


def ask_from_bot():
    query = textF.get()
    answer_from_bot = my_bot.get_response(query)
    msgs.insert(END, "You : " + query)
    msgs.insert(END, "Bot : " + str(answer_from_bot))
    textF.delete(0, END)
    msgs.yview(END)


frame = Frame(main)

sc = Scrollbar(frame)
msgs = Listbox(frame, width=80, height=20, yscrollcommand=sc.set)
sc.pack(side=RIGHT, fill=Y)
msgs.pack(side=LEFT, fill=BOTH, pady=10, padx=10)
frame.pack()

# creating text field

textF = Entry(main, font=("Verdana", 15))
textF.pack(pady=10, padx=12)

# creating a button

btn = Button(main, text="Enter", font=("Verdana", 16), command=ask_from_bot)
btn.pack()


# function to be invoked on pressing ENTER key
def enter_function(event):
    btn.invoke()


main.bind('<Return>', enter_function)

main.mainloop()
