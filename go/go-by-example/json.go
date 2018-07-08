package main

import (
	"encoding/json"
	"fmt"
	"os"
)

type response1 struct {
	Page   int
	Things []string
}

type response2 struct {
	Page   int      `json:"page-tagged"`
	Things []string `json:"things-tagged"`
}

func typeof(v interface{}) string {
	return fmt.Sprintf("%T", v)
}

func main() {
	fmt.Println("-- Basic data types Marshaled to JSON and then printed --")

	bolB, _ := json.Marshal(true)
	fmt.Println("\nBoolean:\n", string(bolB))

	fmt.Println("\nOnce Marshaled, the data is an array of ASCII, as we can see with the integer 1.")
	intB, _ := json.Marshal(1)
	fmt.Println("\nInteger:\n", intB, string(intB))

	fltB, _ := json.Marshal(2.34)
	fmt.Println("\nFloat\n", string(fltB))

	strB, _ := json.Marshal("gopher")
	fmt.Println("\nString\n", string(strB))

	slcD := []string{"foo", "bar", "qux"}
	slcB, _ := json.Marshal(slcD)
	fmt.Println("\nSlice:\n", string(slcB))

	mapD := map[string]int{"foo": 0, "bar": 99}
	mapB, _ := json.Marshal(mapD)
	fmt.Println("\nMap:\n", string(mapB))

	fmt.Println("\nCustom data type, no tags:")
	res1D := &response1{
		Page:   1,
		Things: []string{"foo", "bar", "baz"}}
	res1B, _ := json.Marshal(res1D)
	fmt.Println(string(res1B))

	fmt.Println("\nCustom data type with tags, using same data values:")
	res2D := &response2{
		Page:   1,
		Things: []string{"foo", "bar", "baz"}}
	res2B, _ := json.Marshal(res2D)
	fmt.Println(string(res2B))

	fmt.Println("\n-- Now we'll Unmarshal some byte strings --\n")
	byt := []byte(`{"num":6.13,"strings":["urr","yzz"]}`)

	var dat map[string]interface{}

	if err := json.Unmarshal(byt, &dat); err != nil {
		panic(err)
	}
	fmt.Println("Given the following JSON:")
	fmt.Println("{\"num\":6.13,\"strings\":[\"urr\",\"yzz\"]}")
	fmt.Println("\nGo can read/store it as a slice of bytes.")
	fmt.Println("To Unmarshal it, we use a map of strings for keys and - recursively, as needed - use empty\ninterfaces to discover the rest of the data by interface conversion.")
	fmt.Println("\nFor all the bytes: \n", dat)

	num := dat["num"].(float64)
	fmt.Println("\nOr just for 'dat[\"num\"].(float64)':\n", num)

	fmt.Println("\nFor the strings, we have two steps;")
	strs := dat["strings"].([]interface{})
	fmt.Println("First, we declare 'strs := dat[\"strings\"].([]interface{})', which gives us:\n", strs)
	str1 := strs[0].(string)
	fmt.Println("\nThen we can declare 'str1 := strs[0].(string)' and get:\n", str1)

	fmt.Println("\nMore commonly, we will define a custom type - tagged or not - as above, and use them.\n")
	str := `{"page-tagged": 0, "things-tagged": ["ENIAC", "MARC-1"]}`
	fmt.Println("Given the JSON:\n", str)
	res := response2{}
	json.Unmarshal([]byte(str), &res)
	fmt.Println("\nHere is the Unmarshalled data, now stored in the - tagged - custom type:\n", res)
	fmt.Println("\nWe can also drill to specific properties:\n", res.Things[0])

	enc := json.NewEncoder(os.Stdout)
	d := map[string]int{"Turing Machine": 0, "ENIAC": 1}
	fmt.Println("\nFinally, we can also take a map:\n", d)
	fmt.Println("\nAnd use an 'Encoder' to write that map as JSON. In this case to stdout, but we could also write to a file, HTTP etc.:\n")
	enc.Encode(d)
	fmt.Println()
}
