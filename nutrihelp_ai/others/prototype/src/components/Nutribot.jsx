import React, { useState, useEffect, useRef } from 'react';
import '../Nutribot.css';

export default function Nutribot() {
  
  const [messages, setMessages] = useState(() => {
    try {
      return JSON.parse(localStorage.getItem('chatHistory')) || [];
    } catch {
      return [];
    }
  });
  const [input, setInput] = useState('');
  const [darkMode, setDarkMode] = useState(false);
  const [showTooltip, setShowTooltip] = useState(false);
  const [showMenu, setShowMenu] = useState(false);
  
  const [isThinking, setIsThinking] = useState(false);
  const chatRef = useRef(null);
  const mascotRef = useRef(null);
 
  const requestControllerRef = useRef(null);

  const API_BASE_URL = process.env.REACT_APP_API_BASE_URL || 'http://127.0.0.1:8000';
  const AI_API_PATH = '/ai-model/chatbot/chat';

  useEffect(() => {
    document.body.classList.toggle('dark-mode', darkMode);
  }, [darkMode]);

  useEffect(() => {
    const msg = new SpeechSynthesisUtterance("Hi! I'm Nutribot. Feel free to ask me anything about nutrition or health.");
    msg.lang = 'en-US';
    window.speechSynthesis.speak(msg);
  }, []);

  useEffect(() => {
    localStorage.setItem('chatHistory', JSON.stringify(messages));
    if (chatRef.current) {
      chatRef.current.scrollTop = chatRef.current.scrollHeight;
    }
  }, [messages]);

  
  useEffect(() => {
    return () => {
      if (requestControllerRef.current) {
        requestControllerRef.current.abort();
      }
    };
  }, []);

  
  const getNow = () => new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });

  const normalizeReplyText = (data) => {
    const detailText =
      typeof data?.detail === 'string'
        ? data.detail
        : typeof data?.detail?.detail === 'string'
          ? data.detail.detail
          : '';

    const candidates = [
      data?.msg,
      data?.response_text,
      data?.response,
      data?.answer,
      data?.data?.msg,
      detailText,
    ];
    const valid = candidates.find((value) => typeof value === 'string' && value.trim().length > 0);
    return valid ? valid.trim() : '';
  };


  const buildApiUrl = (path) => `${API_BASE_URL.replace(/\/$/, '')}${path}`;

  const postToAssistant = async (path, text, signal) => {
    const res = await fetch(buildApiUrl(path), {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ query: text }),
      signal,
    });

    let data = null;
    try {
      data = await res.json();
    } catch {
      data = null;
    }

    if (!res.ok) {
      const detail =
        data?.detail?.detail || data?.detail?.error || data?.detail || data?.error || `HTTP ${res.status}`;
      throw new Error(typeof detail === 'string' ? detail : 'Assistant request failed.');
    }

    return normalizeReplyText(data);
  };

  const getBestReply = async (text, signal, onPhaseChange) => {
    onPhaseChange('Asking NutriHelp AI...');
    const reply = await postToAssistant(AI_API_PATH, text, signal);
    return { reply };
  };

  const sendMessage = async (text) => {
    const trimmed = text.trim();
    if (!trimmed || isThinking) return;

    const now = getNow();
   
    const userMessage = { id: `${Date.now()}-user`, sender: 'user', text: trimmed, time: now };
    const pendingBotMessage = {
      id: `${Date.now()}-bot-loading`,
      sender: 'bot',
      text: 'Thinking...',
      time: now,
      status: 'loading',
      meta: 'Preparing answer...',
    };

    setMessages((prev) => [...prev, userMessage, pendingBotMessage]);
    setInput('');
    setIsThinking(true);

    requestControllerRef.current = new AbortController();

    try {
      const best = await getBestReply(trimmed, requestControllerRef.current.signal, (phase) => {
        setMessages((prev) =>
          prev.map((msg) =>
            msg.id === pendingBotMessage.id ? { ...msg, text: 'Thinking...', meta: phase, time: getNow() } : msg
          )
        );
      });

      setMessages((prev) =>
        prev.map((msg) =>
          msg.id === pendingBotMessage.id
            ? { ...msg, text: best.reply, status: 'sent', source: best.source, meta: '', time: getNow() }
            : msg
        )
      );
    } catch (error) {
      setMessages((prev) =>
        prev.map((msg) =>
          msg.id === pendingBotMessage.id
            ? {
                ...msg,
                text: 'I’m having trouble reaching the nutrition service right now. If you want, I can still share general Australian nutrition guidance while this is unavailable.',
                status: 'error',
                meta: error?.message || 'Temporary connection issue.',
                time: getNow(),
              }
            : msg
        )
      );
    } finally {
      setIsThinking(false);
      requestControllerRef.current = null;
    }
  };

  const handleKeyDown = (e) => {
    if (e.key === 'Enter') sendMessage(input);
  };

  const quickAsk = (text) => {
    setInput(text);
    sendMessage(text);
    setShowMenu(false);
  };

  const toggleMascotMenu = () => {
    setShowTooltip(true);
    setShowMenu(true);
    setTimeout(() => {
      setShowTooltip(false);
      setShowMenu(false);
    }, 5000);
  };

  // 拖动卡通小人
  useEffect(() => {
    const mascot = mascotRef.current;
    if (!mascot) return undefined;

    let isDragging = false;
    let offsetX, offsetY;

    const handleMouseDown = (e) => {
      isDragging = true;
      offsetX = e.clientX - mascot.getBoundingClientRect().left;
      offsetY = e.clientY - mascot.getBoundingClientRect().top;
      mascot.style.transition = 'none';
    };

    const handleMouseMove = (e) => {
      if (isDragging) {
        mascot.style.left = `${e.clientX - offsetX}px`;
        mascot.style.top = `${e.clientY - offsetY}px`;
        mascot.style.right = 'auto';
        mascot.style.bottom = 'auto';
        mascot.style.position = 'fixed';
      }
    };

    const handleMouseUp = () => {
      isDragging = false;
      mascot.style.transition = 'transform 0.2s';
    };

    mascot.addEventListener('mousedown', handleMouseDown);
    document.addEventListener('mousemove', handleMouseMove);
    document.addEventListener('mouseup', handleMouseUp);
    return () => {
      mascot.removeEventListener('mousedown', handleMouseDown);
      document.removeEventListener('mousemove', handleMouseMove);
      document.removeEventListener('mouseup', handleMouseUp);
    };
  }, []);

  return (
    <div className="nutribot-container">
      <div className="sidebar">
        <div className="sidebar-header">Nutribot</div>
        <button onClick={() => setMessages([])}>🗑 Clear Chat</button>
        <button onClick={() => setDarkMode(!darkMode)}>
          {darkMode ? '☀️ Light Mode' : '🌙 Dark Mode'}
        </button>
      </div>

      <div className="main-container">
        <div className="chat-box" ref={chatRef}>
          {messages.map((msg, i) => (
            <div key={msg.id || i} className={`message-row ${msg.sender}`}>
              <div className={`message-bubble ${msg.status === 'error' ? 'error' : ''}`}>
                {msg.status === 'loading' ? (
                  <>
                    <span>{msg.text}</span>
                    <span className="typing-dots" aria-hidden="true">
                      <span />
                      <span />
                      <span />
                    </span>
                  </>
                ) : (
                  msg.text
                )}
              </div>
              <div className="timestamp">
                {msg.time}
                {msg.source
                  ? ` · ${
                      msg.source === 'rag'
                        ? 'RAG'
                        : msg.source === 'guided_fallback'
                          ? 'Guided Fallback'
                          : 'Fallback'
                    }`
                  : ''}
              </div>
              {msg.meta ? <div className="message-meta">{msg.meta}</div> : null}
            </div>
          ))}
        </div>

        <div className="nutribot-input">
          <input
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={handleKeyDown}
            placeholder="Ask me anything..."
            
            disabled={isThinking}
          />
          <button onClick={() => sendMessage(input)} disabled={isThinking || !input.trim()}>
            ➤
          </button>
        </div>

        <div className="file-upload">
          <label>
            📂 Upload File
            <input
              type="file"
              hidden
              onChange={(e) => {
                const file = e.target.files[0];
                if (file) {
                  const now = getNow();
                  setMessages((prev) => [...prev, { sender: 'bot', text: `📂 File "${file.name}" uploaded.`, time: now }]);
                }
              }}
            />
          </label>
        </div>
      </div>

      <div className="mascot-container" onClick={toggleMascotMenu} ref={mascotRef}>
        <img src="https://cdn-icons-png.flaticon.com/512/4712/4712103.png" alt="Mascot" />
      </div>

      {showTooltip && (
        <div className="mascot-tooltip">
          💬 Try asking: What is BMI? Or upload a file!
        </div>
      )}

      {showMenu && (
        <div className="mascot-menu">
          <button onClick={() => quickAsk('What is my BMI?')}>📏 What is my BMI?</button>
          <button onClick={() => quickAsk('Give me healthy tips')}>🥗 Healthy Tips</button>
          <button onClick={() => quickAsk('Help me make a meal plan')}>📋 Meal Plan</button>
        </div>
      )}
    </div>
  );
}
