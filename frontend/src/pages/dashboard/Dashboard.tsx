import { useAppSelector } from "@/app/hooks";

const Dashboard = () => {
  const { user } = useAppSelector((state) => state.auth);
  return (
   <div>
     {user ? user.email : "No user logged in"}
   </div>
  );
};

export default Dashboard;
