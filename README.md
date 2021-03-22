
requirements: 
1. `python3`
* there are problems with vanilla MacOs using the wrong (older python version). may need to poke around and make sure python3 is
actually beging invoked.
  * as of 2021/02/18 running with `Python 3.8.2` worked
2. `pygame` library 
  * to install pygame on MacOs use command `pip3 install pygame`
  `pip3 install pygame --user`
3. only been tried on MacOs
  * as of 2021/02/18 running with `macOS catalina 10.15.7` worked

to determine if pygame is installed: 
`$ pip3 show pygame`

should show something like this if so:
```
Name: pygame
Version: 2.0.1
Summary: Python Game Development
Home-page: https://www.pygame.org
Author: A community project.
Author-email: pygame@pygame.org
License: LGPL
Location: /Users/alexmtaft/Library/Python/3.8/lib/python/site-packages
Requires:
Required-by:
```

-----------------------------

*NOTE* 

executing the program directly usually doesn't work (unable to find the python interpreter for some reason)

```
$ ./avoidTheStroid.py
-bash: ./avoidTheStroid.py: /usr/local/bin/python: bad interpreter: No such file or directory
```

to run just call `python` out directly: 
```
$ python avoidTheStroid.py
```




