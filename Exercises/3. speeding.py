def speeding_ticket(speed, is_birthday):
    no_ticket_limit = 60 if not is_birthday else 65
    small_ticket_limit = 80 if not is_birthday else 85

    # Determine the type of ticket based on the speed
    if speed <= no_ticket_limit:
        return "No Ticket"
    elif speed <= small_ticket_limit:
        return "Small Ticket"
    else:
        return "Big Ticket"

print(speeding_ticket(60, False)) 
print(speeding_ticket(75, False))  
print(speeding_ticket(85, False))  
print(speeding_ticket(65, True))  
print(speeding_ticket(85, True))  
