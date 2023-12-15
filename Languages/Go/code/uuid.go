package main

import (
	"fmt"

	"github.com/google/uuid"
)

/* the key difference is in the version of the UUID generated. If you
specifically want a Version 4 UUID (randomly generated), you can use
`uuid.NewV4().String()`. If you use `uuid.New()`, the version generated may
depend on the default version supported by the underlying library. Always check
the documentation of the UUID library you're using to determine the default
version behavior. */

func main() {
    u := uuid.New()
    fmt.Println(u.String()) // ex: 4fbbf1e6-6b4a-4f1b-9bfc-2a3b4b1c9b4f

	u4, err := uuid.NewUUID()
    if err != nil {
        fmt.Println("Error:", err)
        return
    }
    fmt.Println(u4.String()) // ex: 4fbbf1e6-6b4a-4f1b-9bfc-2a3b4b1c9b4f
}
