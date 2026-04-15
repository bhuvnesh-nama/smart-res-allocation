import { useEffect, useState } from "react";
import { useDispatch } from "react-redux";
import { Outlet } from "react-router-dom";
import { Toaster } from "sonner";
import { ModeToggle } from "@/components/mode-toggle";
import { checkAuthStatus } from "@/features/auth/authThunk";

function AppLayout() {
  const dispatch = useDispatch();
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const loadAuthStatus = async () => {
      try {
        await dispatch(checkAuthStatus() as any);
      } finally {
        setLoading(false);
      }
    };

    loadAuthStatus();
  }, [dispatch]);

  if (loading) {
    return (
      <div className="flex h-screen items-center justify-center">
        <p>Loading...</p>
      </div>
    );
  }

  return (
    <>
      <Outlet />
      <Toaster position="top-right" richColors />
      <ModeToggle className="absolute top-4 right-4" />
    </>
  );
}

export default AppLayout;
