#   My first chat bot program

import tkinter as tk
import random

from nltk.chat.util import Chat, reflections

chat_pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?", ]
    ],
    [

        r"what is your name ?",
        ["My name is Santty and I'm a chatbot ?", ]
    ],
    [
        r"how are you ?",
        ["I'm doing good\nHow about You ?", ]
    ],
    [
        r"sorry (.*)",
        ["Its alright", "Its OK, never mind", ]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that", "Alright :)", ]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there", ]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program dude\nSeriously you are asking me this?", ]

    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse", ]

    ],
    [
        r"(.*) created ?",
        ["Nagesh created me using Python's NLTK library ", "top secret ;)", ]
    ],
    [
        r"(.*) (location|city) ?",
        ['Salem,Chennai, Tamil Nadu', ]
    ],
    [
        r"how is weather in (.*)?",
        ["Weather in %1 is awesome like always", "Too hot man here in %1",
            "Too cold man here in %1", "Never even heard about %1"]
    ],
    [
        r"i work in (.*)?",
        ["%1 is an Amazing company, I have heard about it. But they are in huge loss these days.", ]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain since last week here in %2",
            "Damn its raining too much here in %2"]
    ],
    [
        r"how (.*) health(.*)",
        ["I'm a computer program, so I'm always healthy ", ]
    ],
    [
        r"(.*) (sports|game) ?",
        ["I'm a very big fan of Football", ]
    ],
    [
        r"who (.*) sportsperson ?",
        ["Messi", "Ronaldo", "Hazard"]
    ],
    [
        r"who (.*) (moviestar|actor)?",
        ["Brad Pitt"]
    ],
    [
        r"quit",
        ["Bye take care. See you soon :) ",
            "It was nice talking to you. See you soon :)"]
    ],
]


def chatty():
    print("Hi, I'm santty and I chat bot.\nType quit to leave ")
    chat = Chat(chat_pairs, reflections)
    chat.converse()


window = tk.Tk()


window.title("Developer Chat bot")
#title.grid(column=0,row=20)
window.geometry("800x700")

# Print Text
lab1 = tk.Label(text = "Chat Bot", font= ("Courier New",30))
lab1.grid(column= 100,row = 0)

label1 = tk.Label(text="Let's chat\nEnter your message:", font=("Times New Roman", 20))
label1.grid(column=0, row=2)


# Print Button
entry1 = tk.Entry()
entry1.grid(column=0, row = 5)
str(entry1.get())

but1 = tk.Button(text="Send message",command=chatty)
but1.grid(column=0, row=7)

output = tk.Text(master=window, height=10, width=10)
output.grid(column=10, row=10)

output.insert(tk.END,)

window.mainloop()




