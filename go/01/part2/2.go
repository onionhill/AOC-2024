package main

import (
	"bufio"
	"fmt"
	"os"
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
	counts := make(map[int]int)
	for _, num := range c2 {
		counts[num]++
	}

	sum := 0
	for _, num := range c1 {
		sum += (num * counts[num])
	}

	fmt.Println(sum)
}
