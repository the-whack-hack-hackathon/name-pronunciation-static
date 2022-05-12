const express = require("express");

const app = express();

const port = process.env.PORT || 3000

app.use(express.static("dist"))

app.listen(port,() => {
    console.log(`Pronunciation Tool UI starting on port ${port}`);
});