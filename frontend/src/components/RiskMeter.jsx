function RiskMeter({ score, showLabel = true, size = 'default' }) {
  const getColor = () => {
    if (score >= 70) return '#ef4444';
    if (score >= 40) return '#eab308';
    return '#22c55e';
  };

  const getLabel = () => {
    if (score >= 70) return 'High Risk';
    if (score >= 40) return 'Moderate Risk';
    return 'Low Risk';
  };

  const getBgClass = () => {
    if (score >= 70) return 'bg-red-500/20';
    if (score >= 40) return 'bg-yellow-500/20';
    return 'bg-green-500/20';
  };

  const getTextClass = () => {
    if (score >= 70) return 'text-red-400';
    if (score >= 40) return 'text-yellow-400';
    return 'text-green-400';
  };

  const getGradient = () => {
    if (score >= 70) return 'from-red-500 to-red-600';
    if (score >= 40) return 'from-yellow-500 to-yellow-600';
    return 'from-green-500 to-green-600';
  };

  const sizeClasses = size === 'small' 
    ? 'h-2' 
    : size === 'large' 
    ? 'h-4' 
    : 'h-3';

  // Generate the filled portion of the bar
  const filledBlocks = Math.floor(score / 10);
  const emptyBlocks = 10 - filledBlocks;

  return (
    <div className="w-full">
      {showLabel && (
        <div className="flex items-center justify-between mb-2">
          <span className="text-sm font-medium text-slate-300">Health Risk Score</span>
          <span className={`text-sm font-bold ${getTextClass()}`}>{getLabel()}</span>
        </div>
      )}
      
      {/* Progress Bar Style */}
      <div className={`w-full ${sizeClasses} bg-slate-700/50 rounded-full overflow-hidden`}>
        <div 
          className={`h-full bg-gradient-to-r ${getGradient()} transition-all duration-1000 ease-out rounded-full`}
          style={{ width: `${score}%` }}
        />
      </div>

      {/* ASCII-style indicator */}
      <div className="flex items-center justify-between mt-2">
        <div className="flex gap-0.5">
          {[...Array(10)].map((_, i) => (
            <span 
              key={i} 
              className={`w-2 h-4 transition-colors ${
                i < filledBlocks 
                  ? score >= 70 
                    ? 'bg-red-500' 
                    : score >= 40 
                    ? 'bg-yellow-500' 
                    : 'bg-green-500'
                  : 'bg-slate-700'
              }`}
              style={{ 
                borderRadius: i === 0 ? '4px 0 0 4px' : i === 9 ? '0 4px 4px 0' : '2px' 
              }}
            />
          ))}
        </div>
        <span className={`text-lg font-bold ${getTextClass()}`}>{score}%</span>
      </div>
    </div>
  );
}

export default RiskMeter;
