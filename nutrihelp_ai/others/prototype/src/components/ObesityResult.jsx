import React, { useEffect, useState, useRef } from 'react';
import '../ObesityPredict.css';
import { Link } from 'react-router-dom';
import html2pdf from 'html2pdf.js';

export default function ObesityResult() {
  const [result, setResult] = useState(null);
  const resultRef = useRef(null);

  useEffect(() => {
    const stored = localStorage.getItem('obesityResult');
    if (stored) {
      const parsed = JSON.parse(stored);
      setResult(parsed.medical_report); // ✅ extract the nested object
    }
  }, []);

  const handleDownloadPDF = () => {
    if (!resultRef.current) return;
    html2pdf().from(resultRef.current).save('Obesity_Report.pdf');
  };

  const handleCopyLink = () => {
    const url = window.location.href;
    navigator.clipboard.writeText(url).then(() => {
      alert('🔗 Link copied to clipboard!');
    });
  };

  return (
    <div className="result-card" ref={resultRef}>
      <h2>🎯 Your Health Report</h2>
      {result ? (
        <div className="result-info">
          <div className="result-item">
            <span className="result-label">⚖️ Obesity Level:</span>
            <span className="result-value">
              {result.obesity_prediction.obesity_level} ({(result.obesity_prediction.confidence * 100).toFixed(1)}% confidence)
            </span>
          </div>
          <div className="result-item">
            <span className="result-label">🩺 Diabetes Risk:</span>
            <span className="result-value">
              {result.diabetes_prediction.diabetes ? 'Positive' : 'Negative'} ({(result.diabetes_prediction.confidence * 100).toFixed(1)}% confidence)
            </span>
          </div>
        </div>
      ) : (
        <p>No result data available.</p>
      )}

      <div className="result-buttons">
        <button className="submit-btn" onClick={handleDownloadPDF}>
          📄 Save as PDF
        </button>
        <button className="submit-btn" onClick={handleCopyLink}>
          🔗 Copy Share Link
        </button>
        <Link to="/predict">
          <button className="submit-btn">← Back to Questionnaire</button>
        </Link>
      </div>
    </div>
  );
}
