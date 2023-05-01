title="Hello World"
description="First post"
keywords="go"
date="01-05-2023"
---

# Hello World

This is a test post.

```go
package main

import (
	"syscall"
)

func main() {
	syscall.Write(1, []byte("Hello world\n"))
}
```