import os
import time
import random

class WordApp():
    def __init__(self):
        
        self.words = {}
        self.refresh_words()
        self.sequence = []
        self.correct_ans_index = 0
        self.user_index = 0
        self.correct_count = 0
        self.quest_count = 0
        self.shuffled_word_list = []
        self.asked_quests = []
        self.asked_quests_index = 0
        
        print("\nWelcome to our exam!\nThese exam will last approximately 20 minute. There will be 30 questions in a row.To exit exam press ctrl+c.")
        self.exam()
        
    def merge(self, dict1, dict2):
        return(dict2.update(dict1))
    
    def set_results(self,word):
        counter = 0
        for ans in self.sequence:
            if self.words[word] == ans:
                self.correct_ans_index = counter
                return
            counter+=1

    def ask_quest(self):
        
        self.quest_count+=1
        
        self.shuffled_word_list = list(self.words.items())
        random.shuffle(self.shuffled_word_list)

        word1, definition1 = self.shuffled_word_list[0]
        word2, definition2 = self.shuffled_word_list[1]
        word3, definition3 = self.shuffled_word_list[2]
        word4, definition4 = self.shuffled_word_list[3]
        word5, definition5 = self.shuffled_word_list[4]
        
        
        self.sequence = [definition1,definition2,definition3,definition4,definition5]
        random.shuffle(self.sequence)
        
        self.set_results(word1)
        self.words.pop(word1)
        
        self.asked_quests.append({word1:definition1})
        self.asked_quests_index+=1
        
        print(f"\nWhat is the meaning of '{word1}'? ({self.quest_count}/30)\n")
        for index in range(len(self.sequence)):
            print(f"{index+1}) {self.sequence[index]}")
            
        
        while True:
            self.user_index = int(input("\nAnswer : "))
            
            if(self.user_index<1 or self.user_index>5):
                print("\nPlease write an convenient answer.")
                continue    
        
            if(self.user_index-1 == self.correct_ans_index):
                print("\nCorrect!")
                return 1
            else:
                print(f"\nWrong. '{word1}' means '{self.sequence[self.correct_ans_index]}'")
                return 0
        

    def refresh_words(self):
        
        temp = []
        
        with open("current_words.txt","r",encoding="utf-8") as f:
            data = f.readlines()
        
        for i in data:
            temp = i.strip().split("=")
            self.words[temp[0].strip()] = temp[1].strip()
            
    def exam(self):
        
        
        while True:
            for i in range(30):
                if self.ask_quest():
                    self.correct_count+=1
            
            print(f"You get {self.correct_count} out of 30. Congratulations!\n")
            
            for quest in self.asked_quests:
                self.merge(quest,self.words)
                
            ans = input("Do you want one more? (y/n)")
            if (ans=="y"):
                self.quest_count = 0
                self.correct_count = 0
                print("Good luck!\n")
                
            elif (ans=="n"):
                print("See you soon!\n")
                break
            else:
                print("Are you kidding me?\n")
                break
            
        
        
    def print_words(self):
        print(self.words)


if __name__ == "__main__":
    
    app = WordApp()
    
    
    