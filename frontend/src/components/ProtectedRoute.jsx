import { Navigate } from "react-router-dom";

function ProtectedRoute({ children }) {
  const userStr = localStorage.getItem("user");
  
  if (!userStr) {
    return <Navigate to="/login" replace />;
  }

  try {
    const user = JSON.parse(userStr);
    if (!user || !user.name) {
      return <Navigate to="/login" replace />;
    }
  } catch (e) {
    return <Navigate to="/login" replace />;
  }

  return children;
}

export default ProtectedRoute;