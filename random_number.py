from random import randint

class random_number:

    def __init__(self, low, high, guess):
        self.low = low
        self.high = high
        self.guess = guess
        #stores all guesses
        self.store_number = [guess]
        #run functions
        self.generate_number()
        self.compare_random_number()

    def generate_number(self):
        #generates a random number between the given parameters
        self.rand_num = randint(self.low, self.high)

    def guess_again(self):
        #allows user to guess again and stores the guess in a list
        self.new_guess = int(input("What's your new guess? "))
        self.store_number.append(self.new_guess)
        self.guess = self.new_guess
        self.compare_random_number()

    def compare_random_number(self):
        #uncomment to revel the generated random number
        #print("Random number: ", self.rand_num)
        #uncomment to revel all guessed numbers
        #print(self.store_number)
        
        #compares guesses
        if self.rand_num == self.guess:
            print("You guessed right!\nThanks for playing!")
            print("It took you {} guesses".format(len(self.store_number)))
            exit()
        else:
            #prompts user to try again
            self.retry = input("You did not guess right! \nTry again?(y/n): ").lower()
            if self.retry == "y":
                self.guess_again()
            else:
                print("Thanks for playing!")
                print("You guessed {} times".format(len(self.store_number)))
                exit()

def nums():
    l = 0
    h = 0
    g = 0

    l = int(input("Enter the starting range: "))
    h = int(input("Enter the ending range: "))
    g = int(input("Enter a number between those numbers: "))

    #if user makes the starting number higher than the ending number, they will swap places
    while 1:
        if l > h:
            n = h
            h = l
            l = n
        #verifies the guess is in between the two ranges
        if l <= g <= h:
            break
        #if both the high and low numbers are the same, new numbers will be selected
        if l == h:
            print("Don't pick the same number please\nPick new numbers")
            l = int(input("Enter the starting range: "))
            h = int(input("Enter the ending range: "))
            g = int(input("Enter a number between those numbers: "))
        #if guess is out of range, a new guess will be made
        if g < l or g > h:
            while g < l or g > h:
                print("You must pick a number between {} and  {}  \nTry again..".format(l, h))
                g = int(input("Enter a number between those numbers: "))
            else: 
                break
    #prints the starting, ending, and guess
    print(l, h, g)
    rand = random_number(l, h, g)
try:
    nums()

except ValueError:
    print("Please select a number!\nLetters are not acceptable. Try again..")
    nums()
