package main

import (
	"fmt"
	"math/rand"
	"time"
)

func bubbleSort(num_list []int) {

	n := len(num_list)
	swapped := true

	for swapped {
		swapped = false
		for i := 1; i < n; i++ {
			if num_list[i-1] > num_list[i] {
				num_list[i], num_list[i-1] = num_list[i-1], num_list[i]
				swapped = true
			}
		}
	}
}

func main() {

	var num_list []int

	for i := 0; i < 10000; i++ {
		num_list = append(num_list, rand.Intn(100))
	}

	start := time.Now()
	bubbleSort(num_list)
	elapsed := time.Since(start)

	fmt.Printf("%dms", elapsed.Milliseconds())

}