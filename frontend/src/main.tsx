import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { createBrowserRouter, createRoutesFromElements,Route, RouterProvider } from 'react-router-dom'
import { Provider } from 'react-redux'
import { store } from './app/store'
import ProtectedRoute from './layouts/ProtectedRoute'
import "./index.css"

// Importing Pages
import Dashboard from './pages/dashboard/Dashboard'
import Login from './pages/login/Login'
import Register from './pages/register/Register'
import ForgotPassword from './pages/forgot-password/ForgotPassword'
import ResetPassword from './pages/reset-password/ResetPassword'
import ResetPasswordEmailSentSuccessFully from './pages/forgot-password/ResetPasswordEmailSentSuccessFully'
import VerifyEmail from './pages/verify-email/VerifyEmail'
import GuestRoute from './layouts/GuestRoute'
import AppLayout from './layouts/AppLayout'
import Home from './pages/home/Home'
import { ThemeProvider } from './components/theme-provider'

const router = createBrowserRouter(createRoutesFromElements(
  <Route path="/" element={<AppLayout/>}>
    <Route>
      <Route index element={<Home />} />
      <Route path="/verify-email" element={<VerifyEmail />} />
    </Route>
    
    <Route path="/" element={<GuestRoute />}>
      <Route path="/login" element={<Login />} />
      <Route path="/register" element={<Register />} />
      <Route path="/forgot-password" element={<ForgotPassword />} />
      <Route path="/reset-password/:token" element={<ResetPassword />} />
      <Route path="/reset-password-email-sent" element={<ResetPasswordEmailSentSuccessFully />} />
    </Route>

    <Route path="/" element={<ProtectedRoute />}>
      <Route path='/dashboard'  element={<Dashboard />} />
    </Route>
  </Route>
))

  createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <Provider store={store}>
      <ThemeProvider defaultTheme='system' storageKey='ui-theme'>
        <RouterProvider router={router} />
      </ThemeProvider>
    </Provider>
  </StrictMode>,
)