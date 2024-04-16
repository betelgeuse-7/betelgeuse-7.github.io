title="Let's talk about Sirin"
description="Sirin programming language"
keywords="sirin, pl, compilers, programming languages"
date="25-01-2024"
---

## Let's talk about Sirin

Sirin is a programming language that I've been developing for a while (approx. 6-7 months). Despite the fact that this language was intended to be a simple language, it turned out to be not-so-simple. Of course, it is still a small and simple language compared to real-world languages like Swift, Rust, D, Java, etc.

My aim was to design my own programming language, and create a compiler for it. I designed it, and I am now building the compiler.

I said I designed it. I didn't say I designed it well. To design a language, you first have to have a reason to come up with a new language. And, that reason can't simply be: "I want my own language". Well, mine was just that. I now feel like a state declaring war on another country without a *casus belli*. But, unlike that hostile country, I don't think I will lose too much. I might've lost quite a lot of precious time, but I will gain new knowledge and experience. If I wasn't so lazy, I could've built the first working prototype of the compiler by now. I procrastinated too much. I thought I had to first thorougly design the language, and only after that, I can start building the implementation. I knew I was wrong, but I kept doing what I was doing: dreaming.

I like Go, but I wish Go had Rust-like enums and pattern matching. That way, the error handling mechanism could be based on `Result[T, E]` and `Option[T]`. I think it'd be great. So, I am basically creating that language. This is not a serious project, though. I don't expect anyone to use my language, and it is not the goal anyways.



The compiler will produce x86-64 assembly code for a 64-bit Linux computer. I guess, it must have a register allocator and an instruction selector. There will be a lowering phase, which will turn higher-level language constructs into lower-level and more ubiquitous ones. For example, match statements will be lowered into decision trees built with if statements. There will be a monomorphization phase which will create a specialized version with concrete types for each polymorphic type.

There may also be a phase in the front-end doing constant folding and propagation. The Go compiler performs these optimizations to type-check static array initializations at compile-time.


The module system will be based on files. Each file will be a module. I plan to add "public imports" in the future. With public imports, the programmer will be able to export many files from a single file. This way, he will have the luxury to split up a big module into different files.


I look forward to the days when I will have a simple HTTP 1.1 or HTTP 1.0 server created with Sirin.

Imagine:

```
import std.net.http

func main {
    s :: http.createServer({ port: 8000 })    ;; this is passing a struct{ port: Int } instance to http.createServer

    s.get("/", func(req: ->http.Request, res: http.Responder) {
        res.text("Hello world")
    })

    s.listen()
}
```

See you.