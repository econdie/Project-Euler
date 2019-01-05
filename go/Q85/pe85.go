package main

import (
    "fmt"
    "math"
)

func main() {
    var target float64 = 2000000
    var currentError float64 = 10000
    var currentArea float64 = 0
    var numRects float64

    for x := 1000; x > 1; x-- {
        for y := 0; y < x; y++ {
            numRects = float64(x * (x + 1) * y * (y + 1) / 4)
            if math.Abs(numRects - target) < currentError {
                currentError = math.Abs(numRects - target)
                currentArea = float64(x * y)
            }
        }
    }
    
    fmt.Printf("Answer: %v", currentArea)
}
