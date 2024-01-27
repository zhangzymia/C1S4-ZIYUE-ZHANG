def speeding_ticket(speed, is_birthday):
    if is_birthday:
        speed_limit_no_ticket = 65
        speed_limit_small_ticket = 85
    else:
        speed_limit_no_ticket = 60
        speed_limit_small_ticket = 80
    if speed <= speed_limit_no_ticket:
        return "No Ticket"
    elif speed <=speed_limit_small_ticket:
        return "Small Ticket"
    else:
        return "Big Ticket"
print(speeding_ticket(60, False))
print(speeding_ticket(75, False))
print(speeding_ticket(85, False))
print(speeding_ticket(65, True))
print(speeding_ticket(85, True))
