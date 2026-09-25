import json

def main():
    looping = True
    while looping == True:
        userInput = input("> ")
        print(userInput)
        if userInput.lower()=='exit':
            looping = False
        

if __name__=="__main__":
    main()
    exit()

