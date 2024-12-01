package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
	"strconv"
	"strings"
)

func main() {
	file, err := os.Open("../inputs.txt")
	if err != nil {
		fmt.Println("Error reading sample.txt")
		return
	}
	defer file.Close()

	var c1, c2 []int
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		if strings.TrimSpace(line) != "" {
			cols := strings.Fields(line)
			x1, _ := strconv.Atoi(cols[0])
			x2, _ := strconv.Atoi(cols[1])
			c1 = append(c1, x1)
			c2 = append(c2, x2)
		}
	}

	sort.Ints(c1)
	sort.Ints(c2)

	diff := 0
	for i := 0; i < len(c1); i++ {
		diff += int(math.Abs(float64(c1[i] - c2[i])))
	}
	fmt.Println(diff)
}
