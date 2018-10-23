// Package emptyinterface is an autodidactic tool of @recursivelycurious to aid understanding and use of the empty interface construct in Go.

// Why use the empty interface in the example below rather than a struct? Well, what if we have multiple structs but we want to add the same meta data to all of them?

package main

import (
	"encoding/json"
	"fmt"
)

type book struct {
	Title         string `json:"title"`
	Author        string `json:"author"`
	YearPublished int    `json:"published"`
}

type webpage struct {
	URL          string `json:"url"`
	Author       string `json:"author"`
	DateAccessed string `json:"accessed"`
}

type marshalWrapper struct {
	Data        interface{} `json:"data"`
	RequestedBy string      `json:"Requested By"`
}

func errHandler(err error) {
	fmt.Printf("Unexpected error: %v\n", err)
}

func addRequestInfo(req *marshalWrapper, madeBy string) {
	req.RequestedBy = madeBy
}

func main() {
	zen := book{
		Title:         "Zen and the Brain",
		Author:        "Austin, James",
		YearPublished: 1998,
	}

	meditation := webpage{
		URL:          "https://en.wikipedia.org/wiki/Meditation",
		DateAccessed: "10/23/2018",
	}

	wrappedForMarshelling := marshalWrapper{Data: zen}
	addRequestInfo(&wrappedForMarshelling, "Anon")
	wrapped, err := json.Marshal(wrappedForMarshelling)
	if err != nil {
		errHandler(err)
	} else {
		fmt.Printf("Book object marshalled for storage:\n\t%v\n", string(wrapped))
	}

	webpageForMarshelling := marshalWrapper{Data: meditation}
	addRequestInfo(&webpageForMarshelling, "Nona")
	wrappedWebPage, err := json.Marshal(webpageForMarshelling)
	if err != nil {
		errHandler(err)
	} else {
		fmt.Printf("Webpage object marshalled for storage:\n\t%v\n", string(wrappedWebPage))
	}

	wrappedBook := &book{}
	receivedWrappedToPrint := marshalWrapper{Data: wrappedBook}
	json.Unmarshal(wrapped, &receivedWrappedToPrint)

	fmt.Printf("\n\nAnd the book object un-marshalled from storage:\n\t%v\n", *wrappedBook)

}
