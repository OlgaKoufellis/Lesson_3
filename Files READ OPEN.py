'''
Let's analyze it:
the name of the function (open) speaks for itself;
if the opening is successful, the function returns a stream object;
 otherwise, an exception is raised (e.g., FileNotFoundError if the file you're going to read doesn't exist);

the first parameter of the function (file) specifies the name of the file to be associated with the stream;

the second parameter (mode) specifies the open mode used for the stream;
 it's a string filled with a sequence of characters, and each of them has its own special meaning (more details soon);

the third parameter (encoding) specifies the encoding type (e.g., UTF-8 when working with text files)
the opening must be the very first operation performed on the stream.

Opening the streams: modes
[r] open mode: read

the stream will be opened in read mode;
the file associated with the stream must exist and has to be readable, otherwise the open() function raises an exception.
[w] open mode: write

the stream will be opened in write mode;
the file associated with the stream doesn't need to exist;
if it doesn't exist it will be created;
if it exists, it will be truncated to the length of zero (erased);
if the creation isn't possible (e.g., due to system permissions) the open() function raises an exception.
[a] open mode: append

the stream will be opened in append mode;
the file associated with the stream doesn't need to exist; if it doesn't exist, it will be created; if it exists the virtual recording head will be set at the end of the file (the previous content of the file remains untouched.)
[r+] open mode: read and update

the stream will be opened in read and update mode;
the file associated with the stream must exist and has to be writeable, otherwise the open() function raises an exception;
both read and write operations are allowed for the stream.
[w+] open mode: write and update

the stream will be opened in write and update mode;
the file associated with the stream doesn't need to exist;
if it doesn't exist, it will be created;
the previous content of the file remains untouched;
both read and write operations are allowed for the stream.

Selecting text and binary modes
If there is a letter [b] at the end of the mode string it means that the stream is to be opened in the binary mode.
If the mode string ends with [a] letter t the stream is opened in the text mode.
Text mode is the default behaviour assumed when no binary/text mode specifier is used.
Finally, the successful opening of the file will set the current file position
(the virtual reading/writing head) before the first byte of the file if the mode is not [a] and
after the last byte of file if the mode is set to [a].

Text mode	   Binary mode	Description
rt	            rb	            read
wt	            wb	            write
at	            ab	            append
r+t 	        r+b	        read and update
w+t	            w+b 	    write and update


'''

# try:
#     stream = open("/Users/User/Desktop/file.txt", "rt")
#     # Processing goes here.
#     stream.close()
# except Exception as exc:
#     print("Cannot open the file:", exc)

'''
Let's analyze them:

[sys.stdin]
stdin (as standard input)
the stdin stream is normally associated with the keyboard, pre-open for reading and regarded as the primary data source
 for the running programs;
the well-known input() function reads data from stdin by default.

[sys.stdout]
stdout (as standard output)
the stdout stream is normally associated with the screen, pre-open for writing, 
regarded as the primary target for outputting data by the running program;
the well-known print() function outputs the data to the stdout stream.

[sys.stderr]
stderr (as standard error output)
the stderr stream is normally associated with the screen, pre-open for writing, 
regarded as the primary place where the running program should send information on the errors encountered during its work;
we haven't presented any method to send the data to this stream (we will do it soon, we promise)
the separation of stdout (useful results produced by the program) from the stderr 
(error messages, undeniably useful but does not provide results)
gives the possibility of redirecting these two types of information to the different targets.
More extensive discussion of this issue is beyond the scope of our course. 
The operation system handbook will provide more information on these issues.


Diagnosing stream problems
The IOError object is equipped with a property named errno 
(the name comes from the phrase error number) and you can access it as follows:

try:
    # Some stream operations.
except IOError as exc:
    print(exc.errno)


The value of the errno attribute can be compared with one of the predefined symbolic 
constants defined in the errno module.

Let's take a look at some selected constants useful for detecting stream errors:

[errno.EACCES] → Permission denied 
The error occurs when you try, for example, to open a file with the read only attribute for writing.

[errno.EBADF] → Bad file number 
The error occurs when you try, for example, to operate with an unopened stream.

[errno.EEXIST] → File exists 
The error occurs when you try, for example, to rename a file with its previous name.

[errno.EFBIG] → File too large 
The error occurs when you try to create a file that is larger than the maximum allowed by the operating system.

[errno.EISDIR] → Is a directory 
The error occurs when you try to treat a directory name as the name of an ordinary file.

[errno.EMFILE] → Too many open files 
The error occurs when you try to simultaneously open more streams than acceptable for your operating system.

[errno.ENOENT] → No such file or directory 
The error occurs when you try to access a non-existent file/directory.

[errno.ENOSPC] → No space left on device 
The error occurs when there is no free space on the media.
The complete list is much longer (it includes also some error codes not related to the stream processing.)
'''
# import errno
#
# try:
#     s = open("c:/users/user/Desktop/file.txt", "rt")
#     # Actual processing goes here.
#     s.close()
# except Exception as exc:
#     if exc.errno == errno.ENOENT:
#         print("The file doesn't exist.")
#     elif exc.errno == errno.EMFILE:
#         print("You've opened too many files.")
#     else:
#         print("The error number is:", exc.errno)
#



# # Opening tzop.txt in read mode, returning it as a file object:
# stream = open("tzop.txt", "rt", encoding = "utf-8")
# print(stream.read()) # printing the content of the file

'''#######################  посчитать кол-во символов в тексте 
The routine is rather simple:

use the try-except mechanism and open the file of the predetermined name (text.txt in our case)
try to read the very first character from the file (ch = s.read(1))
if you succeed (this is proven by a positive result of the while condition check), output the character (note the end= argument - it's important! You don't want to skip to a new line after every character!);
update the counter (cnt), too;
try to read the next character, and the process repeats.
'''

# from os import strerror
# try:
#     cnt = 0
#     s = open('text.txt', "rt")
#     ch = s.read(1)
#     while ch != '':
#         print(ch, end='')
#         cnt += 1
#         ch = s.read(1)
#     s.close()
#     print("\n\nCharacters in file:", cnt)
# except IOError as e:
#     print("I/O error occurred: ", strerror(e.errno))
#


# II
# from os import strerror
# try:
#     cnt = 0
#     s = open('text.txt', "rt")
#     content = s.read()
#     for ch in content:
#         print(ch, end='')
#         cnt += 1
#     s.close()
#     print("\n\nCharacters in file:", cnt)
# except IOError as e:
#     print("I/O error occurred: ", strerr(e.errno))
#
# ####Processing text files: readline()

# from os import strerror
# try:
#     ccnt = lcnt = 0
#     s = open('text.txt', 'rt')
#     line = s.readline()
#     while line != '':
#         lcnt += 1
#         for ch in line:
#             print(ch, end='')
#             ccnt += 1
#         line = s.readline()
#     s.close()
#     print("\n\nCharacters in file:", ccnt)
#     print("Lines in file:     ", lcnt)
# except IOError as e:
#     print("I/O error occurred:", strerror(e.errno))



