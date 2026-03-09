import { useState, useEffect } from 'react';
import { Link, useLocation } from 'react-router-dom';
import logo from '../assets/logo.png';

function Navbar() {
  const location = useLocation();
  const [user, setUser] = useState(null);
  
  useEffect(() => {
    // Get user from localStorage
    const storedUser = localStorage.getItem("user");
    if (storedUser) {
      try {
        const parsedUser = JSON.parse(storedUser);
        setUser(parsedUser);
      } catch (e) {
        localStorage.removeItem("user");
      }
    }
  }, [location]);
  
  const isActive = (path) => {
    return location.pathname === path ? 'text-nutri-primary' : 'text-slate-300 hover:text-white';
  };

  const handleLogout = () => {
    // Remove user from localStorage
    localStorage.removeItem("user");
    // Reload the app to trigger authentication check
    window.location.reload();
  };

  const navLinks = [
    { path: '/', label: 'Home', icon: '🏠' },
    { path: '/analyze', label: 'Analyze', icon: '🔬' },
    { path: '/history', label: 'History', icon: '📋' },
    { path: '/chemicals', label: 'Database', icon: '🧪' },
    { path: '/guide', label: 'Food Safety Guide', icon: '📖' },
    { path: '/about', label: 'About', icon: 'ℹ️' },
  ];

  return (
    <header className="glass sticky top-0 z-50">
      <div className="max-w-7xl mx-auto px-4 py-4">
        <div className="flex items-center justify-between">
          <Link to="/" className="flex items-center space-x-3">
            <img 
              src={logo} 
              alt="NutriDetect AI Logo" 
              className="w-10 h-10 transition duration-300 transform hover:scale-110 drop-shadow-[0_0_10px_rgba(34,211,238,0.7)] hover:drop-shadow-[0_0_20px_rgba(34,211,238,1)]" 
            />
            <span className="text-xl font-bold gradient-text">
              NutriDetect AI
            </span>
          </Link>
          
          <nav className="hidden md:flex items-center space-x-1">
            {navLinks.map((link) => (
              <Link
                key={link.path}
                to={link.path}
                className={`px-4 py-2 rounded-lg transition flex items-center space-x-2 ${isActive(link.path)}`}
              >
                <span>{link.icon}</span>
                <span>{link.label}</span>
              </Link>
            ))}
          </nav>

          <div className="hidden md:flex items-center space-x-4">
            {user ? (
              <>
                <div className="flex items-center space-x-3">
                  <div className="w-8 h-8 bg-gradient-to-br from-nutri-primary to-nutri-accent rounded-full flex items-center justify-center text-white font-bold text-sm">
                    {(user?.name || 'U').charAt(0).toUpperCase()}
                  </div>
                  <div className="text-sm">
                    <div className="text-white font-medium">Hello, {user?.name || 'User'} 👋</div>
                    <div className="text-green-400 text-xs flex items-center">
                      <span className="w-2 h-2 bg-green-400 rounded-full mr-1 animate-pulse"></span>
                      Logged In
                    </div>
                  </div>
                </div>
                <button
                  onClick={handleLogout}
                  className="px-4 py-2 border border-slate-600 text-slate-300 hover:bg-slate-800 rounded-lg transition flex items-center space-x-2"
                >
                  <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" />
                  </svg>
                  <span>Logout</span>
                </button>
              </>
            ) : (
              <Link
                to="/login"
                className="px-4 py-2 bg-nutri-primary/20 text-nutri-primary hover:bg-nutri-primary/40 rounded-lg transition flex items-center space-x-2"
              >
                <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                </svg>
                <span>Login</span>
              </Link>
            )}
            <span className="px-3 py-1 bg-nutri-primary/20 text-nutri-primary rounded-full text-sm">
              🔬 1000+ Additives
            </span>
          </div>

          {/* Mobile menu button */}
          <div className="md:hidden flex items-center space-x-2">
            {user ? (
              <div className="w-8 h-8 bg-gradient-to-br from-nutri-primary to-nutri-accent rounded-full flex items-center justify-center text-white font-bold text-xs">
                {(user?.name || 'U').charAt(0).toUpperCase()}
              </div>
            ) : (
              <Link
                to="/login"
                className="p-2 rounded-lg text-slate-300 hover:text-white transition"
              >
                <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                </svg>
              </Link>
            )}
            {navLinks.map((link) => (
              <Link
                key={link.path}
                to={link.path}
                className={`p-2 rounded-lg transition ${isActive(link.path)}`}
              >
                <span className="text-xl">{link.icon}</span>
              </Link>
            ))}
          </div>
        </div>
      </div>
    </header>
  );
}

export default Navbar;
