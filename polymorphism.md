title="Polymorphism"
description="polymorphism, parametric, ad-hoc, subtype, Sirin, go, golang"
keywords="polymorphism, sirin, go"
date="20-07-2024"
---

# Polymorphism

This post is going to be about what I know of polymorphism in the context of programming languages.

*This post is not about a formal approach to polymorphism. I am not knowledgeable in type theory. I've only seen some examples of type judgments etc.*

I've done a little research about polymorphism, because I wanted my programming language *Sirin* to support polymorphism.

### Sirin

Sirin is a programming language project of mine. It is not public, yet, and I am currently revising the design of the language. I realized how hard it is to design a programming language.

Sirin supports three types of polymorphism: parametric polymorphism, ad-hoc polymorphism, and subtype polymorphism.

### Parametric polymorphism

Parametric polymorphism is the ability of a type (constructor) or a function to have *type parameters* that act like a placeholder for some concrete type. Type parameters are very similar to (function) parameters. They are given names, and, potentially, constraints. Let's see an example in Sirin:

```
func id|T|(x: T): T {
    return x;
}
```

This is the identity function. It returns a copy of the value given to it, so the type of the returned value and the given value are the same. The type parameter here is called `T`, and it is put inside pipes (`|`) after the function name. The type parameter can be referenced in the function definition just like any other type. 

This function is like a template. The type parameter will eventually be instantiated to a concrete type. For example, if we called this function with a value of type `Int`:

```
id(4);
```
or
```
id|Int|(4);
```

The compiler would need to create a *specialized* version of the `id` function that accepts a value of type `Int`. This technique is called *monomorphization* and it is used in Rust, and C++ compilers.

#### We need to set a limit

What if we want to declare a parametrically-polymorphic function, but we want it to accept only a set of allowed type arguments? This is where we need type parameter *constraints*.

The syntax is as follows:

```
func id|T: SomeConstraint|(x: T): T {
    return x;
}
```

Now that we set a constraint on type parameter `T`, we can't call `id` with a value of type `E`, if `E` is not a part of the *class* `SomeConstraint`.

#### Classes in Sirin

Classes in Sirin are not like classes in Java, or C++. They are not used to create objects. They are like *interfaces* of [Go](https://go.dev/). You might now ask two questions:

- Why did you use the keyword `class` instead of, say, `interface`, `protocol`, or `trait` ?
- Did you steal the keyword from Haskell?

My answers to these questions would be:

- I think `class`, too, is a suitable name for what these entities stand for. Think of it like this, "Type A is part of class B". It is like set theory, right? And types are very similar to sets, so, using the keyword `class` here reflects the intent of setting some boundaries.

- Maybe. I didn't come up with the keyword after a thorough session of thinking. I just put `class` when I was sketching the language. So, I might've been subconsciously influenced by Haskell, but who knows.


Okay, let's see how to declare `class`es.

```
type Printable: class {
    func toString(): String;
}
```

Declarations starting with the keyword `type` are *type declarations*. Here, the class actually comes after the colon (`:`). You can use *inline*/*anonymous* classes in contexts where you'd put a named class, too.

An inline class is just:
```
class { }
```

The `Printable` class is going to be a very popular class in the language. It is very similar to the type class `ToString` in Haskell. It defines a method called `toString` which has type `fn: String` or `fn(): String`. Types that want to be *a part of* class `Printable` need to have a *method* called `toString` that matches the type `fn: String` (*the method must take 0 arguments, and a return value of type `String`*).

Let's define a type that has a method `toString`:

```
type Foo: struct {
    quux: Int;
}

func (f: Foo) toString(): String {
    return "I am Foo. " ++ f.quux.toString();
}
```

Struct `Foo` is now a part of the `Printable` <s>family</s> class.

Let's, then, modify the `id` function so that it sets a type parameter constraint of `Printable` on `T`.

```
func id|T: Printable|(x: T): T {
    return x;
}
```

We can pass `Foo` instances to it.

```
f: Foo := { x: 4; };
fStringified :: id(f);

io.println(fStringified);
```

We cannot pass a type that is not a `Printable` to `id`.

----- 

This is parametric polymorphism in Sirin.

### Ad-hoc polymorphism

Ad-hoc polymorphism is achieved when, for example, a function accepts any kind of value, and behaves differently depending on the type of the value. It requires a *type introspection* mechanism to figure out the type of the argument at runtime. As of now, Sirin does not have type introspection. I still have not added the feature to the language. I will, though.

Anyway, let's give an example in Go.

```go
func foo(x interface{}) {
    switch x.(type) {
    case int:
        fmt.Println("This is an int")
    case string:
        fmt.Println("This is a string")
    case bool:
        fmt.Println("George Boole")
    default:
        panic("What do I do?!")
    }
}
```

Constraints can also be used here to prevent runtime panics. That way, type errors can be caught at compile-time.

Operator overloading is an example of ad-hoc polymorphism.

### Subtype polymorphism

Subtype polymorphism allows a specialized type to be used in contexts where a generalized type is expected. There is a *subtype* and a *supertype* in subtype polymorphism. A subtype can be used in place of a supertype, but the opposite is not possible (every apple is a fruit, but not every fruit is an apple. You can give an apple to someone asking for a fruit, but you can't give someone asking for an apple, a peach.)

 Type theorists formalize this concept with their lovely notation of `S <: T` where `S` is a subtype of `T`.

#### Subtype polymorphism in Sirin

```
type Fruit: class {
    func taste(): String;
}

type Lemon: struct {}
func (Lemon) taste(): String { return "sour and tangy"; }

type Banana: struct {}
func (Banana) taste(): String { return "sweet and soft"; }

func describeFruit(f: Fruit) {
    io.print("This fruit is ");
    io.println(f.taste());
}
```

The function `describeFruit` would typecheck if were to pass it an instance of `Lemon` or `Banana`, but how does the compiler know which method to call? Generally, it can't know it at compile-time, and it needs to figure it out at run-time. This is called *late binding*, and it is achieved through the well-known mechanism of *dynamic dispatch*.

`Lemon` and `Banana` are subtypes of `Fruit`, because `Fruit` is the generalized type.


------

*If you spot any errors, please let me know by sending me an email.*

### Okay, I think this is enough for today's post. Until next time