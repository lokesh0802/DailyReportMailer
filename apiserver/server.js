const express = require("express");
const cors = require("cors");

const app = express();
app.use(cors()); 
const PORT = 3000;


// API Endpoint
app.get("/data", (req, res) => {
    const salesReportData = {
        report_date: new Date().toDateString(),
        business_name: "TEST SALON 15TH",
        owner_name: "Bhawna ",
        address: "Bennett",
        email: "lokesh@gmail.com",
        total_sales: 5000,
        num_invoices: 10,
        num_appointments: 5,
        payment_methods: {  
            "Cash": 1000,
            "Credit Card": 1500,
            "Debit Card": 800,
            "UPI": 1200,
            "Wallet": 300,
            "Royalty Points": 200
        },
        sales_by_category: {
            "Services": 3000,
            "Products": 1500,
            "Packages": 500
        }
    };

    res.json(salesReportData);
});


app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
