devops_course
 ##Lab_2a: Основи роботи з Python.
1. результат після python .:
 TWe are in the __main__
2020-11-08 00:43:10.924586
linux
  
2. результат після python3.6 . -h:
   usage: . [-h] [-o OPT] [-l]
   
3. результат після python3.6 . -o "Цей текст також має вивестись":
We are in the __main__
2020-11-08 00:48:39.953249
linux
З консолі було передано аргумент
 ========== >> Цей текст також має вивестись << ==========
 
4. результат після python3.6 . --logs
2020-11-08 00:50:02,869 root INFO: Тут буде просто інформативне повідомлення
2020-11-08 00:50:02,869 root WARNING: Це Warning повідомлення
2020-11-08 00:50:02,869 root ERROR: Це повідомлення про помилку

5. Результат після  python . --logs: були виведені усі логи, які були можливими та прописаними у самій програмі.
2020-11-08 16:00:47,264 root INFO: Тут буде просто інформативне повідомлення
2020-11-08 16:00:47,264 root WARNING: Це Warning повідомлення
2020-11-08 16:00:47,264 root ERROR: Це повідомлення про помилку

6. Далі створила в common.py функцію, яка виводить парні числа від 0 до 100 при true i непарні при false:
def myfunc(x):                         
  if x:                                
    a=[i for i in range (0,101,2)]     
    print(a)                           
  else:                                
    a=[i for i in range(1,100,2)]      
    print(a)            
    і передала її в main.py:
          a=input()
    common.myfunc(a)          
7. Неправильна функція: 
def myfunc1(x='str'):
    try:
        print("Що буде якщо", x*2 - x, "?")
    except Exception as e:
        logger.error("Помилка")
    else:
        logger.info("Інформативне повідомлення")
    finally:
        print("Кінецььь")

