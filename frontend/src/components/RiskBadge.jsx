function RiskBadge({ level, size = 'default' }) {
  const getBadgeStyles = () => {
    const baseClasses = size === 'small' 
      ? 'px-2 py-0.5 text-xs' 
      : 'px-3 py-1 text-sm';

    switch (level?.toLowerCase()) {
      case 'high':
      case 'high risk':
        return `${baseClasses} bg-red-500/20 text-red-400 border border-red-500/30`;
      case 'moderate':
        return `${baseClasses} bg-yellow-500/20 text-yellow-400 border border-yellow-500/30`;
      case 'low':
      case 'low risk':
        return `${baseClasses} bg-green-500/20 text-green-400 border border-green-500/30`;
      case 'minimal':
      case 'minimal risk':
        return `${baseClasses} bg-blue-500/20 text-blue-400 border border-blue-500/30`;
      default:
        return `${baseClasses} bg-slate-500/20 text-slate-400 border border-slate-500/30`;
    }
  };

  const getLabel = () => {
    switch (level?.toLowerCase()) {
      case 'high':
      case 'high risk':
        return 'High Risk';
      case 'moderate':
        return 'Moderate Risk';
      case 'low':
      case 'low risk':
        return 'Low Risk';
      case 'minimal':
      case 'minimal risk':
        return 'Minimal Risk';
      default:
        return level || 'Unknown';
    }
  };

  return (
    <span className={`inline-flex items-center rounded-full font-medium ${getBadgeStyles()}`}>
      <span className={`w-1.5 h-1.5 rounded-full mr-2 ${
        level?.toLowerCase() === 'high' || level?.toLowerCase() === 'high risk'
          ? 'bg-red-400'
          : level?.toLowerCase() === 'moderate'
          ? 'bg-yellow-400'
          : level?.toLowerCase() === 'low' || level?.toLowerCase() === 'low risk'
          ? 'bg-green-400'
          : level?.toLowerCase() === 'minimal' || level?.toLowerCase() === 'minimal risk'
          ? 'bg-blue-400'
          : 'bg-slate-400'
      }`}></span>
      {getLabel()}
    </span>
  );
}

export default RiskBadge;
