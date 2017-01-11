package main

import "fmt"

type Vertex struct {
	Lat, Long float64
}

var mLit = map[string]Vertex{
	"Bell Labs": Vertex{
		40.68433, -74.39967,
	},
	"Google": Vertex{
		37.42202, -122.08408,
	},
}

var m map[string]Vertex

func main() {
	// m has to be built
	m = make(map[string]Vertex)
	m["Bell Labs"] = Vertex{
		40.68433, -74.39967,
	}
	m["Google"] = Vertex{
		37.42202, -122.08408,
	}
	m["Denver"] = Vertex{
		39.7640021, -105.1352965,
	}
	mLit["Denver"] = Vertex{
		39.7640021, -105.1352965,
	}
	fmt.Println(mLit)
	fmt.Println(m)
}
