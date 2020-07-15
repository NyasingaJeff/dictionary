import json #import the lib that is resposible for json file
from difflib import get_close_matches #this lib is used to spot diff in patterns etc..  niow we import get_close_match for use on strings
# get_close_match("the var bueng checked", "the collection bieng matches", n=4 : thre number of matching elements to return, cuttoff() : a float that puts a cutoff on the value of similaruity returned)   
data = json.load(open('data.json'))

def define():
    word = input("Enter Word:: ").lower()
    
    while word == 'q':
        return 
    else:
        if word in data:
            print (data[word])
            define()    
        else:
            print ('word doestnt exist')
            define()

def translate():
    w =  input('input the word or "Q" to Quit Program: ') 
    if w !='q':  #this is to check if the user has quit
        w.lower()
        if w in data: #to check if the user has enterd a word found in the data provided
            if type(data[w])== type('string'):
                print (w.upper() +':'+ data[w])
            elif type(data[w]) == type([]):
                x=1
                print( w.upper())
                for de in data[w]:
                    print (str(x)+' '+de)
                    x+=1
            else:
                pass

        elif len(get_close_matches(w , data.keys())) > 0:  #chek the number of keyes that the get_close_match will return
            content = get_close_matches(w , data.keys(), cutoff= 0.5)
            print('Did You mean... : ')
            i = 0 
            for con in content:              
                print (str(i) + ' : '+ con) #print the options
                i +=1
            prompt = input(' Select the Word Appropriate word , or "Q" to quit : ')
            
            if prompt == 'q' :
                pass
            
            elif prompt.isdecimal() == False or int(prompt) > len(content):
                return print ('invalid entry')
            
            else:
                w = content[int(prompt)]    #to  get the exact word from the list returned       
            # print("did You mean %s instead?"  %content[0]) #string formatter
            defination = data[w]
            if type(defination) == list:
                x=1
                print (w.upper())
                for de in defination:
                    print (str(x)+':'+de)
                    x +=1
            else:
                print (w.upper() +':'+ defination)
        else:
            print ("msee enda gooogle")
    else:
        return print ("Gpoodbye")
    translate()
    
translate()




# print (define())