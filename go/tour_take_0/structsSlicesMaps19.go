package main

import "fmt"

type Vertex struct {
	Lat, Long float64
}

var m map[string]Vertex

func main() {
	m = make(map[string]Vertex)
	m["Bell Labs"] = Vertex{
		40.68433, -74.39967,
	}
	m["Denver"] = Vertex{
		39.7640021, -105.1352965,
	}
	for k, v := range m {
		fmt.Printf("Key[%v] Value[%v]\n", k, v)
	}
}
