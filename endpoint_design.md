**[GET] /addresss**

Get a list of User addresses

RequestBody:

	None

ResponseBody:

	Addresses: list of ID

  

**[GET] /address/{ID}**

Get Address by ID

RequestBody:

	None

ResponseBody:

	Name: String

	Address1: String

	Address2: String

	Address3: String

	City: String

	State: String

	PhoneNumber: String

	isDefault: Boolean

**[POST] /address**

Create new user Address

RequestBody:

	Name: String [Required]

	Address1: String [Required]

	Address2: String [Optional]

	Address3: String [Optional]

	City: String [Required]

	State: String [Required]

	PhoneNumber: String [Required]

ResponseBody:

	AddressID: String

	Result: ['Success', 'Failed']

	Message: String

**[PATCH] /address/{ID}**

Update User's Address

RequestBody:

	Name: String [Optional]

	Address1: String [Optional]

	Address2: String [Optional]

	Address3: String [Optional]

	City: String [Optional]

	State: String [Optional]

	PhoneNumber: String [Optional]

	isDefault: Boolean [Optional]

ResponseBody:

	Result: ['Success', 'Failed']

	Message: String

  

**[DELETE] /address/{ID}**

Delete User's Address by ID

RequestBody:

	None

ResponseBody:

	Result: ['Success', 'Failed']

	Message: String

**[GET] /storelocations**

Get a list of store location near by

RequestBody:

	Lat: Float
	Long: Float

ResponseBody:

	storelocations: list of ID

**[GET] /store/{ID}**

Get a store info by ID

RequestBody:

	None

ResponseBody:

	Name: String

	Address1: String

	Address2: String

	Address3: String

	City: String

	State: String

	PhoneNumber: String

	Lat: Float

	Long: Float

	StoreHours: List of Hours
**[GET] /items**

Get a list of menu item

RequestBody:

	None

ResponseBody:

	items: list of ID

  

**[GET] /items?category={catagory}**

Get a list of menu item by catagory

RequestBody:

	Category: String

ResponseBody:

	items: list of ID

  

**[GET] /itemsCategories**

Get a list of menu categories

RequestBody:

	None

ResponseBody:

	categories: list of categories

  

**[GET] /item/{ID}**

Get detail of the menu item

RequestBody:

	None

ResponseBody:

	Name: String

	Description: String

	Category: String

	Available_Size: List of Size

	ItemDependencies: List of Item ID

	Active: Boolean

**[GET] /item/{ID}?size={Size}**

Get detail of the menu item price by size

RequestBody:

	Size: String

ResponseBody:

	Name: String

	Description: String

	Price: float

	Active: Boolean

**[GET] /orders**

Get order history

RequestBody:

	None

ResponseBody:

	Orders: List of Order ID

**[GET] /order/{ID}**

Get order information by ID

RequestBody:

	None

ResponseBody:

	Items: List of Items

	AddressID: String

	SubTotal: Float

	Tax: Float

	Total: Float

	TimeStamp: DateTime

**[POST] /order**

Submit ordering information

RequestBody:

	AddressID: String [Required]

	PaymentID: String [Required]

	Items: List of Item ID [Required]

	Coupon: String [Optional]

ResponseBody:
	
	OrderID: String

	Status: ['Confirmed', 'Declined', 'Error']

	Message: String

**[GET] /payments**

Get a list of payments

RequestBody:

	None

ResponseBody:

	Payments: List of PaymentID

  

**[GET] /payment/{id}**

Get Payment by ID

RequestBody:

	None

ResponseBody:

	Name: String

	CCValue: long

	CCV: Int

	Exp: Date

  

**[POST] /payment**

Add Payment

RequestBody:

	Name: String [Required]

	CCValue: long [Required]

	CCV: Int [Required]

	Exp: Date [Required]

ResponseBody:

	PaymentID: string

	Result: ['Success', 'Failed']

	Message: String

  

**[Patch] /payment/{id}**

Update Payment

RequestBody:

	Name: String [Optional]

	CCValue: long [Optional]

	CCV: Int [Optional]

	Exp: Date [Optional]

ResponseBody:

	Result: ['Success', 'Failed']

	Message: String

  

**[DELETE] /payment/{ID}**

Delete User's Payment by ID

RequestBody:

	None

ResponseBody:

	Result: ['Success', 'Failed']

	Message: String
