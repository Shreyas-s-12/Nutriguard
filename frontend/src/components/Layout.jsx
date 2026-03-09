import { useState } from 'react';
import Sidebar from './Sidebar';

function Layout({ children, hideSidebar = false }) {
  const [sidebarCollapsed, setSidebarCollapsed] = useState(false);

  if (hideSidebar) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-slate-900 via-slate-900 to-slate-800">
        {children}
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-slate-900 to-slate-800">
      {/* Background Effects */}
      <div className="fixed inset-0 overflow-hidden pointer-events-none">
        <div className="absolute top-0 left-1/4 w-96 h-96 bg-cyan-500/10 rounded-full blur-3xl" />
        <div className="absolute bottom-0 right-1/4 w-96 h-96 bg-purple-500/10 rounded-full blur-3xl" />
      </div>
      
      <Sidebar />
      
      {/* Main Content */}
      <main className={`transition-all duration-300 ${sidebarCollapsed ? 'ml-20' : 'ml-64'}`}>
        <div className="p-8">
          {children}
        </div>
      </main>
    </div>
  );
}

export default Layout;