'''
Processing text files: readlines()
Another method, which treats text file as a set of lines, not characters, is readlines().
The readlines() method, when invoked without arguments, tries to read all the file contents, 
and returns a list of strings, one element per file line.
If you're not sure if the file size is small enough and don't want to test the OS, 
you can convince the readlines() method to read not more than a specified number of bytes at once 
(the returning value remains the same - it's a list of a string).
Feel free to experiment with the following example code to understand how the readlines() method works:

s = open("text.txt")
print(s.readlines(20))
print(s.readlines(20))
print(s.readlines(20))
print(s.readlines(20))
s.close()


The maximum accepted input buffer size is passed to the method as its argument.
You may expect that readlines() can process a file's contents more effectively than readline(), 
as it may need to be invoked fewer times.
Note: when there is nothing to read from the file, the method returns an empty list. 
Use it to detect the end of the file.
To the extent of the buffer's size, you can expect that increasing it may improve input performance, 
but there is no golden rule for it - try to find the optimal values yourself.
Look at the code in the editor. We've modified it to show you how to use readlines().
We've decided to use a 15-byte-long buffer. Don't think it's a recommendation.
We've used such a value to avoid the situation in which the first readlines() invocation consumes the whole file.
We want the method to be forced to work harder, and to demonstrate its capabilities.
There are two nested loops in the code: the outer one uses readlines()'s result to iterate through it, 
while the inner one prints the lines character by character.
'''
# from os import strerror
#
# try:
#     ccnt = lcnt = 0
#     s = open('text.txt', 'rt')
#     lines = s.readlines(20)
#     while len(lines) != 0:
#         for line in lines:
#             lcnt += 1
#             for ch in line:
#                 print(ch, end='')
#                 ccnt += 1
#         lines = s.readlines(10)
#     s.close()
#     print("\n\nCharacters in file:", ccnt)
#     print("Lines in file:     ", lcnt)
# except IOError as e:
#     print("I/O error occurred:", strerror(e.errno))

'''
Processing text files: continued
The last example we want to present shows a very interesting trait of the object returned by the open() function in text mode.
We think it may surprise you - the object is an instance of the iterable class.
Strange? Not at all. Usable? Yes, absolutely.
The iteration protocol defined for the file object is very simple - its __next__ method 
just returns the next line read in from the file.
Moreover, you can expect that the object automatically invokes close() when any of the file reads reaches the end of the file.
Look at the editor and see how simple and clear the code has now become.
'''

# from os import strerror
#
# try:
# 	ccnt = lcnt = 0
# 	for line in open('text.txt', 'rt'):
# 		lcnt += 1
# 		for ch in line:
# 			print(ch, end='')
# 			ccnt += 1
# 	print("\n\nCharacters in file:", ccnt)
# 	print("Lines in file:     ", lcnt)
# except IOError as e:
# 	print("I/O error occurred: ", strerror(e.errno))


'''#####################################################################

Dealing with text files: write()
Writing text files seems to be simpler, as in fact there is one method that can be used to perform such a task.
The method is named write() and it expects just one argument - a string that will be transferred to an open file 
(don't forget - the open mode should reflect the way in which the data is transferred - 
writing a file opened in read mode won't succeed).
No newline character is added to the write()'s argument, so you have to add it yourself 
if you want the file to be filled with a number of lines.
The example in the editor shows a very simple code that creates a file named newtext.txt 
(note: the open mode w ensures that the file will be created from scratch, even if it exists and contains data) 
and then puts ten lines into it.
The string to be recorded consists of the word line, followed by the line number. 
We've decided to write the string's contents character by character (this is done by the inner for loop) 
but you're not obliged to do it in this way.
We just wanted to show you that write() is able to operate on single characters.
The code creates a file filled with the following text:

line #1
line #2
line #3
line #4
line #5
line #6
line #7
line #8
line #9
line #10
output


Can you print the file's contents to the console?
We encourage you to test the behavior of the write() method locally on your machine.'''

# from os import strerror
#
# try:
# 	fo = open('newtext.txt', 'wt') # A new file (newtext.txt) is created.
# 	for i in range(10):
# 		s = "line #" + str(i+1) + "\n"
# 		for ch in s:
# 			fo.write(ch)
# 	fo.close()
# except IOError as e:
# 	print("I/O error occurred: ", strerror(e.errno))


'''
Dealing with text files: continued
Look at the example in the editor. We've modified the previous code to write whole lines to the text file.
The contents of the newly created file are the same.
Note: you can use the same method to write to the stderr stream, but don't try to open it, as it's always open implicitly.
For example, if you want to send a message string to stderr to distinguish it from normal program output, 
it may look like this:
'''
# from os import strerror
#
# try:
#     fo = open('newtext.txt', 'wt')
#     for i in range(10):
#         fo.write("line #" + str(i+1) + "\n")
#     fo.close()
# except IOError as e:
#     print("I/O error occurred: ", strerror(e.errno))

'''
Bytearrays: continued
Bytearrays resemble lists in many respects.
For example, they are mutable, they're a subject of the len() function, 
and you can access any of their elements using conventional indexing.
There is one important limitation - you mustn't set any byte array elements with a value which is not an integer
(violating this rule will cause a TypeError exception) and you're not allowed to assign a value that doesn't come 
from the range 0 to 255 inclusive (unless you want to provoke a ValueError exception).
You can treat any byte array elements as integer values - just like in the example in the editor.
Note: we've used two methods to iterate the byte arrays, and made use of the hex() function to see 
the elements printed as hexadecimal values.
Now we're going to show you how to write a byte array to a binary file - binary, 
as we don't want to save its readable representation - we want to write a one-to-one 
copy of the physical memory content, byte by byte.
'''
data = bytearray(3)

print (data)

# for i in range(len(data)):
#     data[i] = 10 - i
#
# for b in data:
#     print(hex(b))

'''
Bytearrays: continued
So, how do we write a byte array to a binary file?
Look at the code in the editor. Let's analyze it:
first, we initialize bytearray with subsequent values starting from 10; 
if you want the file's contents to be clearly readable, replace 10 with something like ord('a') - 
this will produce bytes containing values corresponding to the alphabetical part of the ASCII code 
(don't think it will make the file a text file - it's still binary, as it was created with a wb flag);
then, we create the file using the open() function - the only difference compared to the previous variants 
is the open mode containing the b flag;
the write() method takes its argument (bytearray) and sends it (as a whole) to the file;
the stream is then closed in a routine way.
The write() method returns a number of successfully written bytes.
If the values differ from the length of the method's arguments, it may announce some write errors.
In this case, we haven't made use of the result - this may not be appropriate in every case.
Try to run the code and analyze the contents of the newly created output file.
You're going to use it in the next step.

How to read bytes from a stream

Reading from a binary file requires use of a specialized method name readinto(), as the method doesn't create 
a new byte array object, but fills a previously created one with the values taken from the binary file.

Note:

the method returns the number of successfully read bytes;
the method tries to fill the whole space available inside its argument; 
if there are more data in the file than space in the argument, the read operation will stop before the end of the file;
otherwise, the method's result may indicate that the byte array has only been filled fragmentarily 
(the result will show you that, too, and the part of the array not being used by the newly read contents
remains untouched)
Look at the complete code below:

from os import strerror

data = bytearray(10)
try:
    bf = open('file.bin', 'rb')
    bf.readinto(data)
    bf.close()

    for b in data:
        print(hex(b), end=' ')
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))


Let's analyze it:

first, we open the file (the one you created using the previous code) with the mode described as rb;
then, we read its contents into the byte array named data, of size ten bytes;
finally, we print the byte array contents - are they the same as you expected?
Run the code and check if it's working.
# '''
# from os import strerror
#
# data = bytearray(10)
#
# for i in range(len(data)):
#     data[i] = 10 + i
#
# try:
#     bf = open('file.bin', 'wb')
#     bf.write(data)
#     bf.close()
# except IOError as e:
#     print("I/O error occurred:", strerror(e.errno))
#
# # Your code that reads bytes from the stream should go here.


'''#
How to read bytes from a stream
An alternative way of reading the contents of a binary file is offered by the method named read().
Invoked without arguments, it tries to read all the contents of the file into the memory, 
making them a part of a newly created object of the bytes class.
This class has some similarities to bytearray, with the exception of one significant difference - it's immutable.
Fortunately, there are no obstacles to creating a byte array by taking its initial value directly from the bytes object,
just like here:

from os import strerror
try:
    bf = open('file.bin', 'rb')
    data = bytearray(bf.read())
    bf.close()

    for b in data:
        print(hex(b), end=' ')

except IOError as e:
    print("I/O error occurred:", strerror(e.errno))


Be careful - don't use this kind of read if you're not sure that the file's contents will fit the available memory.
'''

