# file i/o  in python 
#  python can we  used to  perform opreation on  a file .(read and write)

#  type of all file 
#  text file :  txt ,docs ,.log etc 
# binary files  :  mp4, mov,  png ,jpeg ect

# open  read and close files 
#  we have to open file before  reading or write file 

# f = open("file name ","mode")
#  text file open by default  but     we have option to  two mode combine rt  = read text   , wt wite text file 
#  text file open by defalt but in case of binary  we need to  add  mode br =  binary read , bw  = binary write   without  using b not   open binary file 


f = open("/home/neha-int109/python.txt","r")
data= f.read()
print(data)
f.close()

# Demonstration of common file I/O methods and modes

fname = "sample_io_demo.txt"

# 1) write modes: w (write), x (create exclusive), a (append)
with open(fname, "w", encoding="utf-8") as f:
    f.write("Line 1\n")
    f.writelines(["Line 2\n", "Line 3\n"])   # write multiple lines
    f.flush()                                # flush to disk (file still open)
    # f.fileno(), f.readable(), f.writable(), f.seekable(), f.isatty() are available here
    print("fileno:", f.fileno(), "writable:", f.writable(), "seekable:", f.seekable())

# 2) append
with open(fname, "a", encoding="utf-8") as f:
    f.write("Appended line\n")

# 3) read entire content, read(size), readline(), readlines(), iterate
with open(fname, "r", encoding="utf-8") as f:
    all_text = f.read()           # read all
    print("Whole file length:", len(all_text))
with open(fname, "r", encoding="utf-8") as f:
    chunk = f.read(7)             # read first 7 characters
    print("Chunk:", repr(chunk))
with open(fname, "r", encoding="utf-8") as f:
    first_line = f.readline()     # read one line
    rest_lines = f.readlines()    # read remaining lines into list
    print("First line:", repr(first_line), "Remaining count:", len(rest_lines))
with open(fname, "r", encoding="utf-8") as f:
    for i, line in enumerate(f, 1):   # iterate lines (memory efficient)
        if i > 3:
            break
        print("Line", i, ":", line.strip())

# 4) random access: tell(), seek(), truncate()
with open(fname, "r+", encoding="utf-8") as f:
    f.seek(0, 2)    # move to end
    end_pos = f.tell()
    print("End position:", end_pos)
    f.seek(0)       # go back to start
    f.write("OVERWRITE\n")   # will overwrite from start
    f.truncate()    # truncate after current position (useful when shortening)

# 5) binary modes and readinto
bin_name = "sample_io_demo.bin"
data = b"\x00\x01\x02HelloBytes"
with open(bin_name, "wb") as b:
    b.write(data)
with open(bin_name, "rb") as b:
    buf = bytearray(8)
    n = b.readinto(buf)   # fill a pre-allocated buffer (returns bytes read)
    print("readinto bytes:", n, "buffer:", buf[:n])

# 6) other useful operations
with open(fname, "r", encoding="utf-8") as f:
    print("readable:", f.readable(), "writable:", f.writable(), "isatty:", f.isatty())

# 7) safe exclusive creation (fails if file exists)
try:
    with open("unique_file.txt", "x", encoding="utf-8") as f:
        f.write("created once\n")
except FileExistsError:
    print("unique_file.txt already exists")

# Cleanup (optional)
# import os
# os.remove(fname); os.remove(bin_name); os.remove("unique_file.txt")





