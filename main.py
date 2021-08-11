from datetime import datetime
import time


def robot():
  
  while True:
    
    print(datetime.now())
    time.sleep(60)

if __name__ == '__main__':
    robot()
    