# from os import strerror
#
# data = bytearray(10)
#
# for i in range(len(data)):
#     data[i] = 10 + i
#
# try:
#     bf = open('file.bin', 'wb')
#     bf.write(data)
#     bf.close()
# except IOError as e:
#     print("I/O error occurred:", strerror(e.errno))
#
# # Your code that reads bytes from the stream should go here.

'''
How to read bytes from a stream: continued
If the read() method is invoked with an argument, it specifies the maximum number of bytes to be read.
The method tries to read the desired number of bytes from the file, and the length of the returned object 
can be used to determine the number of bytes actually read.
You can use the method just like here:

try:
    bf = open('file.bin', 'rb')
    data = bytearray(bf.read(5))
    bf.close()

    for b in data:
        print(hex(b), end=' ')

except IOError as e:
    print("I/O error occurred:", strerror(e.errno))


Note: the first five bytes of the file have been read by the code - the next five are still waiting to be processed.
'''
#
# from os import strerror
#
# data = bytearray(10)
#
# for i in range(len(data)):
#     data[i] = 10 + i
#
# try:
#     bf = open('file.bin', 'wb')
#     bf.write(data)
#     bf.close()
# except IOError as e:
#     print("I/O error occurred:", strerror(e.errno))
#
# # Your code that reads bytes from the stream should go here.
'''
Copying files - a simple and functional tool
Now you're going to amalgamate all this new knowledge, add some fresh elements to it, and use it to write a real code which is able to actually copy a file's contents.

Of course, the purpose is not to make a better replacement for commands like copy (MS Windows) or cp (Unix/Linux) but to see one possible way of creating a working tool, even if nobody wants to use it.

Look at the code in the editor. Let's analyze it:

lines 3 through 8: ask the user for the name of the file to copy, and try to open it to read; terminate the program execution if the open fails; note: use the exit() function to stop program execution and to pass the completion code to the OS; any completion code other than 0 says that the program has encountered some problems; use the errno value to specify the nature of the issue;
lines 10 through 16: repeat nearly the same action, but this time for the output file;
line 18: prepare a piece of memory for transferring data from the source file to the target one; such a transfer area is often called a buffer, hence the name of the variable; the size of the buffer is arbitrary - in this case, we decided to use 64 kilobytes; technically, a larger buffer is faster at copying items, as a larger buffer means fewer I/O operations; actually, there is always a limit, the crossing of which renders no further improvements; test it yourself if you want.
line 19: count the bytes copied - this is the counter and its initial value;
line 21: try to fill the buffer for the very first time;
line 22: as long as you get a non-zero number of bytes, repeat the same actions;
line 23: write the buffer's contents to the output file (note: we've used a slice to limit the number of bytes being written, as write() always prefer to write the whole buffer)
line 24: update the counter;
line 25: read the next file chunk;
lines 30 through 32: some final cleaning - the job is done.

'''

# from os import strerror
#
# srcname = input("Enter the source file name: ")
# try:
#     src = open(srcname, 'rb')
# except IOError as e:
#     print("Cannot open the source file: ", strerror(e.errno))
#     exit(e.errno)
#
# dstname = input("Enter the destination file name: ")
# try:
#     dst = open(dstname, 'wb')
# except Exception as e:
#     print("Cannot create the destination file: ", strerror(e.errno))
#     src.close()
#     exit(e.errno)
#
# buffer = bytearray(65536)
# total  = 0
# try:
#     readin = src.readinto(buffer)
#     while readin > 0:
#         written = dst.write(buffer[:readin])
#         total += written
#         readin = src.readinto(buffer)
# except IOError as e:
#     print("Cannot create the destination file: ", strerror(e.errno))
#     exit(e.errno)


'''
Estimated time
30-60 minutes

Level of difficulty
Medium

Objectives
improving the student's skills in operating with files (reading)
using data collections for counting numerous data.
Scenario
A text file contains some text (nothing unusual) but we need to know how often (or how rare) each letter appears 
in the text. Such an analysis may be useful in cryptography, so we want to be able to do that in reference 
to the Latin alphabet.

Your task is to write a program which:

asks the user for the input file's name;
reads the file (if possible) and counts all the Latin letters (lower- and upper-case letters are treated as equal)
prints a simple histogram in alphabetical order (only non-zero counts should be presented)
Create a test file for the code, and check if your histogram contains valid results.

Assuming that the test file contains just one line filled with:

aBc
samplefile.txt

the expected output should look as follows:

a -> 1
b -> 1
c -> 1
output

Tip: We think that a dictionary is a perfect data collection medium for storing the counts. 
The letters may be keys while the counters can be values.
'''

'''
Estimated time
15-30 minutes

Level of difficulty
Medium

Prerequisites
4.3.1.15

Objectives
improve the student's skills in operating with files (reading/writing)
using lambdas to change the sort order.
Scenario
The previous code needs to be improved. It's okay, but it has to be better.

Your task is to make some amendments, which generate the following results:

the output histogram will be sorted based on the characters' frequency (the bigger counter should be presented first)
the histogram should be sent to a file with the same name as the input one, but with the suffix '.hist' 
(it should be concatenated to the original name)
Assuming that the input file contains just one line filled with:

cBabAa
samplefile.txt

the expected output should look as follows:

a -> 3
b -> 2
c -> 1
output

Tip: Use a lambda to change the sort order.
'''



'''
Introduction to the os module
In this section, you'll learn about a module called os, which lets you interact with the operating system using Python.

It provides functions that are available on Unix and/or Windows systems. 
If you're familiar with the command console, you'll see that some functions give the same results as the commands 
available on the operating systems.
A good example of this is the mkdir function, which allows you to create a directory just like the mkdir 
command in Unix and Windows. If you don't know this command, don't worry.
You'll soon have the opportunity to learn the functions of the os module, to perform operations on 
files and directories along with the corresponding commands.
In addition to file and directory operations, the os module enables you to:
get information about the operating system;
manage processes;
operate on I/O streams using file descriptors.
'''


