title="Creating Hardlinks Using Go"
description="ln"
keywords="go, hardlinks, ln, os, cgo"
date="21-05-2023"
---

# Creating hard links in Go (implementing a tiny subset of `ln`)

There are two kinds of links on a Linux system: A hard link and a soft link (or a symbolic link).

In this post, I will be giving a brief information on inodes. After that, I will be presenting how to build a tool that allows us to create hard links on a Linux machine, in Go. 

### Inodes

Each file in a file system has an associated structure stored on the disk called an inode (index node). These structures include metadata about the file. One of the components of this data structure is a unique number that is given to each file to differentiate each file. This number is called an inode, too.

The inode structure includes metadata such as the date of creation, last modification time, owner id, permissions (read/write/execute), data block address (a pointer to the block(s) in which the bytes live), inode number, etc.

Directories also have an inode structure, but theirs is a bit different than that of a file's. The most significant difference is that a directory's inode contains a list of directory entries (Different implementations might use different data structures to hold directory entries. I said "a list" to make the explanation simpler). A directory entry is, in its simplest form, a pair of human-friendly name of the file and an inode number.

```
struct Dir_Inode = {
    int         inode
    timestamp   created_at
    timestamp   last_updated
    int         owner_id
    ...
    Dir_Entry[] entries
}

pair Dir_Entry = (string name | int inode)
```

### How the OS knows where to look for the file data

```
struct File_Inode = {
    int inode
    ...
    int block_addr  
}
```

When you double-click on a text file to read it, or when you use `cat` to read a file; under the hood, the operating system (the file system, more specifically) has to do a few things. 

Suppose the file `hello.txt` lives at the location of `/home/btlgs/Documents/txt/hello.txt`. The operating system has to find the inode of the file called `hello.txt` located at that specific location. The reason why it has to find the inode (structure) is because the OS doesn't know where in the disk `hello.txt` resides. That information is stored in the inode (inode tells in which block(s) the data lives on the disk). To find it, the OS first reads directory entries of `/` to look for the `home` directory. If it is not there, an error is returned. If it is there, it grabs the inode number of `/home/` and, by using that number, reads the inode *structure* of `/home/` to search the list of directory entries of `/home/` to find the `btlgs` directory. This goes on like that till the file is found. 

When the inode number of `hello.txt` is found, the file system initiates an I/O request to the disk driver to read the relevant block using the disk block address found in the inode structure.

### Difference between hard links and soft links

A hard link creates a new directory entry in the directory. A soft link is just an alias for a file name.

When we create a hard link, we indirectly add a directory entry with the same inode number of the linked-to file.

We can create hard links using `ln` on Linux.

```bash
ln existing_file new_file
```

If you use `stat` to check the inodes of both files, you will see they are the same.

```
File: new_file
Size: 8         	Blocks: 8          IO Block: 4096   regular file
Device: 802h/2050d	Inode: 2101066     Links: 2
(omitted)
```

```
File: existing_file
Size: 8         	Blocks: 8          IO Block: 4096   regular file
Device: 802h/2050d	Inode: 2101066     Links: 2
(omitted)
```

We can also create soft links (symbolic links) using `ln`.

```bash
ln --symbolic existing_file new_file
```

Now, use `stat` to check inodes of both of the files. You can see they are indeed different. You can also observe that the type of the file '`new_file`' is not a regular file; instead, it is a 'symbolic link'.

```
File: existing_file
Size: 4         	Blocks: 8          IO Block: 4096   regular file
Device: 802h/2050d	Inode: 2101087     Links: 1
(omitted)
```

```
File: new_file -> existing_file
Size: 9        	    Blocks: 0          IO Block: 4096   symbolic link
Device: 802h/2050d	Inode: 2101090     Links: 1
(omitted)
```

Sizes of symbolic links are equal to the length of linked-to file's name, plus the null terminator.

### How to build a tool to create hard links

**Note: There is a way easier method of building this same program using a standard library function. I just wanted to use cgo.**

Code:
<script src="https://gist.github.com/betelgeuse-7/23934b0f250389d4a290014feac3d106.js"></script>

We first parse command line arguments. Then, we make sure the file actually exists on the file system; if it does not, we print out an error message and exit the process. After that we call the `makeHardlink` function defined below. That function relies on a system call called `linkat` that basically does what we want: It creates hard links. Since the `linkat` function is not a part of the standard library, we use Go's C interoperability feature called cgo (There's the `syscall.Link` function in the standard library that uses `//sys` directives to make it possible to use the `linkat` function. See [syscall.Link](https://cs.opensource.google/go/go/+/refs/tags/go1.20.4:src/syscall/syscall_linux.go;l=259). `//sys` directives are used to tell the compiler to generate necessary `.c`, `.h`, and `.go` files.). 

```
/*
#include <fcntl.h>
#include <unistd.h>
int _linkat(int olddirfd, const char *oldpath, int newdirfd, const char *newpath, int flags) {
    return linkat(olddirfd, oldpath, newdirfd, newpath, flags);
}
*/
import "C"
```

This code snippet above makes the `C._linkat` function available in our Go program. 

`makeHardlink` takes two arguments of type string, but we can't pass them to the `C._linkat` function because the types do not match. `C._linkat` function expects a C-style string (null-terminated). So, we convert the two arguments to C strings (We actually need to free them, but since this is a very short-lived program, I ignored it (I had an error I don't remember.).). `C.AT_FDCWD` argument passed to `makeHardlink` stands for the file descriptor of the current working directory. The last argument, '0', means we want a straightforward hard link operation. No flags, no symbolic link, or other configuration...

### That's it. Take care. See you next time.