import { Server } from "socket.io";
import cookie from "cookie";
import jwt from "jsonwebtoken";

const setUpSocket = (io: Server) => {
  const userSocketMap = new Map<string, string>();

  io.on("connection", (socket) => {
    const cookies = cookie.parse(socket.handshake.headers?.cookie || "");
    const token = cookies.accessToken;

    if (!token) {
      console.log("No token provided, disconnecting socket");
      socket.disconnect();
      return;
    }

    try {
      const decoded = jwt.verify(token, process.env.JWT_SECRET || "secret") as { _id: string };
      const userId = decoded._id;


      socket.on("disconnect", () => {
        userSocketMap.delete(userId);
        console.log(`❌ User disconnected: ${userId}`);
      });
    } catch (error) {
      console.log("Invalid token, disconnecting socket");
      socket.disconnect();
    }
  });
};

export default setUpSocket;