'''
Getting information about the operating system
Before you create your first directory structure, you'll see how you can get information 
about the current operating system. This is really easy because the os module provides a function called uname, 
which returns an object containing the following attributes:

systemname — stores the name of the operating system;
nodename — stores the machine name on the network;
release — stores the operating system release;
version — stores the operating system version;
machine — stores the hardware identifier, e.g., x86_64.
Let's look at how it is in practice:

import os
print(os.uname())


Result:

posix.uname_result(sysname='Linux', nodename='192d19f04766', release='4.4.0-164-generic', 
version='#192-Ubuntu SMP Fri Sep 13 12:02:50 UTC 2019', machine='x86_64')
output
As you can see, the uname function returns an object containing information about the operating system.
 The above code was launched on Ubuntu 16.04.6 LTS, so don't be surprised if you get a different result, 
 because it depends on your operating system.
Unfortunately, the uname function only works on some Unix systems. If you use Windows, 
you can use the uname function in the platform module, which returns a similar result.
The os module allows you to quickly distinguish the operating system using the name attribute,
 which supports one of the following names:

posix — you'll get this name if you use Unix;
nt — you'll get this name if you use Windows;
java — you'll get this name if your code is written in Jython.
For Ubuntu 16.04.6 LTS, the name attribute returns the name posix:

import os
print(os.name)


Result:

posix
output

NOTE: On Unix systems, there's a command called uname that returns the same information 
(if you run it with the -a option) as the uname function.

'''
import os
print(os.name)
'''
Creating directories in Python
The os module provides a function called mkdir, which, like the mkdir command in Unix and Windows, 
allows you to create a directory. The mkdir function requires a path that can be relative or absolute. 
Let's recall what both paths look like in practice:

[my_first_directory] — this is a relative path which will create the my_first_directory directory 
in the current working directory;

[./my_first_directory] — this is a relative path that explicitly points to the current working directory. 
It has the same effect as the path above;

[../my_first_directory ]— this is a relative path that will create the my_first_directory directory 
in the parent directory of the current working directory;

[/python/my_first_directory] — this is the absolute path that will create the my_first_directory directory, 
which in turn is in the python directory in the root directory.

Look at the code in the editor. It shows an example of how to create the my_first_directory directory using a relative 
path. This is the simplest variant of the relative path, which consists of passing only the directory name.
If you test your code here, it will output the newly created ['my_first_directory'] directory 
(and the entire content of the current working catalog).
The mkdir function creates a directory in the specified path. Note that running the program twice 
will raise a FileExistsError.
This means that we cannot create a directory if it already exists. 
In addition to the path argument, the mkdir function can optionally take the mode argument, 
which specifies directory permissions. However, on some systems, the mode argument is ignored.
To change the directory permissions, we recommend the chmod function, which works similarly 
to the chmod command on Unix systems. You can find more information about it in the documentation.
In the above example, another function provided by the os module named listdir is used. 
The listdir function returns a list containing the names of the files and directories that are in the path passed as an argument.
If no argument is passed to it, the current working directory will be used (as in the example above). 
It's important that the result of the listdir function omits the entries '.' and '..', which are displayed, e.g., 
when using the ls -a command on Unix systems.
NOTE: In both Windows and Unix, there's a command called mkdir, which requires a directory path. 
The equivalent of the above code that creates the my_first_directory directory is the mkdir my_first_directory command.
'''

# import os
#
# os.mkdir("my_first_directory")
# print(os.listdir())


'''
Recursive directory creation
The mkdir function is very useful, but what if you need to create another directory in the directory you've just created.
Of course, you can go to the created directory and create another directory inside it, but fortunately the os 
module provides a function called makedirs, which makes this task easier.
The makedirs function enables recursive directory creation, which means that all directories in the path will be created.
Let's look at the code in the editor and see how it is in practice.
The code should produce the following result:

['my_second_directory']
output
The code creates two directories. The first of them is created in the current working directory, 
while the second in the my_first_directory directory.
You don't have to go to the my_first_directory directory to create the my_second_directory directory, 
because the makedirs function does this for you. In the example above, we go to the my_first_directory directory 
to show that the makedirs command creates the my_second_directory subdirectory.
To move between directories, you can use a function called chdir, which changes the current working 
directory to the specified path. As an argument, it takes any relative or absolute path. In our example, 
we pass the first directory name to it.
NOTE: The equivalent of the makedirs function on Unix systems is the mkdir command with the -p flag, 
while in Windows, simply the mkdir command with the path:

Unix-like systems: 
mkdir -p my_first_directory/my_second_directory

Windows: 
mkdir my_first_directory/my_second_directory

'''

# import os
#
# os.makedirs("my_first_directory/my_second_directory")
# os.chdir("my_first_directory")
# print(os.listdir())
#

'''
Where am I now?
You already know how to create directories and how to move between them. Sometimes, when you have a really large 
directory structure that you navigate, you may not know which directory you're currently working in.
Lost programmer
As you’ve probably guessed, the os module provides a function that returns information about the current working
directory. It's called getcwd. Look at the code in the editor to see how to use it in practice.

Result:

.../my_first_directory
.../my_first_directory/my_second_directory
output

In the example, we create the my_first_directory directory, and the my_second_directory directory inside it.
 In the next step, we change the current working directory to the my_first_directory directory, 
 and then display the current working directory (first line of the result).
Next, we go to the my_second_directory directory and again display the current working directory 
(second line of the result). As you can see, the getcwd function returns the absolute path to the directories.
NOTE: On Unix-like systems, the equivalent of the getcwd function is the pwd command, 
which prints the name of the current working directory.
'''
#
# import os
#
# os.makedirs("my_first_directory/my_second_directory")
# os.chdir("my_first_directory")
# print(os.getcwd())
# os.chdir("my_second_directory")
# print(os.getcwd())


'''
Deleting directories in Python
The os module also allows you to delete directories. 
It gives you the option of deleting a single directory or a directory with its subdirectories. 
To delete a single directory, you can use a function called rmdir, which takes the path as its argument. 
Look at the code in the editor.
The above example is really simple. First, the my_first_directory directory is created, 
and then it's removed using the rmdir function. The listdir function is used as proof that the directory 
has been removed successfully. In this case, it returns an empty list. When deleting a directory, 
make sure it exists and is empty, otherwise an exception will be raised.
To remove a directory and its subdirectories, you can use the removedirs function, which requires you 
to specify a path containing all directories that should be removed:

import os

os.makedirs("my_first_directory/my_second_directory")
os.removedirs("my_first_directory/my_second_directory")
print(os.listdir())


As with the rmdir function, if one of the directories doesn't exist or isn't empty, an exception will be raised.
NOTE: In both Windows and Unix, there's a command called rmdir, which, just like the rmdir function, 
removes directories. What's more, both systems have commands to delete a directory and its contents. 
In Unix, this is the rm command with the -r flag.
'''

# import os
#
# os.mkdir("my_first_directory")
# print(os.listdir())
# os.rmdir("my_first_directory")
# print(os.listdir())
#

'''
The system() function
All functions presented in this part of the course can be replaced by a function called system, 
which executes a command passed to it as a string.
The system function is available in both Windows and Unix. Depending on the system, it returns a different result.
In Windows, it returns the value returned by the shell after running the command given, while in Unix,
it returns the exit status of the process.
Let's look at the code in the editor and see how it is in practice.

Result:
0

The above example will work in both Windows and Unix. In our case, we receive exit status 0,
 which indicates success on Unix systems.
This means that the my_first_directory directory has been created. As part of the exercise, 
try to list the contents of the directory where you created the my_first_directory directory.
# '''
# import os
#
# returned_value = os.system("mkdir my_first_directory")
# print(returned_value)


'''
Estimated time
15-30 min

Level of difficulty
Easy

Objectives
improving the student's skills in interacting with the operating system;
practical use of known functions provided by the os module.
Scenario
It goes without saying that operating systems allow you to search for files and directories. 
While studying this part of the course, you learned about the functions of the os module, 
which have everything you need to write a program that will search for directories in a given location.
To make your task easier, we have prepared a test directory structure for you:

Directory structure

Your program should meet the following requirements:

Write a function or method called find that takes two arguments called path and dir. 
The path argument should accept a relative or absolute path to a directory where the search should start, 
while the dir argument should be the name of a directory that you want to find in the given path. 
Your program should display the absolute paths if it finds a directory with the given name.
The directory search should be done recursively. This means that the search should also include 
all subdirectories in the given path.
Example input:

path="./tree", dir="python"

Example output:

.../tree/python
.../tree/cpp/other_courses/python
.../tree/c/other_courses/python

'''



