import React, { useEffect, useState, useRef } from 'react';
import '../ObesityPredict.css';
import { Link } from 'react-router-dom';
import html2pdf from 'html2pdf.js';

export default function ObesityResult() {
  const [result, setResult] = useState(null);           // medical_report
  const [plan, setPlan] = useState(null);              // health plan response
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const resultRef = useRef(null);

  useEffect(() => {
    const stored = localStorage.getItem('obesityResult');
    if (stored) {
      const parsed = JSON.parse(stored);
      setResult(parsed.medical_report);
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

  const handleGenerateHealthPlan = async () => {
    if (!result) {
      setError('No medical report found. Please complete prediction first.');
      return;
    }
    setError('');
    setLoading(true);
    try {
      const payload = {
        medical_report: result,
        n_results: 4,
        max_tokens: 1200,
        temperature: 0.2,
      };

      const resp = await fetch('http://localhost:3000/api/medical-report/plan', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
      });

      const data = await resp.json();
      if (!resp.ok) {
        throw new Error(data?.error || 'Plan API request failed');
      }
      if (!data.weekly_plan) {
        throw new Error('Plan API responded without weekly_plan');
      }
      setPlan(data);
    } catch (e) {
      setError(e.message || 'Unknown error');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="result-card" ref={resultRef}>
      <h2>🎯 Your Health Report</h2>
      {result ? (
        <div className="result-info">
          <div className="result-item">
            <span className="result-label">⚖️ Obesity Level:</span>
            <span className="result-value">
              {result.obesity_prediction.obesity_level} (
              {(result.obesity_prediction.confidence * 100).toFixed(1)}% confidence)
            </span>
          </div>
          <div className="result-item">
            <span className="result-label">🩺 Diabetes Risk:</span>
            <span className="result-value">
              {result.diabetes_prediction.diabetes ? 'Positive' : 'Negative'} (
              {(result.diabetes_prediction.confidence * 100).toFixed(1)}% confidence)
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
        <button className="submit-btn" onClick={handleGenerateHealthPlan} disabled={loading}>
          {loading ? 'Generating…' : 'Generate Weekly Health Plan'}
        </button>
      </div>

      {error && (
        <div style={{ color: 'red', marginTop: 10 }}>
          <strong>Error:</strong> {error}
        </div>
      )}

      {plan && (
        <div className="plan-wrapper" style={{ marginTop: 20 }}>
          <div className="suggestion-box">
            <strong>Suggestion:</strong> {plan.suggestion}
          </div>
          <div className="weeks-grid">
            {plan.weekly_plan.map((week) => (
              <div key={week.week} className="week-card">
                <h3>Week {week.week}</h3>
                <p><strong>Calories/day:</strong> {week.target_calories_per_day}</p>
                <p><strong>Focus:</strong> {week.focus}</p>

                <div>
                  <strong>Workouts:</strong>
                  <ul>
                    {week.workouts.map((w, i) => <li key={i}>{w}</li>)}
                  </ul>
                </div>

                <div>
                  <strong>Meal notes:</strong>
                  <p>{week.meal_notes}</p>
                </div>

                <div>
                  <strong>Reminders:</strong>
                  <ul>
                    {week.reminders.map((r, i) => <li key={i}>{r}</li>)}
                  </ul>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}
