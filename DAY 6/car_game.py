command=""
started=True

while True:
 command=input(">>")
 if command=="start":
  if started==True:
            print("car is already started")
  else:
    started=True
    print("car started")
 elif command=="stop":
    if not started:
     print("car is already stopped")
    else:
     started=False
     print("car stopped")
 elif command=="help":
        print(''' Start : To start the car
                Stop : To stop the car
                Quit : To quit the game
            ''')
 elif command=="quit":
      print("game has quitted")
 else:
    print("Sorry, Unknown command")