'''
Introduction to the datetime module
In this section, you'll learn about a Python module called datetime.
As you can guess, it provides classes for working with date and time.
 If you think you don't need to delve into this topic, let's talk about examples of using date and time in programming.
Date and time have countless uses and it's probably hard to find a production application that doesn't use them. 
Here are some examples:

event logging — thanks to the knowledge of date and time, we are able to determine when exactly a critical 
error occurs in our application. When creating logs, you can specify the date and time format;
tracking changes in the database — sometimes it's necessary to store information about when a record was 
created or modified. The datetime module will be perfect for this case;
data validation — you'll soon learn how to read the current date and time in Python. 
Knowing the current date and time, we're able to validate various types of data, e.g., 
whether a discount coupon entered by a user in our application is still valid;
storing important information — can you imagine bank transfers without storing the information of when they were made? 
The date and time of certain actions must be preserved, and we must deal with it.

Getting the current local date and creating date objects
One of the classes provided by the datetime module is a class called date. 
Objects of this class represent a date consisting of the year, month, and day.
 Look at the code in the editor to see what it looks like in practice and get the current local date using the today method.
Run the code to see what happens.
The today method returns a date object representing the current local date. 
Note that the date object has three attributes: year, month, and day.
Be careful, because these attributes are read-only. To create a date object, 
you must pass the year, month, and day parameters as follows:

[from datetime import date
my_date = date(2019, 11, 4)
print(my_date)]

When creating a date object, keep the following restrictions in mind:

Parameter	Restrictions
year	    The year parameter must be 
            greater than or equal to 1 
            (MINYEAR constant) and less than or equal to 9999 (MAXYEAR constant).

month	    The month parameter must be greater 
            than or equal to 1 and less than or equal to 12.

day	        The day parameter must be greater than or equal 
            to 1 and less than or equal to the last day of 
            the given month and year.

Note: Later in this course you'll learn how to change the default date format.


'''
# from datetime import date
#
# today = date.today()
#
# print("Today:", today)
# print("Year:", today.year)
# print("Month:", today.month)
# print("Day:", today.day)


'''
Creating a date object from a timestamp
The date class gives us the ability to create a date object from a timestamp.
In Unix, the timestamp expresses the number of seconds since January 1, 1970, 00:00:00 (UTC). 
This date is called the Unix epoch, because this is when the counting of time began on Unix systems.
The timestamp is actually the difference between a particular date (including time) and January 1, 1970, 00:00:00 (UTC),
 expressed in seconds.
To create a date object from a timestamp, we must pass a Unix timestamp to the fromtimestamp method.
For this purpose, we can use the time module, which provides time-related functions. 
One of them is a function called time() that returns the number of seconds from January 1, 1970 
to the current moment in the form of a float number. Take a look at the example in the editor.
Run the code to see the output.
If you run the sample code several times, you'll be able to see how the timestamp increments itself. 
It's worth adding that the result of the time function depends on the platform, because in Unix and Windows systems, 
leap seconds aren't counted.
Note: In this part of the course we'll also talk about the time module.
'''
# from datetime import date
# import time
#
# timestamp = time.time()
# print("Timestamp:", timestamp)
#
# d = date.fromtimestamp(timestamp)
# print("Date:", d)



'''
Creating a date object using the ISO format
The datetime module provides several methods to create a date object. 
One of them is the fromisoformat method, which takes a date in the YYYY-MM-DD format compliant with the ISO 8601 standard.
The ISO 8601 standard defines how the date and time are represented. It's often used, 
so it's worth taking a moment to familiarize yourself with it. Take a look at the picture 
describing the values required by the format:

The ISO 8601 date and time format
Now look at the code in the editor and run it.
In our example, YYYY is 2019, MM is 11 (November), and DD is 04 (fourth day of November).

When substituting the date, be sure to add 0 before a month or a day that is expressed by a number less than 10.
Note: The fromisoformat method has been available in Python since version 3.7.

'''
# from datetime import date
#
# d = date.fromisoformat('2019-11-04')
# print(d)

'''
The replace() method
Sometimes you may need to replace the year, month, or day with a different value. 
You can’t do this with the year, month, and day attributes because they're read-only. 
In this case, you can use the method named replace.

Run the code in the editor.

Result:
1991-02-05
1992-01-16


The year, month, and day parameters are optional. 
You can pass only one parameter to the replace method, e.g., year, or all three as in the example.
The replace method returns a changed date object, so you must remember to assign it to some variable.
'''

# from datetime import date
#
# d = date(1991, 2, 5)
# print(d)
#
# d = d.replace(year=1992, month=1, day=16)
# print(d)


'''
What day of the week is it?
One of the more helpful methods that makes working with dates easier is the method called weekday. 
It returns the day of the week as an integer, where 0 is Monday and 6 is Sunday. Run the code in the editor.

Result:
0
The date class has a similar method called isoweekday, which also returns the day of the week as an integer, 
but 1 is Monday, and 7 is Sunday:

from datetime import date
d = date(2019, 11, 4)
print(d.isoweekday())

Result:
1


As you can see, for the same date we get a different integer, but expressing the same day of the week. 
The integer returned by the isodayweek method follows the ISO 85601 specification.
'''

# from datetime import date
#
# d = date(2019, 11, 4)
# print(d.weekday())

'''
Creating time objects
You already know how to present a date using the date object.
 The datetime module also has a class that allows you to present time. Can you guess its name? Yes, it's called time:
time(hour, minute, second, microsecond, tzinfo, fold)
The time class constructor accepts the following optional parameters:

Parameter	    Restrictions
hour	        The hour parameter must be greater 
                than or equal to 0 and less than 23.

minute	        The minute parameter must be greater 
                than or equal to 0 and less than 59.

second	        The second parameter must be greater 
                than or equal to 0 and less than 59.

microsecond	    The microsecond parameter must be 
                greater than or equal to 0 and less than 1000000.

tzinfo	        The tzinfo parameter must be a tzinfo 
                subclass object or None (default).

fold	        The fold parameter must be 0 or 1 (default 0).

The tzinfo parameter is associated with time zones, while fold with wall times. 
We won't use them during this course, but we encourage you to familiarize yourself with them.
Let's look at how to create a time object in practice. Run the code in the editor.

Result:

Time: 14:53:20.000001
Hour: 14
Minute: 53
Second: 20
Microsecond: 1

In the example, we passed four parameters to the class constructor: 
hour, minute, second, and microsecond. Each of them can be accessed using the class attributes.
Note: Soon we'll tell you how you can change the default time formatting.

'''
# from datetime import time
#
# t = time(14, 53, 20, 1)
#
# print("Time:", t)
# print("Hour:", t.hour)
# print("Minute:", t.minute)
# print("Second:", t.second)
# print("Microsecond:", t.microsecond)

'''
The time module
In addition to the time class, the Python standard library offers a module called time, 
which provides a time-related function. You already had the opportunity to learn the function called 
time when discussing the date class. Now we'll look at another useful function available in this module.
You must spend many hours in front of a computer while doing this course. 
Sometimes you may feel the need to take a nap. 
Why not? Let's write a program that simulates a student's short nap. Have a look at the code in the editor.

Result:
I'm very tired. I have to take a nap. See you later.
I slept well! I feel great!

The most important part of the sample code is the use of the sleep function 
(yes, you may remember it from one of the previous labs earlier in the course), 
which suspends program execution for the given number of seconds.
In our example it's 5 seconds. You're right, it's a very short nap.
Extend the student's sleep by changing the number of seconds. 
Note that the sleep function accepts only an integer or a floating point number.
'''
# import time
#
# class Student:
#     def take_nap(self, seconds):
#         print("I'm very tired. I have to take a nap. See you later.")
#         time.sleep(seconds)
#         print("I slept well! I feel great!")
#
# student = Student()
# student.take_nap(5)


'''
The ctime() function
The time module provides a function called ctime, 
which converts the time in seconds since January 1, 1970 (Unix epoch) to a string.
Do you remember the result of the time function? 
That's what you need to pass to ctime. Take a look at the example in the editor.

Result:
Mon Nov  4 14:53:00 2019

The ctime function returns a string for the passed timestamp. 
In our example, the timestamp expresses November 4, 2019 at 14:53:00.
It's also possible to call the ctime function without specifying the time in seconds. 
In this case, the current time will be returned:

import time
print(time.ctime())
'''
# import time
#
# timestamp = 1572879180
# print(time.ctime(timestamp))
#

