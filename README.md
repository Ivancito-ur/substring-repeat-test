
# Test Solving Programming Problems API

Having a string of random characters and random length, create a method that identifies how many substrings of 4 characters appear more than once along the main string. The method’s only argument should be the main string.

It should return the substrings that repeat and how many times they appear in the text in a data structure.

Important:
- Substrings of 4 characters
- How many times they appear in the text
- Random characters and random length
## Install Python
Verify that you have Python on your operating system with:

Windows
```bash
py --version
```

Mac o Linux
```bash
python --version
```


You need install Python 3.9^

- [Link to download Python](https://www.python.org/downloads/)


## Clone and Run Project

Clone the project from repository in any folder:

```bash
git clone https://gitlab.com/ivanuribe39/substring-repeat-test.git
```

After you have cloned the project. Enter the project and run the following command to run the script.


Windows (CMD)
```bash
py string_random.py 
```

Linux or Mac (bash or zsh)
```bash
python string_random.py 
```

In the terminal it will show the following text:
```bash
$ py string_random.py 
Insert a string of characters with the range you want. To exit execution CTRL+BREAK
String: 
```



## Example Test

For testing we use the following string:

```bash
$ py string_random.py 
Insert a string of characters with the range you want. To exit execution CTRL+BREAK
String: acceaceaceeabcbabcdabcdebcde
```


The script will return the responses in the following order:


```bash
ceac 2
eace 2
abcd 2
bcde 2
```


The first value corresponds to the repeated substring and the second value the times it is repeated.