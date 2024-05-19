
def usun_puste(lst):
    i=0
    while i < len(lst):
        if lst [i] == '':
            lst.pop(i)
        else:
            i += 1

