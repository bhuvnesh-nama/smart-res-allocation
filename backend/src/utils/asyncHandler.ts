import { Request, Response, NextFunction } from "express";

type AsyncHandler = (
  req: Request,
  res: Response,
  next: NextFunction
) => Promise<any> | any;

const asyncHandler = (fn: AsyncHandler) =>
  async (req: Request, res: Response, next: NextFunction) => {
    try {
      await fn(req, res, next);
    } catch (error: { statusCode?: number; message?: string } | any) {
      res.status(error.statusCode || 500).json({ message: (error as Error).message });
    }
  };

export default asyncHandler;
