import { useState, useEffect } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import Layout from '../components/Layout';

function History() {
  const navigate = useNavigate();
  const [history, setHistory] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Load history from localStorage
    const storedHistory = localStorage.getItem('analysisHistory');
    if (storedHistory) {
      try {
        const parsedHistory = JSON.parse(storedHistory);
        // Sort by date, most recent first
        parsedHistory.sort((a, b) => new Date(b.date) - new Date(a.date));
        setHistory(parsedHistory);
      } catch (err) {
        console.error('Failed to parse history:', err);
      }
    }
    setLoading(false);
  }, []);

  const handleDelete = (index) => {
    const newHistory = [...history];
    newHistory.splice(index, 1);
    setHistory(newHistory);
    localStorage.setItem('analysisHistory', JSON.stringify(newHistory));
  };

  const handleClearAll = () => {
    if (confirm('Are you sure you want to clear all history?')) {
      setHistory([]);
      localStorage.removeItem('analysisHistory');
    }
  };

  const formatDate = (dateString) => {
    const date = new Date(dateString);
    return date.toLocaleDateString('en-US', {
      month: 'short',
      day: 'numeric',
      year: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    });
  };

  const getFactorCount = (factors) => {
    return factors ? factors.length : 0;
  };

  const getEffectCount = (effects) => {
    return effects ? effects.length : 0;
  };

  if (loading) {
    return (
      <Layout>
        <div className="flex items-center justify-center h-96">
          <div className="text-center">
            <div className="w-12 h-12 border-4 border-cyan-500/30 border-t-cyan-500 rounded-full animate-spin mx-auto mb-4" />
            <p className="text-slate-400">Loading history...</p>
          </div>
        </div>
      </Layout>
    );
  }

  return (
    <Layout>
      <div className="max-w-4xl mx-auto">
        {/* Header */}
        <div className="flex flex-col md:flex-row md:items-center md:justify-between mb-8">
          <div>
            <div className="flex items-center mb-2">
              <span className="w-2 h-2 bg-green-500 rounded-full mr-2 animate-pulse"></span>
              <span className="text-sm text-slate-400">History Active</span>
            </div>
            <h1 className="text-4xl font-bold">
              <span className="bg-gradient-to-r from-cyan-400 via-purple-400 to-pink-400 bg-clip-text text-transparent">
                Analysis History
              </span>
            </h1>
            <p className="text-slate-400 mt-1">View your past food safety analyses</p>
          </div>
          <div className="mt-4 md:mt-0 flex gap-3">
            {history.length > 0 && (
              <button
                onClick={handleClearAll}
                className="px-6 py-3 border border-red-500/50 text-red-400 hover:bg-red-500/20 font-semibold rounded-xl transition flex items-center"
              >
                <svg className="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                </svg>
                Clear All
              </button>
            )}
            <button
              onClick={() => navigate('/analyze')}
              className="px-6 py-3 bg-gradient-to-r from-cyan-500 to-purple-500 text-white font-semibold rounded-xl hover:opacity-90 transition flex items-center"
            >
              <svg className="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 4v16m8-8H4" />
              </svg>
              New Analysis
            </button>
          </div>
        </div>

        {history.length === 0 ? (
          <div className="bg-white/5 backdrop-blur-xl border border-white/10 rounded-2xl p-12 text-center">
            <div className="w-20 h-20 bg-slate-800 rounded-full flex items-center justify-center mx-auto mb-6">
              <svg className="w-10 h-10 text-slate-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
              </svg>
            </div>
            <h2 className="text-2xl font-bold mb-3">No Analysis History</h2>
            <p className="text-slate-400 mb-8">
              You haven't analyzed any food products yet. Start by analyzing a nutrition label.
            </p>
            <Link
              to="/analyze"
              className="inline-flex items-center px-6 py-3 bg-gradient-to-r from-cyan-500 to-purple-500 text-white font-semibold rounded-xl hover:opacity-90 transition"
            >
              <svg className="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 10V3L4 14h7v7l9-11h-7z" />
              </svg>
              Start Analyzing
            </Link>
          </div>
        ) : (
          <div className="space-y-4">
            {history.map((item, index) => (
              <div key={index} className="bg-white/5 backdrop-blur-xl border border-white/10 rounded-2xl p-6 transition-all duration-300 hover:bg-white/10">
                <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-4">
                  <div className="flex-1">
                    <div className="flex items-center gap-3 mb-3">
                      <span className="text-slate-400 text-sm">
                        {formatDate(item.date)}
                      </span>
                      <span className="px-2 py-0.5 bg-cyan-500/20 text-cyan-400 rounded-full text-xs">
                        {getFactorCount(item.detected_factors)} factors
                      </span>
                      <span className="px-2 py-0.5 bg-red-500/20 text-red-400 rounded-full text-xs">
                        {getEffectCount(item.health_effects)} effects
                      </span>
                    </div>
                    
                    {/* Detected Factors */}
                    <div className="mb-3">
                      <span className="text-slate-400 text-sm font-medium">Detected:</span>
                      <div className="flex flex-wrap gap-1 mt-1">
                        {item.detected_factors && item.detected_factors.slice(0, 5).map((factor, idx) => (
                          <span 
                            key={idx}
                            className="px-2 py-0.5 bg-slate-700/50 text-slate-300 rounded text-xs"
                          >
                            {factor.replace(/_/g, ' ')}
                          </span>
                        ))}
                        {item.detected_factors && item.detected_factors.length > 5 && (
                          <span className="px-2 py-0.5 bg-slate-700/50 text-slate-400 rounded text-xs">
                            +{item.detected_factors.length - 5} more
                          </span>
                        )}
                      </div>
                    </div>

                    {/* Health Effects */}
                    {item.health_effects && item.health_effects.length > 0 && (
                      <div>
                        <span className="text-slate-400 text-sm font-medium">Concerns:</span>
                        <div className="flex flex-wrap gap-1 mt-1">
                          {item.health_effects.slice(0, 5).map((effect, idx) => (
                            <span 
                              key={idx}
                              className="px-2 py-0.5 bg-red-500/10 text-red-300 rounded text-xs"
                            >
                              {effect.replace(/_/g, ' ')}
                            </span>
                          ))}
                          {item.health_effects.length > 5 && (
                            <span className="px-2 py-0.5 bg-red-500/10 text-red-400 rounded text-xs">
                              +{item.health_effects.length - 5} more
                            </span>
                          )}
                        </div>
                      </div>
                    )}
                  </div>

                  <div className="flex items-center gap-2">
                    <button
                      onClick={() => {
                        sessionStorage.setItem('analysisResults', JSON.stringify(item));
                        navigate('/results');
                      }}
                      className="px-4 py-2 bg-cyan-500/20 text-cyan-400 hover:bg-cyan-500/40 rounded-lg transition text-sm"
                    >
                      View Details
                    </button>
                    <button
                      onClick={() => handleDelete(index)}
                      className="p-2 text-slate-400 hover:text-red-400 hover:bg-red-500/20 rounded-lg transition"
                    >
                      <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                      </svg>
                    </button>
                  </div>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </Layout>
  );
}

export default History;
