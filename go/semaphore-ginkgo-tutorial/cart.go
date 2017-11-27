package cart

type Cart struct {
	items map[string]Item
}

type Item struct {
	ID    string
	Name  string
	Price float64
	Qty   int
}

func (c *Cart) init() {
	if c.items == nil {
		c.items = map[string]Item{}
	}
}

func (c *Cart) AddItem(i Item) {
	c.init()
	if existingItem, ok := c.items[i.ID]; ok {
		existingItem.Qty++
		c.items[i.ID] = existingItem
	} else {
		i.Qty = 1
		c.items[i.ID] = i
	}
}

func (c *Cart) RemoveItem(id string, n int) {
	c.init()
	if existingItem, ok := c.items[id]; ok {
		if existingItem.Qty <= n {
			delete(c.items, id)
		} else {
			existingItem.Qty -= n
			c.items[id] = existingItem
		}
	}
}

func (c *Cart) TotalAmount() float64 {
	c.init()
	totalAmount := 0.0
	for _, i := range c.items {
		totalAmount += i.Price * float64(i.Qty)
	}
	return totalAmount
}

func (c *Cart) TotalUnits() int {
	c.init()
	totalUnits := 0
	for _, i := range c.items {
		totalUnits += i.Qty
	}
	return totalUnits
}

func (c *Cart) TotalUniqueItems() int {
	return len(c.items)
}
