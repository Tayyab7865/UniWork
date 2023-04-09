# credits_pass = int(input("Enter your credits at pass: "))
# print("credits_pass")
# credits_fail = input("Enter your credits at fail: ")
# print("credits_fail")
# credits_defer = input("Enter your credits at defer: ")
# print("credits_defer")
# total_credits = [credits_pass ,credits_defer, credits_fail]
# if total_credits == ['120', '0', '0']:
#     print("Progress")
# if total_credits == ['100','20','0']:
#     print("Progress module trailer")
# if total_credits == ['100','0','20']:
#     print("Progress module trailer")
# if total_credits == ['80','40','0']:
#     print("Do not Progress – module retriever")
# if total_credits == ['80','20','20']:
#     print("Do not Progress – module retriever")
# if total_credits == ['80','0','40']:
#     print("Do not Progress – module retriever")
# if total_credits == ['60','60','0']:
#     print("Do not Progress – module retriever")
# if total_credits == ['60','40','20']:
#     print("Do not Progress – module retriever")
# if total_credits == ['60','20','40']:
#     print("Do not Progress – module retriever")
# if total_credits == ['60','0','60']:
#     print("Do not Progress – module retriever")
# if total_credits == ['40','80','0']:
#     print("Do not Progress – module retriever")
# if total_credits == ['40','60','20']:
#     print("Do not Progress – module retriever")
# if total_credits == ['40','40','40']:
#     print("Do not Progress – module retriever")
# if total_credits == ['40','20','60']:
#     print("Do not Progress – module retriever")
# if total_credits == ['40','0','80']:
#     print("Exclude")
# if total_credits == ['20','100', '0']:
#     print("Do not Progress – module retriever")
# if total_credits == ['20','80','20']:
#     print("Do not Progress – module retriever")
# if total_credits == ['20','60','40']:
#     print("Do not Progress – module retriever")
# if total_credits == ['20','40','60']:
#     print("Do not Progress – module retriever")
# if total_credits == ['20','20','80']:
#     print("Exclude")
# if total_credits == ['20','0', '100']:
#     print("Exclude")
# if total_credits == ['0','120', '0']:
#     print("Do not Progress – module retriever")
# if total_credits == ['0','100', '20']:
#     print("Do not Progress – module retriever")
# if total_credits == ['0', '80', '40']:
#     print("Do not Progress – module retriever")
# if total_credits == ['0', '60', '60']:
#     print("Do not Progress – module retriever")
# if total_credits == ['0', '40', '80']:
#     print("Exclude")
# if total_credits == ['0', '20', '100']:
#     print("Exclude")
# if total_credits == ['0', '0', '120']:
#     print("Exclude")
#     



def progress_outcome(pass_credits, defer_credits):
    if pass_credits == 120:
        print("Progress")
    elif pass_credits == 100:
        print("Progress (module trailer)")
    elif pass_credits == 80:
        print("Do not Progress - module retriever")
    elif pass_credits == 60:
        print("Do not Progress - module retriever")
    elif pass_credits == 40 and defer_credits != 0:
        print("Do not Progress - module retriever")
    elif pass_credits == 40 and defer_credits == 0:
        print("Exclude")
    elif pass_credits == 20 and defer_credits >= 40:
        print("Do not Progress - module retriever")
    elif pass_credits == 20 and defer_credits <= 20:
        print("Exclude")
    elif pass_credits == 0 and defer_credits >= 60:
        print("Do not Progress - module retriever")
    elif pass_credits == 0 and defer_credits <= 40:
        print("Exclude")
def validation ():
    while true:
        if credits_pass not in range (0, 140, 20):
            print("Out of range")
            continue
        if credits_defer not in range (0, 140, 20):
            continue
        if credits_fail not in range (0, 140, 20):
            continue

# credits= input("Enter your credits")
# range = arr.array('i', [0, 20, 40, 60, 80, 100, 120]):
#     print("Out of range")

    
    
    
    
    