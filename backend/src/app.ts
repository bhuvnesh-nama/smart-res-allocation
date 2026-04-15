import express from "express";
import helmet from "helmet";
import morgan from "morgan";
import cors from "cors";
import cookieParser from "cookie-parser";
import { createServer } from "http";
import setUpSocket from "./utils/socket";
import { Server } from "socket.io";

const app = express();
const server = createServer(app);

const io = new Server(server, {
    cors: {
        origin: ["http://localhost:5173", "http://localhost:5174"],
        methods: ["GET", "POST"],
        credentials: true,
    },
});

setUpSocket(io);

app.use(helmet());
// app.use(morgan("combined"));
app.use(cors({
    origin: ["http://localhost:5173", "http://localhost:5174"],
    credentials: true,
}))
app.use(cookieParser());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// importing routes
import authRouter from "./routes/auth.route";

// applying routes
app.use("/api/auth", authRouter);

export default server;