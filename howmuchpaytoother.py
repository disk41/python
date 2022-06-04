# This code can be used to calculate what transactions have to be made, so that every person payed the same amount of money.
# I use this in my flat share, when at the end of the month, we split the costs of the kitchen items we all use.

Example = True
payments = {}

if not Example:
    # In this loop, we collect the information about what everybody paid
    while True :
        
        print("Type in the name of the person. If no more person needs to be added, type 'done'.")
        name = input(">")
        
        if name == "done" :
            break
        
        print("\nType in the prices, confirming each price with ENTER.")
        print("If nothing more needs to be added, just type in '0'.")
        
        payment = 0
        while True :
            
            payed = input(">")
            
            if payed == "0" :
                break
            else :
                # my numpad has "," instead of "." ... so this is why
                payed.replace( "," , "." )
                payment += float(payed)
            
        payments[name] = payment
        print()



# Some example to test/demonstrate the code
if Example:
    payments = {"A":150 , "B": 105, "C": 30, "D": 51,"E": 74}
    
    print("Who payed how much money?\n")
    for name in payments :
        print("{}: {:3.2f}".format(name, payments[name]) )
        
    print("\nIf everyone is supposed to have payed the same; the follwoing transactions have to be done:\n")



# What did all of them payed together?
Sum = 0
for name in payments :
    Sum += payments[name]
    

# make a list of the transactions. Imagine they go and come from a big stack
N = len(payments)
transactions = {}
for name in payments :
    diff = payments[name] - Sum/N
    
    if diff >= 0 :
        transactions[ ("stack", name) ] = diff
    elif diff < 0 :
        transactions[ (name, "stack") ] = -diff


from_stack = [ (x,_) for (x,_) in transactions if x == "stack" ]
to_stack = [ (_,x) for (_,x) in transactions if x == "stack" ]

# instead of giving and receiving money from a sack, we want everyone to make direct exchangements of money
while from_stack != [] :
    
    receiver = from_stack[0]
    
    for giver in to_stack :
        
        if transactions[receiver] > transactions[giver] :
            
            transactions[ ( giver[0] , receiver[1] ) ] = transactions[giver]
            transactions[receiver] -= transactions[giver]
            transactions.pop(giver)
            to_stack.remove(giver)
        
        elif transactions[receiver] <= transactions[giver] :
            
            transactions[ ( giver[0] , receiver[1] ) ] = transactions[receiver]
            transactions[giver] -= transactions[receiver]
            transactions.pop(receiver)
            from_stack.remove(receiver)
            break

# print who has to do what
for T in transactions :
    if transactions[T] > 0.001 :
        (giver, receiver) = T
        print("{} has to give {:3.2f} to {}".format(giver , transactions[T] , receiver ) )



