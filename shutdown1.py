def shutdown(user_input):
    if user_input == "yes":
        return "Shutting Down"
    elif user_input == "no":
        return "Abort Shutdown"
    else:
        return "Sorry"
    
answer = input("Do you want to shutdown?")
print(shutdown(answer))
