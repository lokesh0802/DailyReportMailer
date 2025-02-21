const express = require("express");
const cors = require("cors");

const app = express();
app.use(cors()); // Enable CORS for cross-origin requests

const PORT = 3000;

// Sample JSON data
const sampleData = {
    date: new Date().toISOString().split("T")[0],
    clients: [
        { id: 1, name: "Client A", email: "clientA@example.com", report: "Report data A" },
        { id: 2, name: "Client B", email: "clientB@example.com", report: "Report data B" },
        { id: 3, name: "Client C", email: "clientC@example.com", report: "Report data C" }
    ]
};

// API Endpoint
app.get("/data", (req, res) => {
    res.json(sampleData);
});

app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
