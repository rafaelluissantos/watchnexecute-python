# Watch directory and execute
#### for each new file in the watched directory, execute given command 



# how to?
- Download and install python 3
- Execute: pip3 install watchdog
- Execute: python3 main.py --help

## expected result

```python
r-santos@rafmbp ~/d/p/watchnexecute-python> python3 main.py --help                                           
usage: main.py [-h] dir cmd

Watch directory and execute cmd.

positional arguments:
  dir         directory to watch
  cmd         cmd to be executued for each new file

optional arguments:
  -h, --help  show this help message and exit
```

# Usage example #1
```bash
start: 
python3 main.py ./ "cat %s | grep thingy"

output: 
watching directory: "./"
will execute "cat %s | grep thingy" for directory modified files.

input: 
touch example.test

output: 
executing "cat ./example.test | grep thingy"

input:
echo "thingy" >> example.test 

output: 
executing "cat ./example.test | grep thingy"
thingy
```
# Usage example #2
### open new file in text editor MacOS 
```sh
r-santos@rafmbp ~/d/p/watchnexecute-python> python3 main.py ./ "open -a Visual\ Studio\ Code %s"

watching directory "./"

will execute "open -a open -a Visual\ Studio\ Code %s" for directory modified files.
```
### Visual studio code should pop up with the modified or created file. 
### If the file is deleted the cmd will throw an error, telling visual studio couldn't find the file. 