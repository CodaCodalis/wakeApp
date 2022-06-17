def computation(time):
    dep_time = time.get_arrival_time() - time.get_duration() - time.get_prep_time() - time.get_delay()
    counter = 0
    while dep_time < 0:
        dep_time += 24
        counter += 1

    hours = int(dep_time)
    minutes = int(round((dep_time - hours) * 60, 2))
    if minutes < 10:
        str_minutes = "0" + str(minutes)
    else:
        str_minutes = str(minutes)

    if counter == 0:
        return str(hours) + ':' + str_minutes + ' Uhr'
    else:
        return str(hours) + ':' + str_minutes + ' Uhr (' + str(counter) + ' Tag(e) vorher)'


class WakeController:
    pass
