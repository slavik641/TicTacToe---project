pattern = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
player_x=0
player_o=0

def when_Empty(pointer): #בדיקה שהתא ריק
    if pointer == '_':
        return False
    else:
        return True

def clean_Pattern():  #מנקה את התבנית
    global pattern
    pattern = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
    print("it's a draw!")
    print("please, try again")

def print_Board(): #פונקציה המדפיסה את לוח המשחק

    global pattern
    for i in pattern:
        print(i)
print_Board()
while True:
    line=int(input('enter the line (0-2)'))
    raw=int(input('enter the raw (0-2)'))
    if 2 >= line >= 0 and 2 >= raw >= 0 and pattern[line][raw] == '_':
      if player_x>=player_o:
          pattern[line][raw] = 'x'
          print_Board()
          player_o += 1
      else:
          pattern[line][raw] = 'o'
          print_Board()
          player_x += 1
# בדיקה של כל התנאים לנצחון
    if pattern[0][0] == pattern[0][1]== pattern[0][2] and when_Empty(pattern[0][2]) :
        print(pattern[0][0] + ' you win!')
        break
    if pattern[1][0] == pattern[1][1] == pattern[1][2] and when_Empty(pattern[1][2]) :
        print(pattern[1][0] + ' you win!')
        break
    if pattern[2][0] == pattern[2][1] == pattern[2][2] and when_Empty(pattern[2][2]):
        print(pattern[2][0] + ' you win!')
        break
    if pattern[0][0] == pattern[1][0] == pattern[2][0] and when_Empty(pattern[2][0]):
        print(pattern[0][0] + ' you win!')
        break
    if pattern[0][1] ==pattern[1][1] == pattern[2][1] and when_Empty(pattern[2][1]):
        print(pattern[0][1] + ' you win!')
        break
    if pattern[0][2] == pattern[1][2] == pattern[2][2] and when_Empty(pattern[2][2]):
        print(pattern[0][2] + ' you win!')
        break
    if pattern[0][0] == pattern[1][1] == pattern[2][2] and when_Empty(pattern[2][2]):
        print(pattern[0][0] + ' you win!')
        break
    if pattern[0][2] == pattern[1][1] == pattern[2][0] and when_Empty(pattern[2][0]):
        print(pattern[0][2] + ' you win!')
        break
    #  בדיקה של כל התאים שמילאו אותם ויצא תיקו, ריקון התבנית והרצת המשחק מההתחלה
    if when_Empty(pattern[0][0]) and when_Empty(pattern[0][1])\
         and when_Empty(pattern[0][2]) and when_Empty(pattern[1][0]) \
         and when_Empty(pattern[1][1]) and when_Empty(pattern[1][2]) and when_Empty(pattern[2][0]) \
         and when_Empty(pattern[2][1]) and when_Empty(pattern[2][2]):
        clean_Pattern()

