# Smart Resource Allocation

Full-stack TypeScript project with:
- Backend: Express + MongoDB
- Frontend: React + Vite

## Project Structure

- `backend` - API server, auth flows, email templates
- `frontend` - React client app

## Prerequisites

- Node.js 24.14.1 (recommended: latest LTS)
- npm 9+
- MongoDB instance (local or cloud)

## 1. Clone and Install

From the project root, install dependencies for both apps.

```bash
cd backend
npm install

cd ../frontend
npm install
```

## 2. Backend Environment Setup

Create a `.env` file in `backend/.env`.

Example:

```env
PORT=8000
DATABASE_URL=mongodb://127.0.0.1:27017/smart-res-allocation
JWT_SECRET=your_jwt_secret

EMAIL_HOST=smtp.example.com
EMAIL_USER=your_smtp_user
EMAIL_PASS=your_smtp_password
EMAIL_ADDRESS=no-reply@example.com

DOMAIN_NAME=localhost
```

Notes:
- Set `PORT=8000` to match the frontend API client default (`http://localhost:8000/api`).
- `DOMAIN_NAME` is used when generating reset-password links.
- Email variables are required for forgot-password and email verification flows.

## 3. Run the Backend

From `backend`:

```bash
npm run dev
```

Backend scripts:
- `npm run dev` - start in development mode (nodemon + tsx)
- `npm run build` - build with tsup
- `npm start` - run built app from `dist`

## 4. Run the Frontend

From `frontend` (new terminal):

```bash
npm run dev
```

Frontend scripts:
- `npm run dev` - start Vite dev server (usually `http://localhost:5173`)
- `npm run build` - type-check and production build
- `npm run preview` - preview production build
- `npm run lint` - run ESLint

## 5. Access the App

- Frontend: `http://localhost:5173`
- Backend API base: `http://localhost:8000/api`

## Development Notes

- Backend CORS is configured for `http://localhost:5173` and `http://localhost:5174`.
- Cookies are configured with `secure: true` in backend constants. For local HTTP-only development, auth cookies may not be set unless served over HTTPS.
