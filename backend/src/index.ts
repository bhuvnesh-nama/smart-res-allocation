import "dotenv/config";
import server from "./app";
import connectDB from "./config/db";

const PORT = process.env.PORT || 3000;

// Start the server after connecting to the database
connectDB()
    .then(() => {
        server.listen(PORT, () => {
            console.log(`Server is running on port ${PORT}`);
        });
    })
    .catch((error) => {
        console.error("Error starting server:", error);
    });