'''
The gmtime() and localtime() functions
Some of the functions available in the time module require knowledge of the struct_time class, 
but before we get to know them, let's see what the class looks like:

time.struct_time:
    tm_year   # specifies the year
    tm_mon    # specifies the month (value from 1 to 12)
    tm_mday   # specifies the day of the month (value from 1 to 31)
    tm_hour   # specifies the hour (value from 0 to 23)
    tm_min    # specifies the minute (value from 0 to 59)
    tm_sec    # specifies the second (value from 0 to 61 )
    tm_wday   # specifies the weekday (value from 0 to 6)
    tm_yday   # specifies the year day (value from 1 to 366)
    tm_isdst  # specifies whether daylight saving time applies (1 – yes, 0 – no, -1 – it isn't known)
    tm_zone   # specifies the timezone name (value in an abbreviated form)
    tm_gmtoff # specifies the offset east of UTC (value in seconds)


The struct_time class also allows access to values using indexes. 
Index 0 returns the value in tm_year, while 8 returns the value in tm_isdst.
The exceptions are tm_zone and tm_gmoff, which cannot be accessed using indexes. 
Let's look at how to use the struct_time class in practice. Run the code in the editor.

Result:

time.struct_time(tm_year=2019, tm_mon=11, tm_mday=4, tm_hour=14, tm_min=53, tm_sec=0, tm_wday=0, tm_yday=308, tm_isdst=0)
time.struct_time(tm_year=2019, tm_mon=11, tm_mday=4, tm_hour=14, tm_min=53, tm_sec=0, tm_wday=0, tm_yday=308, tm_isdst=0)

The example shows two functions that convert the elapsed time from the Unix epoch to the struct_time object. 
The difference between them is that the gmtime function returns the struct_time object in UTC, 
while the localtime function returns local time. For the gmtime function, the tm_isdst attribute is always 0.

# '''
# import time
#
# timestamp = 1572879180
# print(time.gmtime(timestamp))
# print(time.localtime(timestamp))


'''
The asctime() and mktime() functions
The time module has functions that expect a struct_time object or a tuple that stores values 
according to the indexes presented when discussing the struct_time class. Run the example in the editor.

Result:

Mon Nov  4 14:53:00 2019
1572879180.0

The first of the functions, called asctime, converts a struct_time object or a tuple to a string. 
Note that the familiar gmtime function is used to get the struct_time object. If you don't provide an argument 
to the asctime function, the time returned by the localtime function will be used.
The second function called mktime converts a struct_time object or a tuple that expresses the local 
time to the number of seconds since the Unix epoch. In our example, we passed a tuple to it, 
which consists of the following values:

2019 => tm_year
11 => tm_mon
4 => tm_mday
14 => tm_hour
53 => tm_min
0 => tm_sec
0 => tm_wday
308 => tm_yday
0 => tm_isdst

'''
# import time
#
# timestamp = 1572879180
# st = time.gmtime(timestamp)
#
# print(time.asctime(st))
# print(time.mktime((2019, 11, 4, 14, 53, 0, 0, 308, 0)))


'''
Creating datetime objects
In the datetime module, date and time can be represented as separate objects or as one. 
The class that combines date and time is called datetime.
datetime(year, month, day, hour, minute, second, microsecond, tzinfo, fold)

Its constructor accepts the following parameters:

Parameter	Restrictions
year	    The year parameter must be greater than or equal 
            to 1 (MINYEAR constant) and less than or equal 
            to 9999 (MAXYEAR constant).

month	    The month parameter must be greater than or equal
            to 1 and less than or equal to 12.

day	        The day parameter must be greater than or equal to
            1 and less than or equal to the last day of the 
            given month and year.

hour	    The hour parameter must be greater than or equal 
            to 0 and less than 23.

minute	    the minute parameter must be greater than or equal
            to 0 and less than 59.

second	    The second parameter must be greater than or equal
            to 0 and less than 59.

microsecond	   The microsecond parameter must be greater than 
               or equal to 0 and less than 1000000.

tzinfo	    The tzinfo parameter must be a tzinfo subclass 
            object or None (default).

fold	    The fold parameter must be 0 or 1 (default 0).

Now let's have a look at the code in the editor to see how we create a datetime object.

Result:

Datetime: 2019-11-04 14:53:00
Date: 2019-11-04
Time: 14:53:00

The example creates a datetime object representing November 4, 2019 at 14:53:00. 
All parameters passed to the constructor go to read-only class attributes. 
They're year, month, day, hour, minute, second, microsecond, tzinfo, and fold.
The example shows two methods that return two different objects. 
The method called date returns the date object with the given year, month, and day, 
while the method called time returns the time object with the given hour and minute.


'''
# from datetime import datetime
#
# dt = datetime(2019, 11, 4, 14, 53)
#
# print("Datetime:", dt)
# print("Date:", dt.date())
# print("Time:", dt.time())
#

'''
Methods that return the current date and time
The datetime class has several methods that return the current date and time. These methods are:

today() — returns the current local date and time with the tzinfo attribute set to None;
now() — returns the current local date and time the same as the today method, unless we pass the optional argument 
tz to it. The argument of this method must be an object of the tzinfo subclass;
utcnow() — returns the current UTC date and time with the tzinfo attribute set to None.
Run the code in the editor to see them all in practice. What can you say about the output?
As you can see, the result of all the three methods is the same. The small differences are caused by the time elapsed
 between subsequent calls.
Note: You can read more about tzinfo objects in the documentation.
'''
# from datetime import datetime
#
# print("today:", datetime.today())
# print("now:", datetime.now())
# print("utcnow:", datetime.utcnow())


'''
Getting a timestamp
There are many converters available on the Internet that can calculate a timestamp based 
on a given date and time, but how can we do it in the datetime module?
This is possible thanks to the timestamp method provided by the datetime class. Look at the code in the editor.

Result:

Timestamp: 1601823300.0

The timestamp method returns a float value expressing the number of seconds elapsed between the date and time 
indicated by the datetime object and January 1, 1970, 00:00:00 (UTC).
'''
#
# from datetime import datetime
#
# dt = datetime(2020, 10, 4, 14, 55)
# print("Timestamp:", dt.timestamp())


'''
Date and time formatting (part 1)
All datetime module classes presented so far have a method called strftime. 
This is a very important method, because it allows us to return the date and time in the format we specify.
The strftime method takes only one argument in the form of a string specifying the format that can consist of directives.
A directive is a string consisting of the character % (percent) and a lowercase or uppercase letter, e.g., 
the directive %Y means the year with the century as a decimal number. Let's see it in an example. Run the code in the editor.

Result:
2020/01/04

In the example, we passed a format consisting of three directives separated by / (slash) to the strftime method. 
Of course, the separator character can be replaced by another character, or even by a string.
You can put any characters in the format, but only recognizable directives will be replaced with the appropriate values.
 In our format we've used the following directives:
%Y – returns the year with the century as a decimal number. In our example, this is 2020.
%m – returns the month as a zero-padded decimal number. In our example, it's 01.
%d – returns the day as a zero-padded decimal number. In our example, it's 04.
Note: You can find all available directives here.
'''
# from datetime import date
#
# d = date(2020, 1, 4)
# print(d.strftime('%Y/%m/%d'))


'''
Date and time formatting (part 2)
Time formatting works in the same way as date formatting, but requires the use of appropriate directives. 
Let's take a closer look at a few of them in the editor.

Result:
14:53:00
20/November/04 14:53:00

The first of the formats used concerns only time. As you can guess, %H returns the hour as a zero-padded decimal number,
 %M returns the minute as a zero-padded decimal number, while %S returns the second as a zero-padded decimal number. 
 In our example, %H is replaced by 14, %M by 53, and %S by 00.
The second format used combines date and time directives. There are two new directives, %Y and %B. 
The directive %Y returns the year without a century as a zero-padded decimal number (in our example it's 20).
 The %B directive returns the month as the locale’s full name (in our example, it's November).
In general, you've got a lot of freedom in creating formats, but you must remember to use the directives properly. 
As an exercise, you can check what happens if, for example, you try to use the %Y directive in the format passed 
to the time object's strftime method. Try to find out why you got this result yourself. Good luck!
'''
# from datetime import time
# from datetime import datetime
#
# t = time(14, 53)
# print(t.strftime("%H:%M:%S"))
#
# dt = datetime(2020, 11, 4, 14, 53)
# print(dt.strftime("%y/%B/%d %H:%M:%S"))


