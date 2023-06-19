from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from spellchecker import SpellChecker
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from Word_List import words
import random

english = SpellChecker()

class Home_Page(Screen,Widget):
    pass


class Translate_Game(Screen,Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        

    def number_turn(self):
        self.number_turn_value = int(self.ids.number_turn_input.text)
        self.count = self.number_turn_value
        self.ids.answer.text = ""
        print(self.count)
        print(self.number_turn_value)
        
        if self.number_turn_value <= 0 or self.number_turn_value > 100:
            self.ids.number_turn_label.color = (255/255,0/255,0/255,1) 
            print("merci de saisir un nombre compris entre 1 et 100")
        else: 
            
            self.ids.number_turn_label.text = "Translate this word :"
            self.ids.number_turn_label.color = (100/255,255/255,47/255,1)
            self.ids.number_turn_input.pos_hint = {"x":0.25, "y":2}
            self.ids.answer.pos_hint = {"x":0.25,"y":0.55}
            self.ids.start.pos_hint = {"x":0.25,"y": 2}
            self.ids.restartbutton.pos_hint = {"y":2}
            self.ids.returnbutton.pos_hint = {"y":2}
            self.ids.checkbutton.pos_hint = {"x":0.25, "y":0.3}
            self.score = 0 
            self.update_word()
    
            

    def update_word(self):

        self.word = random.choice(list(words.keys()))
        print(self.word)
        self.useranswer = Label(text= self.word, color = (0/255, 0/255, 0/255, 1), font_size = 50, pos_hint = {"x":0,"y":0.3})
        self.add_widget(self.useranswer)
        self.ids.answer.text = ""

    def check(self, answer):
        answer = english.correction(self.ids.answer.text)
        print(answer)
        self.remove_widget(self.useranswer)
        self.count -=1
        print(self.count)
        
        if answer == words[self.word]:
            print("bravo")
            self.score += 1
            
            
        else:
            print("dommage")
        self.update_word()
        
        if self.count == 0:
            self.ids.number_turn_label.text =  "Votre score est de "
            self.ids.answer.pos_hint = {"y":2}
            self.ids.checkbutton.pos_hint = {"y":2}
            self.useranswer.text = f"{self.score}/{self.number_turn_value}"
            self.ids.restartbutton.pos_hint = {"x":0.25,"y":0.55}
            self.ids.returnbutton.pos_hint = {"x":0.25,"y":0.3}

    def restart(self):
        self.ids.number_turn_input.text = ''
        self.ids.number_turn_label.text = "Combien de mots souhaitez vous ?"
        self.useranswer.pos_hint = {"y":2}
        self.ids.restartbutton.pos_hint = {"y":2}
        self.ids.returnbutton.pos_hint = {"y":2}
        self.ids.number_turn_input.pos_hint = {"x":0.25,"y":0.65}
        self.ids.start.pos_hint = {"x":0.25,"y":0.3}

        
        
            
class End_Translate_Game(Screen,Widget):
    pass
class Clicker_Game(Screen,Widget):
    pass

class FinalPage(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass

file=Builder.load_file('main.kv')

class QuizApp(App):
    def build(self):
        return file

QuizApp().run()
