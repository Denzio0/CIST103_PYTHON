#CONDITIONALS STATEMENTS (PYTHON IF ELSE)
#IF STATEMENT
#IF- ELSE STATEMENT
#IF-ELIF-ELSE STATEMENT
#NESTED CONDITIONAL STATEMENTS
#"SEQUENCING IS IMPORTANT IN PYTHON"

heroPower = int(input("INPUT HERO POWER: ")) #initialize variabels first
survivePower = int(input("INPUT HERO POWER: "))  

if heroPower >= 50 or heroPower == 100:
    if survivePower  >= 50 or survivePower == 100: #MUST SATISFY BOTH TO BECOME POSSIBLE
        print ("THE HERO IS VERY POWERFUL")

elif heroPower >= 30 and heroPower < 50:
    if survivePower  >= 30 or survivePower == 50:
        print ("THE HERO IS JUST OKAY")

elif heroPower >= 10 and heroPower < 30:
    if survivePower  >= 10 or survivePower == 30:
        print ("THE HERO IS NOT IN THE META")

else:
    print ("THE HERO IS TOO WEAK")
    
print ("====THANK YOU FOR CHECKING HERO POWER====") #NOT INDENT
