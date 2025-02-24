const express = require("express");
const cors = require("cors");

const app = express();
app.use(cors()); 
const PORT = 3000;

const sampleData = [
  {
    "get_sales_breakup_by_email_new": [
      {
        "email": "lokesh08519137@gmail.com",
        "companyID": "3c256656-8ca8-4e91-8759-f7b58effc838",
        "phoneNumber": "9996643376",
        "Firstname": "Nils",
        "Contact Name": "main hu na",
        "title": "Legros, Runolfsdottir and Bechtelar Pvt. Ltd.",
        "Address": "N/A",
        "Date": "2025-02-24",
        "total_sales": 25000.00,
        "num_invoices": 15,
        "appointments": 5,
        "payment_methods": [
          {"method": "Cash", "amount": 5000.00},
          {"method": "Credit Card", "amount": 8000.00},
          {"method": "UPI", "amount": 4000.00},
          {"method": "Wallet", "amount": 2000.00},
          {"method": "Royalty Points", "amount": 1500.00},
          {"method": "Net Banking", "amount": 4500.00}
        ],
        "sales_categories": [
          {"name": "Services", "amount": 12000.00},
          {"name": "Products", "amount": 6000.00},
          {"name": "Packages", "amount": 4000.00},
          {"name": "Membership Plan", "amount": 3000.00}
        ],
        "staff_sales": [
          {"name": "John Doe", "sales": 12000.00, "services": 8},
          {"name": "Jane Smith", "sales": 13000.00, "services": 7}
        ]
      },
      {
        "email": "lokeshkumar3393@gmail.com",
        "companyID": "c650a71c-7322-4c57-a7be-4b1066cd3eb2",
        "phoneNumber": "amit",
        "Firstname": "amit",
        "Contact Name": "Sumit",
        "title": "creation unisex salon",
        "Address": "SHOP NO:- 102, NOIDA NOIDA UTTER PRADESH 201010",
        "Date": "2025-02-24",
        "total_sales": 18000.00,
        "num_invoices": 10,
        "appointments": 3,
        "payment_methods": [
          {"method": "Cash", "amount": 4000.00},
          {"method": "Credit Card", "amount": 6000.00},
          {"method": "UPI", "amount": 3000.00},
          {"method": "Wallet", "amount": 2500.00},
          {"method": "Royalty Points", "amount": 2000.00},
          {"method": "Net Banking", "amount": 3500.00}
        ],
        "sales_categories": [
          {"name": "Services", "amount": 10000.00},
          {"name": "Products", "amount": 4000.00},
          {"name": "Packages", "amount": 2000.00},
          {"name": "Membership Plan", "amount": 2000.00}
        ],
        "staff_sales": [
          {"name": "Rahul Sharma", "sales": 9000.00, "services": 5},
          
        ]
      }
    ]
  }
  
  
      
];

// API Endpoint
app.get("/data", (req, res) => {
    res.json(sampleData);
});

app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
