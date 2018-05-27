1、导入标准库：datetime

 >>> import datetime
 >>> datetime.date.today()
  datetime.date(2018, 5, 27)
  
  >>> datetime.date.today().day
  27
  >>> datetime.date.today().month
  5
  >>> datetime.date.today().year
  2018



>>> import datetime
>>> datetime.date.isoformat(datetime.date.today())
 '2018-05-27'


>>> import time
>>> time.strftime("%H:%M")
'20:27'

>>> import time
>>> time.strftime("%A:%P")
'Sunday:pm'


>>> import html
>>> html.escape("This is HTML fragment contains a <script>script</script> tag.")
'This is HTML fragment contains a &lt;script&gt;script&lt;/script&gt; tag.'
>>> html.unescape ("I &hearts;Python's &lt;standard library&gt;.")
"I ♥Python's <standard library>."

2、循环
>>> for i in [1,2,3]:
	print(i)

	
1
2
3
>>> 


>>> for ch in "Hi!":
	print(ch)

	
H
i
!
>>>

3、循环指定次数：

>>> for num in range(5):
	print('Head Fist Rocks!')

	
Head Fist Rocks!
Head Fist Rocks!
Head Fist Rocks!
Head Fist Rocks!
Head Fist Rocks!
>>>

4、让程序暂停秒数：

>>> import time
>>> time.sleep(5)
>>> 


5、生成随机数：

>>> import random
>>> dir(random)
['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom', 'TWOPI', '_BuiltinMethodType', '_MethodType', '_Sequence', '_Set', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_acos', '_bisect', '_ceil', '_cos', '_e', '_exp', '_inst', '_itertools', '_log', '_pi', '_random', '_sha512', '_sin', '_sqrt', '_test', '_test_generator', '_urandom', '_warn', 'betavariate', 'choice', 'choices', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 'paretovariate', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']
>>> help(random.randint)
Help on method randint in module random:

randint(a, b) method of random.Random instance
    Return random integer in range [a, b], including both end points.

>>> random.randint(1,60)
1
>>> random.randint(1,60)
18
>>> random.randint(1,60)
56
>>> random.randint(1,60)
25
>>> random.randint(1,60)
12
>>> 

