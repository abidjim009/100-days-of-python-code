print("welcome to kon benega crorepati season one , total reward is 10,000 and 1000 will be added for each correct answers ")
question = ["Who is the best programmer :- a Harry   b Striver   c Love Babbar  d All"
            ,"What does SQL stand for ? :- a) Super Quick Language b) Software Query Logic c) Structured Query Logic d) Structured Query Language" 
            , "What does the Boolean datatype represent? :- a) Numbers b) True/False c) Decimal d) Fraction"
            ,"Which of these is not a core data type? :- a) Class b) Lists c) Dictionary d) Tuples"
            ,"What data type is the object below ? L = [1, 23, 1] :- a) List b) Dictionary c) Tuple d) Array"
            ,"Which of the following is the use of id() function in python? :- a) returns identity of the object  b)doesnot return unique id  c)All of the mentioned  d)None of the mentioned"
            ,"What will be the output of the following code : print type(type(int)) :- a) Error b) type 'int'  c) type 'type' d) 0 "
            ,"What is the maximum length of a Python identifier? :- a) 32 b) 16 c) 128 d) No fixed length specified"
            ," What will be the output of the following code snippet - print(type(5 / 2)) and print(type(5 // 2)) :- a) int and float b) float and int c) int and int d) float and float"
            ," What keyword is used in Python to raise exceptions? :- a) Except b) goto c) Try d) None of the above"]

ans = ["d","d","b","a","a","a","c","d","b","d"]
reward = 0
i = 0
j = 0

while i != 10:
    print(question[i])
    x = input("enter your answer as a or b or c or d :- ")
    if ans[j] == x:
        print("correct answer")
        reward += 1000
        
    else:
        print("INCORRECT ANSWER YOU REWARD IS- ",reward)
        break
    i += 1 
    j +=1

if(reward==10000):
    print("AP JEET GAYE 7 CRORE , JUST KIDDING YOUR REWARD IS 10,000")