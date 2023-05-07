title="A New Programming Language"
description="A new programming language"
keywords="programming, compilers, programming languages"
date="04-05-2023"
---

# A New Programming Language

I have plans to design and implement a programming language this year. 

### Why ?

If I were to list all the things people say that irritate me the most, this would certainly be in that list:

***There is already X. Why are you reinventing the wheel?***

I have so much respect for people who value reinventing things. I have that respect not for people who are reinventing things just for the sole purpose of feeling different than other people. I have that respect for people who are reinventing things in the hopes that he will gain a deeper understanding of the various choices one would have and trade-offs one would face in the design and implementation of the thing.

I believe you figured out the motivation behind my attempt of utter stupidness behind this undertaking of a mission so unnecessary and so hard. (I sometimes exaggerate things.)

### How ?

By building a compiler... 

I built a compiler (or a transpiler, should I say?) that takes Quoi source code, and outputs Go source code. Quoi is a toy language. Go is not a toy language.

So, I can say I have some experience in building compilers though `qc` (Quoi compiler) didn't have a lot of complex parts. I didn't implement optimization passes. I didn't implement register allocation. Quoi doesn't have modules, so I didn't implement anything like modules or packages.

But this time I will probably be dealing with these. At first, I want the compiler to be able to produce x86-64 code that runs on 64-bit Linux machines.

### Possible features of the language

Although I can't say I know a lot of things about programming language design and PL Theory, I can list a few things I would want my language to have.

- Static typing

- Type inference
    Not a full type inference found in languages like F#, OCaml or Haskell. Rather, a basic inference (You will have to specify the types of function parameters, for example).

- Automatic memory management
    I have to admit I picked this one to have an opportunity to implement a garbage collector. So, we can say this language will not be best suited to high-performance systems because of performance penalties brought about by GC pauses.

- Composite types
    Structs, arrays, lists (dynamic arrays), records (or maps, records, dictionaries, associative arrays), tuples

- First-class functions
    Functions as values. Function signatures.

- A module system
    Based on file names.

- A standard library
    Containing modules for networking, json, and file I/O.

- Variadic arguments
    The ability to pass an arbitrary number of arguments of same type to a function.

- Some mechanism to extend a struct
    We can call that composition (rather than inheritance).

- Access modifiers
    Variables, and fields of a struct are private by default. Programmer can set them public in which case they can be referenced in other modules.

- Generics
    If not too hard to implement.

There may be some I forgot to mention. I will be posting about this language anyways. 

### Possible syntax

Not C-like, but not alien-like either...

It will be different than most languages. I have some candidates. The most probable to win looks like a combination of Typescript, Rust, Jai, Odin, Go, Coq, and OCaml (That's a lot of languages).

### Possible primitive types

This is not very exciting. Boring stuff...

`Int32, Int, Uint32, Uint, String, Bool, Float32, Float, Byte`

For strings, I am not sure how I will handle Unicode.

`Byte` is an 8-bit unsigned integer for representing ASCII characters.

There are pointers, but no pointer arithmetic.


---

There are other aspects to the language. I will post more here.

---

## I am feeling sleepy. Good night.