Bar =""
def ProgressBar(Runs):
    Bar = "{:.0f}%  [{}] ".format( Runs*10,"%" * Runs + "." * (10-Runs ))
    print(Bar)
    return Bar
dd = int(input())
if 0 <= dd <=100:
  Runs =int( dd / 10)
  if Runs ==10 :
   print('100% Complete!')
   print("[%%%%%%%%%%]")
  else:
    progressBar = "\r " + ProgressBar( Runs)
    print(Bar+"Still loading..." )
    