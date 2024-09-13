#search if the word "learning " exists in the file practice.txt or not
word="learning"
def check_word():
    with open("practice.txt","r")as f:
        data=f.read()
        if(data.find(word)!=-1):
            print("found")
        else:
            print("Not found")

check_word()
    