'''
The strftime() function in the time module
You probably won't be surprised to learn that the strftime function is available in the time module. 
It differs slightly from the strftime methods in the classes provided by the datetime module because, 
in addition to the format argument, it can also take (optionally) a tuple or struct_time object.
If you don't pass a tuple or struct_time object, the formatting will be done using the current local time. 
Take a look at the example in the editor.

Our result looks as follows:

2019/11/04 14:53:00
2020/10/12 12:19:40

Creating a format looks the same as for the strftime methods in the datetime module. 
In our example, we use the %Y, %m, %d, %H, %M, and %S directives that you already know.
In the first function call, we format the struct_time object, while in the second call (without the optional argument), 
we format the local time. You can find all available directives in the time module here.

'''
# import time
#
# timestamp = 1572879180
# st = time.gmtime(timestamp)
#
# print(time.strftime("%Y/%m/%d %H:%M:%S", st))
# print(time.strftime("%Y/%m/%d %H:%M:%S"))


'''
The strptime() method
Knowing how to create a format can be helpful when using a method called strptime in the datetime class. 
Unlike the strftime method, it creates a datetime object from a string representing a date and time.
The strptime method requires you to specify the format in which you saved the date and time. 
Let's see it in an example. Take a look at the code in the editor.

Result:
2019-11-04 14:53:00

In the example, we've specified two required arguments. 
The first is a date and time as a string: "2019/11/04 14:53:00", 
while the second is a format that facilitates parsing to a datetime object. Be careful, 
because if the format you specify doesn't match the date and time in the string, it'll raise a ValueError.
Note: In the time module, you can find a function called strptime, which parses a string representing 
a time to a struct_time object. Its use is analogous to the strptime method in the datetime class:
'''

# from datetime import datetime
# print(datetime.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S"))


'''
Date and time operations
Sooner or later you'll have to perform some calculations on the date and time. 
Fortunately, there's a class called timedelta in the datetime module that was created for just such a purpose.
To create a timedelta object, just do subtraction on the date or datetime objects, 
just like we did in the example in the editor. Run it.

Result:

366 days, 0:00:00
365 days, 9:07:00

The example shows subtraction for both the date and datetime objects. 
In the first case, we receive the difference in days, which is 366 days. Note that the difference in hours, 
minutes, and seconds is also displayed. In the second case, we receive a different result, 
because we specified the time that was included in the calculations. As a result, we receive 365 days, 
9 hours, and 7 minutes.

In a moment you'll learn more about creating timedelta objects and about the operations you can do with them.
'''
#
from datetime import date
# from datetime import datetime
# #
# # d1 = date(2020, 11, 4)
# # d2 = date(2019, 11, 4)
# #
# # print(d1 - d2)
# #
# dt1 = datetime(2020, 11, 4, 0, 0, 0)
# dt2 = datetime(2019, 11, 4, 14, 53, 0)
#
# print(dt1 - dt2)
# #

'''
Creating timedelta objects
You've already learned that a timedelta object can be returned as a result of subtracting two date or datetime objects.

Of course, you can also create an object yourself. For this purpose, let's get acquainted with the arguments accepted by the class constructor, which are: days, seconds, microseconds, milliseconds, minutes, hours, and weeks. Each of them is optional and defaults to 0.

The arguments should be integers or floating point numbers, and can be either positive or negative. Let's look at a simple example in the editor.

Result:

16 days, 3:00:00
output

The result of 16 days is obtained by converting the weeks argument to days (2 weeks = 14 days) 
and adding the days argument (2 days). This is normal behavior, because the timedelta object only stores days, 
seconds, and microseconds internally. Similarly, the hour argument is converted to minutes. 
Take a look at the example below:

from datetime import timedelta

delta = timedelta(weeks=2, days=2, hours=3)
print("Days:", delta.days)
print("Seconds:", delta.seconds)
print("Microseconds:", delta.microseconds)

Result:

Days: 16
Seconds: 10800
Microseconds: 0

The result of 10800 is obtained by converting 3 hours into seconds. 
In this way the timedelta object stores the arguments passed during its creation.
Weeks are converted to days, hours and minutes to seconds, and milliseconds to microseconds.

'''
# from datetime import timedelta
#
# delta = timedelta(weeks=2, days=2, hours=3)
# print(delta)


'''
Creating timedelta objects: continued
You already know how the timedelta object stores the passed arguments internally. 
It's time to see how it can be used in practice.
Let's look at some operations supported by the datetime module classes. Run the code we've provided in the editor.

Result:

16 days, 2:00:00
32 days, 4:00:00
2019-11-05
2019-11-05 18:53:00

The timedelta object can be multiplied by an integer. 
In our example, we multiply the object representing 16 days and 2 hours by 2. As a result, 
we receive a timedelta object representing 32 days and 4 hours.
Note that both days and hours have been multiplied by 2. Another interesting operation using the timedelta 
object is adding. In the example, we've added the timedelta object to the date and datetime objects.
As a result of these operations, we receive date and datetime objects increased by days and hours stored i
n the timedelta object.
The presented multiplication operation allows you to quickly increase the value of the timedelta object, 
while multiplication can also help you get a date from the future.
Of course, the timedelta, date, and datetime classes support many more operations. 
We encourage you to familiarize yourself with them in the documentation.

'''
# from datetime import timedelta
# from datetime import date
# from datetime import datetime
#
# delta = timedelta(weeks=2, days=2, hours=2)
# print(delta)
#
# delta2 = delta * 2
# print(delta2)
#
# d = date(2019, 10, 4) + delta2
# print(d)
#
# dt = datetime(2019, 10, 4, 14, 53) + delta2
# print(dt)


'''
Introduction to the calendar module
In addition to the datetime and time modules, the Python standard library provides a module called calendar which, 
as the name suggests, offers calendar-related functions.
One of them is of course displaying the calendar. 
It's important that the days of the week are displayed from Monday to Sunday, 
and each day of the week has its representation in the form of an integer:

Day of the week	Integer value	Constant
Monday	            0	        calendar.MONDAY
Tuesday	            1	        calendar.TUESDAY
Wednesday	        2	        calendar.WEDNESDAY
Thursday	        3	        calendar.THURSDAY
Friday	            4	        calendar.FRIDAY
Saturday	        5	        calendar.SATURDAY
Sunday	            6	        calendar.SUNDAY
The table above shows the representation of the days of the week in the calendar module. 
The first day of the week (Monday) is represented by the value 0 and the calendar.MONDAY constant, 
while the last day of the week (Sunday) is represented by the value 6 and the calendar.SUNDAY constant.
For months, integer values are indexed from 1, i.e., January is represented by 1, and December by 12. 
Unfortunately, there aren't constants that express the months.
The above information will be useful to you when working with the calendar module in this part of the course, 
but first let's start with some simple calendar examples.
Your first calendar
You will start your adventure with the calendar module with a simple function called calendar, 
which allows you to display the calendar for the whole year. 
Let's look at how to use it to display the calendar for 2020. Run the code in the editor and see what happens.
The result displayed is similar to the result of the cal command available in Unix. If you want to change the default calendar formatting, you can use the following parameters:

w – date column width (default 2)
l – number of lines per week (default 1)
c – number of spaces between month columns (default 6)
m – number of columns (default 3)
The calendar function requires you to specify the year, while the other parameters responsible 
for formatting are optional. We encourage you to try these parameters yourself.
A good alternative to the above function is the function called prcal, 
which also takes the same parameters as the calendar function, 
but doesn't require the use of the print function to display the calendar. Its use looks like this:
'''
# import calendar
# print(calendar.calendar(2020))


