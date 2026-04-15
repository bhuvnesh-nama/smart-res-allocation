import { useAppSelector } from "@/app/hooks"

function Home() {
  const user = useAppSelector((state) => state.auth.user)

  return (
    <div>
      {user ? (
        <h1>Welcome back, {user.name}!</h1>
      ) : (
        <h1>Please log in to access your account.</h1>
      )}
    </div>
  )
}

export default Home