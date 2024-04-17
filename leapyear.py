while True:
    try:
        a = input("Enter year: To stop loop enter exit:")
        if a == "exit":
            break
        a = int(a)
        b = bool(a % 4 == 0)
        c = bool(a % 400 == 0)
        d = bool(a % 100 != 0)
        if b and (c or d):
            print("leap year")
        else:
            print("not leap year")
    except ValueError:
        print("invalid input")  

#ALTERNATIVE METHOD
# while True:
#     try:
#         a = raw_input("enter year and exit to break:")
#         if a == "exit":
#             break
#         a = int(a)
#         if a % 4 == 0:
#             if a % 100 == 0:
#                 if a % 400 == 0:
#                     print("leap year")
#                 else:
#                     print("not leap year")
#             else:
#                 print("leap year")        
#         else:
#             print("not leap year")             
#     except ValueError:
#         print("invalid input")