'''
Calendar for a specific month
The calendar module has a function called month, which allows you to display a calendar for a specific month. 
Its use is really simple, you just need to specify the year and month - check out the code in the editor.
The example displays the calendar for November 2020. As in the calendar function, 
you can change the default formatting using the following parameters:

w – date column width (default 2)
l – number of lines per week (default 1)
Note: You can also use the prmonth function, which has the same parameters as the month function, 
but doesn't require you to use the print function to display the calendar.
'''
#
# import calendar
# c = calendar.Calendar()
# for weekly in c.iterweekdays():
#     print(weekly, end='')


# print(calendar.month(2020, 11))
#

'''
The setfirstweekday() function
As you already know, by default in the calendar module, the first day of the week is Monday. 
However, you can change this behavior using a function called setfirstweekday.
Do you remember the table showing the days of the week and their representation in the form of integer values? 
It's time to use it, because the setfirstweekday method requires a parameter expressing the day of 
the week in the form of an integer value. Take a look at the example in the editor.
The example uses the calendar.SUNDAY constant, which contains a value of 6. Of course, you could pass this 
value directly to the setfirstweekday function, but the version with a constant is more elegant.
As a result, we get a calendar showing the month of December 2020, in which the first day of all the weeks is Sunday.

'''
# import calendar
#
# calendar.setfirstweekday(calendar.SUNDAY)
# calendar.prmonth(2020, 12)


'''
The weekday() function
Another useful function provided by the calendar module is the function called weekday, 
which returns the day of the week as an integer value for the given year, month, and day. Let's see it in practice.
Run the code in the editor to check the day of the week that falls on December 24, 2020.

The weekday function returns 3, which means that December 24, 2020 is a Thursday.
'''
# import calendar
# print(calendar.weekday(2020, 12, 24))


'''
The weekheader() function
You've probably noticed that the calendar contains weekly headers in a shortened form. 
If needed, you can get short weekday names using the weekheader method.
The weekheader method requires you to specify the width in characters for one day of the week. 
If the width you provide is greater than 3, you'll still get the abbreviated weekday names consisting of three characters.
So let's look at how to get a smaller header. Run the code in the editor.

Result:
Mo Tu We Th Fr Sa Su

Note: If you change the first day of the week, e.g., using the setfirstweekday function, 
it'll affect the result of the weekheader function.

'''

# import calendar
# calendar.setfirstweekday(calendar.SUNDAY)
# print(calendar.weekheader(3))
# print("9999999999999")

'''
How do we check if a year is a leap year?
The calendar module provides two useful functions to check whether years are leap years.
The first one, called isleap, returns True if the passed year is leap, or False otherwise. 
The second one, called leapdays, returns the number of leap years in the given range of years.
In the example, we obtain the result 3, because in the period from 2010 to 2020 there are only 
three leap years (note: 2021 is not included). They are the years 2012, 2016, and 2020.
'''
# import calendar
#
# print(calendar.isleap(2020))
# print(calendar.leapdays(2010, 2021))  # Up to but not including 2021.


'''
Classes for creating calendars
The presented functions aren't everything the calendar module offers. In addition to them, 
we can use the following classes:

calendar.Calendar – provides methods to prepare calendar data for formatting;
calendar.TextCalendar – is used to create regular text calendars;
calendar.HTMLCalendar – is used to create HTML calendars;
calendar.LocalTextCalendar – is a subclass of the calendar.TextCalendar class. 
The constructor of this class takes the locale parameter, which is used to return the appropriate months and weekday names.
calendar.LocalHTMLCalendar – is a subclass of the calendar.HTMLCalendar class. 
The constructor of this class takes the locale parameter, 
which is used to return the appropriate months and weekday names.
During this course, you've already had the opportunity to create text 
calendars when discussing the functions of the calendar module.

Time to try something new. Let's take a closer look at the methods of the calendar class.
Creating a Calendar object
The Calendar class constructor takes one optional parameter named firstweekday, by default equal to 0 (Monday).
The firstweekday parameter must be an integer between 0-6. 
For this purpose, we can use the already-known constants - look at the code in the editor.
The program will output the following result:
6 0 1 2 3 4 5

The code example uses the Calendar class method named iterweekdays, which returns an iterator for week day numbers.
The first value returned is always equal to the value of the firstweekday property. 
Because in our example the first value returned is 6, it means that the week starts on a Sunday.
'''

# import calendar
#
# c = calendar.Calendar(calendar.SUNDAY)
#
# for weekday in c.iterweekdays():
#     print(weekday, end=" ")


'''
The itermonthdates() method
The Calendar class has several methods that return an iterator. One of them is the itermonthdates method, 
which requires specifying the year and month.
As a result, all days in the specified month and year are returned, as well as all days before the beginning 
of the month or the end of the month that are necessary to get a complete week.
Each day is represented by a datetime.date object. Take a look at the example in the editor.
The code displays all days in November 2019. Because the first day of November 2019 was a Friday, 
the following days are also returned to get the complete week: 10/28/2019 (Monday) 10/29/2019 (Tuesday) 
10/30/2019 (Wednesday) 10/31/2019 (Thursday).
The last day of November 2019 was a Saturday, so in order to keep the complete week, 
one more day is returned 12/01/2019 (Friday).
'''
# import calendar
#
# c = calendar.Calendar()
#
# for date in c.itermonthdates(2019, 11):
#     print(date, end=" ")
#

'''
Other methods that return iterators
Another useful method in the Calendar class is the method called itermonthdates, which takes year and month as 
parameters, and then returns the iterator to the days of the week represented by numbers.
Take a look at the example in the editor.
You’ll have certainly noticed the large number of 0s returned as a result of the example code. 
These are days outside the specified month range that are added to keep the complete week.
The first four zeros represent 10/28/2019 (Monday) 10/29/2019 (Tuesday) 10/30/2019 (Wednesday) 10/31/2019 (Thursday). 
The remaining numbers are days in the month, except the last value of 0, which replaces the date 12/01/2019 (Sunday).
There are four other similar methods in the Calendar class that differ in data returned:

itermonthdates2 – returns days in the form of tuples consisting of a day of the month number and a week day number;

itermonthdates3 – returns days in the form of tuples consisting of a year, a month, and a day of the month numbers. 
This method has been available since version 3.7;

itermonthdates4 – returns days in the form of tuples consisting of a year, a month, a day of the month, 
and a day of the week numbers. This method has been available since Python version 3.7.
For testing purposes, use the example above and see how the return values of the described methods look in practice.
'''
# import calendar
#
# c = calendar.Calendar()
#
# for iter in c.itermonthdays(2019, 11):
#     print(iter, end=" ")


'''
The monthdays2calendar() method
The Calendar class has several other useful methods that you can learn more about in the documentation 
(https://docs.python.org/3/library/calendar.html).
One of them is the monthdays2calendar method, which takes the year and month, 
and then returns a list of weeks in a specific month. Each week is a tuple consisting of day 
numbers and weekday numbers. Look at the code in the editor.
Note that the days numbers outside the month are represented by 0, while the weekday numbers are a number from 0-6, 
where 0 is Monday and 6 is Sunday.
In a moment, this method may be useful for you to complete a laboratory task. Are you ready?
'''
# import calendar
#
# c = calendar.Calendar()
#
# for data in c.monthdays2calendar(2020, 12):
#     print(data)



import os

os.mkdir('pictures')
os.chdir('pictures')
print(os.getcwd())


